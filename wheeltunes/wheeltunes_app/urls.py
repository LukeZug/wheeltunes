from wheeltunes_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('sliders/', views.sliders, name='sliders'),
]