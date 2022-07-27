from django.shortcuts import redirect, render
from .models import Receipt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ReceiptForm
from django.shortcuts import redirect


@login_required
def receipts(request):
  user = request.user
  receipts = Receipt.objects.filter(purchaser=user)

  print(receipts)

  context = {
    "receipts": receipts
  }

  return render(request, 'receipts/list.html', context)


@login_required
def create_receipt(request):
  form = ReceiptForm()
  if request.method == "POST":
    form = ReceiptForm(request.POST)
    if form.is_valid():
      item = form.save(commit=False)
      item.purchaser = request.user
      item.save()
      return redirect('home')

  context = {
    "form": form
  }

  return render(request, 'receipts/create.html', context)