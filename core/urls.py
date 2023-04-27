from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("menu.urls")),
]

if settings.DEBUG:
    urlpatterns = [path('silk/', include('silk.urls', namespace='silk'))]\
                  + urlpatterns