from django.shortcuts import render, redirect
from wheeltunes_app.models import *
from wheeltunes_app.forms import UploadSongForm


# Create your views here.
def index(request):
    if request.method =="POST":
        form = UploadSongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UploadSongForm()

    songs = Song.objects.all()
    context = {'songs': songs, 'form': form}


    return render(request, 'wheeltunes_app/index.html', context=context)


def sliders(request):
    context_dict = {}
    return render(request, 'wheeltunes_app/sliders_determine_song.html', context=context_dict)
