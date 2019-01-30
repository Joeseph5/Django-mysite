from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# from django.views import generic


def index(request):
    return render(request, 'homepage/index.html')
