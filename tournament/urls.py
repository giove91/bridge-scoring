from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
