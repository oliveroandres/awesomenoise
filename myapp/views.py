from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Artist, Albume, Genre, Video_Clip

# Create your views here.
#Home
class Home(ListView):
    model = Albume
    template_name = 'myapp/home.html'
    paginate_by = 12
#Artists 
class ArtistListView(ListView):
    model = Artist
    template_name = 'myapp/artist_list.html'
    paginate_by = 12
   
    

class ArtistDetailView(DetailView):
    model = Artist    
    

#Albumes    
class AlbumeListView(ListView):
    model = Albume
    template_name = 'myapp/albume_list.html'  
    paginate_by = 12

class AlbumeDetailView(DetailView):
    model = Albume
    
#Genres
class GenreListView(ListView):
    model = Genre
    template_name = 'myapp/genre_list.html'   
    paginate_by = 12

class GenreDetailView(DetailView):  
    model = Genre

#Video Clips
class Video_ClipListView(ListView):
    model = Video_Clip
    template_name = 'myapp/video_clip_list.html'        
    paginate_by = 12

class Video_ClipDetailView(DetailView):
    model = Video_Clip 

#Search Function

class Search_ResultListView(ListView):
    model = Albume
    template_name = 'myapp/search_result.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Albume.objects.filter(
            Q(name__icontains=query) | Q(audio_Format__icontains=query) | Q(published__icontains=query) 
        )
        return object_list

        