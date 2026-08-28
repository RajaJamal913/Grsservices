from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control rounded', 'placeholder': 'Enter your message', 'rows': 5})
    )
