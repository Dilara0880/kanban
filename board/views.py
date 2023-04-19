from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from board.models import Board, Column, Task


def index(request):
    context = {
        "boards": Board.objects.order_by('id'),
    }
    return render(request, 'index.html', context)


def view_board(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    columns = Column.objects.filter(board_id=board_id)
    tasks = set()
    for column in columns:
        tasks.add(Task.objects.filter(column_id=column.id))
    context = {
        'board': board,
        'columns': columns,
        'tasks': tasks,
    }
    print(board.title)
    return render(request, 'view_board.html', context)


def create_task(request):
    return HttpResponse("You're creating a new task")


def choose_board(request):
    return HttpResponse("You're choosing a board")
