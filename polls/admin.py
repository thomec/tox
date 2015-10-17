# polls/admin.py


from django.contrib import admin
from polls.models import Poll, Question, Answer


class QuestionInline(admin.TabularInline):
    
    model = Question
    # list of answers?
    extra = 2


class AnswerInline(admin.TabularInline):
    
    model = Answer
    extra = 3


class PollAdmin(admin.ModelAdmin):

    search_fields = ['title', 'description']  
    
    # admin/polls/polls/
    list_display =('title', 'pub_date',)
    list_filter = ['pub_date']

    # admin/polls/polls/<num>/
    fieldsets = (
        ('Poll', {'fields': ['title']}),
        ('Details', {'classes': ('collapse',),
            'fields': ('description', 'pub_date')}),
    )
    inlines = [QuestionInline]
        

class QuestionAdmin(admin.ModelAdmin):
    
    search_fields = ['text']
    list_display =('text', 'number')
    list_filter = ['text']

    fieldsets = (
            ('Poll', {'fields': ('poll',), 'classes': ('collapse',)}),
        ('Question', {'fields': ['number', 'text']}),
        )
    inlines = [AnswerInline]
        

class AnswerAdmin(admin.ModelAdmin):
    
    fieldsets = [
            ('Question', {'fields': ('question',), 'classes':('collapse',)}),
        ('Answer', {'fields': ('number', 'text')}),
    ]


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)


