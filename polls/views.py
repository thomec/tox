# polls/views.py


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from polls.models import Poll, Question, Answer, Vote


def index(request):

    polls = Poll.objects.order_by('-pub_date')[:5]
    questions = Question.objects.all()[:5]

    context = {'polls': polls, 'questions': questions}
    return render(request, 'polls/index.html', context)


def about(request):
    return render(request, 'polls/about.html', {})


def poll(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    questions = poll.question_set.all()

    context = {'poll': poll, 'questions': questions}
    return render(request, 'polls/poll.html', context)


def question(request, question):
    
    question = get_object_or_404(Question, id=question)
    answers = question.answer_set.all()
    
    context = {'question': question, 'answers': answers}
    return render(request, 'polls/question.html', context)


def vote(request, question):

    question = get_object_or_404(Question, id=question)
    poll = question.poll
    context = {'poll': poll, 'question': question}

    try:
        choice = question.answer_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context['error_message'] = "You didn't select a choice" # kann weg?
        return render(request, 'polls/question.html', context)
    else:
        print("\nchoice:\n"+str(choice))
        vote = Vote.objects.create(poll=poll)
        vote.questions.add(question)
        vote.answers.add(choice)
        vote.save()
       
    return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))


def results(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    questions = poll.question_set.all()

    #votes = poll.vote_set.all() # dict { question: answer}    
    
    context ={'poll': poll, 'questions': questions}
    
    return render(request, 'polls/results.html', context)

