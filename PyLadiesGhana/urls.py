"""PyLadiesGhana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('coc/', include('coc.urls', namespace='coc')),
    path('events/', include('events.urls', namespace='events')),
    path('about/', include('about.urls', namespace='about')),
    path('resources/', include('resources.urls', namespace='resources')),
    path('sponsors/', include('sponsors.urls', namespace='sponsors')),
    path('locations/', include('locations.urls', namespace='locations')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('blog/', include("pinax.blog.urls", namespace="pinax_blog")),
    path('announcements/', include("pinax.announcements.urls", namespace="pinax_announcements")),
    path('photologue/', include('photologue.urls', namespace='photologue')),
    path('', include('pwa.urls')),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin Header Settings
admin.site.site_header = "PyLadies Ghana Admin"
admin.site.index_title = "PyLadies Ghana"
admin.site.site_title = "PyLadies Ghana Webiste"