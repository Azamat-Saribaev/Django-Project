from django.contrib import admin

# from members import views
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
]