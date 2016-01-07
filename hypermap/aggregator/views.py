from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from models import Service

def index(request):
    services = Service.objects.all()
    template = loader.get_template('aggregator/index.html')
    context = RequestContext(request, {
        'services': services,
    })
    return HttpResponse(template.render(context))


def service_detail(request, service_id):
    try:
        service = Service.objects.get(pk=service_id)
    except Service.DoesNotExist:
        raise Http404
    return render(request, 'aggregator/service_detail.html', {'service': service})
