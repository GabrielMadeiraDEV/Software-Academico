# urls.py do projeto principal (ex: config/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Aqui você inclui as URLs do seu app
]
