from django.shortcuts import render, redirect
from .models import Board, Comment


def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}
    return render(request, 'boards/index.html', context) # templates 안의 boards 폴더에 있는 index.html을 랜더하겠다.

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        board = Board(title=title, content=content, image=image)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/create.html')

def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()

    context = {'board': board, 'comments': comments}
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    if request.method =='POST':
        board = Board.objects.get(pk=board_pk)
        board.delete()
        return redirect('boards:index')
    else:
        return render(request, 'boards/detail.html')

def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.image = request.FILES.get('image')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        context = {'board': board}
        return render(request, 'boards/edit.html', context)

def comments_create(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        comment = Comment()
        # comment.board = board 도 가능하나 정확한 명시가 아니다.
        comment.board_id = board.pk
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:detail', board.pk)

def comments_edit(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board_pk)
    else:
        context = {'comment': comment}
        return render(request, 'boards/comment_edit.html', context)

def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method =='POST':
        comment.content = request.POST.get('content')
        comment.delete()
        return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)