'''
A thread is an entity within a process that can be scheduled for execution. It is the smallest unit of exection in a program.
In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code.

x.start() call run() fn, and before completion of for-loop, proceeds to y.start()

So for a bried period of time, both x and y threads are running at the same time
Result is a random combination of 'send' and 'receive' since the 2 threads - x and y run independently
'''

import threading

class Messenger(threading.Thread):

	def run(self):			# run() is a special name required for threads
		
		for _ in range(10):		# _ is if variable doesn't matter
			print(threading.currentThread().getName())


x = Messenger(name='Send')
y = Messenger(name='Receive')

x.start()			# start() function kickstarts a thread
y.start()