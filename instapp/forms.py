from .models import Image,Profile
from django import forms
#......
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['users','comments','likes']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewProflieForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['users','comments','likes']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }