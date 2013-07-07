from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'navalny.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'picket.views.home', name='home'),
    url(r'^go$', 'picket.views.go', name='go'),
    url(r'^wont_go$', 'picket.views.wont_go', name='wont_go'),

    url(r'^cb$', 'picket.views.auth_callback', name='auth_callback'),

    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
