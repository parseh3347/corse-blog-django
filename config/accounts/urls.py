from django.urls import path
from . import views
# from django.conf.urls import url
# from django.contrib.auth import views as authentication_views



urlpatterns = [
    path ( 'signup/',views.SignUpView.as_view(),name='signup'),
    path ( 'logout/',views.logout_views,name='logout'),
]


    # path('logout', 'django.contrib.auth.views.logout', name='logout'),

    # path('logout/',authentication_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    # path("logout/", auth_views.LogoutView.as_view()),
