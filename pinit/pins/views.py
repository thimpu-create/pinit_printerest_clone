from django.shortcuts import render,redirect, get_object_or_404
from . forms import CreatePinForm,SaveToBoard,CommentForm,EditPinForm
from .models import Pin,Board,Comment,Like
from django.contrib.auth.decorators import login_required

@login_required
def create_pin(request):
    if request.method == 'POST':
        form = CreatePinForm(request.user,request.POST,request.FILES)
        if form.is_valid():
            forms=form.cleaned_data
            p=Pin.objects.create(
                user = request.user,
                board = forms['board'],
                file = forms['file'],
                title = forms['title'],
                link = forms['link'],
                description = forms['description']
            )
            b=Board.objects.filter(User = request.user, title = forms['board'] ).first()
            b.pins.add(p)
            b.cover = forms['file']
            b.save()

            b=Board.objects.filter(User = request.user, title = 'profile' ).first()
            b.pins.add(p)
            b.cover = forms['file']
            b.save()

            return redirect( 'accounts:profile_saved',request.user.username)
    form = CreatePinForm(request.user)
    return render(request,"create_pin.html",{'form':form})


@login_required
def pin_detail(request,id):
    pin = Pin.objects.filter(id=id).first()
    pinobj = get_object_or_404(Pin,id = id)
    saved_pin = request.user.pin_user.filter(id=id).first()
    is_following = request.user.user.filter(following=pin.user).first()
    likes = Like.objects.filter(pin = id).count()
    liked = Like.objects.filter(user = request.user, pin=pinobj).count()
    if liked == 0:
        liked = False
    else:
        liked = True
    print(type(likes))
    save_to_board_form = SaveToBoard(request.user, instance=saved_pin, initial={'title': 'profile'})
    edit_form = EditPinForm(request.user, instance=pin)
    comment_form = CommentForm()
    context = {
        'pin': pin,
        'save_to_board_form': save_to_board_form,
        'is_following': is_following,
        'edit_form': edit_form,
        'comment_form': comment_form,
        'like': likes,
        'liked': liked,
    }
    return render(request, 'pin_detail.html', context)

@login_required
def add_comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST, instance = request.user)
        if form.is_valid():
            forms=form.cleaned_data
            pins = Pin.objects.get(id = id)
            Comment.objects.create(pins = pins,
                    user = request.user,
                    text = forms['text']
            )
        print(forms['text'])

    prev_url = request.META.get('HTTP_REFERER')#Very verry important!!!!
    return redirect(prev_url)

@login_required
def delete_comment(request, id):
    comments = Comment.objects.get(user = request.user,id = id)
    comments.delete()
    prev_url = request.META.get('HTTP_REFERER')#Very verry important!!!!
    return redirect(prev_url)


@login_required
def edit_pin(request, id):
    pin = get_object_or_404(Pin, id=id)
    if request.method == 'POST' and request.user == pin.user:
        form = EditPinForm(request.user, request.POST, instance=pin)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            board = Board.objects.filter(id=instance.board.id).first()
            instance.save()
            board.pins.add(instance)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_pin(request, id):
    if request.method == "POST":
        pin = get_object_or_404(Pin, id=id)
        pin.delete()
    return redirect('home:home')

@login_required
def like(request,id):
    print(request.user.id)
    # print(request.pin.id)
    pinOb = get_object_or_404(Pin,id = id)
    print(id)
    # user_id = request.user.id
    if request.method == 'POST':
        check=Like.objects.filter(user = request.user , pin = pinOb).count()
        print(type(check))
        if check==0:
            Like.objects.create(user = request.user,pin = pinOb)
        else:
            likeobj=Like.objects.get(user = request.user,pin=pinOb)
            likeobj.delete()
    prev_url = request.META.get('HTTP_REFERER')#Very verry important!!!!
    return redirect(prev_url)

@login_required
def save_to_board(request,pin_id):
    if request.method == 'POST':
        pinobj = get_object_or_404(Pin,id = pin_id)
        board_title = request.POST.get('board')
        b=Board.objects.filter(id = board_title).first()
        b.pins.add(pinobj)
        b.save()
    prev_url = request.META.get('HTTP_REFERER')#Very verry important!!!!
    return redirect(prev_url)
