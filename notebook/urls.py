from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('core/', include('core.urls')),
    path('notes/', include('notes.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
