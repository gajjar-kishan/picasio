from django.conf.urls import include, url
from django.contrib import admin
from sketcher.views import sketch, suggestions
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'flippypicasio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
    url(r'^sketch-it$', sketch, name = 'sketch'),
    url(r'^suggestions$', suggestions, name = 'suggestions'),
]
