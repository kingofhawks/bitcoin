# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db import transaction
from django.db import connection
from api.models import Alert
from django.views.decorators.csrf import csrf_exempt


def test(request):
    return render_to_response('bitcoin1.html', locals())

def market(request):
    alert = Alert.objects.distinct()
    print alert.values()[0]['high']
    
    return render(request,'market.html', {'alert':alert.values()[0]})

def bitcoin(request):
    return render_to_response('bitcoin.html', locals())

def dropdown(request):
    return render_to_response('dropdown.html', locals())

@csrf_exempt
def update_alert(request):
    print request.POST.get('high')
    print request.POST.get('low')
    alert = Alert(high = request.POST.get('high'),low = request.POST.get('low'),id = 1)
    alert.save()
    return HttpResponse("OK")

