from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def seller_home(request):
    return render (request,'seller/seller_home.html')


def seller_login(request):
    if request.method =='POST':
      Email=request.POST["email"]
      Password=request.POST["password"]
      try:
            sell=SellerRegistration.objects.get(email=Email , password=Password)
            request.session['seller']=sell.id
            return redirect('seller:seller_dashboard')
      except SellerRegistration.DoesNotExist:

    #   if SellerRegistration.objects.filter(email=Email,password=Password).exists():
    #      return redirect('seller:seller_dashboard')
    #   else:
         return render( request, 'seller/seller_login.html',{'msg':'INVALID EMAIL OR PASSWORD'})
    return render(request,'seller/seller_login.html')


def seller_dashboard(request):
    if 'seller' in request.session:
      return render(request,'seller/seller_dashboard.html')
    else:
        return render(request,'seller/seller_home.html')


def addproduct(request):
    categories=Category.objects.all()
    if request.method=='POST':
       name=request.POST.get('pdt_name')
       description=request.POST.get('description')
       price=request.POST.get('price')
       image=request.FILES['image']
       category=request.POST.get('category')
       cat=Category.objects.get(id=category)
       product=Product(product_name=name, description=description, price=price, image=image , category=cat)
       product.save()
    return render(request,'seller/addproduct.html',{'categories':categories})

def view_products(request):
   products=Product.objects.all()
   return render(request,'seller/view_products.html',{'products': products})

def delete_product(request,product_id):
   Product.objects.get(id=product_id).delete()
   return redirect('seller:view_products')

def update_product(request,product_id):
   categories=Category.objects.all()
   product=Product.objects.get(id=product_id)
   if request.method=='POST':
       name=request.POST.get('pdt_name')
       description=request.POST.get('description')
       price=request.POST.get('price')
       image=request.FILES.get('image')
       category=request.POST.get('category')
       cat=Category.objects.get(id=category)

       product.product_name=name
       product.description=description
       product.price=price
       product.image=image
       product.category=cat

       product.save()
       return redirect('seller:view_products')
   return render(request,'seller/update_product.html',{'categories': categories,'product': product})


def sellerlogout(request):
    if 'seller' in request.session:
        del request.session['seller']
        return render(request,'seller/seller_home.html') 
    else:
        return render(request,'seller/seller_home.html') 