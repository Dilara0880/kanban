from datetime import datetime

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
    if request.POST.get('delete'):
        Board.objects.filter(pk=board_id).delete()
        return redirect('index')
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
    priority_choices = ['Easy', 'Medium', 'Hard']
    context = {'columns': columns,
               'board_id': board_id,
               'priority_choices': priority_choices,
               }
    if request.method == 'POST':
        update_task_db(request)
        return redirect('view_board', board_id)
    return render(request, 'create_new_task.html', context)


def add_column(request, board_id):
    board_title = get_object_or_404(Board, pk=board_id).title
    context = {
        'board_id': board_id,
        'board_title': board_title,
    }
    if request.method == 'POST':
        title = request.POST.get('column_title')
        column = Column(title=title, board_id=board_id)
        column.save()
        return redirect('view_board', board_id)
    return render(request, 'add_column.html', context)


def edit_task(request, board_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_column = get_object_or_404(Column, pk=task.column_id)
    columns = Column.objects.filter(board_id=board_id)
    priority_choices = ['Easy', 'Medium', 'Hard']
    deadline_time = task.deadline
    deadline = deadline_time.strftime('%Y-%m-%dT%H:%M')
    context = {
        'task': task,
        'board_id': board_id,
        'task_id': task_id,
        'task_column': task_column,
        'columns': columns,
        'priority_choices': priority_choices,
        'deadline': deadline,
    }
    if request.POST.get('edit'):
        task.id = task_id
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.column_id = request.POST.get('column')
        task.deadline = request.POST.get('deadline')
        task.priority = request.POST.get('priority')
        task.save()
        return redirect('view_board', board_id)
    if request.POST.get('delete'):
        Task.objects.filter(pk=task_id).delete()
        return redirect('view_board', board_id)
    return render(request, 'edit_task.html', context)


def add_board(request):
    if request.method == 'POST':
        board_id = Board.objects.order_by('-id').first().id + 1
        board_title = request.POST.get('board_title')
        board = Board(id=board_id, title=board_title)
        board.save()
        columns = request.POST.get('columns')
        columns = columns.split(',')
        print(columns)
        for column in columns:
            column_model = Column(title=column.strip(), board_id=board_id)
            column_model.save()
        return redirect('index')
    return render(request, 'add_board.html')