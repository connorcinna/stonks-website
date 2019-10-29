from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def stonk_image_view(request):

    if request.method == 'POST':
        form = StonkForm(request.POST, request.FILES)
         if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'stonk_image_form.html', {'form' : form}) 
  
def success(request): 
    return HttpResponse('successfuly uploaded') 
# Create your views here.
