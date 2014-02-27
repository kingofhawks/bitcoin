"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        import datetime
#        print(datetime.datetime.fromtimestamp(int("1294311545")).strftime('%Y-%m-%d %H:%M:%S'))
#        print(datetime.datetime.fromtimestamp(int("1294317813")).strftime('%Y-%m-%d %H:%M:%S'))
        print(datetime.datetime.fromtimestamp(int("1360378451")).strftime('%Y-%m-%d %H:%M:%S'))
        print(datetime.datetime.fromtimestamp(int("1379597358")).strftime('%Y-%m-%d %H:%M:%S'))
#        d = datetime.datetime.now()
#        import calendar
#        print calendar.timegm(d.timetuple())
#        import time
#        timestamp2 = time.mktime(d.timetuple())
#        print datetime.datetime.fromtimestamp(timestamp2)
#        self.assertEqual(1 + 1, 2)
#        print(datetime.datetime.fromtimestamp(int("1379642151")).strftime('%Y-%m-%d %H:%M:%S'))
#        print(datetime.datetime.fromtimestamp(int("1316354111")).strftime('%Y-%m-%d %H:%M:%S'))
        

#        import csv
#        print 'hha'
#        fileObject = csv.reader('mtgox_trades.csv')
#        print 'hh222a'
#        print fileObject
#        row_count = sum(1 for row in fileObject)
#        print row_count
#        import csv
#        with open('mtgox_trades.csv', 'rb') as f:
#            reader = csv.reader(f)
#            for row in reader:
#                print row
                
        import time

        ts = time.time()
        data = list()
        for i in range(1000000):
            d = {}
            d['a'] = 1
            d['b'] = 2
            d['c'] = 3
            d['d'] = 4
            d['a'] = 5
            data.append(d)
        
        print(time.time() - ts)
        #print len(list(csv.reader(open('mtgox_trades.csv')))) 
