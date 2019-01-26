"""Alzitoona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete, logout

from Alzitoona import settings
from Begining import views
from Begining.views import start, Registeration, student_register, professor_register, Professor_home, Student_home
from Questions.views import ask, questions,  search_query, All_Questions, search_bar, question_full_page, \
    answer_question, voting_answer, Upload_File, Remove_File, Library, Files_Gallery, Download_File, General_Library, \
    Download_File_General
from chat.views import chat
from professor_section.views import rating_professors
from user_section.views import activity, profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', start.as_view()),
    url(r'^register/', Registeration.as_view()),
    url(r'^student/', student_register.as_view()),
    url(r'^professor/', professor_register.as_view()),
    url(r'^Student_home/', Student_home.as_view()),
    url(r'^Professor_home/', Professor_home.as_view()),
    url(r'^login/$', login),

    url(r'^password/reset/$', password_reset, {'post_reset_redirect': '/password/reset/done/'}, name='password_reset'),

    url(r'^password/reset/done/$', password_reset_done),

    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'post_reset_redirect': '/password/done/'}, name='password_reset_confirm'),

    url(r'^password/done/$', password_reset_complete),

    url(r'^home/$', views.home),
    url(r'^logout/', logout, {"next_page": "/"}),
    url(r'^home/ask/', ask.as_view()),

    # QUESTIONS SECTION
    url(r'^home/questions/$', questions.as_view()),
    url(r'^home/questions/All/$', All_Questions.as_view()),

    url(r'^home/questions/search/$', search_bar.as_view()),
    url(r'^home/questions/search/SQ/$', search_query.as_view()),
    # Questiom full page.
    url(r'^home/questions/All/(?P<question_id>\d+)/$', question_full_page),
    url(r'^home/questions/search/(?P<question_id>\d+)/$', question_full_page),
    url(r'^home/questions/search/SQ/(?P<question_id>\d+)/$', question_full_page),
    #Question-full-page-2  (POST LINKS)
    url(r'^home/questions/All/answer/$',answer_question),

    url(r'^home/questions/answer/votes/$',voting_answer),

    # END OF QUESTIONS SECTION

    url(r'^home/library/$', Library),
    url(r'^home/library/Gallery/$', Files_Gallery),
    url(r'^home/library/Gallery/(?P<id>\d+)/$', Download_File),

    url(r'^home/general_library/(?P<id>\d+)/$', Download_File_General),

    url(r'^home/library/Gallery/delete/$', Remove_File),
    url(r'^home/library/Upload/$', Upload_File),



    url(r'^home/activity/', activity),
    url(r'^home/rating_professors/', rating_professors.as_view()),
    url(r'^home/chat/', chat.as_view()),

    url(r'^home/general_library/', General_Library),
    url(r'^home/profile/', profile.as_view()),


]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
