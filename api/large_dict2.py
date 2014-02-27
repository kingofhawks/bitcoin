import gc, random, time
if "xrange" not in dir(__builtins__):
    xrange = range

class DataObject(object):
    def __init__(self, time, price, amount, type):
        self.time = time
        self.price = price
        self.amount = amount
        self.type = type

def create_data(n):
    from api.models import MtgoxTrade
    result = MtgoxTrade.objects.values('time','price','amount','type')
    print result
    print len(result)
    return result

def convert1(trades):
    data = []
    for trade in trades:
                js = dict()
                js['time']= trade.time
                js['price']= trade.price
                js['amount']= trade.amount
                js['type']= trade.type
                data.append(js)
    return data

def convert2(trades):
    data = [{'time': trade.time, 'price': trade.price, 'amount': trade.amount, 'type': trade.type}
        for trade in trades]
    return data

def convert3(trades):
    ndata = len(trades)
    data = ndata*[None]
    for index in xrange(ndata):
        t = trades[index]
        js = dict()
        js['time']= t.time
        js['price']= t.price
        js['amount']= t.amount
        js['type']= t.type
        #js = {"time" : t.time, "price" : t.price, "amount" : t.amount, "type" : t.type}
    return data

def main(n=1000000):

    t0s = time.time()
    trades = create_data(n);
    t0f = time.time()
    t0 = t0f - t0s

    #gc.disable()

#    t1s = time.time()
#    jtrades1 = convert1(trades)
#    t1f = time.time()
#    t1 = t1f - t1s
#
#    t2s = time.time()
#    jtrades2 = convert2(trades)
#    t2f = time.time()
#    t2 = t2f - t2s
#
#    t3s = time.time()
#    jtrades3 = convert3(trades)
#    t3f = time.time()
#    t3 = t3f - t3s

    #gc.enable()

    print ("Times:")
    print ("  Build ............ " + str(t0))
    #print ("  For loop ......... " + str(t1))
    print ("  List Comp. ....... " + str(t2))
    #print ("  Ratio ............ " + str(t2/t1))
    print ("  For loop 2 ....... " + str(t3))
    #print ("  Ratio ............ " + str(t3/t1))

main()