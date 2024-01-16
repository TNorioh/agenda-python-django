from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.taskList, name = "task-list"),
    path('newtask/', views.newTask, name = "new-task"),
    path('task/<int:id>', views.taskView, name="task-view")
]
