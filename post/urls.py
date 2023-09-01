from django.urls import path
from post.views import index, NewPost, PostDetails, tags, like, favorite, profile_search

urlpatterns = [
    path('', index, name='index'),
    path('newpost/',NewPost, name='newpost'),
    path('<uuid:post_id>', PostDetails, name='postdetails'),
    path('tag/<slug:tag_slug>', tags, name='tags'),
    path('<uuid:post_id>/like', like, name='postlike'),
    path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
    path('profile/', profile_search, name='profile_search')


]
