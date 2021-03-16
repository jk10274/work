# Below are the import statements 

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

# Below is the TestWrapper/EWrapper class

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

# Below is the API management



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

OneZero = float
OneOne = float
OneTwo = float
OneThree = float
OneFour = float
OneFive = float
OneSix = float
OneSeven = float
OneEight = float
OneNine = float

TwoZero = float
TwoOne = float
TwoTwo = float
TwoThree = float
TwoFour = float
TwoFive = float
TwoSix = float
TwoSeven = float
TwoEight = float
TwoNine = float

ThreeZero = float
ThreeOne = float
ThreeTwo = float
ThreeThree = float
ThreeFour = float
ThreeFive = float
ThreeSix = float
ThreeSeven = float
ThreeEight = float
ThreeNine = float

FourZero = float
FourOne = float
FourTwo = float
FourThree = float
FourFour = float
FourFive = float
FourSix = float
FourSeven = float
FourEight = float
FourNine = float

FiveZero = float
FiveOne = float
FiveTwo = float
FiveThree = float
FiveFour = float
FiveFive = float
FiveSix = float
FiveSeven = float
FiveEight = float
FiveNine = float

SixZero = float
SixOne = float
SixTwo = float
SixThree = float
SixFour = float
SixFive = float
SixSix = float
SixSeven = float
SixEight = float
SixNine = float

SevenZero = float
SevenOne = float
SevenTwo = float
SevenThree = float
SevenFour = float
SevenFive = float
SevenSix = float
SevenSeven = float
SevenEight = float
SevenNine = float

EightZero = float
EightOne = float
EightTwo = float
EightThree = float
EightFour = float
EightFive = float
EightSix = float
EightSeven = float
EightEight = float
EightNine = float

NineZero = float
NineOne = float
NineTwo = float
NineThree = float
NineFour = float
NineFive = float
NineSix = float
NineSeven = float
NineEight = float
NineNine = float

OneZeroZero = float
OneZeroOne = float
OneZeroTwo = float
OneZeroThree = float
OneZeroFour = float
OneZeroFive = float
OneZeroSix = float
OneZeroSeven = float
OneZeroEight = float
OneZeroNine = float

OneOneZero = float
OneOneOne = float
OneOneTwo = float
OneOneThree = float
OneOneFour = float
OneOneFive = float
OneOneSix = float
OneOneSeven = float
OneOneEight = float
OneOneNine = float

OneTwoZero = float
OneTwoOne = float
OneTwoTwo = float
OneTwoThree = float
OneTwoFour = float
OneTwoFive = float
OneTwoSix = float
OneTwoSeven = float
OneTwoEight = float
OneTwoNine = float

OneThreeZero = float
OneThreeOne = float
OneThreeTwo = float
OneThreeThree = float
OneThreeFour = float
OneThreeFive = float
OneThreeSix = float
OneThreeSeven = float
OneThreeEight = float
OneThreeNine = float

OneFourZero = float
OneFourOne = float
OneFourTwo = float
OneFourThree = float
OneFourFour = float
OneFourFive = float
OneFourSix = float
OneFourSeven = float
OneFourEight = float
OneFourNine = float

OneFiveZero = float
OneFiveOne = float
OneFiveTwo = float
OneFiveThree = float
OneFiveFour = float
OneFiveFive = float
OneFiveSix = float
OneFiveSeven = float
OneFiveEight = float
OneFiveNine = float

OneSixZero = float
OneSixOne = float
OneSixTwo = float
OneSixThree = float
OneSixFour = float
OneSixFive = float
OneSixSix = float
OneSixSeven = float
OneSixEight = float
OneSixNine = float

OneSevenZero = float
OneSevenOne = float
OneSevenTwo = float
OneSevenThree = float
OneSevenFour = float
OneSevenFive = float
OneSevenSix = float
OneSevenSeven = float
OneSevenEight = float
OneSevenNine = float

OneEightZero = float
OneEightOne = float
OneEightTwo = float
OneEightThree = float
OneEightFour = float
OneEightFive = float
OneEightSix = float
OneEightSeven = float
OneEightEight = float
OneEightNine = float

OneNineZero = float
OneNineOne = float
OneNineTwo = float
OneNineThree = float
OneNineFour = float
OneNineFive = float
OneNineSix = float
OneNineSeven = float
OneNineEight = float
OneNineNine = float

TwoZeroZero = float
TwoZeroOne = float
TwoZeroTwo = float
TwoZeroThree = float
TwoZeroFour = float
TwoZeroFive = float
TwoZeroSix = float
TwoZeroSeven = float
TwoZeroEight = float
TwoZeroNine = float

TwoOneZero = float
TwoOneOne = float
TwoOneTwo = float
TwoOneThree = float
TwoOneFour = float
TwoOneFive = float
TwoOneSix = float
TwoOneSeven = float
TwoOneEight = float
TwoOneNine = float

TwoTwoZero = float
TwoTwoOne = float
TwoTwoTwo = float
TwoTwoThree = float
TwoTwoFour = float
TwoTwoFive = float
TwoTwoSix = float
TwoTwoSeven = float
TwoTwoEight = float
TwoTwoNine = float

TwoThreeZero = float
TwoThreeOne = float
TwoThreeTwo = float
TwoThreeThree = float
TwoThreeFour = float
TwoThreeFive = float
TwoThreeSix = float
TwoThreeSeven = float
TwoThreeEight = float
TwoThreeNine = float

TwoFourZero = float
TwoFourOne = float
TwoFourTwo = float
TwoFourThree = float
TwoFourFour = float
TwoFourFive = float
TwoFourSix = float
TwoFourSeven = float
TwoFourEight = float
TwoFourNine = float

TwoFiveZero = float
TwoFiveOne = float
TwoFiveTwo = float
TwoFiveThree = float
TwoFiveFour = float
TwoFiveFive = float
TwoFiveSix = float
TwoFiveSeven = float
TwoFiveEight = float
TwoFiveNine = float

TwoSixZero = float
TwoSixOne = float
TwoSixTwo = float
TwoSixThree = float
TwoSixFour = float
TwoSixFive = float
TwoSixSix = float
TwoSixSeven = float
TwoSixEight = float
TwoSixNine = float

TwoSevenZero = float
TwoSevenOne = float
TwoSevenTwo = float
TwoSevenThree = float
TwoSevenFour = float
TwoSevenFive = float
TwoSevenSix = float
TwoSevenSeven = float
TwoSevenEight = float
TwoSevenNine = float

TwoEightZero = float
TwoEightOne = float
TwoEightTwo = float
TwoEightThree = float
TwoEightFour = float
TwoEightFive = float
TwoEightSix = float
TwoEightSeven = float
TwoEightEight = float
TwoEightNine = float

TwoNineZero = float
TwoNineOne = float
TwoNineTwo = float
TwoNineThree = float
TwoNineFour = float
TwoNineFive = float
TwoNineSix = float
TwoNineSeven = float
TwoNineEight = float
TwoNineNine = float

ThreeZeroZero = float
ThreeZeroOne = float
ThreeZeroTwo = float
ThreeZeroThree = float
ThreeZeroFour = float
ThreeZeroFive = float
ThreeZeroSix = float
ThreeZeroSeven = float
ThreeZeroEight = float
ThreeZeroNine = float

ThreeOneZero = float
ThreeOneOne = float
ThreeOneTwo = float
ThreeOneThree = float
ThreeOneFour = float
ThreeOneFive = float
ThreeOneSix = float
ThreeOneSeven = float
ThreeOneEight = float
ThreeOneNine = float

