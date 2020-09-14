from .forms import ApplyJobForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

#def index(request):
#    context = {}
#    return render(request,'portal/index.html',context)

def index(request):
    form = ApplyJobForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ApplyJobForm()
        print("Data Saved")
    else:
        print("error")

    context = {
        'form': form
    }
    return render(request, "portal/index.html", context)

def detail(request, id):
    return HttpResponse("You're looking at Name %s." % id)

def results(request, id):
    response = "You're looking at the results of Name %s."
    return HttpResponse(response % id)

def vote(request, id):
    return HttpResponse("You're voting on Name %s." % id)