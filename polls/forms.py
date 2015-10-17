# polls/forms.py

import datetime

from django import forms
from django.utils import timezone
from django.forms.formsets import formset_factory

from polls.models import Poll, Question, Answer


class PollForm(forms.ModelForm):

    # default=timezone.now()+datetime.timedelta(days=366)

     class Meta:
        # Provide an association between the ModelForm and a model
        model = Poll
        fields = ('title', 'description', 'pub_date')
        #exclude = ('pub_date',)
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'exp_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
                }


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('number', 'text')
        #pub_date = forms.DateTimeField(help_text="Please enter a publication date.")
        #exp_date = forms.DateTimeField(help_text="Please enter a expiery date.")

        widgets = {
                'text': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'exp_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
                }


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text',)
        # ToDo: field 'question' as choice set from selected poll


class NewPollForm(forms.Form):
    poll_title = forms.CharField(label='Title', max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    question_text = forms.CharField(label='Question', max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    answer_one = forms.CharField(label='Answer 1', max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    answer_two = forms.CharField(label='Answer 2', max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))

    answer_formset = formset_factory(AnswerForm)

    def save(self):
        pass


QuestionFormSet = forms.models.inlineformset_factory(Poll, Question,
        fields=['poll', 'text'],
        widgets={'text': forms.TextInput(attrs={'class': 'form-control'}),}
        )


AnswerFormSet = forms.models.inlineformset_factory(Question, Answer,
        fields=['question', 'text'],
        widgets={'text': forms.TextInput(attrs={'class': 'form-control'}),}
        )



