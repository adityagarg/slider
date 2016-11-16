from slidingCounter import *
import time, datetime as dt

#Specify max window in second
window=3600					

#Instantiate Sliding Counter Class object
counter=Slider(window)		







def addEvents(num):
	events=[]
	for i in range(0,num):
		e=Event()
		events.append(e)
	counter.incrementEvents(events)
	return None


def createTimestamps(start, x):
	timeList=[]
	current=start
	for i in range(1,x):
		current=current+dt.timedelta(milliseconds=random.randrange(1000))
		timeList.append(current)

	print timeList














while True:
	blah=raw_input("Press Enter to register an event or x to exit. ")
	if(blah=='x'):
		print "Thanks for playing"
		break
	if(blah=='s'):
		print "Events in last second"
		print counter.numLastSecond()
		continue
	if(blah=='m'):
		print "Events in last minute"
		print counter.numLastMinute()
		continue
	if(blah=='h'):
		print "Events in last hour"
		print counter.numLastHour()
		continue
	if(blah.isdigit()):
		start=time.time()
		addEvents(int(blah))
		end=time.time()
		print "time taken - "+ str(end-start)
		print "Added " + str(blah)+" events"
		print ("list size= " + str(len(counter.vector)))
		continue
	else:
		# e=Event()
		# print ("event id= " + str(e.id))
		start=time.time()
		counter.increment()	
		end=time.time()
		print "time taken - "+ str(end-start)
		print ("list size= " + str(len(counter.vector)))
		# print(counter.vector)

	

		
