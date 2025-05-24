from django.shortcuts import render,redirect
from django.contrib import messages
from userauth.forms import login_form, register_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_view(request):
    form=register_form(request.POST or None)
    if request.method =='POST' and form.is_valid():
        user=form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(request,'Account created successfully')
        return redirect('login')
    return render(request,'register.html', {'form':form})
def login_view(request):
    form = login_form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('in')  # redirect to index page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out.")
        return render (request,'logout.html')
    else:
        return render(request, 'in.html', {'user': request.user}) 

@login_required
def in_view(request):
    return render(request, 'in.html', {'user': request.user})