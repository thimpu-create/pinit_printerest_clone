from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from pins.models import Pin
from PIL import Image
from django.http import FileResponse,HttpResponse


@login_required
def home(request):
    pins = Pin.objects.order_by('-date_created')
    context = {'pins' : pins ,
               }
    return render(request,'home.html',context)

@login_required
def download(request, filename):
    # filename = "D:\project\pinit\media\pins\lab2_1.jpg"
    print(filename)
    with open(filename, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'image/png'
        return response