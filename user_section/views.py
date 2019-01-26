import datetime
import os

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render_to_response, render

# Create your views here.
from django.views.generic import View

from Begining.models import Student, Professor
from Questions.models import ask_question, answer, libarary


class profile(View):
    def get(self, request):

        requester = request.user
        user = User.objects.get_by_natural_key(username=requester)
        print user.username

        try:

            check = Student.objects.filter(user=user).exists()


            if check:
                student = Student.objects.get(user=user)

                context = {"user": student}

                return render(request,"profile.html", context)

        except:
            pass


        try:
            check2 = Professor.objects.filter(user=user).exists()



            if check2:
                professor = Professor.objects.get(user=user)
                context = {"user": professor}
                return render(request,"profile.html", context)


        except:
            pass

    def post(self,request):

        requester=request.user
        image=request.FILES.get('fileInput')
        nickname=request.POST.get('nickname')
        phoneNumber=request.POST.get('phoneNumber')
        specialization=request.POST.get('specialization')

        user = User.objects.get_by_natural_key(username=requester)

        try:

            check = Student.objects.filter(user=user).exists()

            if check:
                student = Student.objects.get(user=user)
                student.nickname=nickname
                student.phone_number=phoneNumber
                student.specialization=specialization
                student.photo=image
                one=str(student.photo.name)

                photoName= "/media/"+one

                student.photo_name=photoName

                student.save()


                context = {"user": student}

                return render(request,"profile.html",context)

        except:
            pass


        try:
            check2 = Professor.objects.filter(user=user).exists()



            if check2:
                professor = Professor.objects.get(user=user)

                professor.nickname=nickname
                professor.phone_number=phoneNumber
                professor.specialization=specialization
                professor.photo=image
                professor.save()

                context = {"user": professor}
                return render(request,"profile.html", context)


        except:
            pass



        return JsonResponse({"thanks":"thanks"})



def activity(request):
    day_of_week = datetime.datetime.today().isocalendar()[1]
    user = request.user

    QuestionsActivty = []
    AnswersActivity = []
    FilesActivity = []

    for day in range(0, 7):
        number_of_questions = ask_question.objects.filter(
            Q(asker=user) & Q(weekday=day) & Q(dayOfWeek=day_of_week)).count()
        QuestionsActivty.append(number_of_questions)

    for day in range(0, 7):
        number_of_answers = answer.objects.filter(Q(answer_by=user) & Q(weekday=day) & Q(dayOfWeek=day_of_week)).count()
        AnswersActivity.append(number_of_answers)

    for day in range(0, 7):
        number_of_files = libarary.objects.filter(Q(uploader=user) & Q(weekday=day) & Q(dayOfWeek=day_of_week)).count()
        FilesActivity.append(number_of_files)

    f = open(os.getcwd() + "/static/js/chart/ActivityChart.js", 'w')

    f.write('''$( document ).ready(function() {
    var data = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
            {
                label: "Site Registrations in the Last 30 Days",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: %s
            }
        ]
    };

    Chart.defaults.global.responsive = true;
    var zChart = document.getElementById("zchart").getContext("2d");
    var myLineChart = new Chart(zChart).Line(data);


    /////////////////////////////////////////////////////////////////////////////////
    //////////////////////////ANSWER ACTIVITY///////////////////////////////////////

    var data2 = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
            {
                label: "Site Registrations in the Last 30 Days",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: %s
            }
        ]
    };

    Chart.defaults.global.responsive = true;
    var zChart2 = document.getElementById("zchart2").getContext("2d");
    var myLineChart2= new Chart(zChart2).Line(data2);



    /////////////////////////////////////////////////////////////////////////////////
    //////////////////////////Files ACTIVITY///////////////////////////////////////

    var data3 = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
            {
                label: "Site Registrations in the Last 30 Days",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: %s
            }
        ]
    };

    Chart.defaults.global.responsive = true;
    var zChart3 = document.getElementById("zchart3").getContext("2d");
    var myLineChart3= new Chart(zChart3).Line(data3);










    });''' % (QuestionsActivty, AnswersActivity, FilesActivity))

    f.close()

    return render(request,"activity.html")


def chart(request):
    return
