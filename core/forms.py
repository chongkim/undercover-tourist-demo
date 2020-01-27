from django import forms

from core.models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['customer_email', 'customer_name', 'customer_phone', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(),
            'customer_phone': forms.TextInput(),
        }
