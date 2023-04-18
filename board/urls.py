from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("board/<int:board_id>/", views.view_board, name="view_board"),
    path("board/", views.choose_board, name="choose_board"),
    path("task/", views.create_task, name="create_task"),
]