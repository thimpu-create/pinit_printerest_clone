from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import CreatePinForm
# Create your views here.
from .models import Pin


from django.contrib.auth.decorators import login_required

@login_required
def create_pin(request):
    if request.method == 'POST':
        form = CreatePinForm(request.user,request.POST,request.FILES)
        if form.is_valid():
            forms=form.cleaned_data
            Pin.objects.create(
                user = request.user,
                board = forms['board'],
                file = forms['file'],
                title = forms['title'],
                link = forms['link'],
                description = forms['description']
            )
            # print(title1)
            # form.save()
            return redirect( 'accounts:profile',request.user.username)
            # return HttpResponse("Your pin is saved")
    form = CreatePinForm(request.user)
    return render(request,"create_pin.html",{'form':form})