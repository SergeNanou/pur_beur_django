"""amateurs_nutella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
import debug_toolbar
import connect
import research
import save
from research import views
from connect import views
from save import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', connect.views.register, name='register'),
    url(r'^user_login/$', connect.views.user_login, name='user_login'),
    url(r'^legal/$', connect.views.legal, name='legal'),
    url(r'^$', research.views.reception, name='reception'),
    url(r'^search/$', research.views.search, name='search'),
    url(r'^save/$', save.views.save_prod, name='save'),
    url(r'^aliment/$', save.views.aliment, name='aliment'),
    url(r'^index/$', connect.views.index, name='index'),
    url(r'^special/', connect.views.special, name='special'),
    url(r'^connect/', include('connect.urls')),
    url(r'^logout/$', connect.views.user_logout, name='logout'),
    url(r'ind_pge_connex/', connect.views.ind_pge_connex,
        name='ind_pge_connex'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:

    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
