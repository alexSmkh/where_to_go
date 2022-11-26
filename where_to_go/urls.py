from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from where_to_go import views as where_to_go_views
from places import views as places_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', where_to_go_views.show_main_page),
    path('places/<int:pk>/', places_views.get_place, name='get_place'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
