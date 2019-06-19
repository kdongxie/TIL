from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
from IPython import embed

# Create your views here.

def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)

def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        #embed()
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            board = Board.objects.create(title=title, content=content)
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'boards/create.html', context)

def detail(request, board_pk):
    #board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)

def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board.title = form.cleaned_data.get('title')
            board.content = form.cleaned_data.get('content')
            board.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(initial=board.__dict__)
    context = {'form': form}
    return render(request, 'boards/create.html', context)

