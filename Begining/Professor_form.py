from django import forms


class Professor_form(forms.Form):

    professor_specialization=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Specialization","required":"true","id":"professor_specialization"}))
    professor_phone_number=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Phone Number","required":"true","id":"professor_PhoneNumber"}))


