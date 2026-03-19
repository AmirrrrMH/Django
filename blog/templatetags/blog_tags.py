from django import template
from blog.models import Post, Category, Tag

register = template.Library()


@register.simple_tag()
def hello():
    return "kir"


@register.simple_tag(name="get")
def func():
    posts = Post.objects.all()
    return posts


@register.filter(name="snip")
def func(value, arg):
    word = value.split()
    return word[:arg]


@register.inclusion_tag("blog/blog-latest.html")
def latest():
    posts = Post.objects.filter(status=1).order_by("-published_date")[:3]
    return {"posts": posts}


@register.inclusion_tag("blog/blog-categories.html", name="cate")
def catpost():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"categories": cat_dict}


@register.inclusion_tag("blog/blog-tags.html", name="tage")
def tagpost():
    posts = Post.objects.filter(status=1)
    tags = Tag.objects.all()
    tag_dict = {}
    for name in tags:
        tag_dict[name] = posts.filter(tag=name).count()
    return {"tags": tag_dict}
