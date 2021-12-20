from django.shortcuts import render


def index(request):
    """
    Polls index
    """
    return render(request, 'polls/index.html')
