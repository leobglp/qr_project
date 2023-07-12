from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm, UserUpdateForm
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Card
from cryptography.fernet import Fernet

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def about(request):
    return render(request, 'users/about.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'cards': Card.objects.filter(author=request.user)
    }

    return render(request, 'users/profile.html', context)

class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['numero', 'validade', 'titular', 'cvv']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Card
    fields = ['numero', 'validade', 'titular', 'cvv']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        card = self.get_object()
        if self.request.user == card.author:
            return True
        return False


class CardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Card
    success_url = '/profile'

    def test_func(self):
        card = self.get_object()
        if self.request.user == card.author:
            return True
        return False