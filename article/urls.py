from django.urls import path

from home.views import(
    dashboard_view,
    addarticle_view,
    single_view,
    update_view,
    delete_view,
    post_view,
    like_post
    )

app_name = 'article'

urlpatterns = [
    path('dashboard/',dashboard_view,name='dashboard'),
    path('addarticle/',addarticle_view),
    path('single/',single_view,name='single'),
    path('update/<int:id>',update_view),
    path('delete/<int:id>',delete_view),
    path('', post_view ,name='post-list'),
    path('like/',like_post,name='like-post'),


]