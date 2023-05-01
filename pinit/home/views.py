from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from pins.models import Pin
# from PIL import Image
from django.http import FileResponse,HttpResponse,JsonResponse
from boards.models import Board
from django.core.paginator import Paginator


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
    context = {'pins' : pins ,
               }
    return render(request,'home.html',context)
