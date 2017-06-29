from django.shortcuts import render, HttpResponse

def home(request):
    numbers = [1,2,3,4,5,6]
    name = "Ashwar Gupta"
    arg = {'myname': name, 'nos': numbers}
    return render(request, 'poll/home.html', arg)

def reg(request):
    return render(request, 'poll/form1.html')

