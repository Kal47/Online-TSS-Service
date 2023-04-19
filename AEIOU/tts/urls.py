from django.urls import path

from . import views

urlpatterns = [
    path('', views.DecTalkView.as_view(), name='dectalk'),
    path('tts/', views.DecTalkPostView, name='dectalk')
]
