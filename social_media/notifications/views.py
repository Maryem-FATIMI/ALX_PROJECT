from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import Notification
from .serializers import NotificationSerializer
# Create your views here.


class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
