"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.url.static import static

from django.contrib import admin
from django.urls import path
from mytestsite.views import saludo,despedida,damefecha,calculaEdad,cursoC,cursoCss


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('nosvemos/',despedida),
    path('fecha/',damefecha),
    path('edades/<int:edad>/<int:anio>',calculaEdad),
    path('cursoC/',cursoC),
    path('cursoCss/',cursoCss)
]
##
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)