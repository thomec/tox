# polls/models


from django.db import models


class Poll(models.Model):
    title = models.CharField('title', max_length=255, help_text="Title")
    question = models.CharField(
            'question',
            max_length=255,
            help_text="Question",)
    description = models.CharField(
            'description',
            max_length=4095,
            help_text="Description"
            )
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    # exp_date = models.DateTimeField('expiery date')

    def __str__(self):
        return self.title

    def count_choices(self):
        return self.choice_set.all().count()

    def count_votes(self):
        return self.vote_set.all().count()

    class Meta:
        ordering = ['pub_date', 'title']


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    text = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.text

    def count_votes(self):
        return self.vote_set.all().count()

    class Meta:
        ordering = ['number']


class Vote(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
    timestamp = models.DateTimeField(auto_now_add=True)
    sessionid = models.CharField(max_length=32)

    def __str__(self):
        return "Vote on Poll {0} at {1}".format(self.poll, self.timestamp)

    class Meta:
        ordering = ['-timestamp']


