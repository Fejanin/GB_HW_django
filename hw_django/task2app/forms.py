from django import forms


class ImgForm(forms.Form):
    img = forms.ImageField()