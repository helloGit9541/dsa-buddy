from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request,template_name='base/home.html', context=context)