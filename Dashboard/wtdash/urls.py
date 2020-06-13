from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib.auth import views as auth
# from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

urlpatterns = [

    #FrontEnd
    url(r'^$', views.index, name='home'),
    url(r'^home/$', views.index, name='home'),
    url(r'^login/$', auth.login, {'template_name': 'login.html'}, name='login'),
    url(r'^register/', views.register, name="register"),
    url(r'^logout/$', auth.logout, {'next_page': 'home'}, name='logout'),

]