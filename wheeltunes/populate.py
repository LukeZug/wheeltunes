import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wheeltunes.settings')

import django
django.setup()

from wheeltunes_app.models import *
import random

NUM_OF_SONGS = 100

def populate():

    Song.objects.get_or_create(
        title='Fluorescent Adolescent',
        artist='Arctic Monkeys',
        static_url='/static/songs/FluorescentAdolescent.mp3',
        energy=50,
        tempo=112,
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Hurt ME',
        artist='Juice WRLD',
        static_url='/static/songs/HurtMe.mp3',
        energy=20,
        tempo=157,
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Way Down We Go',
        artist='KALEO',
        static_url='/static/songs/WayDownWeGo.mp3',
        energy=10,
        tempo=163,
        mood='sad',
    )

    Song.objects.get_or_create(
        title='I got U',
        artist='Duke Dumont',
        static_url='/static/songs/IGotYou.mp3',
        energy=50,
        tempo=128,
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Someone You Loved',
        artist='Lewis Capaldi',
        static_url='/static/songs/SomeoneYouLoved.mp3',
        energy=1,
        tempo=110,
        mood='sad',
    )

    Song.objects.get_or_create(
        title='I fall apart',
        artist='Post Malone',
        static_url='/static/songs/IFallApart.mp3',
        energy=30,
        tempo=144,
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Get Out My Head',
        artist='Shane Codd',
        static_url='/static/songs/GetOutMyHead.mp3',
        energy=60,
        tempo=124,
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Paul Is Dead',
        artist='Scooter',
        static_url='/static/songs/PaulIsDead.mp3',
        energy=90,
        tempo=170,
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Undercover Martyn',
        artist='Two Door Cinema Club',
        static_url='/static/songs/UndercoverMartyn.mp3',
        energy=60,
        tempo=160,
        mood='middle',
    )

    Song.objects.get_or_create(
        title='FML',
        artist='Wasted Penguinz',
        static_url='/static/songs/FML.mp3',
        energy=80,
        tempo=150,
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Runaway',
        artist='Lil Peep',
        static_url='/static/songs/Runaway.mp3',
        energy=1,
        tempo=80,
        mood='sad',
    )

    for i in range(NUM_OF_SONGS):
        create_mock_song(i)

def create_mock_song(i):
    Song.objects.get_or_create(
        title=f"Song number {i+1}",
        artist=f"Artist {i+1}",
        static_url="/static/songs/UndercoverMartyn.mp3",
        energy=random.randint(0, 100),
        tempo=random.randint(50,150),
        mood=random.choice(['sad', 'middle', 'happy']),
        playable=True
    )

if __name__ == "__main__":
    populate()