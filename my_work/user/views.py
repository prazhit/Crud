from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm
from .models import User

def show_user(request):
    users = User.objects.all()
    return render(request,'home.html',{'users':users})

def add_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("show_user")

    return render(request, 'add_user.html',{'form':form})

def edit_user(request,id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('show_user')
    return render(request, 'add_user.html', {'form': form},{'user':user})

def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('show_user')
