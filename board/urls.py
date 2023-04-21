from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("board/<int:board_id>/", views.view_board, name="view_board"),
    path("column/<int:board_id>/", views.add_column, name="add_column"),
    path("task/<int:board_id>/", views.create_task, name="create_task"),
    path("edittask/<int:board_id>/<int:task_id>/", views.edit_task, name="edit_task"),

]
