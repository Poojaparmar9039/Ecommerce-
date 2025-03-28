from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,address,order_details,delivery_update
import random


def home(request):
    products =product.objects.all()
    random_image=list(product.objects.order_by('?')[:4])
    categories = product.objects.values_list('category', flat=True).distinct() 
    category_dict = {} 
    for cat in categories:
        category_dict[cat] = product.objects.filter(category=cat)
    return render(request, 'home.html', {'products':products,'category_dict': category_dict,'random':random_image})

def cartDetail(request,id):
    product_obj=product.objects.get(id=id)
    print("------------------------",product_obj)
    return render(request,'cartDetail.html',{'product':product_obj})

#--------------------------------------------add delete and view cart-----------------------------------------------
def AddtoCart(request,id):
    products=product.objects.get(id=id)
    cartlist=request.session.get('cartlist',[])
    if id not in cartlist: 
        cartlist.append(id)
    request.session['cartlist']=cartlist   #updates cawrt
    request.session.modified=True
    items=product.objects.filter(id__in=cartlist)      #id__in will retrieve all products in single query
    cart_num=len(cartlist)
    total_price = sum(item.price for item in items) if items else 0
    print("-------------------",total_price)
    return render(request,'AddtoCart.html',{'cartlist':items,'cart_num':cart_num,'total_price':total_price})


def deletecart(request,id):
    cartlist=request.session.get('cartlist')
    try:
        id = int(id)  # Convert to integer to avoid type mismatch
        if id in cartlist:
            cartlist.remove(id) 
    except ValueError:
        pass
    request.session['cartlist'] = cartlist
    request.session.modified=True
    return redirect('viewcart')

def viewcart(request):
    cartlist = request.session.get('cartlist', [])
    cart_products = product.objects.filter(id__in=cartlist)
    return render(request, 'AddtoCart.html', {'cartlist': cart_products})

#-------------------------------------------------------add ,delete and view the wishlist--------------------------

def wishlist(request,id):
    item=product.objects.get(id=id)
    list=request.session.get('list',[])
    if id not in list:
        list.append(id)
    request.session['list']=list
    request.session.modified=True
    item=product.objects.filter(id__in=list) 
    return render(request,'wishlist.html',{'list':item})

def deletelist(request,id):
    item=product.objects.get(id=id)
    list=request.session.get('list')
    if id in list:
        list.remove(id)
    request.session['list']=list
    request.session.modified=True
    item=product.objects.filter(id__in=list)
    return redirect('viewlist')

def viewlist(request):
    list = request.session.get('list', [])
    cart_products = product.objects.filter(id__in=list)
    return render(request, 'wishlist.html', {'list': cart_products})

#-----------------------------------------------category------------------------------------------

def product_category(request,category):
    category_item=product.objects.filter(category=category)
    return render(request,'category.html',{'category':category_item})

#------------------------------------------random image--------------------------------------------
def best_seller(request):
    random_image=list(product.objects.order_by('?')[:15])
    return render(request,'best.html',{'random_image':random_image})
#--------------------------------------------------------------------------------------------------
def shop(request):
    random_image=list(product.objects.order_by('?')[:30])
    return render(request,'shop.html',{'random_image':random_image})

def buy(request,id):
    item=product.objects.get(id=id)
    return render(request,'Buy.html',{'product':item})

#-------------------------------------order details-------------------------------------------------

def payment(request,id):
    item=product.objects.get(id=id)
    return render(request,'payment.html',{'item':item})

def place_order(request,id):
    item=product.objects.get(id=id)
    order=order_details(product_id=item.id,product_name=item.product_name)
    order.save()
    return render(request,'placeorder.html',{'item':item})

def place_order_cart(request):
    product_ids = request.GET.get('ids')   
    print("Product IDs received:", product_ids)
    if product_ids:
        product_ids = product_ids.split(',')  
        products = product.objects.filter(id__in=product_ids)  

        for item in products:
            order = order_details(product_id=item.id, product_name=item.product_name)
            order.save()

        total_price=sum(item.price for item in products) if products else 0
        print("----------------------------------------",products)
        return render(request, 'placeorder.html', {'items': products,'total_price':total_price})   
    return render(request, 'placeorder.html', {'items': []})




def successful(request):
    return render(request,'successful.html')
#--------------------------------------search category---------------------------------------
def search(request):
    query=request.GET.get('search','')
    category=product.objects.filter(category__icontains=query)
    return render(request,'category.html',{'category':category})

#-------------------------------------address details of user--------------------------------
   
def Address(request):
    return render(request,'Address.html')


def addressDetail(request):
    fullname=request.POST.get('fullname')
    street=request.POST.get('street')
    block=request.POST.get('block')
    city=request.POST.get('city')
    state=request.POST.get('state')
    zip=request.POST.get('zip')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    userDetail=address(name=fullname,street=street,block=block,city=city,state=state,zip_code=zip,phone=phone,email=email)
    userDetail.save()
    print("---------------------------------------------------",fullname,street,block,city,state,zip,phone,email)
    return render(request,'Address.html')


#------------------------------------order details------------------------------------------------------------

def order_update(request):
    updates = delivery_update.objects.filter(order__in=order_details.objects.all()).order_by('-timestamp')[:5]  
    return render(request, 'Delivery.html', {'updates': updates})



