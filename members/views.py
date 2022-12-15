import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *

def welcome(request):
    context = {}
    return render(request, 'welcome.html', context)

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
            
    context = {'form': form}
    return render(request, 'members/register.html', context)

# def login(request):
#     context = {}
#     return render(request, 'members/login.html', context)
    

def join_sacco(request):
    form = MemberRegForm()
    
    if request.method == 'POST':
        form = MemberRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
            
    context = {'form': form}
    return render(request, 'members/join_sacco.html', context)

def create_sacco(request):
    form = SaccoForm()
    
    if request.method == 'POST':
        form = SaccoForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'members/create_sacco.html', context)

def dashboard(request):
    members = RegisterMember.objects.all()
    mem_count = RegisterMember.objects.all().count()
    amount = mem_count*10000

    paid = RegisterMember.objects.filter(received=True)
    unpaid = RegisterMember.objects.filter(received=False)
    
    t_list = unpaid
    next_mem = random.choice(t_list)
    
    context = {'members': members, 'paid': paid, 'unpaid': unpaid, 'next_mem': next_mem, 'amount':amount}
    return render(request, 'members/dashboard.html', context)

def roster(request):
    members = RegisterMember.objects.all()
    
    context = {'members': members}
    return render(request, 'members/roster.html', context)

def paid(request):
    members = RegisterMember.objects.filter(received=True)
    
    context = {'members': members}
    return render(request, 'members/paid.html', context)

def unpaid(request):
    members = RegisterMember.objects.filter(received=False)
    
    context = {'members': members}
    return render(request, 'members/unpaid.html', context)

def update_list(request, pk):
    mem = RegisterMember.objects.get(id=pk)
    members = MemberRegForm(instance=mem)
    context = {'members':members}
    return render(request, 'members/roster.html', context)
