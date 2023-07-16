from django.urls import path

from api.views.page import (PageView, IntroductionView, BasicView,
                            ConstructorView)

urlpatterns = [
    path('', PageView.as_view(), name='index'),
    path('introduction/', IntroductionView.as_view(), name='introduction'),
    path('basics/<str:id>/', BasicView.as_view(), name='basic'),
    path('constructor/', ConstructorView.as_view(), name='constructor'),
]
