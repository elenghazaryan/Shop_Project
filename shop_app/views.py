from django.shortcuts import render
from django.views import generic
from .forms import UserForm
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
    return render(request, 'shop_app/index.html')


def cart(request, id):
    items_list = []
    item = Products.objects.get(pk=id)
    if item not in items_list:
        items_list.append(item)
    # orders_in_cart = Order.objects.all()
    context = {'products_in_cart': items_list}
    return render(request, 'shop_app/cart.html', context)


def shop(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'shop_app/shop.html', context)


def shipping(request):
    return render(request, 'shop_app/shipping.html')


def payment(request):
    return render(request, 'shop_app/payment.html')


def order(request):
    return render(request, 'shop_app/order.html')


def thanks(request):
    return render(request, 'shop_app/thanks.html')


def my_account(request):
    return render(request, 'shop_app/my_account.html')


def my_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'shop_app/my_orders.html', context)


def product(request, id):
    pr = Products.objects.get(pk=id)
    if request.method == 'POST':
        review = request.POST['message']
        Review.objects.create(
            user_id=id,
            product=pr,
            review=review,
        )
        messages.success(request, "Your comment added successfully")
    reviews = Review.objects.filter(product=pr).order_by('-id')
    context = {'product': pr, 'reviews': reviews}
    return render(request, 'shop_app/product.html', context)


# def login(request):
#     return render(request, 'registration/login.html')


def register(request):
    form = UserForm
    if request.method == 'POST':
        reg_form = UserForm(request.POST)
        if reg_form.is_valid():
            # User.objects.create(**reg_form)
            reg_form.save()
            messages.success(request, 'User successfully registered.')
    return render(request, 'shop_app/register.html', {'form': form})


