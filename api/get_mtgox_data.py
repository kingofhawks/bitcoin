'''
Created on 2013-9-20

@author: Simon
'''
#!/usr/bin/env python

""" Calls the MtGox API to get historical trades and saves them in an text file. Checks that trades are 
    don't already exist in the ouput file. 

    Run with:
    python get_mtgox_data.py -s "2013-04-27 08:00:00.00" -e "2013-06-27 13:30:00.00" 

"""

import datetime, urllib2, calendar, json
import pandas as pd
import argparse
import sys

input_dateformat = "%Y-%m-%d %H:%M:%S.%f"
#outfile_name = "/db/private/bitcoin/historical_data/mtgox_trades.csv"
outfile_name = "mtgox_trades.csv"

def get_humantime(unixtime):
    """ returns a string of the unixtime in human readable format
        from a unixtime. Includes microseconds
    """
    return str(pd.datetime.utcfromtimestamp(int(unixtime)/1000000.0))

def get_unixtime(humantime, dateformat):
    """ returns a unixtime from a time in dateformat
    """
    temp = datetime.datetime.strptime(humantime, dateformat)
    # add microseconds which are dropped by timetuple
    return int(calendar.timegm(temp.timetuple()))*1000000.0+temp.microsecond


class mtgox_trade():
    # constructor with input the json format of MtGox
    #format: {"date":1365881612,"price":"105","amount":"0.15","price_int":"10500000","amount_int":"15000000","tid":"1365881612029984",
    #            "price_currency":"USD","item":"BTC","trade_type":"bid","primary":"Y","properties":"market"} 
    def __init__(self, tradedict):
        # tid is the tradeid, which is the most accurate version of the time of a trade.
        # will not use the "date" field at all
        self.timestamp = int(tradedict['tid'])
        self.time = int(tradedict['date'])
        self.price = str(tradedict['price'])
        self.amount = str(tradedict['amount'])
        # properties field sometimes contains "mixed_currency" which I dont know what it means
        if "limit" in str(tradedict['properties']):
            self.ordertype = "limit"
        elif "market" in str(tradedict['properties']):
            self.ordertype = "market"
        else:
            self.ordertype = "unkown"
        self.trade_type = str(tradedict["trade_type"])

    def trade_to_string(self):
        return get_humantime(self.timestamp)+","+self.price+","+self.amount+","+self.ordertype+","+self.trade_type
    
    def __str__ (self):
        return str(self.timestamp)+","+self.price+","+self.amount+","+self.ordertype+","+self.trade_type

def fetch_data(start):
    # cast start into int before casting into string so that it is not in scientific notation
    url = "https://data.mtgox.com/api/1/BTCUSD/trades?raw&since=" + str(int(start))
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    data = res.read()
    res.close()
    return data

def fetch_mtgox():
    main('2013-02-08 18:54:11.00','2013-09-19 13:30:00.00')
    
def main(start,end):
    start=get_unixtime(start, input_dateformat)
    end=get_unixtime(end, input_dateformat)
    if end < start:
        print "End timestamp must be later than start timestamp. Exiting"
        sys.exit()
    print "Will get trades from ", start, "to", end

    """ read the output file and adjust the start date, if it exists
    """
#    try:
#        with open(outfile_name, "r") as in_file:
#            goxdata = in_file.readlines() 
#            saved_start=get_unixtime(goxdata[0].split(",")[0], input_dateformat)
#            saved_end=get_unixtime(goxdata[len(goxdata)-1].split(",")[0], input_dateformat)
#
#            print "File found, with start date:", saved_start, "and end date", saved_end
#            if start < saved_end:
#                print "Adjusted start time from ", start, "to ", saved_end
#                start = saved_end
#    except IOError:
#        print "Output file not found. Will create a new one."

    """ get data from MtGox in chunks
    """
    try:
        currstart = start
        endreached = False
        while endreached == False:
            # populate the trades dictionary with the next batch of data
            data = fetch_data(currstart)
            print "Fetching data", currstart
            if (data == '[]'):
                print 'Empty data'
                break            
            trades = [mtgox_trade(a) for a in json.loads(data)]
            currstart = trades[-1].timestamp

            if trades[-1].timestamp > end:
                endreached = True

            # place trades into the out_file before getting the next batch from MtGox 
            # so that if the program gets interrupt you have saved the trades obtained so far
            with open(outfile_name, "a") as out_file:
                for item in trades:
                    # when you request data from a timestamp gox truncates your start time to seconds and then
                    # send you everything including the initial second. So you must filter here trades
                    # of the start_time second that are already in the database.
                    if item.timestamp > start and item.timestamp < end:
                        #out_file.write(item.trade_to_string()+"\n")
                        print item
                        from api.models import MtgoxTrade
                        mtgox = MtgoxTrade()
                        mtgox.amount = item.amount
                        mtgox.time = item.time
                        mtgox.price = item.price
                        mtgox.type = item.trade_type
                        mtgox.tid = item.timestamp
                        #print mtgox.tid
                        mtgox.save()
                        

    except urllib2.HTTPError, e:
        print "Error:", str(e.code), str(e.reason)
        return
    except urllib2.URLError, e:
        print "Error:", e
        return

if __name__ == "__main__":
    main('2011-07-18 06:55:11.00','2013-09-19 13:30:00.00')