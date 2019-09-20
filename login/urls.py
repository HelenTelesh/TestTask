from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views as local_view
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    # Session Login
#    path('enter/', local_view.get_auth_token, name='login'),
#    url(r'^login /$', local_view.get_auth_token, name='login'),
#    url(r'^logout/$', local_view.logout_user, name='logout'),
#    url(r'^auth/$', local_view.login_form, name='login_form'),
#    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),

    path('entry/', local_view.get_auth_token, name='login'),
    path('signup/', local_view.signup, name='SignUp'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login/logout2.html'), name='LogOut'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login/login.html'), name='LogIn'),
    path('token/', rest_framework_views.obtain_auth_token, name='get_auth_token'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)