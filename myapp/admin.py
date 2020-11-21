from django.contrib import admin
from django.utils.html import format_html
from .models import Albume,Artist,Genre,Video_Clip
# Register your models here.
class AlbumeAdmin(admin.ModelAdmin):
    model = Albume
    list_per_page = 10
    prepopulated_fields = {'slug': ('name',), }
    list_display = (
        'id',
        'name',
        'artist',
        'genre',
        'published',
        'status',
        'albume_art',
    )  
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
        'artist',
        'genre'
    )
    
    def albume_art(self, obj):
            return format_html('<img src={} width="100" height="100" />', obj.image.url )
        

class ArtistAdmin(admin.ModelAdmin): 
    model = Artist
    list_per_page = 10
    prepopulated_fields = {'slug': ('name',), }
    search_fields = (
        'name', 
    )
    list_display =(
        'id',
        'name',
        'artist_picture',    
    )
    def artist_picture(self, obj):
        return format_html('<img src={} width="100" height="100" />', obj.image.url )

class GenreAdmin(admin.ModelAdmin):  
    model = Genre
    prepopulated_fields = {'slug': ('name',), }
    list_per_page = 10 
    search_fields = (
        'name', 
    )
    list_display = (
        'id',
        'name',
    ) 
    

class Video_ClipAdmin(admin.ModelAdmin):
    model = Video_Clip
    list_per_page = 10
    prepopulated_fields = {'slug': ('name',), }
    search_fields = (
        'name', 
    )
    list_display = (
        'id',
        'name',
        'artist',
        'genre',
        'published',
        'status',
        'video_thumbnail',   
    )  
    def video_thumbnail(self, obj):
        return format_html('<img src={} width="100" height="100" />', obj.image.url )

admin.site.register(Albume,AlbumeAdmin)
admin.site.register(Artist,ArtistAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Video_Clip,Video_ClipAdmin)
