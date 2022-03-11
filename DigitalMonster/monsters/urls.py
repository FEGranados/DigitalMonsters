from django.urls import path
from . import views

app_name="monsters"
urlpatterns = [
    path("", views.index, name="index"),
    path("baby/<int:baby_id>/", views.baby, name="baby"),
    path("training/<int:training_id>/", views.training, name="training"),
    path("rookie/<int:rookie_id>/", views.rookie, name="rookie"),
    path("champion/<int:champion_id>/", views.champion, name="champion"),
]
