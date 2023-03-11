from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import CreateBoardForm
from pins.models import Pin,Board
# from pins.forms import SaveToBoard
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse


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
    board = get_object_or_404(Board,User = request.user, title=board_name)
    pins = board.pins.all()
    context = {'pins': pins, 'board': board}
    return render(request, 'board_detail.html', context)


def render_created_board(request):
    return render(request,"created_board.html")
                    
# @login_required
# def edit_board(request, id):
#     board = request.user.board_user.filter(id=id).first()
#     if request.method == 'POST':
#         form = EditBoardForm(request.POST, request.FILES, instance=board)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:profile', request.user.username)
#     form = EditBoardForm(instance=board)
#     context = {'board': board ,'form': form}
#     return render(request, 'edit_board.html', context)


# @login_required
# def save_to_board(request, id):
#     pin = Pin.objects.filter(id=id).first()
#     saved_pin = request.user.pin_user.filter(id=id).first()
#     if request.method == 'POST':
#         form = SaveToBoard(request.user, request.POST, instance=saved_pin)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = pin.user
#             instance.save()
#             board = Board.objects.filter(id=request.POST.get('board')).first()
#             board.pins.add(pin)
#     return redirect(request.META.get('HTTP_REFERER'))


# @login_required
# def remove_from_board(request, pin_id, board_id):
#     board = request.user.board_user.filter(id=board_id).first()
#     get_pin = board.pins.filter(id=pin_id).first()
#     if get_pin:
#         board.pins.remove(get_pin)
#     return redirect(request.META.get('HTTP_REFERER'))
