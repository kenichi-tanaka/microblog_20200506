from django.shortcuts import render
from django.views import generic
from .models import Blog
from django.urls import reverse_lazy, reverse
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogIndexView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    template_name = "blog/blog_create_form.html"
    form_class = BlogForm
    # fields = ["content"]
    success_url = reverse_lazy('blog:index')

    login_url = '/login'

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '保存に失敗しました')
        return super().form_invalid(form)



class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_update_form.html"

    login_url = '/login'

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '更新されました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '更新に失敗しました')
        return super().form_invalid(form)
"""
    success_url = reverse_lazy('blog:index')
"""

class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:index')

    login_url = '/login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '削除しました')
        return super().delete(request, *args, **kwargs)
