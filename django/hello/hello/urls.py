from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Yogesh gaur Website Admin"
admin.site.site_title = "Yogesh gaur Website Admin Portal"
admin.site.index_title = "Welcome to Yogesh gaur Websites"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
