from django.urls import path

from . import views

urlpatterns = [
    path('', views.connect_check, name='connection_check'),
    path('create_strategist', views.create_strategist, name='create'),
    path('fetch_strategist_in_session', views.fetch_strategist_in_session, name='fetch')
]
