#Sliding Window Counter

The slidingCounter.py defines a slider class that implements a Sliding Window Counter. While instantiaiting a counter, user can pass the maximum time window(in seconds) as argument (takes 3600 by default).
E.g- to create a sliding window counter of 2 hours.

from slidingCounter import *  
counter=Slider(7200)  

The slider class has 4 important methods:  
increment() - registers an event (as a timestamp) and increments the counter by 1.  
numLastSecond - returns events that occurred in last second.  
numLastMinute - returns events that occurred in last minute.  
numLastHour - returns events that occurred in last hour.  





##Instructions

Files:
1.	slidingCounter.py - contains the sliding window counter class.  
2.	test1.py - runs tests on the program to check correctness, running time and edge cases.  
3.	test2.py - this is an interactive test where the user can use different hot keys to simulate and run different functions in the sliding window class.  


<b>Instructions for the interactive test (test2.py):</b>

-Press Enter to register an event.  
-Input number to register multiple events.  
-Input s to fetch events occurred in last second.  
-Input m to fetch events occurred in last minute.  
-Input h to fetch events occurred in last hour.  
-Input i to print instructions again.  
 INPUT x TO QUIT :  

<b>Example:</b>
-pressing enter, registers a single event by calling the increment function once.  
-typing 35 and pressing enter registers 35 events in the counter by calling the increment function 35 times.  
-typing m and pressing enter fetches the events that occurred in the last one minute.  
-typing i and pressing enter shows you the above instructions on the screen again.  
-typing x and pressing enter quits the test program.  

