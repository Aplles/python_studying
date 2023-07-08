from django.shortcuts import render
from django.views import View

from models_app.models import Page


class PageView(View):

    def get(self, request, *args, **kwargs):
        page = Page.objects.get(parent_page__isnull=True)
        pages = Page.objects.filter(parent_page=page)
        return render(request, 'index.html', context={
            'page': page,
            'pages': pages
        })
