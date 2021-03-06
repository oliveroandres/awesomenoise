from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Artist, Albume, Genre, Video_Clip

# Create your views here.
#Home
class Home(ListView):
    model = Albume
    template_name = 'myapp/home.html'
    paginate_by = 6
#Artists 
class ArtistListView(ListView):
    model = Artist
    template_name = 'myapp/artist_list.html'
    paginate_by = 12

class Artist_FilterListView(ListView):
    model = Artist    
    template_name = 'myapp/artist_filter.html'
    def get_queryset(self):
        self.artist = get_object_or_404(Artist, slug=self.kwargs['slug'])
        return Albume.objects.filter(artist=self.artist)

    def get_context_data(self, **kwargs):
        context = super(Artist_FilterListView, self).get_context_data(**kwargs)
        context ['artist'] = self.artist
        return context  
    

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


class Genre_FilterListView(ListView):
    model = Albume
    template_name = 'myapp/genre_filter.html'
    def get_queryset(self):
        self.genre = get_object_or_404(Genre, slug=self.kwargs['slug'])
        return Albume.objects.filter(genre=self.genre)

    def get_context_data(self, **kwargs):
        context = super(Genre_FilterListView, self).get_context_data(**kwargs)
        context ['genre'] = self.genre
        return context    


#Video Clips
class Video_ClipListView(ListView):
    model = Video_Clip
    template_name = 'myapp/video_clip_list.html'        
    paginate_by = 12

    

class Video_ClipDetailView(DetailView):
    model = Video_Clip 

#Search Function

class Search_Albume_ResultListView(ListView):
    model = Albume
    template_name = 'myapp/search_albume_result.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Albume.objects.filter(
            Q(name__icontains=query) | Q(audio_Format__icontains=query) | Q(published__icontains=query) 
        )
        return object_list


class Search_Artist_ResultListView(ListView):
    model = Artist
    template_name = 'myapp/search_artist_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Artist.objects.filter(
            Q(name__icontains=query)
        )    
        return object_list

class Search_Video_Clip_ResultListView(ListView):
    model = Video_Clip       
    template_name = 'myapp/search_video_clip_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Video_Clip.objects.filter(
            Q(name__icontains=query)
        )    
        return object_list