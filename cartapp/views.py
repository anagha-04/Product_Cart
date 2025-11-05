from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View,UpdateView

from cartapp.models import ProductModel,CartModel

from cartapp.forms import ProductForm,CartForm

from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

#product

class Product_create_View(View):

    def get(self,request):

       form = ProductForm()

       return render(request,"product_create.html",{"form":form})
    
    def post(self,request):

        print( request.POST)

        name = request.POST.get("name")

        price = request.POST.get("price")

        stock = request.POST.get("stock")

        ProductModel.objects.create(name =name,price = price ,stock = stock)

        form = ProductForm

        return redirect("list")
    

class Product_List_View(View):

    def get (self,request):

        products = ProductModel.objects.all()

        return render(request,"product_list.html",{"products":products})
    

class Product_Update_View(UpdateView):

    model = ProductModel

    form_class = ProductForm

    template_name = "product_update.html"

    success_url = reverse_lazy("list")


class Product_delete_view(View):

    def get(self, request, **kwargs):

        id = kwargs.get("pk")

        product = ProductModel.objects.get(id=id)  # Get the specific product

        product.delete()  # Delete that one
        
        return redirect("list")
    

class Cart_add_view(View):

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        product = ProductModel.objects.get(id = id)

        CartModel.objects.create(product=product,quantity =1)

        return redirect("list")
    
    



    

