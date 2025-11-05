from django import forms
from cartapp.models import ProductModel,CartModel

class ProductForm(forms.ModelForm):

    class Meta:

        model = ProductModel

        fields =['name','price','stock']

class CartForm(forms.ModelForm):

    class Meta:

        model = CartModel

        fields =['product','quantity']

        