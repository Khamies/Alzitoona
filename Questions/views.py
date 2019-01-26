import os
from rexec import FileWrapper

import datetime
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import View

from Questions import library_form
from Questions.ask_from import ask_form
from Questions.models import ask_question, answer, libarary


class ask(View):
    def get(self, request):
        context = {"form": ask_form}
        return render(request, "ask.html", context)

    def post(self, request):
        form = ask_form(request.POST or None)
        if form.is_valid():
            asker = request.user
            title = form.cleaned_data['question_title']
            question = form.cleaned_data['question']
            specialization = form.cleaned_data['specialization']

            model = ask_question()
            model.question_title = title
            model.question = question
            model.specialization = specialization
            model.asker = asker
            weekday=datetime.datetime.today().weekday()
            dayOfWeek=datetime.datetime.today().isocalendar()[1]
            model.weekday=weekday
            model.dayOfWeek=dayOfWeek
            model.save()

            context = {"username": request.user}
            return render(request, "User_htmls/response_to_asker.html", context)

        else:
            return render(request, "test.html")


class questions(View):
    def get(self, request):
        return render(request, "User_htmls/question_selecting_path.html")


class All_Questions(View):
    def get(self, request):
        all_questions = ask_question.objects.all().order_by("-date")

        paginator = Paginator(all_questions, 10)

        requested_page = request.GET.get('page')

        try:
            page = paginator.page(requested_page)

        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        context = {"page": page}

        return render(request, "questions.html", context)


class search_bar(View):
    def get(self, request):
        return render(request, "User_htmls/search_bar.html")


class search_query(View):
    def get(self, request):

        request.POST = request.session["search_post"]
        query = request.POST.get('query')

        found = ask_question.objects.filter(question__contains=query)
        found_2 = serializers.serialize("json", found)
        print found_2
        paginator = Paginator(found, 5)

        requested_page = request.GET.get('page')

        try:
            page = paginator.page(requested_page)

        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        if page.number == 1:

            context = {"page": page, "previous": "?page=", "next": "?page="}
        else:
            context = {"page": page, "previous": "?page=", "next": "?page="}

        return render(request, "User_htmls/questions_search.html", context)

    def post(self, request):

        request.session["search_post"] = request.POST
        query = request.POST.get('query')

        found = ask_question.objects.filter(question__contains=query)
        found_2 = serializers.serialize("json", found)
        print found_2
        paginator = Paginator(found, 5)

        requested_page = request.GET.get('page')

        try:
            page = paginator.page(requested_page)

        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        if page.number == 1:

            context = {"page": page, "previous": "?page=", "next": "SQ/?page"}
        else:
            context = {"page": page, "previous": "?page=", "next": "?page"}

        return render(request, "User_htmls/search_question_response.html", context)


# ////////////////////////////this is function view section.///////////////////////////////
# I did it ,just for flexibility :).

def question_full_page(request, question_id):
    if request.method == "GET":
        all = ask_question.objects.filter(question_id=question_id)

        all_votings = all[0].all_votings
        asker = all[0].asker
        question = all[0].question

        All_Answers_1 = answer.objects.filter(question_key=all[0])
        answer_by = [str(name.answer_by) for name in All_Answers_1]
        answers_id = [str(id.answer_id) for id in All_Answers_1]
        answer_votes = [str(vote.all_votings) for vote in All_Answers_1]

        list = zip(All_Answers_1, answer_by, answers_id, answer_votes)

        context = {"Up_id": question_id, "Down_id": question_id, "asker": asker, "votings": all_votings,
                   "question": question, "All_answers": list}

        return render(request, "User_htmls/question_full_page.html", context)

    if request.method == "POST":

        if request.POST.get('up'):
            question = ask_question.objects.get(question_id=question_id)

            add = question.upvote + 1

            question.upvote = add

            votings = question.all_votings + 1
            question.all_votings = votings

            question.save()

            number = votings

            context = {"number": number}

            return JsonResponse(context)

        if request.POST.get('down'):
            question = ask_question.objects.get(question_id=question_id)

            add = question.downvote + 1
            question.downvote = add

            votings = question.all_votings - 1
            question.all_votings = votings

            question.save()

            number = votings

            context = {"number": number}

            return JsonResponse(context)


