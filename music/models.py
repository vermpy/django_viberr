from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500, verbose_name='title')
    year = models.IntegerField(validators=[MinValueValidator(1920), MaxValueValidator(2017)])
    genre = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    album_logo = models.FileField(verbose_name='logo')

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250, verbose_name='title')
    FILE_TYPE_CHOICES = (
        ('mp3', 'MP3 (MPEG-2 Audio Layer III)'),
        ('wav', 'WAV (Waveform Audio File Format)'),
        ('aiff', 'AIFF (Audio Interchange File Format)'),
    )
    file_type = models.CharField(max_length=4, choices=FILE_TYPE_CHOICES, default='mp3')
    is_favorite = models.BooleanField(default=False)
    audio_file = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.pk})

    def __str__(self):
        return self.song_title
