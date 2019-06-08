from django.urls import path

from .views import (blog_post_detail_view,
    blog_post_list_view, blog_post_create_view,
    blog_post_update_view,
    blog_post_delete_view)


urlpatterns = [
    #path('blog/<int:post_id>', blog_post_detail),
    path('', blog_post_list_view),
    #path('blog-new/', blog_post_create_view), # use blog-new and the slug can cause problems
    path('<str:post_slug>', blog_post_detail_view),
    path('<str:post_slug>/edit', blog_post_update_view),
    path('<str:post_slug>/delete', blog_post_delete_view),
]
