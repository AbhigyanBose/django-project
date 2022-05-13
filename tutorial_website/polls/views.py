from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse, Http404


# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', context={'items': questions})


def question(request, question_id):
    choices = Choice.objects.filter(question_id=question_id)
    if not choices:
        get_object_or_404(Question, pk=question_id)
        raise Http404("Question has no choices")

    context = {'choices': choices}
    return render(request, 'polls/question.html', context=context)


def choice(request, choice_id):
    return HttpResponse("Choice Selected "+str(choice_id))
