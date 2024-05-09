from .models import Post, Comment
from django import forms


class formcreatupdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body','image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostSearchForm(forms.Form):
    search = forms.CharField()
