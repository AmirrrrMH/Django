from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Tag
from django.http import HttpResponseNotFound


def blog_home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {"posts": posts, "categories": categories, "tags": tags}
    return render(request, 'blog/blog.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    categories = Category.objects.all()
    context = {"post": post, "categories": categories}
    return render(request, 'blog/blog-single.html', context)


def test(request):
    return render(request, 'blog/test.html')
