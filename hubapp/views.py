from django.shortcuts import render

from django.http import HttpResponse

# Takes a request object from the browser and returns a response object
def frontpage(request):
    return HttpResponse("<h1>Charlieawbery homepage</h1>")
