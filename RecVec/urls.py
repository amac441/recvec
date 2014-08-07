from datetime import datetime
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView
from django.contrib import admin

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', TemplateView.as_view(template_name="app/index.html"), name='home'),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^blog/', TemplateView.as_view(template_name="app/blog.html"), name='blog'),
    url(r'^user_profile/', TemplateView.as_view(template_name="app/user_profile.html"), name='user_profile'),
    url(r'^search/', TemplateView.as_view(template_name="app/search.html"), name='search'),
    url(r'^listing/', TemplateView.as_view(template_name="app/list_single.html"), name='listing'),
    url(r'^how-it-works/', TemplateView.as_view(template_name="app/how.html"), name='how'),
    url(r'^post/', TemplateView.as_view(template_name="app/post.html"), name='post'),

)
