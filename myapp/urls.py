from django.urls import path
from django.shortcuts import reverse
from myapp.views import (Home)
from myapp.views import (ArtistListView, ArtistDetailView)
from myapp.views import (AlbumeListView, AlbumeDetailView)
from myapp.views import (GenreListView, GenreDetailView)
from myapp.views import (Video_ClipListView, Video_ClipDetailView)
from myapp.views import (Search_ResultListView)



urlpatterns = [
    #Home
    path('', Home.as_view(), name = 'home'), 
    #Artists
    path('artists/', ArtistListView.as_view(),name = 'artists'), 
    path('artist/<slug:slug>/', ArtistDetailView.as_view(),name = 'artist'),
    #Albumes
    path('albumes/', AlbumeListView.as_view(), name = 'albumes'),
    path('albume/<slug:slug>/', AlbumeDetailView.as_view(),name = 'albume'),
    #Genres
    path('genres/', GenreListView.as_view(), name = 'genres'),
    path('genre/<slug:slug>/', GenreDetailView.as_view(),name = 'genre'),
    #Video_Clips
    path('video-clips/',Video_ClipListView.as_view(),name = 'video-clips'),
    path('video-clip/<slug:slug>/', Video_ClipDetailView.as_view(),name = 'video-clip'),
    #Search_Result
    path('search-result/',Search_ResultListView.as_view(),name = 'search-result'),
]
