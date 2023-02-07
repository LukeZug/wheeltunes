from django import forms
from wheeltunes_app.models import Song

class UploadSongForm(forms.ModelForm):
    title = forms.CharField()
    artist = forms.CharField()
    file = forms.FileField()

    class Meta:
        model = Song
        fields = '__all__'
