from .models import Image
#......
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['users',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }