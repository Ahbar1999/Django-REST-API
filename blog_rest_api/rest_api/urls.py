from django.urls import path
from rest_api import views


urlpatterns = [
    path('all', views.blog_post_list),
    path('create', views.create_blog_post),
    path('create/<int:id>', views.update_blog_post)
]
