from django import forms


class login_form(forms.Form):
    email=forms.CharField(max_length=100,min_length=5,required=True,label="",
                          widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','style':'margin-bottom:30px'}))
    password=forms.CharField(max_length=100,min_length=5,required=True,label=""
                             ,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
