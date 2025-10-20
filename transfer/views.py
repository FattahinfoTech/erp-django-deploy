# transfer/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TransferManage
from .forms import TransferManageForm

@login_required
def transfer_create(request):
    transfers = TransferManage.objects.filter(status='Pending')
    if request.method == 'POST':
        form = TransferManageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transfer_create')
    else:
        form = TransferManageForm()
    return render(request, 'transfer/transfer_create.html', {'transfers': transfers, 'form': form})

@login_required
def transfer_approve(request):
    transfers = TransferManage.objects.filter(status='Pending')
    if request.method == 'POST':
        form = TransferManageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transfer_approve')
    else:
        form = TransferManageForm()
    return render(request, 'transfer/transfer_approve.html', {'transfers': transfers, 'form': form})

@login_required
def transfer_receive(request):
    transfers = TransferManage.objects.filter(status='Approved')
    return render(request, 'transfer/transfer_receive.html', {'transfers': transfers})