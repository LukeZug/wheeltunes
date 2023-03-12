import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wheeltunes.settings')

import django
django.setup()

from wheeltunes_app.models import *
import random

NUM_OF_SONGS = 100

def slow_sad_songs():

    Song.objects.get_or_create(
        title='Runaway',
        artist='Lil Peep',
        static_url='/static/songs/Runaway.mp3',
        energy=1,
        tempo=80,
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Demons',
        artist='Imagine Dragons',
        static_url='/static/songs/Demons.mp3',
        energy=20,
        tempo=90,  
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Heat Waves',
        artist='Glass Animals',
        static_url='/static/songs/HeatWaves.mp3',
        energy=20,
        tempo=40,  
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Down By The River',
        artist='Milky Chance',
        static_url='/static/songs/DownByTheRiver.mp3',
        energy=20,
        tempo=50,  
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Someone You Loved',
        artist='Lewis Capaldi',
        static_url='/static/songs/SomeoneYouLoved.mp3',
        energy=1,
        tempo=60,
        mood='sad',
    )

def mid_sad_songs():

    Song.objects.get_or_create(
        title='In The End',
        artist='Linkin Park',
        static_url='/static/songs/InTheEnd.mp3',
        energy=90,
        tempo=110,  
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Numb',
        artist='Linkin Park',
        static_url='/static/songs/Numb.mp3',
        energy=90,
        tempo=120,  
        mood='sad',
    )

    Song.objects.get_or_create(
        title='The Monster',
        artist='Eminem',
        static_url='/static/songs/TheMonster.mp3',
        energy=20,
        tempo=110,  
        mood='sad',
    )

    Song.objects.get_or_create(
        title='Not Afraid',
        artist='Eminem',
        static_url='/static/songs/NotAfraid.mp3',
        energy=20,
        tempo=115,  
        mood='sad',
    )

    return

def fast_sad_songs():

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
        title='I fall apart',
        artist='Post Malone',
        static_url='/static/songs/IFallApart.mp3',
        energy=30,
        tempo=144,
        mood='sad',
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
        title='Crawling',
        artist='Linkin Park',
        static_url='/static/songs/Crawling.mp3',
        energy=90,
        tempo=140, 
        mood='sad',
    )
    return

def slow_middle_songs():

    Song.objects.get_or_create(
        title='Californication',
        artist='Red Hot Chili Peppers',
        static_url='/static/songs/Californication.mp3',
        energy=20,
        tempo=60,  
        mood='middle',
    )

    Song.objects.get_or_create(
        title='The A Team',
        artist='Ed Sheeran',
        static_url='/static/songs/TheATeam.mp3',
        energy=20,
        tempo=60,  
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Candy',
        artist='Paolo Nutini',
        static_url='/static/songs/Candy.mp3',
        energy=20,
        tempo=60,  
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Snow (Hey Oh)',
        artist='Red Hot Chili Peppers',
        static_url='/static/songs/Snow.mp3',
        energy=20,
        tempo=80,  
        mood='middle',
    )

    Song.objects.get_or_create(
        title='3 Nights',
        artist='Dominic Fike',
        static_url='/static/songs/3Nights.mp3',
        energy=20,
        tempo=80,  
        mood='middle',
    )

def mid_middle_songs():

    Song.objects.get_or_create(
        title='Fluorescent Adolescent',
        artist='Arctic Monkeys',
        static_url='/static/songs/FluorescentAdolescent.mp3',
        energy=50,
        tempo=112,
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Alev Alev',
        artist='Hayat',
        static_url='/static/songs/AlevAlev.mp3',
        energy=50,
        tempo=100,
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Rock Your Body',
        artist='Justin Timberlake',
        static_url='/static/songs/RockYourBody.mp3',
        energy=10,
        tempo=100,
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Gives You Hell',
        artist='The All-American Rejects',
        static_url='/static/songs/GivesYouHell.mp3',
        energy=60,
        tempo=100,
        mood='middle',
    )

    Song.objects.get_or_create(
        title='When The Day Comes',
        artist='Nico & Vinz',
        static_url='/static/songs/WhenTheDayComes.mp3',
        energy=20,
        tempo=120,  
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Never Gonna Give You Up',
        artist='Rick Astley',
        static_url='/static/songs/NeverGonnaGiveYouUp.mp3',
        energy=20,
        tempo=115,  
        mood='middle',
    )

