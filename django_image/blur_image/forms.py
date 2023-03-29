from django import forms
from blur_image.models import Image

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('name_image', 'image', 'is_blur')
        
        