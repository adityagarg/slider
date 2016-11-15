from slidingCounter import *
import time

#Specify max window in seconds
window=60
counter=Slider(window)


def addEvents(num):
	for i in range(0,num):
		e=Event()
		counter.increment(e)
	return None





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
		e=Event()
		print ("event id= " + str(e.id))
		counter.increment(e)	
		print ("list size= " + str(len(counter.vector)))
		# print(counter.vector)

	

		
