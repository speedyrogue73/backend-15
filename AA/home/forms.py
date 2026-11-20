from django import forms


class CreatePostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    poster = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))


class PostCommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class PostCommentReplyForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))