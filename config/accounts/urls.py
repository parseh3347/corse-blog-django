from django.urls import path
# from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path ( 'logout/',views.logout_views,name='logout'),

    path ( 'signup/',views.SignUpView.as_view(),name='signup'),
]

    # path('logout', 'django.contrib.auth.views.logout', name='logout'),

    # path("logout/", auth_views.LogoutView.as_view()),
