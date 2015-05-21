# polls/models


from django.db import models


class Poll(models.Model):
    title = models.CharField('title', max_length=255, help_text="Title")
    description = models.CharField('description',
        max_length=4095,
        help_text="Description")
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date', 'title']


class Question(models.Model):
    poll = models.ForeignKey(Poll)
    text = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.text

    def count_answers(self):
        return self.answer_set.count() # error?

    def count_votes(self):
        return self.vote_set.all().count()

    class Meta:
        ordering = ['number', 'text']


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=255)
    #value = models.IntegerField(default=0)
    number = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.text

    def poll(self): # this should allow to read answer.poll
        return self.question.poll

    def count_votes(self):
        return self.vote_set.all().count()

    class Meta:
        ordering = ['number']


class Vote(models.Model):
    poll = models.ForeignKey(Poll)
    questions = models.ManyToManyField(Question)
    answers = models.ManyToManyField(Answer)
    timestamp = models.DateTimeField(auto_now_add=True)
    sessionid = models.CharField(max_length=32)

    def __str__(self):
        return "Vote on Poll {0} at {1}".format(self.poll, self.timestamp)

    class Meta:
        ordering = ['-timestamp']


