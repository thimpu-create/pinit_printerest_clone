from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import Http404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

import json

from django.contrib import messages

from boards.forms import CreateBoardForm
from .forms import UserRegistrationForm, UserLoginForm, EditProfileForm
from django.contrib.auth.models import User
from . models import Follow,Profile
from pins.models import Pin
from boards.models import Board


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            check_user = User.objects.filter(
                Q(username=data['username']) | Q(email=data['email'])
                # username = data['username']
            )
            if not check_user:
                User.objects.create_user(
                    email=data['email'], username=data['username'], password=data['password'],
                    first_name= data['fname'], last_name = data['lname']
                )
                user = User.objects.get(username = data['username'])
                Profile.objects.create(
                    user = user,
                    fname = data['fname'],
                    lname = data['lname']
                )
                # return HttpResponse('Succesful')
                return redirect('accounts:user_login')
            else:
                return HttpResponse('ALready exist')
    else:
        form = UserRegistrationForm()
    context = {'title':'Signup', 'form':form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home:home')
            else:
                return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserLoginForm()
        context = {'title':'Login', 'form': form}
        return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    boards = user.board_user.all()
    created_boards = Board.objects.filter(User = user)
    pins = Pin.objects.filter(user=request.user).defer('date_created')

    # j_file = pins.values()
    # with open("pins.json",'w' ) as file:
    #     for f in j_file:
    #         f = json.dumps(f)
    #         file.write(f)
    # print('Done')

    pins_on_board = Pin.objects.filter(board = created_boards[0].id)
    # print(pins_on_board)
    is_following = Follow.objects.filter(user=user)
    is_followed_by = Follow.objects.filter(following=user)
    create_board_form = CreateBoardForm()
    context = {
        'user': user,
        'boards':boards,
        'pins': pins,
        'is_following': is_following,
        'is_followed_by': is_followed_by,
        'created' : created_boards
        # 'create_board_form':create_board_form
    }
    return render(request, 'profile.html', context)

# @login_required
# def follow(request, username):
#     user = get_object_or_404(User, username=username)
#     check_user = Follow.objects.filter(follower=request.user, following=user)
#     if user == request.user:
#         raise Http404
#     elif check_user.exists():
#         raise Http404
#     else:
#         follow = Follow.objects.create(follower=request.user, following=user)
#         follow.save()
#     return redirect(request.META.get('HTTP_REFERER'))


# @login_required
# def unfollow(request, username):
#     user = get_object_or_404(User, username=username)
#     following = Follow.objects.filter(following=user).delete()
#     return redirect(request.META.get('HTTP_REFERER'))


# @login_required
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     boards = user.board_user.all()
#     is_following = request.user.followers.filter(following=user).first()
#     create_board_form = CreateBoardForm()
#     context = {
#         'user': user,
#         'boards':boards,
#         'is_following': is_following,
#         'create_board_form':create_board_form
#     }
#     return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)
        context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'edit_profile.html', context)
