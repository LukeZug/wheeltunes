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

        # Quite like the Singleton design pattern -- just want to keep zero or one object of this model at all times.
        sensor = SensorData.objects.all().first()
        if sensor:
            sensor.heart_rate = heart_rate
            sensor.background_noise = background_noise
            sensor.speed = speed
            sensor.save()
        else:
            SensorData.objects.create(heart_rate=heart_rate, speed=speed, background_noise=background_noise)

        return redirect(reverse('sliders'))
    else:
        # If we have sensor data (and songs), then pick the songs in a way where
        # songs are most aligned with the users' heart rate, speed, and background noise.

        sensor_data = SensorData.objects.all().first()
        songs = songs_linked_to_heart_rate = Song.objects.all()

        if sensor_data:
            # Get songs with tempo (+/-) 10bpm (or whatever specified) of the user heart rate.
            TEMPO_HEART_RATE_OFFSET = 10
            heart_rate = sensor_data.heart_rate
            songs_linked_to_heart_rate = songs.filter(
                tempo__gte=heart_rate-TEMPO_HEART_RATE_OFFSET
            ).filter(
                tempo__lte=heart_rate+TEMPO_HEART_RATE_OFFSET
            )

        context_dict = {
            'playable_songs': songs_linked_to_heart_rate,
            'sensor_data': sensor_data,
        }
        return render(request, 'wheeltunes_app/sliders_determine_song.html', context=context_dict)
