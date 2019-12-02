from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# def welcome(request):
#     return render(request, 'index.html')

@login_required(login_url='/login')
def index(request):
    title = "Neighbourhood"
    user = Profile.objects.get(user=request.user.id)
    business = Business.objects.all().filter(hood=user.hood)
    context = {
        "title": title,
        "business": business
    }
    return render(request, 'index.html', context)

