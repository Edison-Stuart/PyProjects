# pylint: disable=import-error
# pylint: disable=unused-import

from django.urls import path
from . import views

urlpatterns = [
    path('', views.translator_view, name='translator_view')
]