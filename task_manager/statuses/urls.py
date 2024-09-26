from django.urls import path
from .views import StatusesListView, CreateStatusView, DeleteStatusView, UpdateStatusView


urlpatterns = [
	path('', StatusesListView.as_view(), name='statuses'),
	path('create/', CreateStatusView.as_view(), name='create_status'),
	path('<int:pk>/delete/', DeleteStatusView.as_view(), name='delete_status'),
	path('<int:pk>/update/', UpdateStatusView.as_view(), name='update_status'),
]