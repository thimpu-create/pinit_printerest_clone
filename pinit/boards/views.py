from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import CreateBoardForm
from pins.models import Board
from django.db.models import Q


@login_required
def create_board(request):
    form = CreateBoardForm()
    context = {
        "forms" : form
    }
    if request.method == 'POST':
        form = CreateBoardForm(request.POST, instance = request.user)
        if form.is_valid():
            title1 = form.cleaned_data.get('title')
            vis = form.cleaned_data.get('is_private')
            check_name = Board.objects.filter(
                Q(User=request.user) & Q(title = title1)
            )
            if not check_name:
                is_private = request.POST.get('is_private')
                if is_private == 'on':
                    is_private = True
                else:
                    is_private = False
                Board.objects.create(User=request.user,title=title1, is_private = vis)
                return redirect('pins:create_pin')
        return redirect('pins:create_pin')
    
    return render(request, 'board.html',context)
    
@login_required
def board_detail(request, username, board_name):
    board = get_object_or_404(Board,User = username, title=board_name)
    pins = board.pins.all()
    context = {'pins': pins, 'board': board}
    return render(request, 'board_detail.html', context)
                    
