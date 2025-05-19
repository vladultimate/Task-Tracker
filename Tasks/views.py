from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Board
from .forms import BoardForm, LoginForm

# Create your views here.
class BoardListView(LoginRequiredMixin, ListView):
    model = Board
    template_name = 'board_list.html'
    context_object_name = 'boards'


class BoardDetailView(LoginRequiredMixin, DetailView):
    model = Board
    template_name = 'board_detail.html'
    context_object_name = 'board'


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'board_form.html'
    success_url = reverse_lazy('board_list')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class BoardEditView(LoginRequiredMixin, UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'board_form.html'  
    success_url = reverse_lazy('board_list')

class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Board
    template_name = 'board_confirm_delete.html'
    success_url = reverse_lazy('board_list')

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('board_list')  

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Невірний логін або пароль')
            return self.form_invalid(form)
        
        
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')