#Import

from ibapi.wrapper import *
from ibapi.client import *
from ibapi.contract import *
from ibapi.order import *
from threading import Thread
import queue
import datetime
import time
import math
import json
import websocket
 
class bcolors:
    HEADER = '\033[95m' 
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#--Buy Preparation--

#Define all variables

ConstSignal = float

One = float
Two = float
Three = float
Four = float
Five = float
Six = float
Seven = float
Eight = float
Nine = float


global ConstSignal

    global One
    global Two
    global Three
    global Four
    global Five
    global Six
    global Seven
    global Eight
    global Nine

#Connect to Finnhub API

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    
    #BINANCE:BTCUSDT

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bsnco4vrh5r9m81dt2t0",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

#Connect to IBKR Gateway API

'''Here we will override the methods found inside api files'''

starttime=time.time() 



class TestWrapper(EWrapper):

     # error handling methods
    def init_error(self):
        error_queue = queue.Queue()
        self.my_errors_queue = error_queue

    def is_error(self):
        error_exist = not self.my_errors_queue.empty()
        return error_exist

    def get_error(self, timeout=6):
        if self.is_error():
            try:
                return self.my_errors_queue.get(timeout=timeout)
            except queue.Empty:
                return None
        return None

    def error(self, id, errorCode, errorString):
        ## Overrides the native method
        errormessage = "IB returns an error with %d errorcode %d that says %s" % (id, errorCode, errorString)
        #self.my_errors_queue.put(errormessage)

    # time handling methods
    def init_time(self):
        time_queue = queue.Queue()
        self.my_time_queue = time_queue
        return time_queue

    def currentTime(self, server_time):
        ## Overriden method
        self.my_time_queue.put(server_time)

    
        # Below is the TestClient/EClient Class 

'''Here we will call our own methods, not overriding the api methods'''

class TestClient(EClient):

    def __init__(self, wrapper):
    ## Set up with a wrapper inside
        EClient.__init__(self, wrapper)

    def server_clock(self):

        print("Asking server for Unix time")     

        # Creates a queue to store the time
        time_storage = self.wrapper.init_time()

        # Sets up a request for unix time from the Eclient 
        self.reqCurrentTime()
                  
        #Specifies a max wait time if there is no connection
        max_wait_time = 10

        try:
            requested_time = time_storage.get(timeout = max_wait_time)
        except queue.Empty:
            print("The queue was empty or max time reached")
            requested_time = None

        while self.wrapper.is_error():
            print("Error:")
            print(self.get_error(timeout=5))

        return requested_time

    # Below is TestApp Class

class TestApp(TestWrapper, TestClient):
    #Intializes our main classes 
    def __init__(self, ipaddress, portid, clientid):
        TestWrapper.__init__(self)
        TestClient.__init__(self, wrapper=self)

        #Connects to the server with the ipaddress, portid, and clientId specified in the program execution area
        self.connect(ipaddress, portid, clientid)

        #Initializes the threading
        thread = Thread(target = self.run)
        thread.start()
        setattr(self, "_thread", thread)

        #Starts listening for errors 
        self.init_error() 

    # Below is the program execution

if __name__ == '__main__':

    print("before start")

    # Specifies that we are on local host with port 7497 (paper trading port number)
    app = TestApp("127.0.0.1", 7497, 0)     

    # A printout to show the program began
    print("The program has begun")

    #assigning the return from our clock method to a variable 
    requested_time = app.server_clock()

    #printing the return from the server
    print("This is the current time from the server " )
    print(requested_time)

    # Optional disconnect. If keeping an open connection to the input don't disconnet
    # app.disconnect()

#Save variables(FirstSecondThird) with last-10min-data of Stock

    Nine = Eight
    Eight = Seven
    Seven = Six
    Six = Five
    Five = Four
    Four = Three
    Three = Two
    Two = One
    One = price

#Calculate all variables(FirstSecondThird) to difference(FirstSecondThirdToFirstSecondThird)

#Compare all variables(FirstSecondThirdToFirstSecondThird) with ConstSignal

#-> If FirstSecondThirdToFirstSecondThird >= ConstSignal(0,4%)

#--Buy--

#Buy Stock

#Note BoughtPrice

#--Sell Preparation--

#Calculate AfterBoughtDifference

#Consistently compare realtime price with AfterBoughtDifference

#-> If AfterBoughtDifference >= -0,1%

#--Sell--

#Sell Stock