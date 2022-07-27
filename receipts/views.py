from django.shortcuts import redirect, render
from .models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ReceiptForm, ExpenseCategoryForm, AccountForm
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


def expense_list(request):
  user = request.user
  categories = ExpenseCategory.objects.filter(owner=user)

  context = {
    "categories": categories
  }

  return render(request, 'receipts/expense_list.html', context)


def accounts_list(request):
  user = request.user
  accounts = Account.objects.filter(owner=user)

  context = {
    "accounts": accounts
  }

  return render(request, 'receipts/accounts_list.html', context)


@login_required
def create_expense_category(request):
  form = ExpenseCategoryForm()
  if request.method == "POST":
    form = ExpenseCategoryForm(request.POST)
    if form.is_valid():
      category = form.save(commit=False)
      category.owner = request.user
      category.save()
      return redirect('expenses_list')
  

  context = {
    "form": form
  }
  return render(request, 'receipts/create_category.html', context)


@login_required
def create_account(request):
  form = AccountForm()
  if request.method == "POST":
    form = AccountForm(request.POST)
    if form.is_valid():
      account = form.save(commit=False)
      account.owner = request.user
      account.save()
      return redirect('accounts_list')

  context = {
    "form": form
  }

  return render(request, 'receipts/create_account.html', context)