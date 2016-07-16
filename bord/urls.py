"""Root URL definitions."""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
