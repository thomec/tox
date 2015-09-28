# polls/admin.py


from django.contrib import admin

from polls.models import Poll, Choice, Vote



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


admin.site.register(Poll)
#admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
#admin.site.register(Vote)
