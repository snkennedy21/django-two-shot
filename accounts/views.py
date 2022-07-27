from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

def signup(request):
  form = UserCreationForm()

  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password1')

    print(username)
    print(password)
    user = User.objects.create_user(username, f'{username}@email.com', password)

    print(user)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, "Username Or password does not exist")

  context = {
    "form": form
  }

  return render(request, 'registration/signup.html', context)

