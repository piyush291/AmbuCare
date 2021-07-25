from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *
from hospital.models import H_Details

# Show specific question and choices
def details(request, id):
  hospital = H_Details.objects.get(id=id)
  choices = Choice.objects.all()
  context = {
      'hospital': hospital,
      'choices':choices,
  }
  return render(request,'polls/details.html',context)

# Get question and display results
def results(request, id):
  hospital = get_object_or_404(H_Details, id=id)
  choice = get_object_or_404(feedback_hospital, user_id=id)
  context = {
      'hospital': hospital,
      'choice':choice,
  }
  return render(request,'polls/results.html', context)

# Vote for a question choice
def vote(request, id):
    print(id) # id of hospital in H_Details
    # print(request.POST['choice'])
    hospital = get_object_or_404(H_Details, id=id)
    choices = Choice.objects.all()
    try:
        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'hospital': hospital,
            'choices':choices,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        selected_hospital = get_object_or_404(feedback_hospital, user_id=id)
        choiceText = selected_choice.choice_text
        if choiceText.find('good')!=-1:
            selected_hospital.good_votes += 1
        elif choiceText.find('average')!=-1:
            selected_hospital.average_votes += 1
        elif choiceText.find('bad')!=-1:
            selected_hospital.bad_votes += 1

        selected_hospital.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('polls:results', args=(hospital.id,)))
