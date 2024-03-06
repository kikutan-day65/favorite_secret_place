from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def login_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/login_register.html', {'form': form})
