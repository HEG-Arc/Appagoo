from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Application


def index(request):
    apps_list = Application.objects.all()
    paginator = Paginator(apps_list, 9)

    page = request.GET.get('page')

    try:
        applications = paginator.page(page)
    except PageNotAnInteger:
        applications = paginator.page(1)
    except EmptyPage:
        applications = paginator.page(paginator.num_pages)

    template = loader.get_template('apps/index.html')
    context = RequestContext(request, {
        'applications': applications,
    })
    return HttpResponse(template.render(context))

