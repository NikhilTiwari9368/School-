from django import forms

class userForm(forms.Form):
    Email = forms.EmailField(label="Email" , required=False , widget = forms.TextInput(attrs={'class':"form-control"}))
    Name = forms.CharField(label="Name" , widget = forms.TextInput(attrs={'class':"form-control"}))
    Number = forms.IntegerField(label="Number" , widget = forms.TextInput(attrs={'class':"form-control"}))

