from django.urls import path
from .views import TasksListView, CreateTaskView, DeleteTaskView, UpdateTaskView, TaskDetailView


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_view'),
]
