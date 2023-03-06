from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from wheeltunes_app.models import *
from wheeltunes_app.forms import UploadSongForm


def index(request):
    if request.method =="POST":
        sensor = SensorData.objects.all().first()
        mood = list(request.POST.keys())[1]
        if sensor:
            sensor.mood = mood
            sensor.save()
        else:
            SensorData.objects.create(mood=mood)

        return redirect(reverse('sliders'))
    
    return render(request, 'wheeltunes_app/index.html')


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

        data = generate_sliders_page()

        data['sensor_data'] = {
            'speed': data.get('sensor_data').speed,
            'heart_rate': data.get('sensor_data').heart_rate,
            'background_noise': data.get('sensor_data').background_noise,
        }

        return JsonResponse(data)
    else:
        # If we have sensor data (and songs), then pick the songs in a way where
        # songs are most aligned with the users' heart rate, speed, and background noise.
        print(request)
        context_dict = generate_sliders_page()
        return render(request, 'wheeltunes_app/sliders_determine_song.html', context=context_dict)


def choose_offsets(current_speed):
    # Given a speed, determine how much the songs can vary from the heart rate.
    # Lower speed => songs with tempo quite a bit lower than heart rate are allowed
    # Higher speed => songs with quite a bit higher tempo than HR are allowed

    upper_offset = lower_offset = 10
    if 0 <= current_speed <= 10:
        # Cycling up to 10mph -- despite HR, it's a slow cycle so allow for larger range of slower tempo songs.
        lower_offser = 30
    elif 10 < current_speed <= 20:
        # Cycling between 10 and 20mph, faster cycle so reduce number of slower songs played.
        lower_offser = 10
    else:
        # Cycling over 20mph -- very fast, so allow for a larger range of higher BPM songs.
        upper_offset = 30
        lower_offser = 10  # incase they got to this speed between updates

    return lower_offser, upper_offset


def generate_sliders_page():
    sensor_data = SensorData.objects.all().first()
    songs = songs_linked_to_heart_rate = Song.objects.all()

    if sensor_data:
        # Get songs with tempo (+/-) 10bpm (or whatever specified) of the user heart rate.
        TEMPO_HEART_RATE_LOWER_OFFSET, TEMPO_HEART_RATE_UPPER_OFFSET = choose_offsets(sensor_data.speed)

        heart_rate = sensor_data.heart_rate
        songs_linked_to_heart_rate = songs.filter(
            tempo__gte=heart_rate-TEMPO_HEART_RATE_LOWER_OFFSET
        ).filter(
            tempo__lte=heart_rate+TEMPO_HEART_RATE_UPPER_OFFSET
        ).filter(
            mood=sensor_data.mood
        )

    return {
        'playable_songs': [str(song) for song in list(songs_linked_to_heart_rate)],
        'sensor_data': sensor_data,
        'lower_offset': sensor_data.heart_rate - TEMPO_HEART_RATE_LOWER_OFFSET,
        'upper_offset': sensor_data.heart_rate + TEMPO_HEART_RATE_UPPER_OFFSET,
    }
