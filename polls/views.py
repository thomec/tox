# polls/views.py


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

from polls.models import *
from polls.forms import *



def index(request):

    polls = Poll.objects.order_by('pub_date')[:10]
    context = {'polls': polls}
    
    return render(request, 'polls/index.html', context)


def about(request):

    return render(request, 'polls/about.html', {})


def detail(request, poll_id):

    poll = get_object_or_404(Poll, pk=poll_id)
    questions = poll.question_set.all()
    context = {'poll': poll, 'questions': questions}

    return render(request, 'polls/detail.html', context)


def polls(request):
    # search polls
    polls = Poll.objects.order_by('title')
    context = {'polls': polls}
    
    return render(request, 'polls/index.html', context)


def question(request, question_id):
        
    # ensure session_key exists
    if not request.session.session_key:
        request.session.modified = True
        request.session.save()

    question = get_object_or_404(Question, pk=question_id)
    poll = question.poll
    answers = question.answer_set.all()
    sessionid = request.session.session_key

    print("answer 3:\n"+str(answers[3].__dict__))
    print("image_id:\n"+str(answers[3].image_id))
    print("image:\n"+str(answers[3].image.image))

    
    voted = Vote.objects.filter(question=question, sessionid=sessionid)
    if len(voted) == 1:
        message = "You have already voted on this question"
    elif len(voted) > 1:
        message = "You have already voted {0} times on this question".format(len(voted))
    else:
        message = ""

    context = {'poll': poll, 'question': question,
            'answers': answers, 'message': message, 'prefix': settings.MEDIA_ROOT+"/"}

    return render(request, 'polls/question.html', context)


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    poll = question.poll
    sessionid = request.session.session_key

    selected_answer = get_object_or_404(Answer, pk=request.POST['answer'])
    selected_answer.count += 1
    selected_answer.save()
    
    vote = Vote(poll=poll, question=question, answer=selected_answer, sessionid=sessionid)
    vote.save()

    return HttpResponseRedirect(
            reverse( 'polls:results', args=(question_id,))
            )


def results(request, question_id):
    # takes a question and shows the votes
    question = get_object_or_404(Question, pk=question_id)
    poll = question.poll
    context_dict = {'poll': poll, 'question': question,
            'message': "You're looking at the results of question {0}.".format(question.id)}

    return render(request, 'polls/results.html', context_dict)


# forms

def add_poll(request):

    form = PollForm(request.POST or None)

    if form.is_valid():
        poll = form.save(commit=True)
        return HttpResponseRedirect(reverse('polls:detail', args=(poll.id,)))
    else:
        print("Form has errors:\n"+str(form.errors))

    return render(request, 'polls/add_poll.html', {'form': form,})

   

def add_question(request, poll_id):
    
    poll = get_object_or_404(Poll, pk=poll_id)
    question = Question(poll=poll)
    form = QuestionForm(request.POST or None, instance=question)
    
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('polls:detail', args=(poll.id,)))

    else:
        print(str(form.errors))
    
    context = {'poll': poll, 'question': question, 'form': form}
    return render(request, 'polls/add_question.html', context)


def add_answer(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    poll = question.poll
    answer = Answer(question=question)
    form = AnswerForm(request.POST or None, instance=answer)
    
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('polls:question', args=(question.id,)))
    else:
        print(form.errors)

    context = {'poll': poll, 'question': question,
            'answer': answer, 'form': form}
    return render(request, 'polls/add_answer.html', context)


def new_poll(request):

    if request.method == 'POST':
        form = NewPollForm(request.POST)

        if form.is_valid():
            poll = Poll(title=form.cleaned_data['poll_title'])
            poll.save()

            question = Question(poll=poll, text=form.cleaned_data['question_text'], number=1)
            question.save()

            answer1 = Answer(question=question, text=form.cleaned_data['answer_one'], number=1)
            answer2 = Answer(question=question, text=form.cleaned_data['answer_two'], number=2)

            answer1.save()
            answer2.save()

            return HttpResponseRedirect(reverse('polls:index'))
        else:
            print(form.errors)
    else:
        form = NewPollForm()

    return render(request, 'polls/new_poll.html', {'form': form})


def edit_poll(request, poll_id):

    poll = get_object_or_404(Poll, pk=poll_id)
    questions = poll.question_set.all()
    form = PollForm(request.POST or None, instance=poll)
    formset = QuestionFormSet(request.POST or None, instance=poll)
    context = {'poll': poll, 'questions': questions,
            'form': form, 'formset': formset}

    if form.is_valid() and formset.is_valid():
        poll = form.save()
        questions = formset.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(poll.id,)))
    else:
        print(str(form.errors))
    return render(request, 'polls/edit_poll.html', context)


def edit_question(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    poll = question.poll
    answers = question.answer_set.all()
    form = QuestionForm(request.POST or None, instance=question)
    formset = AnswerFormSet(request.POST or None, instance=question)
    context = {'poll': poll, 'question': question, 'answers': answers,
            'form': form, 'formset': formset}

    if form.is_valid() and formset.is_valid():
        question = form.save()
        answers = formset.save()
        return HttpResponseRedirect(reverse('polls:question', args=(question.id,)))
    else:
        print(str(form.errors))

    return render(request, 'polls/edit_question.html', context)




