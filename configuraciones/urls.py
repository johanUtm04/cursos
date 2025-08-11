"""
URL configuration for CURSOSDJANGO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from contenido import views
from cursos import views as cursos_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    #Urls De cursos
    path('', cursos_views.principal, name= "principal"),
    path('create_curso/', cursos_views.create_course, name='create_curso'),
    path('cursos/', cursos_views.cursos, name= "cursos"),
    path('cursos/<int:pk>/editar/', cursos_views.edit_course, name="edit-curso"),
    path('cursos/<int:pk>/eliminar/', cursos_views.delete_course, name="delete-curso"),
    
    path('contacto/', views.contacto, name= "contacto"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)