from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'poll/home.html', context)

def create(request):
    context = {}
    return render(request, 'poll/create.html', context)

def results(request, poll_id):
    context = {}
    return render(request, 'poll/results.html', context)

def vote(request, poll_id):
    context = {}
    return render(request, 'poll/vote.html', context)
