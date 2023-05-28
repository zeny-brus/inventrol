from django import forms
from .models import Product, Movement

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        amout = cleaned_data.get('amout')
        min_amout = cleaned_data.get('min_amout')
        
        if amout and min_amout and min_amout > amout:
            raise forms.ValidationError("A quantidade minima tem que ser menor ou igual a quantidade")

class MovementForm(forms.ModelForm):
    TYPE_MOVEMENT = [
        ('ENTRY','Entry'),
        ('OUTPUT','Output'),
    ]
    type_movement = forms.ChoiceField(choices=TYPE_MOVEMENT, widget=forms.RadioSelect)
    class Meta:
        model = Movement
        fields = ("product","type_movement","amout")
    