ThreeTwoZero = float
ThreeTwoOne = float
ThreeTwoTwo = float
ThreeTwoThree = float
ThreeTwoFour = float
ThreeTwoFive = float
ThreeTwoSix = float
ThreeTwoSeven = float
ThreeTwoEight = float
ThreeTwoNine = float

ThreeThreeZero = float
ThreeThreeOne = float
ThreeThreeTwo = float
ThreeThreeThree = float
ThreeThreeFour = float
ThreeThreeFive = float
ThreeThreeSix = float
ThreeThreeSeven = float
ThreeThreeEight = float
ThreeThreeNine = float

ThreeFourZero = float
ThreeFourOne = float
ThreeFourTwo = float
ThreeFourThree = float
ThreeFourFour = float
ThreeFourFive = float
ThreeFourSix = float
ThreeFourSeven = float
ThreeFourEight = float
ThreeFourNine = float

ThreeFiveZero = float
ThreeFiveOne = float
ThreeFiveTwo = float
ThreeFiveThree = float
ThreeFiveFour = float
ThreeFiveFive = float
ThreeFiveSix = float
ThreeFiveSeven = float
ThreeFiveEight = float
ThreeFiveNine = float

ThreeSixZero = float
ThreeSixOne = float
ThreeSixTwo = float
ThreeSixThree = float
ThreeSixFour = float
ThreeSixFive = float
ThreeSixSix = float
ThreeSixSeven = float
ThreeSixEight = float
ThreeSixNine = float

ThreeSevenZero = float
ThreeSevenOne = float
ThreeSevenTwo = float
ThreeSevenThree = float
ThreeSevenFour = float
ThreeSevenFive = float
ThreeSevenSix = float
ThreeSevenSeven = float
ThreeSevenEight = float
ThreeSevenNine = float

ThreeEightZero = float
ThreeEightOne = float
ThreeEightTwo = float
ThreeEightThree = float
ThreeEightFour = float
ThreeEightFive = float
ThreeEightSix = float
ThreeEightSeven = float
ThreeEightEight = float
ThreeEightNine = float

ThreeNineZero = float
ThreeNineOne = float
ThreeNineTwo = float
ThreeNineThree = float
ThreeNineFour = float
ThreeNineFive = float
ThreeNineSix = float
ThreeNineSeven = float
ThreeNineEight = float
ThreeNineNine = float

FourZeroZero = float
FourZeroOne = float
FourZeroTwo = float
FourZeroThree = float
FourZeroFour = float
FourZeroFive = float
FourZeroSix = float
FourZeroSeven = float
FourZeroEight = float
FourZeroNine = float

FourOneZero = float
FourOneOne = float
FourOneTwo = float
FourOneThree = float
FourOneFour = float
FourOneFive = float
FourOneSix = float
FourOneSeven = float
FourOneEight = float
FourOneNine = float

FourTwoZero = float
FourTwoOne = float
FourTwoTwo = float
FourTwoThree = float
FourTwoFour = float
FourTwoFive = float
FourTwoSix = float
FourTwoSeven = float
FourTwoEight = float
FourTwoNine = float

FourThreeZero = float
FourThreeOne = float
FourThreeTwo = float
FourThreeThree = float
FourThreeFour = float
FourThreeFive = float
FourThreeSix = float
FourThreeSeven = float
FourThreeEight = float
FourThreeNine = float

FourFourZero = float
FourFourOne = float
FourFourTwo = float
FourFourThree = float
FourFourFour = float
FourFourFive = float
FourFourSix = float
FourFourSeven = float
FourFourEight = float
FourFourNine = float

FourFiveZero = float
FourFiveOne = float
FourFiveTwo = float
FourFiveThree = float
FourFiveFour = float
FourFiveFive = float
FourFiveSix = float
FourFiveSeven = float
FourFiveEight = float
FourFiveNine = float

FourSixZero = float
FourSixOne = float
FourSixTwo = float
FourSixThree = float
FourSixFour = float
FourSixFive = float
FourSixSix = float
FourSixSeven = float
FourSixEight = float
FourSixNine = float

FourSevenZero = float
FourSevenOne = float
FourSevenTwo = float
FourSevenThree = float
FourSevenFour = float
FourSevenFive = float
FourSevenSix = float
FourSevenSeven = float
FourSevenEight = float
FourSevenNine = float

FourEightZero = float
FourEightOne = float
FourEightTwo = float
FourEightThree = float
FourEightFour = float
FourEightFive = float
FourEightSix = float
FourEightSeven = float
FourEightEight = float
FourEightNine = float

FourNineZero = float
FourNineOne = float
FourNineTwo = float
FourNineThree = float
FourNineFour = float
FourNineFive = float
FourNineSix = float
FourNineSeven = float
FourNineEight = float
FourNineNine = float

FiveZeroZero = float
FiveZeroOne = float
FiveZeroTwo = float
FiveZeroThree = float
FiveZeroFour = float
FiveZeroFive = float
FiveZeroSix = float
FiveZeroSeven = float
FiveZeroEight = float
FiveZeroNine = float

FiveOneZero = float
FiveOneOne = float
FiveOneTwo = float
FiveOneThree = float
FiveOneFour = float
FiveOneFive = float
FiveOneSix = float
FiveOneSeven = float
FiveOneEight = float
FiveOneNine = float

FiveTwoZero = float
FiveTwoOne = float
FiveTwoTwo = float
FiveTwoThree = float
FiveTwoFour = float
FiveTwoFive = float
FiveTwoSix = float
FiveTwoSeven = float
FiveTwoEight = float
FiveTwoNine = float

FiveThreeZero = float
FiveThreeOne = float
FiveThreeTwo = float
FiveThreeThree = float
FiveThreeFour = float
FiveThreeFive = float
FiveThreeSix = float
FiveThreeSeven = float
FiveThreeEight = float
FiveThreeNine = float

FiveFourZero = float
FiveFourOne = float
FiveFourTwo = float
FiveFourThree = float
FiveFourFour = float
FiveFourFive = float
FiveFourSix = float
FiveFourSeven = float
FiveFourEight = float
FiveFourNine = float

FiveFiveZero = float
FiveFiveOne = float
FiveFiveTwo = float
FiveFiveThree = float
FiveFiveFour = float
FiveFiveFive = float
FiveFiveSix = float
FiveFiveSeven = float
FiveFiveEight = float
FiveFiveNine = float

FiveSixZero = float
FiveSixOne = float
FiveSixTwo = float
FiveSixThree = float
FiveSixFour = float
FiveSixFive = float
FiveSixSix = float
FiveSixSeven = float
FiveSixEight = float
FiveSixNine = float

FiveSevenZero = float
FiveSevenOne = float
FiveSevenTwo = float
FiveSevenThree = float
FiveSevenFour = float
FiveSevenFive = float
FiveSevenSix = float
FiveSevenSeven = float
FiveSevenEight = float
FiveSevenNine = float

FiveEightZero = float
FiveEightOne = float
FiveEightTwo = float
FiveEightThree = float
FiveEightFour = float
FiveEightFive = float
FiveEightSix = float
FiveEightSeven = float
FiveEightEight = float
FiveEightNine = float

FiveNineZero = float
FiveNineOne = float
FiveNineTwo = float
FiveNineThree = float
FiveNineFour = float
FiveNineFive = float
FiveNineSix = float
FiveNineSeven = float
FiveNineEight = float
FiveNineNine = float

