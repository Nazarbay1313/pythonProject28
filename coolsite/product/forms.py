from django import forms

from product.models import Comment, Contact


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Ваш комментарий: ', widget=forms.Textarea(attrs={'cols': 68, 'rows': 5}))

    class Meta:
        model = Comment
        fields = ('content', )


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Contact
        fields = ('name', 'email')