def fast_middle_songs():

    Song.objects.get_or_create(
        title='Undercover Martyn',
        artist='Two Door Cinema Club',
        static_url='/static/songs/UndercoverMartyn.mp3',
        energy=60,
        tempo=160,
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Boulevard of Broken Dreams',
        artist='Green Day',
        static_url='/static/songs/BoulevardOfBrokenDreams.mp3',
        energy=20,
        tempo=167,  
        mood='middle',
    )

    Song.objects.get_or_create(
        title='Sometimes',
        artist='Gerry Cinnamon',
        static_url='/static/songs/Sometimes.mp3',
        energy=20,
        tempo=150,  
        mood='middle',
    )

def slow_happy_songs():

    Song.objects.get_or_create(
        title='Superstition',
        artist='Stevie Wonder',
        static_url='/static/songs/Superstition.mp3',
        energy=10,
        tempo=40,
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Lean On',
        artist='Major Lazer & DJ Snake',
        static_url='/static/songs/LeanOn.mp3',
        energy=20,
        tempo=60,   
        mood='happy',
    )

    Song.objects.get_or_create(
        title='8TEEN',
        artist='Khalid',
        static_url='/static/songs/8TEEN.mp3',
        energy=20,
        tempo=60,  
        mood='happy',
    )

def mid_happy_songs():

    Song.objects.get_or_create(
        title='I got U',
        artist='Duke Dumont',
        static_url='/static/songs/IGotYou.mp3',
        energy=50,
        tempo=128,
        mood='happy',
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
        title='Mr. Fear',
        artist='SIAMES',
        static_url='/static/songs/Mr.Fear.mp3',
        energy=10,
        tempo=108,
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Pon De Replay',
        artist='Rihanna',
        static_url='/static/songs/PonDeReplay.mp3',
        energy=60,
        tempo=100,
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Stayin Alive',
        artist='Bee Gees',
        static_url='/static/songs/StayinAlive.mp3',
        energy=20,
        tempo=100,  
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Magic',
        artist='Olympic Ayres',
        static_url='/static/songs/Magic.mp3',
        energy=20,
        tempo=120,  
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Good Time',
        artist='Owl City',
        static_url='/static/songs/GoodTime.mp3',
        energy=20,
        tempo=120,  
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Little Talks',
        artist='Of Monsters and Men',
        static_url='/static/songs/LittleTalks.mp3',
        energy=20,
        tempo=100,  
        mood='happy',
    )
    
def fast_happy_songs():

    Song.objects.get_or_create(
        title='Paul Is Dead',
        artist='Scooter',
        static_url='/static/songs/PaulIsDead.mp3',
        energy=90,
        tempo=170,
        mood='happy',
    )

    Song.objects.get_or_create(
        title='Walk',
        artist='Kwabs',
        static_url='/static/songs/Walk.mp3',
        energy=20,
        tempo=140,  
        mood='happy',
    )

    Song.objects.get_or_create(
        title='On Our Way',
        artist='The Royal Concept',
        static_url='/static/songs/OnOurWay.mp3',
        energy=20,
        tempo=130,  
        mood='happy',
    )

    return



def populate():

    slow_sad_songs()
    slow_middle_songs()
    slow_happy_songs()
    mid_sad_songs()
    mid_middle_songs()
    mid_happy_songs()
    fast_sad_songs()
    fast_middle_songs()
    fast_happy_songs()

if __name__ == "__main__":
    populate()