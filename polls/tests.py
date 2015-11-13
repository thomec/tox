# polls/tests.py


from django.test import TestCase

from polls.models import *


class BasicModelTests(TestCase):

    def test_create_and_retrive_a_poll(self):
        
        # create a Poll with one Question and 2 Answers
        print("\n* Create a Poll")
        poll = Poll(title='Titel der Umfrage')
        poll.save()
        question = Question(poll=poll, text='Alles OK?')
        question.save()
        answer = Answer(question=question, text='Ja')
        answer.save()
        answer = Answer(question=question, text='Nein')
        answer.save()

        # get Poll by title
        print("  - get Poll by title")
        poll = Poll.objects.get(title='Titel der Umfrage')
        question = Question.objects.get(poll=poll)
        answers = question.answer_set.all()
        poll_id = poll.id
        question_id = question.id

        # test content Poll
        print("  - test Poll")
        self.assertEqual(str(poll), 'Titel der Umfrage')
        self.assertEqual(str(question), 'Alles OK?')
        self.assertEqual(str(answers[0]), 'Ja')
        self.assertEqual(str(answers[1]), 'Nein')

        # get Poll by id
        print("  - get Poll by id")
        poll = Poll.objects.get(id=poll_id)
        question = Question.objects.get(id=question_id)

        # test poll and question
        print("  - test Poll and Question")
        self.assertEqual(str(poll), 'Titel der Umfrage')
        self.assertEqual(str(question), 'Alles OK?')
        self.assertEqual(str(answers[0]), 'Ja')
        self.assertEqual(str(answers[1]), 'Nein')

        





