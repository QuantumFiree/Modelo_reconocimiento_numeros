from django import forms

class ImageForm(forms.Form):
    image_upload = forms.ImageField()

class ImageView(forms.Form):
    image_view = forms.ImageField(disabled=True)