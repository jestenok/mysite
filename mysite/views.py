from django.shortcuts import render
from django.http import HttpResponse
from mysite.forms import SendMessageForm


def index(request):
    data = {
        'form': SendMessageForm()
    }
    return render(request, 'index.html', data)


def health(request):
    return HttpResponse('uwuwuwuwqwoengfowefwefwefwemqengmfd,ngjewbjkrhebfu')


def mail(request):
    return render(request, 'mailru-domainFq9vlubBVRksuY5D.html')
