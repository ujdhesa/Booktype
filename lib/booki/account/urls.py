from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'booki.account.views.view_accounts', name='view_accounts'),

    url(r'^signin/$', 'booki.account.views.signin', name='signin'),  
    url(r'^login/$', 'booki.account.views.signin', name='login'),  

    url(r'^signout/$', 'booki.account.views.signout', name='signout'),  

    url(r'^register/$', 'booki.account.views.register', name='register'),

    url(r'^(?P<username>\w+)/', 'booki.account.views.view_profile', name='view_profile')                     
)