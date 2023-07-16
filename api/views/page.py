from django.shortcuts import render, redirect
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.page.fill import FillPageService
from api.services.page.get import GetPageService
from api.services.page.get_theme import GetThemeService
from models_app.models import Page, Access


class PageView(View):

    def get(self, request, *args, **kwargs):
        page = Page.objects.get(parent_page__isnull=True)
        pages = Page.objects.filter(parent_page=page)
        return render(request, 'index.html', context={
            'page': page,
            'pages': pages
        })


class IntroductionView(View):
    def dispatch(self, request, *args, **kwargs):
        post = Access.objects.filter(user=request.user, page__id=kwargs['id'])
        if not post.exists():
            return redirect('index')
        return super().dispatch(request, **kwargs)

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(GetThemeService, kwargs)
        return render(request, 'introduction.html', context={
            'theme': outcome.result,
            'blocks': outcome.result.blocks.all().order_by('position')
        })


class BasicView(View):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(GetPageService,
                                 kwargs | {'user_pk': request.user.pk})
        return render(request, 'basics.html', context={
            'page': outcome.result['page'],
            'themes': outcome.result['themes'],
        })


class ConstructorView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'constructor.html', context={
            "pages": Page.objects.all()
        })

    def post(self, request, *args, **kwargs):
        ServiceOutcome(FillPageService, request.GET, request.FILES)
        return redirect("constructor")


class SearchPageView(View):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(GetPageService, kwargs | {'user_pk': request.user.pk} | request.GET.dict())
        return render(request, 'basics.html', context={
            'page': outcome.result['page'],
            'themes': outcome.result['themes'],
        })
