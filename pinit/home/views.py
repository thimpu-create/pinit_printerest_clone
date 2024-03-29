from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from pins.models import Pin
from django.http import HttpResponse
from boards.models import Board
from pins.models import Comment
from django.db.models import Prefetch


@login_required
def download(request, filename):
    with open(filename, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'image/png'
        return response
    
@login_required
def save_pin_profile(request,pin_id):
    if request.method == 'POST':
        cur_url = request.META['HTTP_REFERER']
        p=Pin.objects.get(id = pin_id)
        b=Board.objects.filter(User=request.user,title = "profile").first()
        b.pins.add(p)
        print("done")
        return redirect('home:home')
    

@login_required
def search_pins(request):
    search_key = request.POST.get('q')
    if request.method == 'POST':
        pins = Pin.objects.filter(title__contains=search_key)
        context = {
            'pins' : pins,
        }
    return render(request,'search.html',context)


@login_required
def home(request):
    pins = Pin.objects.order_by('-date_created')
    comments = Comment.objects.filter(
            pins__user_id=request.user
        ).exclude(user_id=request.user).prefetch_related(
                                Prefetch('pins', queryset=Pin.objects.filter(user_id=request.user))
                                )
    context = {'pins' : pins ,
               'comments' : comments,
               }
    return render(request,'home.html',context)
