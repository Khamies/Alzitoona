from django import forms


class ask_form(forms.Form):

    question_title=forms.CharField(max_length=150,widget=forms.TextInput(attrs={"class":"form-control",
                                                                               "placeholder":"title ...","id":"title","required":"true"}))

    question=forms.CharField(max_length=150,widget=forms.Textarea(attrs={"class":"form-control","id":"question"}))

    aviable_specialization=(("Electronics","Electronics"),("Control","Control"),("Software","Software"),
                            ("Power","Power"),("Telecom","Telecom"))

    specialization=forms.CharField(widget=forms.Select(choices=aviable_specialization,attrs={"class":" form-control","required":"true"}))

