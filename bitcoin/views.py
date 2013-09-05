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

def get_alert(request):
    alert = Alert.objects.distinct()
    print alert.values()[0]['high']
    return 

def ohlc(request):    
    #load from JSON data
    print 'ohlc******************'
    period = request.GET.get('period')
    print period;
    if period is None:
        period = '1Min'
    data = [{u'price': u'129.13', u'type': u'sell', u'amount': u'40', u'time': 1378343428}, {u'price': u'129.11', u'type': u'sell', u'amount': u'9', u'time': 1378343368}, {u'price': u'129.11', u'type': u'buy', u'amount': u'7.88', u'time': 1378343347}, {u'price': u'129.11', u'type': u'sell', u'amount': u'69.22', u'time': 1378343342}, {u'price': u'129.11', u'type': u'sell', u'amount': u'18.84', u'time': 1378343340}, {u'price': u'129.11', u'type': u'sell', u'amount': u'82', u'time': 1378343293}, {u'price': u'129.13', u'type': u'buy', u'amount': u'6.38', u'time': 1378343240}, {u'price': u'129.13', u'type': u'sell', u'amount': u'8', u'time': 1378343228}, {u'price': u'130.00', u'type': u'buy', u'amount': u'8.92', u'time': 1378343211}, {u'price': u'129.15', u'type': u'buy', u'amount': u'7.08', u'time': 1378343211}, {u'price': u'129.15', u'type': u'sell', u'amount': u'9.92', u'time': 1378343210}, {u'price': u'129.15', u'type': u'buy', u'amount': u'9.92', u'time': 1378343178}, {u'price': u'129.11', u'type': u'sell', u'amount': u'4', u'time': 1378343145}, {u'price': u'129.15', u'type': u'sell', u'amount': u'38.9', u'time': 1378343132}, {u'price': u'129.10', u'type': u'sell', u'amount': u'4', u'time': 1378343107}, {u'price': u'129.11', u'type': u'sell', u'amount': u'4', u'time': 1378343045}, {u'price': u'129.02', u'type': u'sell', u'amount': u'56', u'time': 1378342988}, {u'price': u'129.10', u'type': u'sell', u'amount': u'12', u'time': 1378342988}, {u'price': u'129.30', u'type': u'sell', u'amount': u'20', u'time': 1378342988}, {u'price': u'129.10', u'type': u'sell', u'amount': u'8', u'time': 1378342986}, {u'price': u'130.00', u'type': u'buy', u'amount': u'8', u'time': 1378342967}, {u'price': u'130.00', u'type': u'sell', u'amount': u'105.84', u'time': 1378342908}, {u'price': u'130.01', u'type': u'sell', u'amount': u'81.8', u'time': 1378342908}, {u'price': u'130.05', u'type': u'sell', u'amount': u'5.14', u'time': 1378342908}, {u'price': u'130.50', u'type': u'sell', u'amount': u'7.22', u'time': 1378342908}, {u'price': u'130.05', u'type': u'sell', u'amount': u'34.86', u'time': 1378342888}, {u'price': u'130.00', u'type': u'sell', u'amount': u'112', u'time': 1378342883}, {u'price': u'130.00', u'type': u'sell', u'amount': u'60', u'time': 1378342868}, {u'price': u'130.00', u'type': u'sell', u'amount': u'80', u'time': 1378342858}, {u'price': u'130.00', u'type': u'sell', u'amount': u'40', u'time': 1378342852}, {u'price': u'130.00', u'type': u'sell', u'amount': u'8', u'time': 1378342771}, {u'price': u'130.00', u'type': u'sell', u'amount': u'28', u'time': 1378342768}, {u'price': u'130.00', u'type': u'buy', u'amount': u'3.44', u'time': 1378342762}, {u'price': u'130.00', u'type': u'buy', u'amount': u'372.78', u'time': 1378342758}, {u'price': u'130.00', u'type': u'buy', u'amount': u'40', u'time': 1378342752}, {u'price': u'130.00', u'type': u'sell', u'amount': u'577.78', u'time': 1378342748}, {u'price': u'130.00', u'type': u'sell', u'amount': u'1000', u'time': 1378342745}, {u'price': u'130.00', u'type': u'sell', u'amount': u'104', u'time': 1378342744}, {u'price': u'130.00', u'type': u'sell', u'amount': u'291', u'time': 1378342740}, {u'price': u'130.00', u'type': u'sell', u'amount': u'717.3', u'time': 1378342732}, {u'price': u'130.01', u'type': u'sell', u'amount': u'170', u'time': 1378342732}, {u'price': u'130.02', u'type': u'sell', u'amount': u'490', u'time': 1378342732}, {u'price': u'130.08', u'type': u'sell', u'amount': u'86.2', u'time': 1378342732}, {u'price': u'130.08', u'type': u'sell', u'amount': u'14', u'time': 1378342722}, {u'price': u'130.08', u'type': u'sell', u'amount': u'40', u'time': 1378342716}, {u'price': u'130.08', u'type': u'sell', u'amount': u'61.8', u'time': 1378342711}, {u'price': u'130.09', u'type': u'sell', u'amount': u'20.04', u'time': 1378342711}, {u'price': u'130.10', u'type': u'sell', u'amount': u'3.2', u'time': 1378342711}, {u'price': u'130.20', u'type': u'sell', u'amount': u'3.4', u'time': 1378342711}, {u'price': u'130.25', u'type': u'sell', u'amount': u'26', u'time': 1378342694}, {u'price': u'130.50', u'type': u'sell', u'amount': u'3.56', u'time': 1378342685}, {u'price': u'130.50', u'type': u'sell', u'amount': u'120', u'time': 1378342680}, {u'price': u'130.50', u'type': u'sell', u'amount': u'20', u'time': 1378342673}, {u'price': u'130.50', u'type': u'sell', u'amount': u'30.38', u'time': 1378342663}, {u'price': u'130.50', u'type': u'sell', u'amount': u'18.06', u'time': 1378342654}, {u'price': u'131.01', u'type': u'sell', u'amount': u'16.24', u'time': 1378342586}, {u'price': u'132.00', u'type': u'sell', u'amount': u'40', u'time': 1378342556}, {u'price': u'132.10', u'type': u'sell', u'amount': u'40', u'time': 1378342556}, {u'price': u'132.20', u'type': u'sell', u'amount': u'40', u'time': 1378342552}, {u'price': u'132.25', u'type': u'sell', u'amount': u'79.26', u'time': 1378342513}, {u'price': u'132.30', u'type': u'sell', u'amount': u'40', u'time': 1378342513}, {u'price': u'132.40', u'type': u'sell', u'amount': u'40', u'time': 1378342513}, {u'price': u'132.50', u'type': u'sell', u'amount': u'290.54', u'time': 1378342513}, {u'price': u'132.50', u'type': u'sell', u'amount': u'166.76', u'time': 1378342507}, {u'price': u'132.60', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'132.70', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'132.80', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'132.90', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'133.00', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'133.10', u'type': u'sell', u'amount': u'33.24', u'time': 1378342507}, {u'price': u'133.10', u'type': u'sell', u'amount': u'6.76', u'time': 1378342494}, {u'price': u'133.20', u'type': u'sell', u'amount': u'40', u'time': 1378342494}, {u'price': u'133.30', u'type': u'sell', u'amount': u'40', u'time': 1378342494}, {u'price': u'133.33', u'type': u'sell', u'amount': u'3.24', u'time': 1378342494}, {u'price': u'133.40', u'type': u'sell', u'amount': u'40', u'time': 1378342463}, {u'price': u'133.50', u'type': u'sell', u'amount': u'240', u'time': 1378342463}, {u'price': u'133.51', u'type': u'sell', u'amount': u'120', u'time': 1378342463}, {u'price': u'133.60', u'type': u'sell', u'amount': u'40', u'time': 1378342457}, {u'price': u'133.70', u'type': u'sell', u'amount': u'24', u'time': 1378342420}, {u'price': u'133.70', u'type': u'sell', u'amount': u'16', u'time': 1378342406}, {u'price': u'133.75', u'type': u'sell', u'amount': u'2', u'time': 1378342381}, {u'price': u'133.80', u'type': u'sell', u'amount': u'1.02', u'time': 1378342273}, {u'price': u'133.80', u'type': u'sell', u'amount': u'4', u'time': 1378342266}, {u'price': u'133.80', u'type': u'sell', u'amount': u'100', u'time': 1378342263}, {u'price': u'133.80', u'type': u'sell', u'amount': u'80', u'time': 1378342253}, {u'price': u'133.80', u'type': u'sell', u'amount': u'6.98', u'time': 1378342234}, {u'price': u'133.80', u'type': u'sell', u'amount': u'48', u'time': 1378342226}, {u'price': u'133.90', u'type': u'sell', u'amount': u'40', u'time': 1378342218}, {u'price': u'134.00', u'type': u'sell', u'amount': u'3.1', u'time': 1378342202}, {u'price': u'134.00', u'type': u'sell', u'amount': u'65', u'time': 1378342200}, {u'price': u'134.00', u'type': u'sell', u'amount': u'3.62', u'time': 1378342194}, {u'price': u'134.00', u'type': u'sell', u'amount': u'24', u'time': 1378342193}, {u'price': u'134.00', u'type': u'sell', u'amount': u'1000', u'time': 1378342192}, {u'price': u'134.00', u'type': u'sell', u'amount': u'2', u'time': 1378342189}, {u'price': u'134.00', u'type': u'sell', u'amount': u'8', u'time': 1378342189}, {u'price': u'134.00', u'type': u'sell', u'amount': u'40.48', u'time': 1378342161}, {u'price': u'134.01', u'type': u'sell', u'amount': u'2.98', u'time': 1378342156}, {u'price': u'134.01', u'type': u'sell', u'amount': u'120', u'time': 1378342151}, {u'price': u'134.10', u'type': u'buy', u'amount': u'42', u'time': 1378342126}, {u'price': u'134.10', u'type': u'sell', u'amount': u'5.58', u'time': 1378342125}]
    from api.collector import get_string_data
    import pandas as pd
    d = pd.read_json(get_string_data(data))
    print d
    d.time = pd.to_datetime(d.time, unit='s')
    d.set_index('time', inplace=True)
    print d
    volume = d['amount'].resample('H', how='ohlc') #maybe how should be "sum"?
    print volume
    price = d['price'].resample('1Min', how='ohlc')
    print price
    js = price.to_json(date_format='iso', orient='records')
    print js
    price = d['price'].resample(period, how='ohlc').reset_index()
    print price
    js = price.to_json(date_format='iso', orient='records')
    print js
    import json
    return HttpResponse(json.dumps(js), mimetype="application/json") 

