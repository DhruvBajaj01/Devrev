from django.urls import path, include
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path(r'admin/',admin.site.urls),
    path('', views.home, name='home'),
    path('app/', include('app.urls')),
    path('',include('django.contrib.auth.urls')),
    path('',TemplateView.as_view(template_name='home.html'),name='home')
]
