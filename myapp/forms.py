from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['username', 'name', 'address', 'tel_number', 'email', 'topic', 'body', 'region', 'gender', 'application_type']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control' }),
            'name': forms.TextInput(attrs={'class': 'form-control' }),
            'address': forms.TextInput(attrs={'class': 'form-control' }),
            'tel_number': forms.TextInput(attrs={'class': 'form-control' }),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
            'topic': forms.TextInput(attrs={'class': 'form-control' }),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5 }),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'application_type': forms.Select(attrs={'class': 'form-control'}),
        }
