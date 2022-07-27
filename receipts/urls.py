from django.urls import path
from . import views

urlpatterns = [
  path('', views.receipts, name="home"),
  path('create/', views.create_receipt, name="create_receipt"),
  path('categories/', views.expense_list, name="expenses_list"),
  path('accounts/', views.accounts_list, name="accounts_list"),
  path('categories/create/', views.create_expense_category, name="create_category")
]