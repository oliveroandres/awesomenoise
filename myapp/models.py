from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=40, null=True, unique=True)
    slug = models.SlugField(max_length=40, null=True, unique=True)
    image =  models.ImageField('artist Picture',upload_to='artist_picture/', default = 'artist_picture/default.png', blank=True, null=True)
    description = models.TextField(max_length=1000, null=True)

    class Meta:
        ordering = ['-id',]
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=40, null=True, unique=True)
    slug = models.SlugField(max_length=40, null=True, unique=True)

    class Meta:
        ordering = ['-id',]
    
    def __str__(self):
        return self.name

class Albume(models.Model):
    
    AUDIO_FORMAT_CHOICES = (
    ('m4a','M4A'),
    ('mp3','MP3'),
    ('flac','FLAC')
    )
    STATUS_CHOICES = (
    ('active','ACTIVE'),
    ('inactive','INACTIVE'),
    )

    

    name = models.CharField(max_length=40, null=True, unique=True)
    slug = models.SlugField(max_length=40, null=True, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    audio_Format = models.CharField(max_length=40, choices=AUDIO_FORMAT_CHOICES, default='M4A', null=True)
    published = models.DateField(null=True, blank=True)
    image =  models.ImageField('Albume Art',upload_to='albume_art/', default = 'albume_art/default.png', blank=True, null=True) 
    link = models.CharField(max_length=100,default='Copy link Here',null=True)
    status = models.CharField(max_length=40, null=True, choices=STATUS_CHOICES, default='ACTIVE')
    description = models.TextField(max_length=1000 , null=True)  

    class Meta:
        ordering = ['-id',] 

    def __str__(self):
        return self.name



class Video_Clip(models.Model):
    
    STATUS_CHOICES = (
    ('active','ACTIVE'),
    ('inactive','INACTIVE'),
    )

    VIDEO_FORMAT_CHOICES = (
    ('m4v','M4V'),
    ('mp4', 'MP4'),
    )
    name = models.CharField(max_length=40, null=True, unique=True)
    slug = models.SlugField(max_length=40, null=True, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    video_Format = models.CharField(max_length=40, choices=VIDEO_FORMAT_CHOICES, default='M4V', null=True)
    published = models.DateField(null=True, blank=True)
    image =  models.ImageField('Video Thumbnail',upload_to='video_thumbnail/', default = 'video_thumbnail/default.png', blank=True, null=True) 
    link = models.CharField(max_length=100, default='Copy link Here',null=True)
    status = models.CharField(max_length=40, null=True, choices=STATUS_CHOICES, default='ACTIVE')
    description = models.TextField(max_length=1000 , null=True)
    
    class Meta:
        ordering = ['-id',]

    class Meta:
        verbose_name = "Video Clip"
    
    def __str__(self):
        return self.name

    
