from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from .models import Board, Comment
from .forms import BoardForm, LoginForm, FilterForm, BoardEditingForm, CommentForm, CustomUserCreationForm
from .mixins import UserIsOwnerMixin, UserIsOwnerCommentMixin

class BoardListView(LoginRequiredMixin, ListView):
    model = Board
    template_name = 'board_list.html'
    context_object_name = 'boards'

    def get_queryset(self):
        queryset = Board.objects.all().order_by('-priority')
        self.form = FilterForm(self.request.GET or None)
        if self.form.is_valid():
            priority = self.form.cleaned_data.get('priority')
            if priority:
                queryset = queryset.filter(priority=priority)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.form
        return context

class BoardDetailView(LoginRequiredMixin, DetailView):
    model = Board
    template_name = 'board_detail.html'
    context_object_name = 'board'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # Додаємо форму до контексту
        return context
class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'board_form.html'
    success_url = reverse_lazy('board_list')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class BoardEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Board
    form_class = BoardEditingForm
    template_name = 'board_form.html'  
    success_url = reverse_lazy('board_list')

class BoardDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
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
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class CommentCreateView(View):
    def post(self, request, board_id):
        board = get_object_or_404(Board, id=board_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.user = request.user  
            comment.save()
        return redirect('board_detail', pk=board.id)
    

class CommentLikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        if user in comment.liked_by.all():
            comment.liked_by.remove(user)
        else:
            comment.liked_by.add(user)
            comment.disliked_by.remove(user) 

        return redirect(request.META.get('HTTP_REFERER', '/'))


class CommentDislikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        if user in comment.disliked_by.all():
              comment.disliked_by.remove(user)
        else:
            comment.disliked_by.add(user)
            comment.liked_by.remove(user)  

        return redirect(request.META.get('HTTP_REFERER', '/'))
    

class CommentUpdateView(LoginRequiredMixin, UserIsOwnerCommentMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'edit_comment.html'

    def get_success_url(self):
        return reverse('board_detail', kwargs={'pk': self.object.board.id})
    
class CommentDeleteView(LoginRequiredMixin, UserIsOwnerCommentMixin, DeleteView):
    model = Comment
    template_name = 'delete_comment.html'

    def get_success_url(self):
        return reverse('board_detail', kwargs={'pk': self.object.board.id})