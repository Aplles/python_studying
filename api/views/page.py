from django.shortcuts import render
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.page.get import GetPageService
from models_app.models import Page


class PageView(View):

    def get(self, request, *args, **kwargs):
        page = Page.objects.get(parent_page__isnull=True)
        pages = Page.objects.filter(parent_page=page)
        return render(request, 'index.html', context={
            'page': page,
            'pages': pages
        })


class IntroductionView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'introduction.html')


class BasicView(View):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(GetPageService,
                                 kwargs | {'user': request.user})
        return render(request, 'basics.html', context={
            'page': outcome.result['page'],
            'themes': outcome.result['themes'],
        })


class ConstructorView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'constructor.html')
