from django.shortcuts import render, redirect
from .models import Boards

# Create your views here.
def index(request):
    return render(request, 'boards/index.html')

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Boards(title=title, content=content)
        board.save()
        return redirect('boards:index')
    else:
        return render(request, 'boards/create.html')