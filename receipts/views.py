from django.shortcuts import render
from .models import Receipt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def receipts(request):
  user = request.user
  receipts = Receipt.objects.get(purchaser=user)

  context = {
    "receipts": receipts
  }

  return render(request, 'receipts/list.html', context)
