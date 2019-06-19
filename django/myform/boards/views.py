from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm
from IPython import embed

# Create your views here.

def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)
@login_required
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        # embed()
        if form.is_valid():
            board = form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form':form}
    return render(request, 'boards/form.html', context)
@login_required
def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board':board}
    return render(request, 'boards/detail.html', context)
@login_required
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)

@login_required
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(instance=board)
    context = {'form':form, 'board':board}
    return render(request, 'boards/form.html', context)