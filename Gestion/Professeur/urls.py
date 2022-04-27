from django.urls import path
from .import views
urlpatterns = [
    path('',views.login_prof,name="login"),
    path('dashbord/',views.dash,name='dashbord'),
    path('logout/',views.logout_prof,name="logout"),
    path('liste_igl/',views.liste_igl ,name='igl'),
    path('liste_rit/',views.liste_rit ,name='rit'),
    path('liste_droit/',views.liste_droit ,name='droit'),
    path('liste_fc/',views.liste_fc ,name='fc'),
    path('liste_acg/',views.liste_acg,name='acg'),
    path('liste_seg/',views.liste_seg ,name='seg'),
    path('liste_fba/',views.liste_fba ,name='fba'),
    path('reset_password/' ,views.reset_pwd ,name="reset"),
    path('verification/',views.verification,name="verification"),
    path('confirmation/' ,views.confirm, name="confirmation"),
]
