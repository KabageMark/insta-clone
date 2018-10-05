from .models import Image
from django import forms
#......
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['users','comments','likes']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }