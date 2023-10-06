from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Post


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('title', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


def display_contacts(request):
    return render(request, 'catalog/contacts.html')


class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset.filter(published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        views = super().get_object(queryset)
        views.increase_views_count()
        return views


class PostCreateView(CreateView):
    model = Post
    fields = ('name', 'content', 'image', 'published')
    success_url = reverse_lazy('catalog:post_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.name)
            new_post.save()

            return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ('name', 'content', 'image', 'published')
    # success_url = reverse_lazy('catalog:post_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.name)
            new_post.save()

            return super().form_valid(form)

    def get_success_url(self):

        return reverse('catalog:post', args=[self.kwargs.get('pk'), self.kwargs.get('slug')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:post_list')
