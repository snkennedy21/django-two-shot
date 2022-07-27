from django.urls import path
from . import views

urlpatterns = [
  path('', views.receipts, name="home"),
  path('create/', views.create_receipt, name="create_receipt")
]