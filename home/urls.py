from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:post_id>/<slug:post_slug>/', views.postdetail.as_view(), name='postdetail'),
    path('post/delete/<int:post_id>/', views.postdelete.as_view(), name='postdelete'),
    path('post/update/<int:post_id>/', views.postupdate.as_view(), name='postupdate'),
    path('post/creat/', views.postcreat.as_view(), name='postcreat'),
    path('reply/<int:post_id>/<int:comment_id>', views.PostAddReplyView.as_view(), name='addreply'),
    path('like/<int:post_id>/', views.PostLikeView.as_view(), name='postlike'),
]
