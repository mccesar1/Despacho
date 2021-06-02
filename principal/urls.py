from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('', views.inicio, name='index'),
    path('contacto', views.contacto),
    path('welcome', views.welcome),
    path('reportes', views.reportes),
    path('declaraciones', views.declaraciones),
    path('login', views.login),
    path('logout', views.logout),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)