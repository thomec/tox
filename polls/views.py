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


def polls(request):

    polls = Poll.objects.all()
    title = "Poll list"
    context = {'polls':polls, 'title': title}
    return render(request, 'polls/polls.html', context)


def questions(request):

    questions = question.objects.all()
    title = "Question list"
    context = {'questions': questions, 'title': title}
    return render(request, 'polls/questions.html', context)


def poll(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    questions = poll.question_set.all()
    title = "Poll detail"
    context = {'poll': poll, 'questions': questions, 'title': title}

    return render(request, 'polls/poll.html', context)


def question(request, question):
    
    question = get_object_or_404(Question, id=question)
    poll = question.poll
    answers = question.answer_set.all()
    title = 'Question detail'
    context = {
            'poll':poll,
            'question': question,
            'answers': answers,
            'title': title
    }

    sessionid = request.session.session_key
    votes = Vote.objects.filter(sessionid=sessionid, questions=question)
    
    if votes:
        context['message'] = "already voted {} times!".format(str(len(votes)))
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
       
    return HttpResponseRedirect(
            reverse('polls:results', args=(poll.id,))
            )


def results(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    questions = poll.question_set.all()
    context ={'poll': poll, 'questions': questions}
    
    return render(request, 'polls/results.html', context)


def edit_poll_questions(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    questions = poll.question_set.all()

    form = PollForm(request.POST or None, instance=poll)
    formset = QuestionFormSet(request.POST or None, instance=poll)

    context = {
            'poll': poll,
            'questions': questions,
            'form': form,
            'formset': formset
    }

    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return HttpResponseRedirect(
                reverse('polls:poll',args=(poll.id,))
                )


    else:
        print(form.errors)
    
    return render(request, 'polls/edit_poll_questions.html', context)


def edit_question_answers(request, question):

    question = get_object_or_404(Question, id=question)
    answers = question.answer_set.all()

    form = QuestionForm(request.POST or None, instance=question)
    formset = AnswerFormSet(request.POST or None, instance=question)

    context = {
            'question': question,
            'answer': answers,
            'form': form,
            'formset': formset
    }

    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return HttpResponseRedirect(reverse('polls:index'))

    else:
        print(form.errors)
    
    return render(request, 'polls/edit_question_answers.html', context)


