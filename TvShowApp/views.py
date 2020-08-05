from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Showsnew, Allshows

def allshows(request):
    context = {
        'shows': Showsnew.objects.all()
    }
    return render(request, 'allshows.html', context)

def showsnew(request):
    return render(request, 'showsnew.html')

def createshow(request):
    validations = Showsnew.objects.show_validator(request.POST)
    if len(validations) > 0:
        for msg in validations.values():
            messages.error(request, msg)
        return redirect('/shows/new')
    Showsnew.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description'],
    )
    print(request.POST)
    return redirect('/shows')

def editshow(request, show_id):
    this_show = Showsnew.objects.get(id=show_id)
    context = {
        'show': this_show
    }
    return render(request, 'editshow.html', context)

def update(request, show_id):
    validations = Showsnew.objects.show_validator(request.POST)
    if len(validations) > 0:
        for msg in validations.values():
            messages.error(request, msg)
        return redirect(f'/shows/{show_id}/edit')
    updateshow = Showsnew.objects.get(id=show_id)
    updateshow.title = request.POST['title']
    updateshow.network = request.POST['network']
    updateshow.release_date = request.POST['release_date']
    updateshow.description = request.POST['description']
    updateshow.save()

    return redirect('/shows/')

def tvshow(request, show_id):
    this_show = Showsnew.objects.get(id=show_id)
    context = {
        'show': this_show
    }
    return render(request, 'tvshow.html', context)

def delete(request, show_id):
    deleteshow = Showsnew.objects.get(id=show_id)
    deleteshow.delete()
    return redirect('/shows')