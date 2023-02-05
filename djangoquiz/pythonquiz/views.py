from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

from .models import *
from django.http import HttpResponse


# Create your views here.
def pythonpage(request):
    if request.method == 'POST':
        questions =PythonQuesModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            answer = request.POST.get(q.question)
            if answer=='option1':
                answer = q.op1
            elif answer=='option2':
                answer = q.op2
            else:
                answer = q.op3


            if q.ans == answer:
                score += 10
                correct += 1
            else:
                wrong += 1
            percent = round((score / (total * 10) * 100))
        context = {
                    'score':score,
                'time': request.POST.get('timer'),
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
                    }
        return render(request,'pythonquiz/pythonresult.html', context)

    else:
        questions = PythonQuesModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'pythonquiz/pythonpage.html', context)


