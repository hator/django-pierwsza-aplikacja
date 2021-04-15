from django.urls import path

from blog import views

urlpatterns = [
    path('', views.post_list),
    path('posts/<int:post_id>', views.post_details),
    path('posts/<int:post_id>/comment', views.add_comment),
]