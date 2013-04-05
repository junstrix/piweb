from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pi_dev.views.home', name='home'),
    # url(r'^pi_dev/', include('pi_dev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$','control.views.index'),
    (r'^tform/','control.views.tform'),
    (r'^login/','control.views.login'),
    (r'^logout/','control.views.logout'),
    (r'^led/','control.views.led'),
    (r'^search_form/','control.views.search_form'),
    (r'^search/','control.views.search'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve'),
)
