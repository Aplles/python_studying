from django.urls import path

from api.views.page import (
    PageView,
    IntroductionView,
    BasicView,
    ConstructorView,
    SearchPageView,
    SearchPageThemeView
)
from api.views.user import UserLoginView, logout_user, UserRenderCreateView

urlpatterns = [
    path('', PageView.as_view(), name='index'),
    path('introductions/<uuid:id>/', IntroductionView.as_view(),
         name='introduction'),
    path('basics/<uuid:id>/', BasicView.as_view(), name='basic'),
    path('basics/<uuid:id>/search/', SearchPageView.as_view(), name='search'),
    path('basics/<uuid:id>/theme_search/', SearchPageThemeView.as_view(), name='theme_search'),
    path('constructor/', ConstructorView.as_view(), name='constructor'),
    path('user/', UserRenderCreateView.as_view(), name='user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
