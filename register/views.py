from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def signup(request):
    if request.user.is_authenticated:
        messages.error(request, 'You are already signed up and logged in!!')
        return redirect('homepage')

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('homepage')
        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'registration/signup.html', {'form':form})