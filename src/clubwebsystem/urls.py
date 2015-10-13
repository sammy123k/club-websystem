import os
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
  # Our site
  url(r'^$', 'mainsite.views.home', name='home'),
  url(r'^about/$', 'mainsite.views.about', name='about'),
  url(r'^editblock/(?P<page>\w+)/$', 'contentblocks.views.contentblock_edit', name='contentblock_edit'),
  url(r'^calendar/', 'events.views.calendar', name='calendar'),
  url(r'^eventjson/', 'events.views.eventjson', name='eventjson'),
  url(r'^eventmodify/', 'events.views.eventmodify', name='eventmodify'),
  url(r'^userprofile/$', 'clubmembers.views.userprofile', name='userprofile'),
  url(r'^userprofile/confirmemail/(?P<confirmation_key>\w+)/', 'clubmembers.views.confirmemail', name='confirmemail'),

  # Built-in pages
  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/', include('regbackend.urls')),

  # Catch-all (must be last)
  url(r'^(?P<page>\w+)/$', 'contentblocks.views.contentblock_view', name='contentblock_view'),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
