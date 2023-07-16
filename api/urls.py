from django.urls import path

from api.views.page import (PageView, IntroductionView, BasicView,
                            ConstructorView)
from api.views.user import UserLoginView, logout_user

urlpatterns = [
    path('', PageView.as_view(), name='index'),
    path('introduction/', IntroductionView.as_view(), name='introduction'),
    path('basics/<uuid:id>/', BasicView.as_view(), name='basic'),
    path('constructor/', ConstructorView.as_view(), name='constructor'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
