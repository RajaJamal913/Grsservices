
from django.contrib import admin
from django.urls import path

from services import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
     path('team/', views.Team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)