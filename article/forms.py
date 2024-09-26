from django import forms
from article.models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'author_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your message'}),

        }