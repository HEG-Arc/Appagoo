from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers import ApplicationSerializer, DownloadsSerializer, CategorySerializer

from models import Application, Downloads, Category


# ViewSets define the view behavior.
class ApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ApplicationSerializer
    paginate_by = 18

    def get_queryset(self):
        queryset = Application.objects.exclude(icon='').exclude(market_url='').exclude(icon=None).exclude(market_url=None)
        if 'price' in self.request.GET:
            price = self.request.GET['price']
            if price == '0':
                queryset = queryset.filter(price=0.0)
            elif price == '1':
                queryset = queryset.filter(price__gt=0.0)
            elif price == '2':
                queryset = queryset.filter(price__gte=0.0)
        if 'name' in self.request.GET:
            name = self.request.GET['name']
            queryset = queryset.filter(name__istartswith=name)
        if 'minRate' in self.request.GET:
            minRate = self.request.GET['minRate']
            queryset = queryset.filter(evaluation__gte=minRate)
        if 'order' in self.request.GET:
            order = self.request.GET['order']
            queryset = queryset.extra(order_by=[order])
        if 'categories' in self.request.GET:
            categories = self.request.GET['categories'].split(',')
            queryset = queryset.exclude(category_id__in=categories)
        if 'profile' in self.request.GET:
            profile = self.request.GET['profile'].split(',')
            queryset = queryset.extra(select={'score': "threat_location*"+profile[0]+"+threat_system*"+profile[1]+"+threat_profil*"+profile[2]+"+threat_social*"+profile[3]+"+threat_interests*"+profile[4]+"+threat_calendar*"+profile[5]+"+threat_media*"+profile[6]})
            queryset = queryset.order_by('score')
        return queryset


class DownloadsViewSet(viewsets.ModelViewSet):
    queryset = Downloads.objects.all()
    serializer_class = DownloadsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

'''
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
'''
