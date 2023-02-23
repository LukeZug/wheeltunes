from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    static_url = models.URLField(blank=True, null=True)
    energy = models.IntegerField(default=0)
    mood = models.CharField(max_length=100, default="middle")
    tempo = models.IntegerField(default=50)
    playable = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} -> Energy: {self.energy} -> Tempo: {self.tempo} BPM -> Mood: {self.mood}"
    

class SensorData(models.Model):
    heart_rate = models.IntegerField(default=40)
    speed = models.IntegerField(default=0)
    background_noise = models.IntegerField(default=20)