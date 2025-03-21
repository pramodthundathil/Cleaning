from django import forms
from .models import Products, ProductImages



class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Products
        # fields = ["name","price"]
        exclude = ["merchant","tax","price_before_tax","price_after_tax",]

        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control","placeholder":"Name Of the Product"}),
            "price": forms.NumberInput(attrs={"class":"form-control","placeholder":"Price of Product"}),
            "stock": forms.NumberInput(attrs={"class":"form-control","placeholder":"Stock Of the Product"}),
            "image": forms.FileInput(attrs={"class":"form-control","placeholder":"Image Of the Product"}),
            "description": forms.Textarea(attrs={"class":"form-control","placeholder":"Description Of the Product"}),
            "tax_slab":forms.Select(attrs={"class":"form-control",}),
            "category":forms.Select(attrs={"class":"form-control",}),
        }


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        exclude  = ["product",]


from django import forms
from .models import Promotions

class PromotionsForm(forms.ModelForm):
    class Meta:
        model = Promotions
        exclude = ['user']  # Excluding the 'user' field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
