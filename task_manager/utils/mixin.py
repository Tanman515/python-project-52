from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.db.models import ProtectedError


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authorized! Please log in.'))
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class OwnerRequiredMixin:
    object_attr = 'id'
    success_url = 'index'
    permission_error_message = _('You do not have permission to change another user.')

    def dispatch(self, request, *args, **kwargs):

        obj = self.get_object()
        obj_user_attr = getattr(obj, self.object_attr)
        user = request.user

        if isinstance(obj_user_attr, int):
            if obj_user_attr != getattr(user, 'id'):
                messages.error(request, self.permission_error_message)
                return redirect(self.success_url)
        else:
            if getattr(obj_user_attr, 'id') != getattr(user, 'id'):
                messages.error(request, self.permission_error_message)
                return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)


class ProtectedErrorHandlingMixin:
    success_url = 'index'
    protected_error_message = _('Cannot delete this object because it is in use')

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_error_message)
            return redirect(self.success_url)
