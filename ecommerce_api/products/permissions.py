from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the product.
        # For DELETE requests, explicitly check if the user is the owner.
        if request.method == 'DELETE':
            return obj.user == request.user

        # For other non-safe methods (like PUT, PATCH), check ownership as before.
        return obj.user == request.user

class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a review to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the review.
        # For DELETE requests, explicitly check if the user is the author.
        if request.method == 'DELETE':
            return obj.author == request.user

        # For other non-safe methods (like PUT, PATCH), check authorship as before.
        return obj.author == request.user
