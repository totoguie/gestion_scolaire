from django.urls import path 
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('formations/',views.formation,name='formation'),
    path('sessions/',views.sesion,name="session"),
    path('nos_atouts/',views.atout, name="nos_atout"),
    path('detail_filiere/',views.details ,name="detail"),
]
