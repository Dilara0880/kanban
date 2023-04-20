from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from board.models import Board, Column, Task


def update_task_db(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    column_id = request.POST.get('column')
    deadline = request.POST.get('deadline')
    priority = request.POST.get('priority')
    task = Task(title=title, description=description, column_id=column_id, deadline=deadline, priority=priority)
    task.save()


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
    return render(request, 'view_board.html', context)


def create_task(request, board_id):
    columns = Column.objects.filter(board_id=board_id)
    priority_choices = Task.Priority.choices
    context = {'columns': columns,
               'board_id': board_id,
               'priority_choices': priority_choices,
               }
    if request.method == 'POST':
        update_task_db(request)
        return redirect('view_board', board_id)
    return render(request, 'create_new_task.html', context)


def choose_board(request):
    return HttpResponse("You're choosing a board")


def edit_task(request, board_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_column = get_object_or_404(Column, pk=task.column_id)
    columns = Column.objects.filter(board_id=board_id)
    context = {
        'task': task,
        'board_id': board_id,
        'task_id': task_id,
        'task_column': task_column,
        'columns': columns,
    }
    if request.method == 'POST':
        update_task_db(request)
        return redirect('view_board', board_id)
    return render(request, 'edit_task.html', context)
