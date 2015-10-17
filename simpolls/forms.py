# polls/forms.py


import datetime

from django import forms
from django.utils import timezone
from django.forms import ModelForm
from django.forms.models import (
        inlineformset_factory,
        BaseInlineFormSet,
        ModelForm
        )
from django.forms.formsets import formset_factory

from polls.models import Poll, Choice



class PollForm(forms.ModelForm):
   
    class Meta:
        model = Poll
        fields = ['title', 'question', 'description']
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'question': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'})
                }

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ['poll', 'number', 'text']


class PollQuestionForm(forms.Form):

    poll_title = forms.CharField(
            label = 'Title',
            max_length = 255,
            widget = forms.TextInput(attrs={'class':'form-control'}))
    question_text = forms.CharField(
            label = 'Question',
            max_length = 255,
            widget = forms.TextInput(attrs={'class':'form-control'}))

 
    def save(self, request, commit=True):

        data = self.cleaned_data
        poll = Poll.objects.create(title=data['poll_title'])
        question = poll.question_set.create(text=data['question_text'])
        poll.save()
        question.save()

        return poll


ChoicesFormSet = inlineformset_factory(Poll, Choice,
        fields=['poll', 'number', 'text'],
        # exclude=[],
        widgets={
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            }
        )



