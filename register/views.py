from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    if request.user.is_authenticated:
        messages.error(request, 'You are already signed up and logged in!!')
        return redirect('homepage')

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(request, username=new_user.username, password=form.cleaned_data['password1'])
            if user:
                login(request, user)
            messages.success(request, 'Account created successfully. Update your profile now.')
            return redirect('editprofile')
        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'registration/signup.html', {'form':form})

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    form = Profile
    fields = '__all__'
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        return self.request.user.profile
