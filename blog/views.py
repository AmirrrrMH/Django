from django.shortcuts import render


def blog_home(request):
    context = {'author': 'atena', 'title': 'Lorem ipsum dolor sit amet.',
               'descript': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. In blanditiis ex ratione molestias earum, consequuntur quos! Autem exercitationem fugit amet.'}
    return render(request, 'blog/blog.html', context)


def blog_single(request):
    return render(request, 'blog/blog-single.html')
