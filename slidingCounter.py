import datetime as dt


class Event():
	i=1
	def __init__(self):
		self.id=self.i
		self.__class__.i+=1
		
		self.time=dt.datetime.now()



class Slider():

	def __init__(self, w, l=32):
		self.window=w       #time-window in minutes
		self.vector=[] 		# dt.time_at_timestamp(0)


	def findIndex(self,window,timeNow):
		#Implement BFS

		for i,j in enumerate(self.vector):
			diff=(timeNow-j.time).total_seconds()
			if(diff<=window):
				return i
		return len(self.vector)



	def increment(self, event):
		if(len(self.vector)!=0):
			i=self.findIndex(self.window, event.time)
			self.vector[:]=self.vector[i:]	
			self.vector.append(event)
		else:
			self.vector.append(event)

		return None


	def getStats(self, window, timeNow):


		#think about removing this function
			
		i=self.findIndex(window, timeNow)
		return len(self.vector[i:])


	def numLastSecond(self):
		timeNow=dt.datetime.now()
		win=1
		value=self.getStats(win, timeNow)
		return value

	def numLastMinute(self):
		timeNow=dt.datetime.now()
		win=60
		value=self.getStats(win, timeNow)
		return value

	def numLastHour(self):
		timeNow=dt.datetime.now()
		win=3600
		value=self.getStats(win, timeNow)
		return value
