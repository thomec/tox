# polls/admin.py


from django.contrib import admin

from polls.models import Poll, Question, Answer, Vote


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'description']}),
        ]
    inlines = [QuestionInline]
    list_display = ('title', 'pub_date')


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poll', {'fields': ['poll']}),
        ('Question', {'fields': ['text']})
        ]
    #prepopulated_fields = {}
    inlines = [AnswerInline]
    list_display = ('text', 'number', 'poll')


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Vote)
