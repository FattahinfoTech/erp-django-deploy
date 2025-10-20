# petty_cash_transaction/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PettyCash
from .forms import PettyCashForm

@login_required
def petty_cash_entry(request):
    petty_cash_list = PettyCash.objects.all()
    if request.method == 'POST':
        form = PettyCashForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('petty_cash_entry')
    else:
        form = PettyCashForm()
    return render(request, 'petty_cash_transaction/petty_cash_entry.html', {
        'petty_cash_list': petty_cash_list,
        'form': form
    })

@login_required
def petty_cash_audit(request):
    petty_cash_list = PettyCash.objects.filter(status='Pending')
    return render(request, 'petty_cash_transaction/petty_cash_audit.html', {
        'petty_cash_list': petty_cash_list
    })

@login_required
def petty_cash_account(request):
    petty_cash_list = PettyCash.objects.filter(status='Audited')
    return render(request, 'petty_cash_transaction/petty_cash_account.html', {
        'petty_cash_list': petty_cash_list
    })

@login_required
def petty_cash_confirm(request):
    petty_cash_list = PettyCash.objects.filter(status='Confirmed')
    return render(request, 'petty_cash_transaction/petty_cash_confirm.html', {
        'petty_cash_list': petty_cash_list
    })