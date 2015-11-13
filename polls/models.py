# polls/models.py


import datetime
from django.db import models
from django.utils import timezone


class Picture(models.Model):

    caption = models.CharField(
            'Caption',
            max_length = 255,
            )
    source = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.caption


class Poll(models.Model):
    
    title = models.CharField(
            'Poll Title',
            max_length = 255,
            help_text = "Provide a title for the Poll."
            )
    description = models.CharField(
            'Poll Description',
            max_length = 4095,
            blank = True,
            help_text='Describe the Poll if you like.'
            )
    pub_date = models.DateTimeField(
            'Publishing Date and Time',
            default = timezone.now,
            help_text = 'Date and Time to start the Poll.'
            )
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date', 'title']


class Question(models.Model):

    poll = models.ForeignKey(
            Poll,
            help_text = "Poll"
            )
    text = models.CharField(
           'Question Text',
           max_length = 255,
           blank = True,
           help_text = 'Ask a Question'
           )
    picture = models.ForeignKey(
            Picture,
            null = True,
            help_text = 'Add a Picture to this Question.'
            )
    number = models.PositiveSmallIntegerField(
            'Question Number',
            default = 1,
            help_text = 'If you have more than one Question, they are ordered by their Number.'
            )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['number']


class Answer(models.Model):

    question = models.ForeignKey(
            Question,
            )
    text = models.CharField(
            'Answer Text',
            max_length=255,
            blank = True,
            help_text = 'Add a possible choice to answer the Question'
            )
    picture = models.ForeignKey(
            Picture,
            null=True,
            help_text='Add a Picture to this Answer.'
            )
    number = models.PositiveSmallIntegerField(
            'Number',
            default = 0,
            help_text = 'The Number is used to order the Answers.'
            )
    value = models.IntegerField(
            'Value',
            blank = True,
            )
    count = models.IntegerField(default=0, editable=False)

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
        
