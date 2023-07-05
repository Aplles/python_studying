from django.urls import path

from api.views.page import PageView

urlpatterns = [
    path('', PageView.as_view(),name='index'),
]
