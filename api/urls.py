from django.urls import path
# from . import views
from .views import TaskList,TaskDetail,TaskCreate

urlpatterns = [
    # path("", views.apiOverview, name='api-overview'),
    path("", TaskList.as_view(), name='task-list'),
    path("task-detail/<int:pk>", TaskDetail.as_view(), name='task-detail'),
    path("task-create/", TaskCreate.as_view(), name='task-create'),
    # path("task-list/", views.taskList, name='task-list'),
    # path("task-update/<int:pk>", views.taskUpdate, name='task-update'),
    # path("task-delete/<int:pk>", views.taskDelete, name='task-delete'),
]
