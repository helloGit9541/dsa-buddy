from itertools import count
from django.shortcuts import render
from accounts.models import *
# Create your views here.
def home(request):
    context = {}
    problems = Problem.objects.filter(user=request.user)
    context['num_problem'] = len(problems)
    count = 1
    for problem in problems:
        new_problem = problem
        if count%2==0:
            new_problem.even = True
        else:
            new_problem.even = False
        problem=new_problem
        ++count
    context['problems'] = problems
    context['topics'] = Topic.objects.all()
    print(context)
    return render(request,template_name='base/home.html', context=context)