from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = "__all__"

class PcForm(forms.ModelForm):
    class Meta:
        model = Pc
        fields = "__all__"

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = "__all__"