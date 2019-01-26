from django.contrib import admin

from Questions.models import ask_question, libarary, answer

admin.site.register(ask_question)
admin.site.register(answer)
admin.site.register(libarary)
