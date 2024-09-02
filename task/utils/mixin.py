from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect



class UserChangeAccessMixin:

    redirect_field_name = None

    def has_permission(self) -> bool:
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                FlashMessages.NO_AUTHENTICATION.value,
            )

            return self.handle_no_permission()

        elif not self.has_permission():
            messages.error(
                request,
                FlashMessages.NO_PERMIT_TO_CHANGE_USER.value,
            )
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)
