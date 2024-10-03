from django.urls import path
from .views import UsersList, CreateUser, DeleteView, UpdateView


urlpatterns = [
    path('', UsersList.as_view(), name='users'),
    path('create/', CreateUser.as_view(), name='register'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', UpdateView.as_view(), name='update'),
]
