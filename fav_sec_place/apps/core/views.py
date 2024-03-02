from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
    return render(request, 'core/home.html')
