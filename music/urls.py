from django.conf.urls import url

from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<pk>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/<pk>/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/<pk>/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/songs/<filter_by>/
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.SongsView.as_view(), name='songs'),

    # /music/song/add/
    url(r'^song/add/$', views.SongCreate.as_view(), name='song-add'),

    # /music/song/<pk>/
    url(r'^song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song-update'),

    # /music/song/<pk>/delete/
    url(r'^song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),

    # /music/song/<pk>/favorite/
    url(r'^song/(?P<pk>[0-9]+)/favorite/$', views.favorite_song, name='song-favorite'),

    # /music/album/<pk>/favorite/
    url(r'^album/(?P<pk>[0-9]+)/favorite/$', views.favorite_album, name='album-favorite'),
]
