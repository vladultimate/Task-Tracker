from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied("u are not owner of this board")
        return super().dispatch(request, *args, **kwargs)
    
class UserIsOwnerCommentMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise PermissionDenied("u are not owner of this board")
        return super().dispatch(request, *args, **kwargs)
