from django import forms


class Student_form(forms.Form):

    aviable_age=((16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28))
    user_age=forms.CharField(widget=forms.Select(choices=aviable_age,attrs={"class":" dropdown","required":"true"}))


    index=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"index","required":"true","id":"index"}))
    student_specialization=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Specialization","required":"true","id":"student_specialization"}))
    student_phone_number=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Phone Number","required":"true","id":"student_PhoneNumber"}))


    aviable_Interest=(("Math","Math"),("Physics","Physics"),("Programming","Programming"),("Designing","Designing"),("business","business"))
    user_interest=forms.CharField(widget=forms.Select(choices=aviable_Interest,attrs={"class":" dropdown","required":"true"}))
