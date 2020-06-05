from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'description', 'type', 'status', 'location', 'beds', 'baths', 'floors', 'metro', 'area',
                  'size', 'photoURL', 'videoURL', 'photo', 'address', 'city', 'country')


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'description', 'type', 'status', 'location', 'beds', 'baths', 'floors', 'metro', 'area',
                  'size', 'photoURL', 'videoURL', 'photo', 'address', 'city', 'country')



