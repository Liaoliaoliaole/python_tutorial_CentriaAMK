#2. Create class Clock and it's subclass AlarmClock. Test clocks in main.
#There has to be ticking and alarming methods...
import time

class Clock:
	def __init__(self, hours, minutes, seconds):
		if hours > 24:
			hours = 24
		elif hours < 0:
			hours = 0
		if minutes >60:
			minute = 60
		elif minutes < 0:
			minutes = 0
		if seconds >60:
			seconds = 60
		elif seconds <0:
			seconds =0
		self.total_seconds = int(hours)*3600 + int(minutes)*60 + int(seconds)

	def getTime(self):
		hours = self.total_seconds // 3600
		minutes = (self.total_seconds - (hours *3600)) // 60
		seconds = self.total_seconds - 3600 * hours - 60 * minutes
		return str(hours) +":"+ str(minutes) + ":" + str(seconds)

	def ticking(self):
		self.total_seconds = self.total_seconds+1
		time.sleep(1)

	def alarming(self):
		while True:
			self.ticking()


class AlarmClock(Clock):
	def __init__(self,hours,minutes,seconds,a_hours,a_minutes,a_seconds):
		super().__init__(hours,minutes,seconds)
		self.a_total_seconds = int(a_hours)*3600 + int(a_minutes)*60 + int(a_seconds)

	def alarming(self):
		while True:
			self.ticking()
			if self.total_seconds >= self.a_total_seconds:
				print("RRRRRRRIIIIIIINNNNNNNNN!!!!")
				break

myTime1 = Clock(20,2,3)
myTime2 = Clock(-3,2.2,0)
myTime3 = Clock(26,0.9,88)
print (myTime1.getTime())
print (myTime2.getTime())
print (myTime3.getTime())
#it will ring after 10 seconds
AlarmClock(8,24,50,8,25,0).alarming()
