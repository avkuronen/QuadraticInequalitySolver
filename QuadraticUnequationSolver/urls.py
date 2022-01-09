from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', solveView, name='solve'),
    path('result/', resultView, name='result'),
    path('manual/', manualView, name='manual')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)