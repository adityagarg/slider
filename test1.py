from slidingCounter import *				#Imports the Sliding Window Counter Class
import time,timeit, datetime as dt          #Using time functions to find running time and datetime to generate timestamps

class test():

	"""
	Class test that has 3 methods/tests - emptyTest, loadTest and correctnessTest

	"""

	def __init__(self, counter):
		"""
		A new instance of class test takes the sliding window counter as argument

		"""


		self.counter=counter
		

	def emptyTest(self):
		"""
		Empty test is used to check how if the program behaves correctly when there have been no inputs or events registered in the counter.
		It fetches the events that have occurred in the last second, minute and hour and should ideally return 0 for each of them without generating any errors.

		It also checks the current size of the eventList in the sliding window counter, which again should be 0 in this case.

		"""

		self.counter.clearList()	#This method is called to reset the sliding window counter in case it has been used for different tests before. It 									clears the eventList of any existing events

		print "last second events : "+str(self.counter.numLastSecond()) + " || Status - " + str(self.counter.numLastSecond()==0)
		print "last minute events : "+str(self.counter.numLastMinute()) + " || Status - " + str(self.counter.numLastMinute()==0)
		print "last hour events : "+str(self.counter.numLastHour()) + " || Status - " + str(self.counter.numLastHour()==0)	
		print "sliding counter list length : "+str(len(self.counter.eventList)) + " || Status - " + str(len(self.counter.eventList)==0)
		print "-------- end of test ----------\n"



		return None

	def loadTest(self, numEvents):
		"""
		Load test is used to check the running time of each function.

		It takes input as numEvents, which is the number of events that are to be registered in the sliding window counter. The increment function is then called numEvents times to register the events. The time taken to add these events is then displayed.

		After calling the increment function, the numLastSecond, numLastMinute and numLastHour functions are called and their corresponding values and running times are displayed.

		The length of the eventList in the sliding window counter after all these functions is also displayed.  

		"""


		self.counter.clearList()

		start=time.time()

		for i in range(numEvents):
			self.counter.increment()

		end=time.time()

		print "Time taken to add "+ str(numEvents) +" elements : " +str(end-start) +" seconds"


		print "last second events : "+str(self.counter.numLastSecond()) + "|| Running time : " + str(timeit.Timer(self.counter.numLastSecond).timeit(number=1))+" seconds"
		print "last minute events : "+str(self.counter.numLastMinute()) + "|| Running time : " + str(timeit.Timer(self.counter.numLastMinute).timeit(number=1))+" seconds"
		print "last hour events : "+str(self.counter.numLastHour()) + "|| Running time : " + str(timeit.Timer(self.counter.numLastHour).timeit(number=1))+" seconds"
		print "sliding counter list length : "+str(len(self.counter.eventList))
		print "-------- end of test ----------\n"


	def correctnessTest(self):
		
		"""
		The correctness Test is writted to check the correctness of the Sliding Window Counter solution. It gives pre-defined inputs to the counter functions and compares their output to the expected value.

		numEvents(=1000) events are generated with unique timestamps, differing from each other by 1 microsecond. These events are created relative to a a random startTime( dateTime object).

		The function createTimestamps returns the list of events (i.e.timestamps) and the timestamp of the last registered event.
		After the first 100 events, the current timestamp is incremented by 1 hour. Therefore, the past 100 events are not expected to show up in the sliding window counter of 3600 seconds and should not idealy be counted while fetching last 1 hour events.
		After first 500 events, the current timestamp is incremented by 1 minute. Therefore, the past 500 events are not expected to show up while fetching last 1 minute events.
		After first 900 events, the current timestamp is incremented by 1 second. Therefore, the past 900 events are not expected to show up while fetching last 1 second events.

		All events(timestamps) within the list of events reated is then passed to the increment function to register events  in the counter.

		The numLastSecond, numLastMinute and numLastHour functions are then called with timeStamp= timeStamp of the last registered event.

		The outputs of each function are then compared against the expected value. If they are equal, Status is displayed as True.


		"""

		def createTimestamps(start, numEvents):
			print "first event time : "+str(start)
			timeList=[]
			current=start

			for i in range(1,numEvents+1):
				current=current+dt.timedelta(microseconds=1)
				if(i==101):
					current=current+dt.timedelta(hours=1,microseconds=1)
				if(i==501):
					current=current+dt.timedelta(minutes=1,microseconds=1)
				if(i==901):
					current=current+dt.timedelta(seconds=1,microseconds=1)
				timeList.append(current)
			return {'timeStamps':timeList, 'last':current}



		self.counter.clearList()

		startTime=dt.datetime(2016,11,16,5,45,10) 	 # Assign random timeStamp for testing
		numEvents=1000          					 # Greater than 901 for the way the test is constructed above
		output=createTimestamps(startTime, numEvents)

		for i in output['timeStamps']:
			self.counter.increment(i)

		queryTime=output['last']	#Setting query time for when the num* functions are called

		print "query Time : " +str(queryTime)+"\n"
		print "last second events : "+str(self.counter.numLastSecond(queryTime)) + " || Status - " + str(self.counter.numLastSecond(queryTime)==(numEvents-900))
		print "last minute events : "+str(self.counter.numLastMinute(queryTime)) + " || Status - " + str(self.counter.numLastMinute(queryTime)==(numEvents-500))
		print "last hour events : "+str(self.counter.numLastHour(queryTime)) + " || Status - " + str(self.counter.numLastHour(queryTime)==(numEvents-100))	
		print "sliding counter list length : "+str(len(self.counter.eventList)) + " || Status - " + str(len(self.counter.eventList)==(numEvents-100))
		print "-------- end of test ----------\n"

		return None

	




#specify maximum time window of Sliding Window Counter 
window=3600

#Instantiate Sliding Window Counter Class object
counter=Slider(window)


testObject=test(counter) #Create the test object and pass the counter that is to be tested as argument
#Run Tests
testObject.emptyTest()
testObject.loadTest(100)
testObject.correctnessTest()




