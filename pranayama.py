import math
from threading import Timer
import pyglet
from Tkinter import *


inhale = 20
exhale = 10
apneia = 0

#gets input from user
def get_input():
	global inhale, exhale, apneia
	inhale = raw_input("How many seconds on the inhale?")
	exhale = raw_input("How many seconds on the exhale?")
	apneia = raw_input("How many seconds for apnea?")
	if (inhale.isdigit() and exhale.isdigit() and apneia.isdigit()):
		inhale = int(inhale)
		exhale = int(exhale)
		apneia = int(apneia)
	else:
		print "Input incorrect. Please try again"
		get_input()

#loads sound into memory
sound = pyglet.resource.media('Bell.wav', streaming=False)


# holds the current second as displayed on the clock
current = 0 
state = "" 
total = 0 
record = 0

#formats time
def formater (seconds):
	string = ""
	second = math.floor(seconds%60)
	minute = int(math.floor(seconds/60))
	string = "Time elapsed " + str(minute) + ":" + str(second) 
	return string

# plays the sound 
def hit_bell ():
	sound.play()

#augments time and updates state
def augment (dt):	
	offset = (dt -1) * 1000
	global current, state, total, label, record
	#updates clock by augmenting it one unit
	current = current%totaltime 
	current += 1 
	total += dt
	if (current <= inhale):
		if (current == 1) :
			hit_bell()
		state = "Inhale" 
	elif (current > inhale and current <= inhale + apneia):
		if (current == inhale + 1) :
			hit_bell()
		state = "Apnea"
	elif (current > inhale + apneia and current <= inhale + apneia + exhale):
		if (current == inhale + apneia + 1):
			hit_bell()
		state = "Exhale" 
	else:
		if (current == inhale + apneia + exhale + 1) :
			hit_bell()
		state = "Apnea"
	if (offset > record):
		record = offset
	print str(current) + " " + str(state) + "                               " + formater(total) + " Off by " + str(math.trunc(offset)) + " miliseconds" + " Max error: " + str(math.trunc(record))
	draw_label()

#Opens window
window = pyglet.window.Window()

def draw_label():
	label = pyglet.text.Label(state,
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
	window.clear()
	label.draw()

#Gets input from user
get_input()
totaltime = inhale + exhale + 2 * apneia


#calls augment every second
pyglet.clock.schedule_interval(augment, 1)

#initializes loop
pyglet.app.run()
