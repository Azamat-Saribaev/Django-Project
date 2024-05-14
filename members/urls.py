from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
                  path('', views.task_list, name='members'),
                  path('add-book/', views.add_book, name='add_book'),
                  path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
                  path('book/<int:book_id>/', views.book_detail, name='book_detail'),
                  path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
              ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
