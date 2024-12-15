from rest_framework import viewsets, generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from notifications.models import Notification


# Create your  here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']

    def get_object(self):
        post = super().get_object()

        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if post.author != self.request.user:
                raise PermissionDenied("You Do not have permission to modify this post")
        return post


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']

    def get_object(self):
        comment = super().get_object()

        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if comment.author != self.request.user:
                raise PermissionDenied('You do not have permission to modify this comment')
        return comment


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()

        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like, create = Like.objects.get_or_create(user=request.user, post=post)

        if not create:
            return Response({'error': 'you have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target=post
        )

        return Response({'status': 'Post Liked'}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({'error': 'you have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()

        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='unliked',
            target=post
        )

        return Response({'status': 'Post Unliked'}, status=status.HTTP_200_OK)
