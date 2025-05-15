from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Board
from .forms import BoardForm

# Create your views here.
class BoardListView(ListView):
    model = Board
    template_name = 'board_list.html'
    context_object_name = 'boards'


class BoardDetailView(DetailView):
    model = Board
    template_name = 'board_detail.html'
    context_object_name = 'board'


class BoardCreateView(CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'board_form.html'
    success_url = reverse_lazy('board_list')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)