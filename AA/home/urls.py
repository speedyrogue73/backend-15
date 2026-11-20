from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<slug:post_slug>/', views.DetailView.as_view(), name='detail'),
    path('create-post/', views.CreatePostView.as_view(), name='create-post'),
    path('reply/<slug:post_slug>/<int:comment_id>/', views.ReplyView.as_view(), name='reply'),
    path('remove-comment/<int:comment_id>/', views.RemoveCommentView.as_view(), name='remove-comment'),
]