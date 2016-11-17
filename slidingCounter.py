import datetime as dt   #Importing datetime module used to generate timestamps
import bisect  			#Importing bisect module to use its binary search function


class Slider():

	def __init__(self, w=3600):
		self.window=w       	# define time-window of Sliding Counter in seconds (1 Hour by default, if not specified)
		self.eventList=[] 		# initialize empty event list to store events



	
	def findIndex(self,window, timeNow):		
		"""Function to find index of first element in the eventList that is within the time-window=window from time=timeNow"""
		
		num=timeNow-dt.timedelta(seconds=window)		# calculate timestamp to search for in the eventList
		i=bisect.bisect_left(self.eventList, num)		# Using binary search to look for index of first element whose timeStamp is equal or greater than num
		return i




	def increment(self, timeStamp=None): 

		"""Function to add event to the eventList. The function looks for the events that are within the Sliding Counter Window, 
		and reassigns only those events to the updated eventList, thereby removing events that are past the sliding counter time window.
		The current event timeStamp is then appended to the end of the updated eventList.

		Note - increment takes in an optional argument= timeStamp which is the timeStamp of the event being registered.
				This is used for running tests with specific timeStamp inputs.
		"""

		if not timeStamp or not isinstance(timeStamp, dt.datetime): 
			timeStamp=dt.datetime.now()
		if(len(self.eventList)!=0):
			i=self.findIndex(self.window, timeStamp)
			self.eventList[:]=self.eventList[i:]	
			self.eventList.append(timeStamp)
		else:
			self.eventList.append(timeStamp)

		return None


	def getStats(self, window, timeNow):

		"""
		Auxillary function to fetch the number of events in the EventList that are within the time-window=window from the timeStamp=timeNow.

		"""

		if not timeNow or not isinstance(timeNow, dt.datetime): 
			timeNow=dt.datetime.now()	
		i=self.findIndex(window, timeNow)
		return len(self.eventList[i:])


	def numLastSecond(self,timeNow=None):
		"""
		Returns the number of events registered in the last second by calling the getStats function with parameter window=1s

		Takes an optional argument= timeNow which is the current timeStamp at which the function numLastSecond is called. 
		Used for running tests with specific timeStamp input.

		"""

		win=1
		value=self.getStats(win, timeNow)
		return value

	def numLastMinute(self, timeNow=None):
		"""
		Returns the number of events registered in the last minute by calling the getStats function with parameter window=60s

		Takes an optional argument= timeNow which is the current timeStamp at which the function numLastMinute is called. 
		Used for running tests with specific timeStamp input.

		"""
		win=60
		value=self.getStats(win, timeNow)
		return value

	def numLastHour(self, timeNow=None):
		"""
		Returns the number of events registered in the last hour by calling the getStats function with parameter window=3600s

		Takes an optional argument= timeNow which is the current timeStamp at which the function numLastHour is called. 
		Used for running tests with specific timeStamp input.

		"""
		win=3600
		value=self.getStats(win, timeNow)
		return value

	def clearList(self):
		"""
		Clears the eventList by setting it as an empty list. Used to reset list while running test functions.
		"""


		self.eventList[:]=[]








