from django.conf.urls import url
from .views import home_view
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^items/$', home_view, name='item_viewer'),
]
