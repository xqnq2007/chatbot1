from django.shortcuts import render

# Create your views here.
from bot1.models import Answers
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return render_to_response("bot1")
    answer_list = Answers.objects.all()
    return render_to_response('index1.html', {'answer_list': answer_list})

def interface(request):
    answer_list = 'ansershaha'
    #question='my question'
    #return render_to_response('interface.html',{'question':answer_list})
    #response = HttpResponse("Text only, please.")
    #return response
    #response = HttpResponse()
    response = HttpResponse("Text only, please.")
    #response.write("<html>")
    #response.write("this is a tiny web page!")
    #response.write("</html>")
    return  response