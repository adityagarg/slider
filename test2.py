"""
This test is designed as a game where the user can test different functions within the Sliding Window Counter using different keys. The instructions of the test provide a comprehensive overview of the test.

"""

from slidingCounter import *
import time, datetime as dt



window=3600       #specify maximum time window of Sliding Window Counter
counter=Slider(window)	#Instantiate Sliding Window Counter Class object


def addEvents(num):
	"""
	function to call increment function num number of times based on user input.
	"""


	for i in range(num):
		counter.increment()
	return None

instructions="\n-Press Enter to register an event.\n-Input number to register multiple events.\n-Input s to fetch events occurred in last second.\n-Input m to fetch events occurred in last minute.\n-Input h to fetch events occurred in last hour.\n-Input i to print instructions again.\n INPUT x TO QUIT : "

while True:
	blah=raw_input(instructions)
	if(blah=='x'):
		print ("Thanks for testing.")
		break

	elif(blah=='s'):
		print ("Events in last second : "+ str(counter.numLastSecond())+"\n")

	elif(blah=='m'):
		print ("Events in last minute : "+ str(counter.numLastMinute())+"\n")

	elif(blah=='h'):
		print ("Events in last hour : "+ str(counter.numLastHour())+"\n")

	elif(blah=='i'):
		instructions="\n-Press Enter to register an event.\n-Input a number to register multiple events.\n-Input s to fetch events occurred in last second.\n-Input m to fetch events occurred in last minute.\n-Input h to fetch events occurred in last hour.\n-Input i to print instructions again.\n INPUT x TO QUIT : "
		print instructions

	elif(blah.isdigit()):
		start=time.time()
		addEvents(int(blah))
		end=time.time()
		print "Added " + str(blah)+" events"
		print "time taken - "+ str(end-start)
		print ("eventList size= " + str(len(counter.eventList))+"\n")

	else:
		start=time.time()
		counter.increment()	
		end=time.time()
		print "Event registered."
		print "time taken - "+ str(end-start)
		print ("eventList size= " + str(len(counter.eventList))+"\n")
	instructions=""

	

		
