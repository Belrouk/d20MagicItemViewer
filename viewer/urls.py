from django.conf.urls import url
from .views import home_view, create_item_view
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^items/$', home_view, name='item_viewer'),
    url(r'^create/$', create_item_view, name='create_item'),
]
