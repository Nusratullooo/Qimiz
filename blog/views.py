from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.http import HttpResponseRedirect
from blog.forms import Comment_detail_Form
from blog.models import Blog, Comment_blog
from product.models import Category
from django.contrib import messages
from django.shortcuts import render


def blog(request):
    blog = Blog.objects.all()
    category = Category.objects.all()
    comment_blog = Comment_blog.objects.all()
    paginator = Paginator(blog, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'blog': blog,
        'category': category,
        'comment_blog': comment_blog,
        }
    return render(request, 'blog.html', context)


def blog_detail(request, id):
    category = Category.objects.all()
    blog_detail = Blog.objects.get(pk=id)
    comment_blog = Comment_blog.objects.filter(blog_id=id)
    comment_blog_all = comment_blog.count()
    context = {
        'category': category,
        'blog_detail': blog_detail,
        'comment_blog': comment_blog,
        'comment_blog_all': comment_blog_all
    }
    return render(request, 'blog_details.html', context)


def comment_blog(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            data.save()
            messages.success(request, "Your message is successfully saved !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
