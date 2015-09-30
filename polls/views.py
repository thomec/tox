# polls/views.py


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from polls.models import Poll, Choice, Vote
from polls.forms import *



def index(request):

    polls = Poll.objects.order_by('-pub_date')[:5]
    form = PollForm(request.POST or None)

    if form.is_valid():
        poll = form.save(request)
        return HttpResponseRedirect(reverse(
            'polls:edit',
            args=(poll.id,)
        ))

    context = {'form': form, 'polls': polls}
    return render(request, 'polls/index.html', context)



def about(request):
    return render(request, 'polls/about.html', {})



def polls(request):

    polls = Poll.objects.all()
    title = "Poll list"
    context = {'polls':polls, 'title': title}
    return render(request, 'polls/polls.html', context)



def poll(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    # questions = poll.question_set.all()
    choices = poll.choice_set.all()
    title = "Poll details"
    context = {'poll': poll, 'choices': choices, 'title': title}

    return render(request, 'polls/poll.html', context)



def edit(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    choices = poll.choice_set.all()
    
    print("poll.title    = "+poll.title)
    print("type(choices) = "+str(type(choices)))
    print("choices       = "+str(choices))

    form = PollForm(request.POST or None, instance=poll)
    formset = ChoicesFormSet(request.POST or None, instance=poll)

    context = {
            'poll': poll,
            'choices': choices,
            'form': form,
            'formset': formset
            }

    if form.is_valid() and formset.is_valid():
        print("Form is valid")
        poll = form.save()
        choices = formset.save()

        print("save poll:    "+str(poll))
        print("save choices: "+str(choices))
        return HttpResponseRedirect(
                reverse('polls:poll',args=(poll.id,))
                )

    else:
        print("Form has errors")
        print(form.errors)
    
    return render(request, 'polls/edit.html', context)



def vote(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    context = {'poll': poll}

    if not request.session.session_key:
        request.session.modified = True
        request.session.save()
    
    print("HURGA")
    print("\nrequest.session.__dict__\n"+str(request.session.__dict__))
    print("\nrequest.session.session_key\n"+str(request.session.session_key))
    
    try:
        selection = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context['error_message'] = "You didn't select a choice" # kann weg?
        return render(request, 'polls/poll.html', context)
    else:
        print("\nselection:\n"+str(selection))
        vote = Vote.objects.create(
                poll=poll,
                choice=selection,
                sessionid=request.session.session_key
                )
        vote.save()
       
    return HttpResponseRedirect(
            reverse('polls:results', args=(poll.id,))
            )



def results(request, poll):

    poll = get_object_or_404(Poll, id=poll)
    choices = poll.choice_set.all()
    context ={'poll': poll, 'choices': choices}
    
    return render(request, 'polls/results.html', context)



