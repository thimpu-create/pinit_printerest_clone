from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import CreatePinForm
# Create your views here.
from .models import Pin,Board


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
            b=Board.objects.filter(User = request.user, title = forms['board']).first()
            b.pins.add(p)
            # print(title1)
            # form.save()
            return redirect( 'accounts:profile_saved',request.user.username)
            # return HttpResponse("Your pin is saved")
    form = CreatePinForm(request.user)
    return render(request,"create_pin.html",{'form':form})