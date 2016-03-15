from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    print req
    print req.user
    return HttpResponse('good')
