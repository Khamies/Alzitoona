from django.shortcuts import render, render_to_response
from django.views.generic import View

from Begining.User_form import User_form
from Begining.Student_form import Student_form
from Begining.Login_form import login_form
from Begining.Professor_form import Professor_form
from Begining.models import Student,User, Professor
from django.contrib.auth.decorators import login_required


class start(View):
    def get(self,request):

        parameter=dict()
        parameter['login_form']=login_form
        http_response = render(request, "index.html", parameter)

        return http_response

class Registeration(View):
    def get(self,request):

        return render(request,"choose.html")


class student_register(View):

    def get(self,request):
        parameters=dict()
        parameters["form"]=Student_form
        parameters["user_form"]=User_form
        return render(request,"Student_Register.html",parameters)


class professor_register(View):

    def get(self,request):
        parameters=dict()
        parameters["form"]=Professor_form
        parameters["user_form"]=User_form
        return render(request,"Professor_Register.html",parameters)


@login_required
def home(request):
    context=dict()
    context["user"]=request.user

    return render_to_response("app.html",context)
#////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////



class Student_home(View):
    def post(self, request):

        if request.POST:
            name=request.POST['username']
            index=request.POST['index']

            try:

               check_username = User.objects.get_by_natural_key(username=name)

            except:

                check_username = None

            try:

                 check_index = Student.objects.get(index=index)

            except:


                check_index = None


            if check_username is not None:

                message = {"errors": " user name is already existed"}
                return render_to_response("Error.html", message)

            if check_index is not None:

                    message = {"errors": " Index is already existed"}
                    return render_to_response("Error.html", message)


            user_form = User_form(data=request.POST or None)
            student_form = Student_form(data=request.POST or None)



            if student_form.is_valid() and user_form.is_valid():

                # extracting info from.
                user_age = student_form.cleaned_data['user_age']
                user_index = student_form.cleaned_data['index']
                user_sepecialization = student_form.cleaned_data['student_specialization']
                user_phone = student_form.cleaned_data['student_phone_number']
                user_interest = student_form.cleaned_data['user_interest']

                # save user info in database.
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                # now saving student info in database.
                student = Student()
                student.user = user
                student.index = user_index
                student.specialization = user_sepecialization
                student.phone_number = user_phone
                student.age = user_age
                student.related_interest = user_interest
                student.save()
                message = {"thanks": "thank you for registering,you can login now"}

                return render_to_response("home.html", message)






class Professor_home(View):
    def post(self, request):

        if request.POST:
            name=request.POST['username']
            print name

            try:

               check_username = User.objects.get_by_natural_key(username=name)

            except:

                check_username = None

            if check_username is not None:

                message = {"errors": " user name is already existed"}
                return render_to_response("Error.html", message)



            user_form = User_form(data=request.POST or None)
            professor_form = Professor_form(data=request.POST or None)


            if professor_form.is_valid() and user_form.is_valid():

                # extracting info from.
                user_sepecialization = professor_form.cleaned_data['professor_specialization']
                user_phone = professor_form.cleaned_data['professor_phone_number']

                # save user info in database.
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                # now saving student info in database.
                professor = Professor()
                professor.user = user
                professor.specialization = user_sepecialization
                professor.phone_number = user_phone
                professor.save()
                message = {"thanks": "thank you for registering,you can login now"}

                return render_to_response("home.html", message)
