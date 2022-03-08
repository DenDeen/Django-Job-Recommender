from django import template
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
import apps.home.models as models
import json

def index(request):
    
    template = 'home/index.html'

    context = {
                'data': ""
              }
    
    return render(request, template, context)

@csrf_exempt
def data(request):
    if request.method == 'POST':
        body_unicode = request.POST.get('items', None)
        payload = json.loads(body_unicode)
        items = models.getItems(payload)

    response = {'data': items}
    
    return JsonResponse(response)

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

