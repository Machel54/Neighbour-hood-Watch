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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {"form": form})

@login_required(login_url='/login')
def profile(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)

