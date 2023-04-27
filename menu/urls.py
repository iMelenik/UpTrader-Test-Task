from django.urls import path

from menu.views import index

app_name = 'menus'
urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug_name>/', index, name='index'),
]
