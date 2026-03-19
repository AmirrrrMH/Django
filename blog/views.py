from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category, Tag
from django.http import HttpResponseNotFound


def blog_home(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kc := kwargs.get("cat_name") != None:
        posts = posts.filter(category__name=kwargs["cat_name"])
    if kwargs.get("author_username") != None:
        posts = posts.filter(author__username=kwargs["author_username"])
    categories = Category.objects.all()[:3]
    context = {"posts": posts, "categories": categories}
    return render(request, 'blog/blog.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    categories = Category.objects.all()
    context = {"post": post, "categories": categories}
    return render(request, 'blog/blog-single.html', context)


def test(request):
    return render(request, 'blog/test.html')


def search(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {"posts": posts}
    return render(request, 'blog/blog.html', context)

# def cat_post(request, cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name=cat_name)
#     context = {"posts": posts}
#     return render(request, 'blog/blog.html', context)
