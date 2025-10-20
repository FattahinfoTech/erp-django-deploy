# adjustment/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProductPlus, ProductMinus
from .forms import ProductPlusForm, ProductMinusForm

@login_required
def product_plus(request):
    adjustments = ProductPlus.objects.all()
    if request.method == 'POST':
        form = ProductPlusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_plus')
    else:
        form = ProductPlusForm()
    return render(request, 'adjustment/product_plus.html', {'adjustments': adjustments, 'form': form})

@login_required
def product_plus_approve(request):
    adjustments = ProductPlus.objects.filter(status='Pending')
    return render(request, 'adjustment/product_plus_approve.html', {'adjustments': adjustments})

@login_required
def product_minus(request):
    adjustments = ProductMinus.objects.all()
    if request.method == 'POST':
        form = ProductMinusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_minus')
    else:
        form = ProductMinusForm()
    return render(request, 'adjustment/product_minus.html', {'adjustments': adjustments, 'form': form})

@login_required
def product_minus_approve(request):
    adjustments = ProductMinus.objects.filter(status='Pending')
    return render(request, 'adjustment/product_minus_approve.html', {'adjustments': adjustments})