from slidingCounter import *
import time,timeit, datetime as dt

class test():

	def __init__(self, counter):
		self.counter=counter
		

	def emptyTest(self):

		self.counter.clearList()

		print "last second events : "+str(self.counter.numLastSecond()) + " || Status - " + str(self.counter.numLastSecond()==0)
		print "last minute events : "+str(self.counter.numLastMinute()) + " || Status - " + str(self.counter.numLastMinute()==0)
		print "last hour events : "+str(self.counter.numLastHour()) + " || Status - " + str(self.counter.numLastHour()==0)	
		print "sliding counter list length : "+str(len(self.counter.vector)) + " || Status - " + str(len(self.counter.vector)==0)
		print "-------- end of test ----------\n"



		return None

	def loadTest(self, numEvents):
		self.counter.clearList()

		start=time.time()

		for i in range(numEvents):
			self.counter.increment()

		end=time.time()

		print "Time taken to add "+ str(numEvents) +" elements : " +str(end-start) +" seconds"


		print "last second events : "+str(self.counter.numLastSecond()) + "|| Running time : " + str(timeit.Timer(self.counter.numLastSecond).timeit(number=1))+" seconds"
		print "last minute events : "+str(self.counter.numLastMinute()) + "|| Running time : " + str(timeit.Timer(self.counter.numLastMinute).timeit(number=1))+" seconds"
		print "last hour events : "+str(self.counter.numLastHour()) + "|| Running time : " + str(timeit.Timer(self.counter.numLastHour).timeit(number=1))+" seconds"
		print "sliding counter list length : "+str(len(self.counter.vector))
		print "-------- end of test ----------\n"


	def correctnessTest(self):

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
		numEvents=8000          					 # Greater than 901 for the way the test is constructed above
		output=createTimestamps(startTime, numEvents)

		for i in output['timeStamps']:
			self.counter.increment(i)

		queryTime=output['last']	#Setting query time for when the num* functions are called

		print "query Time : " +str(queryTime)+"\n"
		print "last second events : "+str(self.counter.numLastSecond(queryTime)) + " || Status - " + str(self.counter.numLastSecond(queryTime)==(numEvents-900))
		print "last minute events : "+str(self.counter.numLastMinute(queryTime)) + " || Status - " + str(self.counter.numLastMinute(queryTime)==(numEvents-500))
		print "last hour events : "+str(self.counter.numLastHour(queryTime)) + " || Status - " + str(self.counter.numLastHour(queryTime)==(numEvents-100))	
		print "sliding counter list length : "+str(len(self.counter.vector)) + " || Status - " + str(len(self.counter.vector)==(numEvents-100))
		print "-------- end of test ----------\n"

		return None

	




#Specify max window in second
window=3600					

#Instantiate Sliding Counter Class object
counter=Slider(window)

#Run Tests
testObject=test(counter)

testObject.emptyTest()
testObject.correctnessTest()
testObject.loadTest(100)



