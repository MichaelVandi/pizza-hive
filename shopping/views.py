from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from .models import Item, Sub, Item_price_by_size, Item_price_no_size, Topping, Orders
from collections import defaultdict

# Global dictionary of cart items
cart_items = defaultdict(list)
# Create your views here.
@login_required(redirect_field_name='login')
def shopping(request):
    # Items to display in the menu sorted by category
    # Getting datasets by category

    context = {
        "user": request.user,

        "pizzas": Item.objects.filter(category__icontains ='pizza'),
        "subs": Sub.objects.all(),
        "pastas":Item.objects.filter(category__icontains ='pasta'),
        "salads": Item.objects.filter(category__icontains ='salads'),
        "dinner_platters":Item.objects.filter(category__icontains ='dinner'),

        "pizza_prices": Item_price_by_size.objects.filter(name__category__icontains="pizza"),
        "pasta_prices": Item_price_no_size.objects.filter(name__category__icontains="pasta"),
        "salad_prices": Item_price_no_size.objects.filter(name__category__icontains="salads"),
        "dinner_prices": Item_price_by_size.objects.filter(name__category__icontains="dinner")
    }
    return render(request, "menu.html", context)

@login_required(redirect_field_name='login')
def buy_view(request, category, name, pk):
    if request.method== 'POST':
        return render(request, "cart.html")
        
    item = Item.objects.get(pk=pk)
    if "pizza" in category.lower():
        # We now know where to get item size:
        item_size=Item_price_by_size.objects.get(name=item)
        toppings = list(Topping.objects.values_list())
        type_ ="pizza"
    elif "sub" in category.lower():
        item=Sub.objects.get(pk=pk)
        type_ ="sub"
        # Item size and toppings are retrieved from the query set since they are already in the sub table
        item_size="xxx"
        toppings = "xxx"
    elif "pasta" in category.lower() or "salads" in category.lower():
        item_size=Item_price_no_size.objects.get(name=item)
        type_ ="pasta"
        # Toppings cant be applied to pastas and salads
        toppings ="xxx"
    elif "dinner" in category.lower():
        item_size = Item_price_by_size.objects.get(name=item)
        type_ ="dinner"
        # No toppings applicable
        toppings = "xxx"

    context={
        "user": request.user,
        "name": name,
        "category": category,
        "item": item,
        "item_size": item_size,
        "toppings": toppings,
        "type_": type_
    }
    

    return render(request, "buy.html", context)

@login_required(redirect_field_name='login')
def cart_view(request):
# Getting relevant data
    username = request.user.username
    cart_string = str(username +"_cart")

    if request.method== 'POST':
        item_name = request.POST['name']
        item_size = request.POST['size']
        toppings = request.POST['toppings']
        total = request.POST['total']

        all_data ={"name": item_name, "size": item_size, "toppings": toppings, "total": total}
        # Save Data in session
        cart_items[username].append(all_data)
        context = { 
            "user": request.user,
            "items": cart_items[username],
        }
        return render(request, "cart.html", context)

    if request.method== 'GET':
        items = cart_items[username]
        context ={
                "user": request.user,
                "items": items,
        }
   
        return render(request, "cart.html", context)

@login_required(redirect_field_name='login')
def orders_view(request, username):
# Getting relevant data
    username = request.user.username

    if request.method== 'POST':
        username = username
        name = request.POST['name']
        items = request.POST['items']
        total = request.POST['total']

        order = Orders(username = username, name=name, items= items, total_amount = total)
        order.save()
        # Clear Cart
        cart_items[username].clear()
        # Get all orders from the table where username is this user
        context = { 
            "user": request.user,
            "items": Orders.objects.filter(username = username),
        }
        return render(request, "orders.html", context)

    if request.method== 'GET':
        context ={
                "user": request.user,
                "items": Orders.objects.filter(username = username),
        }
   
        return render(request, "orders.html", context)

@login_required(redirect_field_name='login')
def delete_order(request, username):
# If post request was to delete
    if request.method== 'POST':
    
        id_to_delete = int(request.POST['delete'])
        delete_instance = Orders.objects.get(pk=id_to_delete)
        delete_instance.delete()
        # Get all orders from the table where username is this user
        context = { 
            "user": request.user,
            "items": Orders.objects.filter(username = username),
        }
        return render(request, "orders.html", context)
