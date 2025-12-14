from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hey, am a django server.")
def success_page(request):
    return HttpResponse("Hey this is a success page")