def answer_question(request):
    if request.method == "POST":
        question_id = request.POST.get("question_id")
        Answer = request.POST.get("answer")
        answer_by = request.user
        question = ask_question.objects.filter(question_id=question_id)
        asker = question[0].asker

        model_answer = answer()
        model_answer.question_key = question[0]
        model_answer.asker = asker
        model_answer.answer_by = answer_by
        model_answer.answer = Answer
        weekday=datetime.datetime.today().weekday()
        dayOfWeek=datetime.datetime.today().isocalendar()[1]
        model_answer.weekday=weekday
        model_answer.dayOfWeek=dayOfWeek
        model_answer.save()

        answer_id = model_answer.answer_id
        voting = model_answer.all_votings

        context = {"answer": Answer, "answer_by": answer_by, "answer_id": answer_id, "answer_id2": answer_id,
                   "voting": voting}

        Response = render_to_string("User_htmls/answer_cart.html", context)
        return JsonResponse(Response, safe=False)


def voting_answer(request):
    if request.method == "POST":
        if request.POST.get('up'):
            answer_id = request.POST.get("answer_id")
            model_answer = answer.objects.get(answer_id=answer_id)

            model_answer.up_vote = model_answer.up_vote + 1
            model_answer.all_votings = model_answer.all_votings + 1
            model_answer.save()

            all_votings = model_answer.all_votings

            context = {"voting": all_votings}

            return JsonResponse(context)

        if request.POST.get('down'):
            answer_id = request.POST.get("answer_id")
            model_answer = answer.objects.get(answer_id=answer_id)

            model_answer.down_vote = model_answer.down_vote + 1
            model_answer.all_votings = model_answer.all_votings - 1
            model_answer.save()

            all_votings = model_answer.all_votings

            context = {"voting": all_votings}

            return JsonResponse(context)


            # //////////////////////////////////////////////////////////////////////////////////////////


def Library(request):
    return render(request, "library_choose_path.html")


def Files_Gallery(request):
    user = request.user
    files = libarary.objects.filter(uploader=user).order_by("-date")

    all_files = [mfile for mfile in files]

    ids = [mfile.file_id for mfile in files]

    file_names = [str(mfile.file_name) for mfile in files]

    file_dates = [str(mfile.date) for mfile in files]


    paginator = Paginator(files, 10)
    requested_page = request.GET.get('page')

    try:
        page = paginator.page(requested_page)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)


    bundle = zip(file_dates, ids, file_names,page.object_list)

    context = {"file": bundle,"page":page}

    return render(request, "Files_Gallery.html", context)




def General_Library(request):

    user = request.user
    files = libarary.objects.all()

    all_files = [mfile for mfile in files]

    ids = [mfile.file_id for mfile in files]

    file_names = [str(mfile.file_name) for mfile in files]

    file_dates = [str(mfile.date) for mfile in files]


    paginator = Paginator(files, 10)
    requested_page = request.GET.get('page')

    try:
        page = paginator.page(requested_page)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)


    bundle = zip(file_dates, ids, file_names,page.object_list,files)

    context = {"file": bundle,"page":page}


    return render(request,"general_library.html",context)




def Upload_File(request):
    if request.method == "GET":
        context = {"form": library_form}
        return render(request, "library.html", context)

    if request.method == 'POST':

        print request.POST.get("description")
        print request.POST.get("specialization")

        newfile = libarary(file=request.FILES['files[]'], specialization=request.POST.get("specialization"),description=request.POST.get("description"))
        newfile.uploader = request.user
        newfile.file_name = newfile.file.name
        weekday=datetime.datetime.today().weekday()
        dayOfWeek=datetime.datetime.today().isocalendar()[1]
        newfile.weekday=weekday
        newfile.dayOfWeek=dayOfWeek
        newfile.save()

        context = {"thanks": "thanks"}

        return JsonResponse(context)


def Download_File(request,id):

    mfile=libarary.objects.get(file_id=id)


    path=os.path.abspath(mfile.file.url)
    print path
    wrapper = FileWrapper(file(path))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(path)
    response['Content-Length'] = os.path.getsize(path)

    return response


def Download_File_General(request,id):

    if request.method=="GET":

        mfile=libarary.objects.get(file_id=id)
        path=os.path.abspath(mfile.file.url)
        print path
        wrapper = FileWrapper(file(path))
        response = HttpResponse(wrapper, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(path)
        response['Content-Length'] = os.path.getsize(path)

        return response



def Remove_File(request):
    if request.method == "POST":
        fileId=request.POST.get('id')
        myfile = libarary.objects.get(file_id=fileId)
        myfile.delete()

        return JsonResponse({"thanks":"thanks"})
