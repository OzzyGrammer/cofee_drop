from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for creating an order.

    This form is based on the Order model and provides fields for selecting the strength of the order,
    adding milk, and frothing the milk.

    The form uses various widgets to customize the appearance and behavior of the form fields.

    Attributes:
        model (Model): The model associated with the form.
        fields (list): The fields to include in the form.
        widgets (dict): Custom widgets to use for the form fields.
    """

    class Meta:
        model = Order
        fields = ["strength", "add_milk", "froth_milk"]
        widgets = {
            "strength": forms.Select(attrs={"class": "form-control"}),
            "add_milk": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "froth_milk": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
