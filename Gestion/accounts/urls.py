from django.urls import path, include

from .import views

urlpatterns = [
    path('login/', views.login_user, name='login_etudiant'),
    path('logout/', views.logout_account, name='logout'),
]
