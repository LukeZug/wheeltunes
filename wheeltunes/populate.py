import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wheeltunes.settings')

import django
django.setup()

from wheeltunes_app.models import *
import random

NUM_OF_SONGS = 20

def populate():
    for i in range(NUM_OF_SONGS):
        create_mock_song(i)

def create_mock_song(i):
    Song.objects.get_or_create(
        title=f"Song number {i+1}",
        artist=f"Artist {i+1}",
        static_url="",
        energy=random.randint(0, 100),
        tempo=random.randint(50,150),
        mood=random.choice(['sad', 'middle', 'happy']),
        playable=True
    )

if __name__ == "__main__":
    populate()