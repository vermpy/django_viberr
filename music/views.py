from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Album, Song


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        if len(self.request.GET) > 0:
            q = self.request.GET['q']
            return Album.objects.filter(album_title__icontains=q)
        else:
            return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'year', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'year', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class SongsView(generic.ListView):
    template_name = 'music/songs.html'
    context_object_name = 'songs'

    def get_queryset(self):
        filter_by = self.kwargs['filter_by']
        if filter_by == 'all':
            return Song.objects.all()
        elif filter_by == 'favorites':
            return Song.objects.filter(is_favorite=True)


class SongCreate(CreateView):
    model = Song
    fields = ['album', 'song_title', 'file_type', 'audio_file']


class SongUpdate(UpdateView):
    model = Song
    fields = ['album', 'song_title', 'file_type', 'audio_file']


class SongDelete(DeleteView):
    model = Song

    def get_success_url(self):
        return reverse_lazy('music:detail', kwargs={'pk': self.object.album.pk})


def favorite_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        pass
    else:
        return redirect('music:detail', pk=song.album.id)


def favorite_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        pass
    else:
        return redirect('music:index')
