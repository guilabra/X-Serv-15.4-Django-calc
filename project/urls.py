from django.conf.urls import include, url
from django.contrib import admin
from calc import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+)\+(\d+)', views.suma),
    url(r'^(\d+)\-(\d+)', views.resta),
    url(r'^(\d+)\*(\d+)', views.multiplica),
    url(r'^(\d+)\/(\d+)', views.divide)

]