SixZeroZero = float

OneToSixZeroZero = float

def on_message(ws, message):
    print(message)
        
    #load the json to a string
    resp = json.loads(message)

    #print the resp
    #print (resp)

    #extract an element in the response
    
    price = resp['data'][0]['p']
    
    print(price)

    
    
    time.sleep(1)
    
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

    global OneZero  
    global OneOne  
    global OneTwo  
    global OneThree  
    global OneFour  
    global OneFive
    global OneSix  
    global OneSeven  
    global OneEight  
    global OneNine  

    global TwoZero  
    global TwoOne  
    global TwoTwo  
    global TwoThree  
    global TwoFour  
    global TwoFive  
    global TwoSix  
    global TwoSeven  
    global TwoEight  
    global TwoNine  

    global ThreeZero  
    global ThreeOne  
    global ThreeTwo  
    global ThreeThree  
    global ThreeFour  
    global ThreeFive  
    global ThreeSix  
    global ThreeSeven  
    global ThreeEight  
    global ThreeNine  

    global FourZero  
    global FourOne  
    global FourTwo  
    global FourThree  
    global FourFour  
    global FourFive  
    global FourSix  
    global FourSeven  
    global FourEight  
    global FourNine  

    global FiveZero  
    global FiveOne  
    global FiveTwo  
    global FiveThree  
    global FiveFour  
    global FiveFive  
    global FiveSix  
    global FiveSeven  
    global FiveEight  
    global SixZero  
    global FiveNine  

    global SixZero  
    global SixOne  
    global SixTwo  
    global SixThree  
    global SixFour  
    global SixFive  
    global SixSix  
    global SixSeven  
    global SixEight  
    global SixNine  

    global SevenZero  
    global SevenOne  
    global SevenTwo  
    global SevenThree  
    global SevenFour  
    global SevenFive  
    global SevenSix  
    global SevenSeven  
    global SevenEight  
    global SevenNine  

    global EightZero  
    global EightOne  
    global EightTwo  
    global EightThree  
    global EightFour  
    global EightFive  
    global EightSix  
    global EightSeven  
    global EightEight  
    global EightNine  

    global NineZero  
    global NineOne  
    global NineTwo  
    global NineThree  
    global NineFour  
    global NineFive  
    global NineSix  
    global NineSeven  
    global NineEight  
    global NineNine  

    global OneZeroZero  
    global OneZeroOne  
    global OneZeroTwo  
    global OneZeroThree  
    global OneZeroFour  
    global OneZeroFive  
    global OneZeroSix  
    global OneZeroSeven  
    global OneZeroEight  
    global OneZeroNine  

    global OneOneZero  
    global OneOneOne  
    global OneOneTwo  
    global OneOneThree  
    global OneOneFour  
    global OneOneFive  
    global OneOneSix  
    global OneOneSeven  
    global OneOneEight  
    global OneOneNine  

    global OneTwoZero  
    global OneTwoOne  
    global OneTwoTwo  
    global OneTwoThree  
    global OneTwoFour  
    global OneTwoFive  
    global OneTwoSix  
    global OneTwoSeven  
    global OneTwoEight  
    global OneTwoNine  

    global OneThreeZero  
    global OneThreeOne  
    global OneThreeTwo  
    global OneThreeThree  
    global OneThreeFour  
    global OneThreeFive  
    global OneThreeSix  
    global OneThreeSeven  
    global OneThreeEight  
    global OneThreeNine  

    global OneFourZero  
    global OneFourOne  
    global OneFourTwo  
    global OneFourThree  
    global OneFourFour  
    global OneFourFive  
    global OneFourSix  
    global OneFourSeven  
    global OneFourEight  
    global OneFourNine  

    global OneFiveZero  
    global OneFiveOne  
    global OneFiveTwo  
    global OneFiveThree  
    global OneFiveFour  
    global OneFiveFive  
    global OneFiveSix  
    global OneFiveSeven  
    global OneFiveEight  
    global OneFiveNine  

    global OneSixZero  
    global OneSixOne  
    global OneSixTwo  
    global OneSixThree  
    global OneSixFour  
    global OneSixFive  
    global OneSixSix  
    global OneSixSeven  
    global OneSixEight  
    global OneSixNine  

    global OneSevenZero  
    global OneSevenOne  
    global OneSevenTwo  
    global OneSevenThree  
    global OneSevenFour  
    global OneSevenFive  
    global OneSevenSix  
    global OneSevenSeven  
    global OneSevenEight  
    global OneSevenNine  

    global OneEightZero  
    global OneEightOne  
    global OneEightTwo  
    global OneEightThree  
    global OneEightFour  
    global OneEightFive  
    global OneEightSix  
    global OneEightSeven  
    global OneEightEight  
    global OneEightNine  

    global OneNineZero  
    global OneNineOne  
    global OneNineTwo  
    global OneNineThree  
    global OneNineFour  
    global OneNineFive  
    global OneNineSix  
    global OneNineSeven  
    global OneNineEight  
    global OneNineNine  

    global TwoZeroZero  
    global TwoZeroOne  
    global TwoZeroTwo  
    global TwoZeroThree  
    global TwoZeroFour  
    global TwoZeroFive  
    global TwoZeroSix  
    global TwoZeroSeven  
    global TwoZeroEight  
    global TwoZeroNine  

    global TwoOneZero  
    global TwoOneOne  
    global TwoOneTwo  
    global TwoOneThree  
    global TwoOneFour  
    global TwoOneFive  
    global TwoOneSix  
    global TwoOneSeven  
    global TwoOneEight  
    global TwoOneNine  

    global TwoTwoZero  
    global TwoTwoOne  
    global TwoTwoTwo  
    global TwoTwoThree  
    global TwoTwoFour  
    global TwoTwoFive  
    global TwoTwoSix  
    global TwoTwoSeven  
    global TwoTwoEight  
    global TwoTwoNine  

    global TwoThreeZero  
    global TwoThreeOne  
    global TwoThreeTwo  
    global TwoThreeThree  
    global TwoThreeFour  
    global TwoThreeFive  
    global TwoThreeSix  
    global TwoThreeSeven  
    global TwoThreeEight  
    global TwoThreeNine  

    global TwoFourZero  
    global TwoFourOne  
    global TwoFourTwo  
    global TwoFourThree  
    global TwoFourFour  
    global TwoFourFive  
    global TwoFourSix  
    global TwoFourSeven  
    global TwoFourEight  
    global TwoFourNine  

    global TwoFiveZero
    global TwoFiveOne  
    global TwoFiveTwo  
    global TwoFiveThree  
    global TwoFiveFour  
    global TwoFiveFive  
    global TwoFiveSix  
    global TwoFiveSeven  
    global TwoFiveEight  
    global TwoFiveNine  

    global TwoSixZero  
    global TwoSixOne  
    global TwoSixTwo  
    global TwoSixThree  
    global TwoSixFour  
    global TwoSixFive  
    global TwoSixSix  
    global TwoSixSeven  
    global TwoSixEight  
    global TwoSixNine  

    global TwoSevenZero  
    global TwoSevenOne  
    global TwoSevenTwo  
    global TwoSevenThree  
    global TwoSevenFour  
    global TwoSevenFive  
    global TwoSevenSix  
    global TwoSevenSeven  
    global TwoSevenEight  
    global TwoSevenNine  

    global TwoEightZero  
    global TwoEightOne  
    global TwoEightTwo  
    global TwoEightThree  
    global TwoEightFour  
    global TwoEightFive  
    global TwoEightSix  
    global TwoEightSeven  
    global TwoEightEight  
    global TwoEightNine  

    global TwoNineZero  
    global TwoNineOne  
    global TwoNineTwo  
    global TwoNineThree  
    global TwoNineFour  
    global TwoNineFive  
    global TwoNineSix  
    global TwoNineSeven  
    global TwoNineEight  
    global TwoNineNine  

    global ThreeZeroZero  
    global ThreeZeroOne  
    global ThreeZeroTwo  
    global ThreeZeroThree  
    global ThreeZeroFour  
    global ThreeZeroFive  
    global ThreeZeroSix  
    global ThreeZeroSeven  
    global ThreeZeroEight  
    global ThreeZeroNine  

    global ThreeOneZero  
    global ThreeOneOne  
    global ThreeOneTwo  
    global ThreeOneThree  
    global ThreeOneFour  
    global ThreeOneFive  
    global ThreeOneSix  
    global ThreeOneSeven  
    global ThreeOneEight  
    global ThreeOneNine  

    global ThreeTwoZero  
    global ThreeTwoOne  
    global ThreeTwoTwo  
    global ThreeTwoThree  
    global ThreeTwoFour  
    global ThreeTwoFive  
    global ThreeTwoSix  
    global ThreeTwoSeven  
    global ThreeTwoEight  
    global ThreeTwoNine  

    global ThreeThreeZero  
    global ThreeThreeOne   
    global ThreeThreeTwo  
    global ThreeThreeThree  
    global ThreeThreeFour  
    global ThreeThreeFive  
    global ThreeThreeSix  
    global ThreeThreeSeven  
    global ThreeThreeEight  
    global ThreeThreeNine  

    global ThreeFourZero  
    global ThreeFourOne  
    global ThreeFourTwo  
    global ThreeFourThree  
    global ThreeFourFour  
    global ThreeFourFive  
    global ThreeFourSix  
    global ThreeFourSeven  
    global ThreeFourEight  
    global ThreeFourNine  

    global ThreeFiveZero  
    global ThreeFiveOne  
    global ThreeFiveTwo  
    global ThreeFiveThree  
    global ThreeFiveFour  
    global ThreeFiveFive  
    global ThreeFiveSix  
    global ThreeFiveSeven  
    global ThreeFiveEight  
    global ThreeFiveNine  

    global ThreeSixZero  
    global ThreeSixOne  
    global ThreeSixTwo  
    global ThreeSixThree  
    global ThreeSixFour  
    global ThreeSixFive  
    global ThreeSixSix  
    global ThreeSixSeven  
    global ThreeSixEight  
    global ThreeSixNine  

    global ThreeSevenZero  
    global ThreeSevenOne  
    global ThreeSevenTwo  
    global ThreeSevenThree  
    global ThreeSevenFour  
    global ThreeSevenFive  
    global ThreeSevenSix  
    global ThreeSevenSeven  
    global ThreeSevenEight  
    global ThreeSevenNine  

    global ThreeEightZero  
    global ThreeEightOne  
    global ThreeEightTwo  
    global ThreeEightThree  
    global ThreeEightFour  
    global ThreeEightFive  
    global ThreeEightSix  
    global ThreeEightSeven  
    global ThreeEightEight  
    global ThreeEightNine  

    global ThreeNineZero  
    global ThreeNineOne  
    global ThreeNineTwo  
    global ThreeNineThree  
    global ThreeNineFour  
    global ThreeNineFive  
    global ThreeNineSix  
    global ThreeNineSeven  
    global ThreeNineEight  
    global ThreeNineNine  

    global FourZeroZero  
    global FourZeroOne  
    global FourZeroTwo  
    global FourZeroThree  
    global FourZeroFour  
    global FourZeroFive  
    global FourZeroSix  
    global FourZeroSeven  
    global FourZeroEight  
    global FourZeroNine  

    global FourOneZero  
    global FourOneOne  
    global FourOneTwo  
    global FourOneThree  
    global FourOneFour  
    global FourOneFive  
    global FourOneSix  
    global FourOneSeven  
    global FourOneEight  
    global FourOneNine  

    global FourTwoZero  
    global FourTwoOne  
    global FourTwoTwo  
    global FourTwoThree  
    global FourTwoFour  
    global FourTwoFive  
    global FourTwoSix  
    global FourTwoSeven  
    global FourTwoEight  
    global FourTwoNine  

    global FourThreeZero  
    global FourThreeOne  
    global FourThreeTwo  
    global FourThreeThree  
    global FourThreeFour  
    global FourThreeFive  
    global FourThreeSix  
    global FourThreeSeven  
    global FourThreeEight  
    global FourThreeNine  

    global FourFourZero  
    global FourFourOne  
    global FourFourTwo  
    global FourFourThree  
    global FourFourFour  
    global FourFourFive  
    global FourFourSix  
    global FourFourSeven  
    global FourFourEight  
    global FourFourNine  

    global FourFiveZero  
    global FourFiveOne  
    global FourFiveTwo  
    global FourFiveThree  
    global FourFiveFour   
    global FourFiveFive  
    global FourFiveSix  
    global FourFiveSeven  
    global FourFiveEight  
    global FourFiveNine  

    global FourSixZero  
    global FourSixOne  
    global FourSixTwo  
    global FourSixThree  
    global FourSixFour  
    global FourSixFive  
    global FourSixSix  
    global FourSixSeven  
    global FourSixEight  
    global FourSixNine  

    global FourSevenZero  
    global FourSevenOne  
    global FourSevenTwo  
    global FourSevenThree  
    global FourSevenFour  
    global FourSevenFive  
    global FourSevenSix  
    global FourSevenSeven  
    global FourSevenEight  
    global FourSevenNine   

    global FourEightZero  
    global FourEightOne  
    global FourEightTwo  
    global FourEightThree  
    global FourEightFour  
    global FourEightFive  
    global FourEightSix  
    global FourEightSeven  
    global FourEightEight  
    global FourEightNine  

    global FourNineZero  
    global FourNineOne  
    global FourNineTwo  
    global FourNineThree  
    global FourNineFour  
    global FourNineFive  
    global FourNineSix  
    global FourNineSeven  
    global FourNineEight  
    global FourNineNine  

    global FiveZeroZero  
    global FiveZeroOne  
    global FiveZeroTwo  
    global FiveZeroThree  
    global FiveZeroFour  
    global FiveZeroFive  
    global FiveZeroSix  
    global FiveZeroSeven  
    global FiveZeroEight  
    global FiveZeroNine  

    global FiveOneZero  
    global FiveOneOne  
    global FiveOneTwo  
    global FiveOneThree  
    global FiveOneFour  
    global FiveOneFive  
    global FiveOneSix  
    global FiveOneSeven  
    global FiveOneEight  
    global FiveOneNine  

    global FiveTwoZero  
    global FiveTwoOne  
    global FiveTwoTwo  
    global FiveTwoThree  
    global FiveTwoFour  
    global FiveTwoFive  
    global FiveTwoSix  
    global FiveTwoSeven  
    global FiveTwoEight  
    global FiveTwoNine  

    global FiveThreeZero  
    global FiveThreeOne  
    global FiveThreeTwo  
    global FiveThreeThree  
    global FiveThreeFour  
    global FiveThreeFive  
    global FiveThreeSix  
    global FiveThreeSeven  
    global FiveThreeEight  
    global FiveThreeNine  

    global FiveFourZero  
    global FiveFourOne  
    global FiveFourTwo  
    global FiveFourThree  
    global FiveFourFour  
    global FiveFourFive  
    global FiveFourSix  
    global FiveFourSeven  
    global FiveFourEight  
    global FiveFourNine  

    global FiveFiveZero  
    global FiveFiveOne  
    global FiveFiveTwo  
    global FiveFiveThree  
    global FiveFiveFour  
    global FiveFiveFive  
    global FiveFiveSix  
    global FiveFiveSeven  
    global FiveFiveEight  
    global FiveFiveNine  

    global FiveSixZero  
    global FiveSixOne  
    global FiveSixTwo  
    global FiveSixThree  
    global FiveSixFour  
    global FiveSixFive  
    global FiveSixSix  
    global FiveSixSeven  
    global FiveSixEight  
    global FiveSixNine  

    global FiveSevenZero  
    global FiveSevenOne  
    global FiveSevenTwo  
    global FiveSevenThree  
    global FiveSevenFour  
    global FiveSevenFive  
    global FiveSevenSix  
    global FiveSevenSeven  
    global FiveSevenEight  
    global FiveSevenNine  

    global FiveEightZero  
    global FiveEightOne  
    global FiveEightTwo  
    global FiveEightThree  
    global FiveEightFour  
    global FiveEightFive  
    global FiveEightSix  
    global FiveEightSeven  
    global FiveEightEight  
    global FiveEightNine  

    global FiveNineZero  
    global FiveNineOne  
    global FiveNineTwo  
    global FiveNineThree  
    global FiveNineFour  
    global FiveNineFive  
    global FiveNineSix  
    global FiveNineSeven  
    global FiveNineEight  
    global FiveNineNine  

    global SixZeroZero

    SixZeroZero = FiveNineNine

    FiveNineNine = FiveNineEight
    FiveNineEight = FiveNineSeven
    FiveNineSeven = FiveNineSix
    FiveNineSix = FiveNineFive
    FiveNineFive = FiveNineFour
    FiveNineFour = FiveNineThree
    FiveNineThree = FiveNineTwo
    FiveNineTwo = FiveNineOne
    FiveNineOne = FiveNineZero
    FiveNineZero = FiveEightNine

    FiveEightNine = FiveEightEight
    FiveEightEight = FiveEightSeven
    FiveEightSeven = FiveEightSix
    FiveEightSix = FiveEightFive
    FiveEightFive = FiveEightFour
    FiveEightFour = FiveEightThree
    FiveEightThree = FiveEightTwo
    FiveEightTwo = FiveEightOne
    FiveEightOne = FiveEightZero
    FiveEightZero = FiveSevenNine

    FiveSevenNine = FiveSevenEight
    FiveSevenEight = FiveSevenSeven
    FiveSevenSeven = FiveSevenSix
    FiveSevenSix = FiveSevenFive
    FiveSevenFive = FiveSevenFour
    FiveSevenFour = FiveSevenThree
    FiveSevenThree = FiveSevenTwo
    FiveSevenTwo = FiveSevenOne
    FiveSevenOne = FiveSevenZero 
    FiveSevenZero = FiveSixNine

    FiveSixNine = FiveSixEight
    FiveSixEight = FiveSixSeven
    FiveSixSeven = FiveSixSix
    FiveSixSix = FiveSixFive
    FiveSixFive = FiveSixFour
    FiveSixFour = FiveSixThree
    FiveSixThree = FiveSixTwo
    FiveSixTwo = FiveSixOne
    FiveSixOne = FiveSixZero
    FiveSixZero = FiveFiveNine

    FiveFiveNine = FiveFiveEight
    FiveFiveEight = FiveFiveSeven
    FiveFiveSeven = FiveFiveSix
    FiveFiveSix = FiveFiveFive
    FiveFiveFive = FiveFiveFour
    FiveFiveFour = FiveFiveThree
    FiveFiveThree = FiveFiveTwo
    FiveFiveTwo = FiveFiveOne
    FiveFiveOne = FiveFiveZero
    FiveFiveZero = FiveFourNine

    FiveFourNine = FiveFourEight
    FiveFourEight = FiveFourSeven
    FiveFourSeven = FiveFourSix
    FiveFourSix = FiveFourFive
    FiveFourFive = FiveFourFour
    FiveFourFour = FiveFourThree
    FiveFourThree = FiveFourTwo
    FiveFourTwo = FiveFourOne
    FiveFourOne = FiveFourZero
    FiveFourZero = FiveThreeNine

    FiveThreeNine = FiveThreeEight
    FiveThreeEight = FiveThreeSeven
    FiveThreeSeven = FiveThreeSix
    FiveThreeSix = FiveThreeFive
    FiveThreeFive = FiveThreeFour
    FiveThreeFour = FiveThreeThree
    FiveThreeThree = FiveThreeTwo
    FiveThreeTwo = FiveThreeOne
    FiveThreeOne = FiveThreeZero
    FiveThreeZero = FiveTwoNine

    FiveTwoNine = FiveTwoEight
    FiveTwoEight = FiveTwoSeven
    FiveTwoSeven = FiveTwoSix
    FiveTwoSix = FiveTwoFive
    FiveTwoFive = FiveTwoFour
    FiveTwoFour = FiveTwoThree
    FiveTwoThree = FiveTwoTwo
    FiveTwoTwo = FiveTwoOne
    FiveTwoOne = FiveTwoZero
    FiveTwoZero = FiveOneNine

    FiveOneNine = FiveOneEight
    FiveOneEight = FiveOneSeven
    FiveOneSeven = FiveOneSix
    FiveOneSix = FiveOneFive
    FiveOneFive = FiveOneFour
    FiveOneFour = FiveOneThree
    FiveOneThree = FiveOneTwo
    FiveOneTwo = FiveOneOne
    FiveOneOne = FiveOneZero
    FiveOneZero = FiveZeroNine

    FiveZeroNine = FiveZeroEight
    FiveZeroEight = FiveZeroSeven
    FiveZeroSeven = FiveZeroSix
    FiveZeroSix = FiveZeroFive
    FiveZeroFive = FiveZeroFour
    FiveZeroFour = FiveZeroThree
    FiveZeroThree = FiveZeroTwo
    FiveZeroTwo = FiveZeroOne
    FiveZeroOne = FiveZeroZero
    FiveZeroZero = FourNineNine

    FourNineNine = FourNineEight
    FourNineEight = FourNineSeven
    FourNineSeven = FourNineSix
    FourNineSix = FourNineFive
    FourNineFive = FourNineFour
    FourNineFour = FourNineThree
    FourNineThree = FourNineTwo
    FourNineTwo = FourNineOne
    FourNineOne = FourNineZero
    FourNineZero = FourEightNine

    FourEightNine = FourEightEight
    FourEightEight = FourEightSeven
    FourEightSeven = FourEightSix
    FourEightSix = FourEightFive
    FourEightFive = FourEightFour
    FourEightFour = FourEightThree
    FourEightThree = FourEightTwo
    FourEightTwo = FourEightOne
    FourEightOne = FourEightZero
    FourEightZero = FourSevenNine

    FourSevenNine  = FourSevenEight
    FourSevenEight = FourSevenSeven
    FourSevenSeven = FourSevenSix
    FourSevenSix = FourSevenFive
    FourSevenFive = FourSevenFour
    FourSevenFour = FourSevenThree
    FourSevenThree = FourSevenTwo
    FourSevenTwo = FourSevenOne
    FourSevenOne = FourSevenZero
    FourSevenZero = FourSixNine

    FourSixNine = FourSixEight
    FourSixEight = FourSixSeven
    FourSixSeven = FourSixSix
    FourSixSix = FourSixFive
    FourSixFive = FourSixFour
    FourSixFour = FourSixThree
    FourSixThree = FourSixTwo
    FourSixTwo = FourSixOne
    FourSixOne = FourSixZero
    FourSixZero = FourFiveNine

    FourFiveNine = FourFiveEight
    FourFiveEight = FourFiveSeven
    FourFiveSeven = FourFiveSix
    FourFiveSix = FourFiveFive
    FourFiveFive = FourFiveFour
    FourFiveFour =  FourFiveThree
    FourFiveThree = FourFiveTwo
    FourFiveTwo = FourFiveOne
    FourFiveOne = FourFiveZero
    FourFiveZero = FourFourNine

    FourFourNine = FourFourEight
    FourFourEight = FourFourSeven
    FourFourSeven = FourFourSix
    FourFourSix = FourFourFive
    FourFourFive = FourFourFour
    FourFourFour = FourFourThree
    FourFourThree = FourFourTwo
    FourFourTwo = FourFourOne
    FourFourOne = FourFourZero
    FourFourZero = FourThreeNine

    FourThreeNine = FourThreeEight
    FourThreeEight = FourThreeSeven
    FourThreeSeven = FourThreeSix
    FourThreeSix = FourThreeFive
    FourThreeFive = FourThreeFour
    FourThreeFour = FourThreeThree
    FourThreeThree = FourThreeTwo
    FourThreeTwo = FourThreeOne
    FourThreeOne = FourThreeZero
    FourThreeZero = FourTwoNine

    FourTwoNine = FourTwoEight
    FourTwoEight = FourTwoSeven
    FourTwoSeven = FourTwoSix
    FourTwoSix = FourTwoFive
    FourTwoFive = FourTwoFour
    FourTwoFour = FourTwoThree
    FourTwoThree = FourTwoTwo
    FourTwoTwo = FourTwoOne
    FourTwoOne = FourTwoZero
    FourTwoZero = FourOneNine

    FourOneNine = FourOneEight
    FourOneEight = FourOneSeven
    FourOneSeven = FourOneSix
    FourOneSix = FourOneFive
    FourOneFive = FourOneFour
    FourOneFour = FourOneThree
    FourOneThree = FourOneTwo
    FourOneTwo = FourOneOne
    FourOneOne = FourOneZero
    FourOneZero = FourZeroNine

    FourZeroNine = FourZeroEight
    FourZeroEight = FourZeroSeven
    FourZeroSeven = FourZeroSix
    FourZeroSix = FourZeroFive
    FourZeroFive = FourZeroFour
    FourZeroFour = FourZeroThree
    FourZeroThree = FourZeroTwo
    FourZeroTwo = FourZeroOne
    FourZeroOne = FourZeroZero
    FourZeroZero = ThreeNineNine

    ThreeNineNine = ThreeNineEight
    ThreeNineEight = ThreeNineSeven
    ThreeNineSeven = ThreeNineSix
    ThreeNineSix = ThreeNineFive
    ThreeNineFive = ThreeNineFour
    ThreeNineFour = ThreeNineThree
    ThreeNineThree = ThreeNineTwo
    ThreeNineTwo = ThreeNineOne
    ThreeNineOne = ThreeNineZero
    ThreeNineZero = ThreeEightNine

    ThreeEightNine = ThreeEightEight
    ThreeEightEight = ThreeEightSeven
    ThreeEightSeven = ThreeEightSix
    ThreeEightSix = ThreeEightFive
    ThreeEightFive = ThreeEightFour
    ThreeEightFour = ThreeEightThree
    ThreeEightThree = ThreeEightTwo
    ThreeEightTwo = ThreeEightOne
    ThreeEightOne = ThreeEightZero
    ThreeEightZero = ThreeSevenNine

    ThreeSevenNine = ThreeSevenEight
    ThreeSevenEight = ThreeSevenSeven
    ThreeSevenSeven = ThreeSevenSix
    ThreeSevenSix = ThreeSevenFive
    ThreeSevenFive = ThreeSevenFour
    ThreeSevenFour = ThreeSevenThree
    ThreeSevenThree = ThreeSevenTwo
    ThreeSevenTwo = ThreeSevenOne
    ThreeSevenOne = ThreeSevenZero
    ThreeSevenZero = ThreeSixNine

    ThreeSixNine = ThreeSixEight
    ThreeSixEight = ThreeSixSeven
    ThreeSixSeven = ThreeSixSix
    ThreeSixSix = ThreeSixFive
    ThreeSixFive = ThreeSixFour
    ThreeSixFour = ThreeSixThree
    ThreeSixThree = ThreeSixTwo
    ThreeSixTwo = ThreeSixOne
    ThreeSixOne = ThreeSixZero
    ThreeSixZero = ThreeFiveNine

    ThreeFiveNine = ThreeFiveEight
    ThreeFiveEight = ThreeFiveSeven
    ThreeFiveSeven = ThreeFiveSix
    ThreeFiveSix = ThreeFiveFive
    ThreeFiveFive = ThreeFiveFour
    ThreeFiveFour = ThreeFiveThree
    ThreeFiveThree = ThreeFiveTwo
    ThreeFiveTwo = ThreeFiveOne
    ThreeFiveOne = ThreeFiveZero
    ThreeFiveZero = ThreeFourNine

    ThreeFourNine = ThreeFourEight
    ThreeFourEight = ThreeFourSeven
    ThreeFourSeven = ThreeFourSix
    ThreeFourSix = ThreeFourFive
    ThreeFourFive = ThreeFourFour
    ThreeFourFour = ThreeFourThree
    ThreeFourThree = ThreeFourTwo
    ThreeFourTwo = ThreeFourOne
    ThreeFourOne = ThreeFourZero
    ThreeFourZero = ThreeThreeNine

    ThreeThreeNine = ThreeThreeEight
    ThreeThreeEight = ThreeThreeSeven
    ThreeThreeSeven = ThreeThreeSix
    ThreeThreeSix = ThreeThreeFive
    ThreeThreeFive = ThreeThreeFour
    ThreeThreeFour = ThreeThreeThree
    ThreeThreeThree = ThreeThreeTwo
    ThreeThreeTwo = ThreeThreeOne
    ThreeThreeOne = ThreeThreeZero
    ThreeThreeZero = ThreeTwoNine

    ThreeTwoNine = ThreeTwoEight
    ThreeTwoEight = ThreeTwoSeven
    ThreeTwoSeven = ThreeTwoSix
    ThreeTwoSix = ThreeTwoFive
    ThreeTwoFive = ThreeTwoFour
    ThreeTwoFour = ThreeTwoThree
    ThreeTwoThree = ThreeTwoTwo
    ThreeTwoTwo = ThreeTwoOne
    ThreeTwoOne = ThreeTwoZero
    ThreeTwoZero = ThreeOneNine

    ThreeOneNine = ThreeOneEight
    ThreeOneEight = ThreeOneSeven
    ThreeOneSeven = ThreeOneSix
    ThreeOneSix = ThreeOneFive
    ThreeOneFive = ThreeOneFour
    ThreeOneFour = ThreeOneThree
    ThreeOneThree = ThreeOneTwo
    ThreeOneTwo = ThreeOneOne
    ThreeOneOne = ThreeOneZero
    ThreeOneZero = ThreeZeroNine

    ThreeZeroNine = ThreeZeroEight
    ThreeZeroEight = ThreeZeroSeven
    ThreeZeroSeven = ThreeZeroSix
    ThreeZeroSix = ThreeZeroFive
    ThreeZeroFive = ThreeZeroFour
    ThreeZeroFour = ThreeZeroThree
    ThreeZeroThree = ThreeZeroTwo
    ThreeZeroTwo = ThreeZeroOne
    ThreeZeroOne = ThreeZeroZero
    ThreeZeroZero = TwoNineNine

    TwoNineNine = TwoNineEight
    TwoNineEight = TwoNineSeven
    TwoNineSeven = TwoNineSix
    TwoNineSix = TwoNineFive
    TwoNineFive = TwoNineFour
    TwoNineFour = TwoNineThree
    TwoNineThree = TwoNineTwo
    TwoNineTwo = TwoNineOne
    TwoNineOne = TwoNineZero
    TwoNineZero = TwoEightNine

    TwoEightNine = TwoEightEight
    TwoEightEight = TwoEightSeven
    TwoEightSeven = TwoEightSix
    TwoEightSix = TwoEightFive
    TwoEightFive = TwoEightFour
    TwoEightFour = TwoEightThree
    TwoEightThree = TwoEightTwo
    TwoEightTwo = TwoEightOne
    TwoEightOne = TwoEightZero
    TwoEightZero = TwoSevenNine

    TwoSevenNine = TwoSevenEight
    TwoSevenEight = TwoSevenSeven
    TwoSevenSeven = TwoSevenSix
    TwoSevenSix = TwoSevenFive
    TwoSevenFive = TwoSevenFour
    TwoSevenFour = TwoSevenThree
    TwoSevenThree = TwoSevenTwo
    TwoSevenTwo = TwoSevenOne
    TwoSevenOne = TwoSevenZero
    TwoSevenZero = TwoSixNine

    TwoSixNine = TwoSixEight
    TwoSixEight = TwoSixSeven
    TwoSixSeven = TwoSixSix
    TwoSixSix = TwoSixFive
    TwoSixFive = TwoSixFour
    TwoSixFour = TwoSixThree
    TwoSixThree = TwoSixTwo
    TwoSixTwo = TwoSixOne
    TwoSixOne = TwoSixZero
    TwoSixZero = TwoFiveNine

    TwoFiveNine = TwoFiveEight
    TwoFiveEight = TwoFiveSeven
    TwoFiveSeven = TwoFiveSix
    TwoFiveSix = TwoFiveFive
    TwoFiveFive = TwoFiveFour
    TwoFiveFour = TwoFiveThree
    TwoFiveThree = TwoFiveTwo
    TwoFiveTwo = TwoFiveOne
    TwoFiveOne = TwoFiveZero
    TwoFiveZero = TwoFourNine

    TwoFourNine = TwoFourEight
    TwoFourEight = TwoFourSeven
    TwoFourSeven = TwoFourSix
    TwoFourSix = TwoFourFive
    TwoFourFive = TwoFourFour
    TwoFourFour = TwoFourThree
    TwoFourThree = TwoFourTwo
    TwoFourTwo = TwoFourOne
    TwoFourOne = TwoFourZero
    TwoFourZero = TwoThreeNine

    TwoThreeNine = TwoThreeEight
    TwoThreeEight = TwoThreeSeven
    TwoThreeSeven = TwoThreeSix
    TwoThreeSix = TwoThreeFive
    TwoThreeFive = TwoThreeFour
    TwoThreeFour = TwoThreeThree
    TwoThreeThree = TwoThreeTwo
    TwoThreeTwo = TwoThreeOne
    TwoThreeOne = TwoThreeZero
    TwoThreeZero = TwoTwoNine

    TwoTwoNine = TwoTwoEight
    TwoTwoEight = TwoTwoSeven
    TwoTwoSeven = TwoTwoSix
    TwoTwoSix = TwoTwoFive
    TwoTwoFive = TwoTwoFour
    TwoTwoFour = TwoTwoThree
    TwoTwoThree = TwoTwoTwo
    TwoTwoTwo = TwoTwoOne
    TwoTwoOne = TwoTwoZero
    TwoTwoZero = TwoOneNine

    TwoOneNine = TwoOneEight
    TwoOneEight = TwoOneSeven
    TwoOneSeven = TwoOneSix
    TwoOneSix = TwoOneFive
    TwoOneFive = TwoOneFour
    TwoOneFour = TwoOneThree
    TwoOneThree = TwoOneTwo
    TwoOneTwo = TwoOneOne
    TwoOneOne = TwoOneZero
    TwoOneZero = TwoZeroNine

    TwoZeroNine = TwoZeroEight
    TwoZeroEight = TwoZeroSeven
    TwoZeroSeven = TwoZeroSix
    TwoZeroSix = TwoZeroFive
    TwoZeroFive = TwoZeroFour
    TwoZeroFour = TwoZeroThree
    TwoZeroThree = TwoZeroTwo
    TwoZeroTwo = TwoZeroOne
    TwoZeroOne = TwoZeroZero
    TwoZeroZero = OneNineNine

    OneNineNine = OneNineEight
    OneNineEight = OneNineSeven
    OneNineSeven = OneNineSix
    OneNineSix = OneNineFive
    OneNineFive = OneNineFour
    OneNineFour = OneNineThree
    OneNineThree = OneNineTwo
    OneNineTwo = OneNineOne
    OneNineOne = OneNineZero
    OneNineZero = OneEightNine

    OneEightNine = OneEightEight
    OneEightEight = OneEightSeven
    OneEightSeven = OneEightSix
    OneEightSix = OneEightFive
    OneEightFive = OneEightFour
    OneEightFour = OneEightThree
    OneEightThree = OneEightTwo
    OneEightTwo = OneEightOne
    OneEightOne = OneEightZero
    OneEightZero = OneSevenNine

    OneSevenNine = OneSevenEight
    OneSevenEight = OneSevenSeven
    OneSevenSeven = OneSevenSix
    OneSevenSix = OneSevenFive
    OneSevenFive = OneSevenFour
    OneSevenFour = OneSevenThree
    OneSevenThree = OneSevenTwo
    OneSevenTwo = OneSevenOne
    OneSevenOne = OneSevenZero
    OneSevenZero = OneSixNine

    OneSixNine = OneSixEight
    OneSixEight = OneSixSeven
    OneSixSeven = OneSixSix
    OneSixSix = OneSixFive
    OneSixFive = OneSixFour
    OneSixFour = OneSixThree
    OneSixThree = OneSixTwo
    OneSixTwo = OneSixOne
    OneSixOne = OneSixZero
    OneSixZero = OneFiveNine

    OneFiveNine = OneFiveEight
    OneFiveEight = OneFiveSeven
    OneFiveSeven = OneFiveSix
    OneFiveSix = OneFiveFive
    OneFiveFive = OneFiveFour
    OneFiveFour = OneFiveThree
    OneFiveThree = OneFiveTwo
    OneFiveTwo = OneFiveOne
    OneFiveOne = OneFourNine
    OneFourNine = OneFourNine

    OneFourNine = OneFourEight
    OneFourEight = OneFourSeven
    OneFourSeven = OneFourSix
    OneFourSix = OneFourFive
    OneFourFive = OneFourFour
    OneFourFour = OneFourThree
    OneFourThree = OneFourTwo
    OneFourTwo = OneFourOne
    OneFourOne = OneFourZero
    OneFourZero = OneThreeNine

    OneThreeNine = OneThreeEight
    OneThreeEight = OneThreeSeven
    OneThreeSeven = OneThreeSix
    OneThreeSix = OneThreeFive
    OneThreeFive = OneThreeFour
    OneThreeFour = OneThreeThree
    OneThreeThree = OneThreeTwo
    OneThreeTwo = OneThreeOne
    OneThreeOne = OneThreeZero
    OneThreeZero = OneTwoNine

    OneTwoNine = OneTwoEight
    OneTwoEight = OneTwoSeven
    OneTwoSeven = OneTwoSix
    OneTwoSix = OneTwoFive
    OneTwoFive = OneTwoFour
    OneTwoFour = OneTwoThree
    OneTwoThree = OneTwoTwo
    OneTwoTwo = OneTwoOne
    OneTwoOne = OneTwoZero
    OneTwoZero = OneOneNine

    OneOneNine = OneOneEight
    OneOneEight = OneOneSeven
    OneOneSeven = OneOneSix
    OneOneSix = OneOneFive
    OneOneFive = OneOneFour
    OneOneFour = OneOneThree
    OneOneThree = OneOneTwo
    OneOneTwo = OneOneOne
    OneOneOne = OneOneZero
    OneOneZero = OneZeroNine

    OneZeroNine = OneZeroEight
    OneZeroEight = OneZeroSeven
    OneZeroSeven = OneZeroSix
    OneZeroSix = OneZeroFive
    OneZeroFive = OneZeroFour
    OneZeroFour = OneZeroThree
    OneZeroThree = OneZeroTwo
    OneZeroTwo = OneZeroOne
    OneZeroOne = OneZeroZero
    OneZeroZero = NineNine

    NineNine = NineEight
    NineEight = NineSeven
    NineSeven = NineSix
    NineSix = NineFive
    NineFive = NineFour
    NineFour = NineThree
    NineThree = NineTwo
    NineTwo = NineOne
    NineOne = NineZero
    NineZero = EightNine

    EightNine = EightEight
    EightEight = EightSeven
    EightSeven = EightSix
    EightSix = EightFive
    EightFive = EightFour
    EightFour = EightThree
    EightThree = EightTwo
    EightTwo = EightOne
    EightOne = EightZero
    EightZero = SevenNine

    SevenNine = SevenEight
    SevenEight = SevenSeven
    SevenSeven = SevenSix
    SevenSix = SevenFive
    SevenFive = SevenFour
    SevenFour = SevenThree
    SevenThree = SevenTwo
    SevenTwo = SevenOne
    SevenOne = SevenZero
    SevenZero = SixNine

    SixNine = SixEight
    SixEight = SixSeven
    SixSeven = SixSix
    SixSix = SixFive
    SixFive = SixFour
    SixFour = SixThree
    SixThree = SixTwo
    SixTwo = SixOne
    SixOne = SixZero
    SixZero = FiveNine

    FiveNine = FiveEight
    FiveEight = FiveSeven
    FiveSeven = FiveSix
    FiveSix = FiveFive
    FiveFive = FiveFour
    FiveFour = FiveThree
    FiveThree = FiveTwo
    FiveTwo = FiveOne
    FiveOne = FiveZero
    FiveZero = FourNine

    FourNine = FourEight
    FourEight = FourSeven
    FourSeven = FourSix
    FourSix = FourFive
    FourFive = FourFour
    FourFour = FourThree
    FourThree = FourTwo
    FourTwo = FourOne
    FourOne = FourZero
    FourZero = ThreeNine

    ThreeNine = ThreeEight
    ThreeEight = ThreeSeven
    ThreeSeven =ThreeSix
    ThreeSix = ThreeFive
    ThreeFive = ThreeFour
    ThreeFour = ThreeThree
    ThreeThree = ThreeTwo
    ThreeTwo = ThreeOne
    ThreeOne = ThreeZero
    ThreeZero = TwoNine

    TwoNine = TwoEight
    TwoEight = TwoSeven
    TwoSeven = TwoSix
    TwoSix = TwoFive
    TwoFive = TwoFour
    TwoFour = TwoThree
    TwoThree = TwoTwo
    TwoTwo = TwoOne
    TwoOne = TwoZero
    TwoZero = OneNine

    OneNine = OneEight
    OneEight = OneSeven
    OneSeven = OneSix
    OneSix = OneFive
    OneFive = OneFour
    OneFour = OneThree
    OneThree = OneTwo
    OneTwo = OneOne
    OneOne = OneZero
    OneZero = Nine

    Nine = Eight
    Eight = Seven
    Seven = Six
    Six = Five
    Five = Four
    Four = Three
    Three = Two
    Two = One
    One = price

    print("Six:")
    print(SixZeroZero)
    print("Five:")
    print(FiveZeroZero)
    print("Four:")
    print(FourZeroZero)
    print("Three:")
    print(ThreeZeroZero)
    print("Two:")
    print(TwoZeroZero)
    print("One:")
    print(OneZeroZero)
    print("half:")
    print(FiveZero)
    print("Real:")
    print(price)
    #print(Five)
    #print(Four)
    #print(Three)
    #print(Two)
    #print(One)
    #print("Test Test")
    

 
    OneToSixZeroZero = ((One-Three)/Three)*100
    print(OneToSixZeroZero)

    

    if OneToSixZeroZero > ConstSignal:

        print(f"{bcolors.WARNING}Buy{bcolors.ENDC}")


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

