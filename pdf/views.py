from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the PDF index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def edit(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def delete(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
