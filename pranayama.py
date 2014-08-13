import math
from threading import Timer
import pyglet

inhale = 20
exhale = 10
apneia = 0
totaltime = inhale + exhale + 2 * apneia
sound = pyglet.resource.media('Bell.wav', streaming=False)


# holds the current second as displayed on the clock
current = 0 
state = "" 
total = 0 

def formater (seconds):
	string = "" 
	second = seconds%60
	minute = int(math.floor(seconds/60))
	string = "Time elapsed " + str(minute) + ":" + str(second) 
	return string

def hit_bell ():
	sound.play()

def augment (dt):
	print dt	
	global current, state, total, label
	#updates clock by augmenting it one unit
	current = current%totaltime 
	current += 1 
	total += dt
	if (current <= inhale):
		if (current == 1) :
			hit_bell()
		state = "Inhale" 
	elif (current > inhale and current <= inhale + apneia):
		state = "Apnea"
	elif (current > inhale + apneia and current <= inhale + apneia + exhale):
		if (current == inhale + apneia + 1):
			hit_bell()
		state = "Exhale" 
	else:
		state = "Apnea"
	print str(current) + " " + str(state) + "                               " + formater(total),
	draw_label()

window = pyglet.window.Window()

def draw_label():
	label = pyglet.text.Label(state,
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
	window.clear()
	label.draw()

pyglet.clock.schedule_interval(augment, 1)

pyglet.app.run()
