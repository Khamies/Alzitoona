from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import View

from Begining.models import Professor
from professor_section.models import Professor_Rating




class rating_professors(View):
    def get(self,request):

        user = request.user
        professors=Professor.objects.all()

        paginator = Paginator(professors, 10)
        requested_page = request.GET.get('page')


        try:
            page = paginator.page(requested_page)

        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)


        context={"page":page}

        return render(request,"rating_professors.html",context)

    def post(self,request):

        if request.POST.get('up'):
            professor_id=request.POST.get('id')
            selected_professor=Professor.objects.get(professor_id=professor_id)
            selected_professor.upvote=selected_professor.upvote+1
            selected_professor.total_votes=selected_professor.total_votes+1
            selected_professor.save()

            data=selected_professor.total_votes
            context={"total_votes":data}
            return JsonResponse(context)


        if request.POST.get('down'):

            professor_id=request.POST.get('id')
            selected_professor=Professor.objects.get(professor_id=professor_id)
            selected_professor.downvote=selected_professor.downvote+1
            selected_professor.total_votes=selected_professor.total_votes-1
            selected_professor.save()

            data=selected_professor.total_votes

            context={"total_votes":data}
            return JsonResponse(context)

        if request.POST.get('comment'):

            comment=request.POST.get("comment")
            professor_id=request.POST.get('id')
            selected_professor=Professor.objects.get(professor_id=professor_id)
            rated_professor=Professor_Rating()
            rated_professor.professor=selected_professor
            rated_professor.comment=comment
            rated_professor.save()

            data={"message":"Thank You !"}


            return JsonResponse(data)