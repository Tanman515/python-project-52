from django.urls import path
from .views import MarksListView, CreateMarkView, DeleteMarkView, UpdateMarkView


urlpatterns = [
	path('', MarksListView.as_view(), name='marks'),
	path('create/', CreateMarkView.as_view(), name='create_mark'),
	path('<int:pk>/delete/', DeleteMarkView.as_view(), name='delete_mark'),
	path('<int:pk>/update/', UpdateMarkView.as_view(), name='update_mark'),
]