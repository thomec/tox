# polls/views.py


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from polls.models import Poll, Question, Answer, Vote
from polls.forms import *


def index(request):
    polls = Poll.objects.order_by('-pub_date')[:5]
    questions = Question.objects.all()[:5]

    form = PollQuestionForm(request.POST or None)

    if form.is_valid():
        poll = form.save(request)
        return HttpResponseRedirect(reverse(
            'polls:edit_poll_questions',
            args=(poll.id,)
        ))

    context = {'form': form, 'polls': polls, 'questions': questions}
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

    sessionid = request.session.session_key
    votes = Vote.objects.filter(sessionid=sessionid, questions=question)
    
    if votes:
        context['message'] = "already voted"
    else:
        context['message'] = "not voted yet"

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
        vote.sessionid = request.session.session_key
        vote.save()
       
    return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))


def results(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    questions = poll.question_set.all()
    context ={'poll': poll, 'questions': questions}
    
    return render(request, 'polls/results.html', context)

def edit_poll_questions(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    questions = poll.question_set.all()

    text = 'Töpfchenhexe'

    form = PollForm(request.POST or None, instance=poll)
    formset = QuestionFormSet(request.POST or None)
    for qform in formset:
        qform.instance.text = text

    context = {
            'poll': poll,
            'questions': questions,
            'form': form,
            'formset': formset
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('polls:index'))

    else:
        print(form.errors)
    
    
    return render(request, 'polls/edit_poll_questions.html', context)


def edit_question_answers(request, question):
    pass

