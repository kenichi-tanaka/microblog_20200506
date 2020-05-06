from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TimeInput(attrs={'size': 50}))
    
    class Meta:
        model = Blog
        fields = '__all__'  #個別でしたい場合は⇒ ('title', 'text', 'date')

