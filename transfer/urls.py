# transfer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.transfer_create, name='transfer_create'),
    path('approve/', views.transfer_approve, name='transfer_approve'),
    path('receive/', views.transfer_receive, name='transfer_receive'),
]