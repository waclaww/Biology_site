from django.shortcuts import render
from .models import *
from Members.models import Result
from json import loads

# Create your views here.

# def test(request, id):
#     test = Test.objects.get(id=id)
#     context = {
#         "title": test.title,
#         "questions": Question.objects.filter(test__id=test.id),
#     }
#     return render(request, 'test.html', context)

def test(request, id):
    if request.method == 'POST':
        if request.user is not None:
            result = loads(request.body).split('#')
            Result.objects.create(user=request.user, test_id=int(result[0]), rightAnswers=int(result[1]), wrongAnswers=int(result[2]), questions=int(result[3]))
    test = Test.objects.get(pk=id)
    if test.is_random == True:
        questions = Question.objects.filter(test__id=id).order_by('?')[:test.amount]
    else:
        questions = Question.objects.filter(test__id=id)[:test.amount]
    context = {
        'value': questions.count(),
        'items': questions, #before news
        'test': test,
        'request': request,
    }
    return render(request, 'test.html', context)