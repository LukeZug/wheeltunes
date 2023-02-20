from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    static_url = models.URLField(blank=True, null=True)
    energy = models.IntegerField(default=0)
    tempo = models.IntegerField(default=50)
    playable = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    

