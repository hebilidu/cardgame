from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Comment

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


class PostListView(generic.ListView):
    model = Post
    template_name = 'listpage.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'List posts'
        return context


class PostDetailView(generic.DetailView):
    model = Post
    fields = '__all__'    
    template_name = 'viewpage.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id = id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'View post'
        return context


class PostAddView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'editpage.html'
    success_url = reverse_lazy('listpost')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Add post'
        return context


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'editpage.html'
    success_url = reverse_lazy('listpost')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update post'
        return context


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    fields = '__all__'
    template_name = 'viewpage.html'
    success_url = reverse_lazy('listpost')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Delete post'
        return context


class CommentAddView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = '__all__'
    template_name = 'viewpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Comment.Post.get()
        context['action'] = 'Add comment'
        return context