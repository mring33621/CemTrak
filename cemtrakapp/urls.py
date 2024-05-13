from django.urls import path

from cemtrakapp.datadump_views import organizations_datadump, emitters_datadump
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('organizations/datadump', organizations_datadump, name='organizations_datadump'),
    path('emitters/datadump', emitters_datadump, name='emitters_datadump'),
]
