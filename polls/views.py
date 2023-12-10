from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("pub_date")
    template = loader.get_template("polls/index.html")

    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request,"polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
          raise Http404("the question does not exist")
          
    return render(request,"polls/detail.html",{"question": question})

def results(request, question_id):
        return HttpResponse("you're looking at results of question %s" % question_id)

def vote(request, question_id):
        return HttpResponse("you're looking at votes for question %s" % question_id)


