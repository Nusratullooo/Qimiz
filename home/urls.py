from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('chef/<int:id>', views.chef, name='chef'),
    path('product_detail/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('category_product/<int:id>/<slug:slug>', views.category_product, name='category_product')
]
