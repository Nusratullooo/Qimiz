from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from home.models import ContactMessage, Phone, About, Chef
from product.models import Category, Product, Comment, Order
from home.forms import ContactForm, OrderForm
from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Blog


def home(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    phone = Phone.objects.all()
    product_latest = Product.objects.filter(status='True').order_by('id')
    product_slider = Product.objects.filter(status='True').order_by('id')
    product_picked = Product.objects.filter(status='True').order_by('?')
    context = {
        'category': category,
        'blog': blog,
        'phone': phone,
        'product_latest': product_latest,
        'product_slider': product_slider,
        'product_picked': product_picked
       }
    return render(request, 'index.html', context)


def product_detail(request, id, slug):
    product = Product.objects.get(pk=id)
    category = Category.objects.all().order_by('id')
    comments = Comment.objects.filter(product_id=id)
    product_image = Product.objects.filter(category_id=id)
    product_name = Product.objects.filter(category_id=id)
    comment_product_all = comments.count()
    product_latest = Product.objects.filter(status='True').order_by('-id')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.amount = form.cleaned_data['amount']
            data.category = form.cleaned_data['category']
            data.food = form.cleaned_data['food']
            data.address = form.cleaned_data['address']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your order is successfully saved !")
            return redirect('home')
    form = OrderForm
    context = {
        'form': form,
        'product': product,
        'category': category,
        'comment_product_all': comment_product_all,
        'product_latest': product_latest,
        'comments': comments,
        'product_image': product_image,
        'product_name': product_name
    }
    return render(request, 'product_details.html', context)


def category_product(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    product_latest = Product.objects.filter(status='True').order_by('-id')[:8]
    paginator = Paginator(products, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'products': products,
        'product_latest': product_latest
    }
    return render(request, 'menu.html', context)


def contact(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Message is successfully saved !")
            return redirect('home')
    form = ContactForm
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'contact.html', context)


def about(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    product_latest = Product.objects.all().order_by('?')
    about = About.objects.all()
    chef = Chef.objects.all()
    context = {
        'product_latest': product_latest,
        'about': about,
        'blog': blog,
        'chef': chef,
        'category': category
    }
    return render(request, 'about.html', context)


def chef(request, id):
    category = Category.objects.all()
    chefs = Chef.objects.get(pk=id)
    context = {
        'chefs': chefs,
        'category': category
    }
    return render(request, 'chef.html', context)
