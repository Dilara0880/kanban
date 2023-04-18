from django.http import HttpResponse
from django.shortcuts import render

from board.models import Board


def index(request):
    context = {
        "boards": Board.objects.order_by('id'),
    }
    return render(request, 'index.html', context)


def view_board(request, board_id):
    return HttpResponse(f"You're looking on board #{board_id}")


def create_task(request):
    return HttpResponse("You're creating a new task")


def choose_board(request):
    return HttpResponse("You're choosing a board")
