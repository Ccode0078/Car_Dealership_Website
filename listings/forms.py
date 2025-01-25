from django import forms
from .models import Listing, Image

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'description', 'brand', 'milage', 'price', 'image']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