# Below are the custom classes and methods 

def contractCreate():
    # Fills out the contract object
    contract1 = Contract()  # Creates a contract object from the import
    contract1.symbol = "AAPL"   # Sets the ticker symbol 
    contract1.secType = "STK"   # Defines the security type as stock
    contract1.currency = "USD"  # Currency is US dollars 
    # In the API side, NASDAQ is always defined as ISLAND in the exchange field
    contract1.exchange = "SMART"
    # contract1.PrimaryExch = "NYSE"
    return contract1    # Returns the contract object

def orderCreate():
    # Fills out the order object 
    order1 = Order()    # Creates an order object from the import
    order1.action = "BUY"   # Sets the order action to buy
    order1.orderType = "MKT"    # Sets order type to market buy
    order1.transmit = True
    order1.totalQuantity = 10   # Setting a static quantity of 10 
    return order1   # Returns the order object 

def orderExecution():
    print("Called: negative")
    #Places the order with the returned contract and order objects 
    contractObject = contractCreate()
    orderObject = orderCreate()
    nextID = 100
    app.placeOrder(nextID, contractObject, orderObject)
    print("order was placed")

"""<summary>
#/ A Market order is an order to buy or sell at the market bid or offer price. A market order may increase the likelihood of a fill 
#/ and the speed of execution, but unlike the Limit order a Market order provides no price protection and may fill at a price far 
#/ lower/higher than the current displayed bid/ask.
#/ Products: BOND, CFD, EFP, CASH, FUND, FUT, FOP, OPT, STK, WAR
</summary>"""

#Algorithm



# Calls the order execution function at the end of the program

time.sleep(3)   # Wait three seconds
orderExecution()

@staticmethod



def MarketOrder(action:str, quantity:float):
    
    
    #! [market]
    order = Order()
    order.action = action
    order.orderType = "MKT"
    order.totalQuantity = quantity
    #! [market]
    return order

