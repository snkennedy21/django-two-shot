from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

def signup(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()

      if user is not None:
        login(request, user)
        return request('home')
      else:
        messages.error(request, "Username Or password does not exist")
  
  else:
    form = UserCreationForm()
    context = {
      "form": form
      }
    return render(request, 'registration/signup.html', context)

