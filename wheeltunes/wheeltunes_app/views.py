from django.shortcuts import render, redirect
from django.urls import reverse
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
    if request.method == "POST":
        speed = int(request.POST.get('speed'))
        heart_rate = int(request.POST.get('heart-rate'))
        background_noise = int(request.POST.get('background-noise'))

        # Almost like the State design pattern -- just want to keep one object of this model.
        sensor = SensorData.objects.all().first()
        if sensor:
            sensor.heart_rate = heart_rate
            sensor.background_noise = background_noise
            sensor.speed = speed
            sensor.save()
        else:
            SensorData.objects.create(heart_rate=heart_rate, speed=speed, background_noise=background_noise)

        songs = Song.objects.all()
        for song in songs:
            song.playable = False
            if abs(song.tempo - heart_rate) <= 10:
                song.playable = True
            song.save()

        return redirect(reverse('sliders'))
    else:
        context_dict = {
            'playable_songs': Song.objects.all().filter(playable=True),
            'sensor_data': SensorData.objects.all().first()
        }
        return render(request, 'wheeltunes_app/sliders_determine_song.html', context=context_dict)
