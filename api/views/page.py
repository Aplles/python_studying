from django.shortcuts import render
from django.views import View

from models_app.models import Page


class PageView(View):

    def get(self, request, *args, **kwargs):
        pages = Page.objects.filter(parent_page__isnull=True)
        return render(request, 'main_page.html', context={
            'pages': pages
        })
