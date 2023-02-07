from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    duration = models.IntegerField()
    file = models.FileField()
    energy = models.IntegerField()
    tempo = models.IntegerField()
    

    def __str__(self):
        return self.title
    

