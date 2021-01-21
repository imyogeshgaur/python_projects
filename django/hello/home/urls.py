from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index.html',views.index,name="index"),
    path('about.html',views.about,name="about"),
    path('portfolio.html',views.portfolio,name="portfolio"),
    path('blog.html',views.blog,name="blog"),
    path('blogpost.html',views.blogPost,name="blogPost"),
    path('contact.html',views.contact,name="contact")
]
