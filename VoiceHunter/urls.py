from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = []

urlpatterns += [ path('favicon.ico', RedirectView.as_view(url=settings.MEDIA_URL + 'main/favicon.png')) ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('<str:lang>', include('App.urls')),
    path('', include('App.urls')),
    path('', include('App.urls_api')),

]