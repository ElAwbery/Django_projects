from django.shortcuts import render, redirect
from hubapp.models import Hubapp
from django.http import HttpResponse

# Request is a Django object that gets passed around everywhere
# Views must return an http response object

# The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

def frontpage(request):
    return HttpResponse("<h1>Charlieawbery homepage</h1>")

def all_projects(request):
    # Load all objects from databaase
    projects=Hubapp.objects.all()
# !!!    return HttpResponse("<h1>Projects: " + str(len(projects)) + "</h1>")

    return render(request, 'hubapp/all_projects.html', {'projects': projects})

def project_detail(request, pk):
    '''pk is a primary key, integer'''
    project = Hubapp.objects.get(pk=pk)
    return render(request, 'hubapp/detail.html', {'project': project})
    
def vajrayana_redirect(request):
    response=redirect("https://vajrayananow.com/")
    return response
'''
def lucky_egg_redirect(request):
    response="<h1>Charlieawbery Lucky egg</h1>"
    # response=redirect("/lucky_egg")
    return response

def idletwilight_redirect(request):
    response="<h1>Charlieawbery Idletwilight</h1>"
    # response=redirect("/idletwilight")
    return response
'''

