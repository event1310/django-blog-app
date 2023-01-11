from django import forms
from .models import Post, Comment

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields = ('title', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')
