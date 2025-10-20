# settings_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import ClusterZone, FinishProductType, CustomerCategory, EmailSetting
from .forms import ClusterZoneForm, FinishProductTypeForm, CustomerCategoryForm, EmailSettingForm

@login_required
def cluster_zone(request):
    clusters = ClusterZone.objects.all()
    if request.method == 'POST':
        form = ClusterZoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cluster_zone')
    else:
        form = ClusterZoneForm()
    
    # Pagination
    paginator = Paginator(clusters, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'settings_app/cluster_zone.html', {
        'clusters': page_obj,
        'form': form
    })

@login_required
def finish_product_type(request):
    product_types = FinishProductType.objects.all()
    if request.method == 'POST':
        form = FinishProductTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finish_product_type')
    else:
        form = FinishProductTypeForm()
    return render(request, 'settings_app/finish_product_type.html', {
        'product_types': product_types,
        'form': form
    })

@login_required
def customer_category(request):
    categories = CustomerCategory.objects.all()
    if request.method == 'POST':
        form = CustomerCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_category')
    else:
        form = CustomerCategoryForm()
    
    # Pagination
    paginator = Paginator(categories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'settings_app/customer_category.html', {
        'categories': page_obj,
        'form': form
    })

@login_required
def email_setting(request):
    email_settings = EmailSetting.objects.all()
    if request.method == 'POST':
        form = EmailSettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_setting')
    else:
        form = EmailSettingForm()
    return render(request, 'settings_app/email_setting.html', {
        'email_settings': email_settings,
        'form': form
    })