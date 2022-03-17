from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete


urlpatterns = [
    path('', TaskList.as_view(), name = 'task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task_detail'),
    path('create-task/', TaskCreate.as_view(), name = 'task_create'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name = 'task_update'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name = 'task_delete')
]