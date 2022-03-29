from django.urls import path
from aplications.home.views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='HomeListView')
]
