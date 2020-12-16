from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

"""
    This function is the main page where the user first goes.
    All this page does is output the 'Hello Django' message.
"""
def index(request):
    return HttpResponse("Hello Django!")