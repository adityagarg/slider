import datetime as dt
import bisect


class Event():
	i=1
	def __init__(self):
		self.id=self.i
		self.__class__.i+=1
		
		self.time=dt.datetime.now()



class Slider():

	def __init__(self, w):
		self.window=w       #time-window in seconds
		self.vector=[] 		# dt.time_at_timestamp(0)


	def findIndex(self,window, timeNow):
		num=timeNow-dt.timedelta(seconds=window)
		i=bisect.bisect_left(self.vector, num)
		return i

	def increment(self, timeStamp=None): 	  
		if not timeStamp: 					#check for correct datatype
			timeStamp=dt.datetime.now()
		if(len(self.vector)!=0):
			i=self.findIndex(self.window, timeStamp)
			self.vector[:]=self.vector[i:]	
			self.vector.append(timeStamp)
		else:
			self.vector.append(timeStamp)

		return None


	def getStats(self, window, timeNow):
		if not timeNow: 					#check for correct datatype
			timeNow=dt.datetime.now()	
		i=self.findIndex(window, timeNow)
		return len(self.vector[i:])


	def numLastSecond(self,timeNow=None):
		win=1
		value=self.getStats(win, timeNow)
		return value

	def numLastMinute(self, timeNow=None):
		win=60
		value=self.getStats(win, timeNow)
		return value

	def numLastHour(self, timeNow=None):
		win=3600
		value=self.getStats(win, timeNow)
		return value

	def clearList(self):
		self.vector[:]=[]
