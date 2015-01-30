from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from serializers import ApplicationSerializer, DownloadsSerializer, CategorySerializer

from models import Application, Downloads, Category


# ViewSets define the view behavior.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.exclude(icon='').exclude(market_url='').exclude(icon=None).exclude(market_url=None)
    serializer_class = ApplicationSerializer


class DownloadsViewSet(viewsets.ModelViewSet):
    queryset = Downloads.objects.all()
    serializer_class = DownloadsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def store(request):
    apps_list = Application.objects.all()

    paginator = Paginator(apps_list, 9)
    page = request.GET.get('page')

    try:
        applications = paginator.page(page)
    except PageNotAnInteger:
        applications = paginator.page(1)
    except EmptyPage:
        applications = paginator.page(paginator.num_pages)

    args = {}
    args.update(csrf(request))
    args['applications'] = applications

    return render_to_response('store.html', args)


def search(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
        filter = request.POST['filter']
        ascdesc = request.POST['ascdesc']
        price = request.POST['price']
        min_evaluation = request.POST['min_evaluation']
    else:
        search_text = ''

    if ascdesc == 'asc':
        apps_list = Application.objects.filter(name__icontains=search_text).filter(evaluation__range=(min_evaluation, 5)).order_by(filter)
    elif ascdesc == 'desc':
        apps_list = Application.objects.filter(name__icontains=search_text).filter(evaluation__range=(min_evaluation, 5)).order_by('-'+filter)
    else:
        apps_list = Application.objects.filter(name__icontains=search_text).filter(evaluation__range=(min_evaluation, 5)).order_by('package')

    paginator = Paginator(apps_list, 9)
    page = request.GET.get('page')

    try:
        applications = paginator.page(page)
    except PageNotAnInteger:
        applications = paginator.page(1)
    except EmptyPage:
        applications = paginator.page(paginator.num_pages)

    args = {}
    args.update(csrf(request))
    args['applications'] = applications

    return render_to_response('apps/ajax_search.html', args)

