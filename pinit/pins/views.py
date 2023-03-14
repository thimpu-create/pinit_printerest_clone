from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import CreatePinForm,SaveToBoard,CommentForm
# Create your views here.
from .models import Pin,Board,Comment
from accounts.models import Follow
from django.contrib.auth.models import User


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

            b=Board.objects.filter(User = request.user, title = 'profile' ).first()
            b.pins.add(p)
            # print(title1)
            # form.save()
            return redirect( 'accounts:profile_saved',request.user.username)
            # return HttpResponse("Your pin is saved")
    form = CreatePinForm(request.user)
    return render(request,"create_pin.html",{'form':form})


@login_required
def pin_detail(request,id):
    pin = Pin.objects.filter(id=id).first()
    saved_pin = request.user.pin_user.filter(id=id).first()
    is_following = request.user.user.filter(following=pin.user).first()
    save_to_board_form = SaveToBoard(request.user, instance=saved_pin)
    # edit_form = EditPinForm(request.user, instance=pin)
    comment_form = CommentForm()
    context = {
        'pin': pin,
        'save_to_board_form': save_to_board_form,
        'is_following': is_following,
        # 'edit_form': edit_form,
        'comment_form': comment_form,
        # 'related_pins': get_related_pins(id)
    }
    return render(request, 'pin_detail.html', context)


@login_required
def follow_user(request,id):
    user = User.objects.get(id = id)
    # request.user follows user
    Follow.objects.create(user = request.user, following = user)
    prev_url = request.META.get('HTTP_REFERER')#Very verry important!!!!
    return redirect(prev_url)


@login_required
def unfollow_user(request,id):
    user = Follow.objects.get(user = request.user,following = id)
    # request.user follows user
    user.delete()
    prev_url = request.META.get('HTTP_REFERER')#Very verry important!!!!
    return redirect(prev_url)

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

def delete_comment(request, id):
    comments = Comment.objects.get(user = request.user,id = id)
    # request.user follows user
    comments.delete()
    prev_url = request.META.get('HTTP_REFERER')#Very verry important!!!!
    return redirect(prev_url)