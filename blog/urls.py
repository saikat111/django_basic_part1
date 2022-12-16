
from django.contrib import admin
from django.urls import path , include
admin.site.site_header = "Saikat Admin"
admin.site.site_title = "Saikat Admin Portal"
admin.site.index_title = "Welcome to Saikat Researcher Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
