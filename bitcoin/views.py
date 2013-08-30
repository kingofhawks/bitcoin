# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db import transaction
from django.db import connection

# from bean import customer

def test(request):
    return render_to_response('bitcoin1.html', locals())

def market(request):
    return render_to_response('market.html', locals())

