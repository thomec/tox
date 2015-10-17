# polls/models.py


import datetime
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    
    title = models.CharField(max_length=255, help_text="Text")
    description = models.CharField(max_length=4095, blank=True, help_text="Description")
    #image = models.ImageField(blank=True, help_text="Image")
    pub_date = models.DateTimeField('date published', default=timezone.now(), help_text="publish date")
    
    def __str__(self):
        return self.title


class Question(models.Model):

    poll = models.ForeignKey(Poll, help_text="Poll")
    text = models.CharField(blank=True, max_length=255, help_text="Text")
    #image = models.ImageField(blank=True, help_text="Image")
    number = models.PositiveSmallIntegerField(default=0, help_text="Number")

    def __str__(self):
        return self.text


class Answer(models.Model):

    question = models.ForeignKey(Question)
    text = models.CharField(blank=True, max_length=255, help_text="Text")
    #image = models.ImageField(blank=True, help_text="Image")
    number = models.PositiveSmallIntegerField(default=0, help_text="Number")
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    def poll(self):
        return self.question.poll


class Vote(models.Model):
    
    poll = models.ForeignKey(Poll)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)
    timestamp = models.DateTimeField(auto_now_add=True)
    sessionid = models.CharField(max_length=32)

    def __str__(self):
        return "Vote on Poll {0} at {1}".format(self.poll, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        
