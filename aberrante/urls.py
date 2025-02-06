"""
URL configuration for aberrante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from .views import home
from django.conf import settings
from django.conf.urls.static import static
# For robots.txt
from django.views.generic.base import RedirectView
from django.http import HttpResponse
# TemplateView for Sitemap
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # home minimal
    re_path(
        r"^robots.txt$",
        lambda r: HttpResponse(
            "User-agent: *\nDisallow: /admin/\nSitemap: https://www.aberrante.art/sitemap.xml",
            content_type="text/plain",
        ),
    ),
    # Sitemap
    re_path(
        r"^sitemap.xml$",
        TemplateView.as_view(
            template_name="sitemap.xml", content_type="application/xml; charset=utf-8"
        ),
    ),
]

# Serve media files in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
