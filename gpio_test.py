
####################################################
#                                               
#                gpio_test.py v1.0               
#                                               
#                 James McCormac                 
#
#
#  ** Hit "CTRL+C" to kill the program at any time **
#                                               
#  Revision history:                            
#  20140908  v1.0  Script written and tested    
#                                               
#                                               
###################################################

# import python modules
# import RPi.GPIO as g to stop us writing "RPi.GPIO." 
# everywhere and just "g." instead
import RPi.GPIO as g
# import time for sleeping and sys for exit command
import time
import sys

# set up the GPIO pins on the Pi using BCM mode
# set pins 23, 24 & 25 (BCM numbering) to inputs  
# these are really pins 16, 18 and 22.
g.setmode(g.BCM)
g.setup(23,g.IN)
g.setup(24,g.IN)
g.setup(25,g.IN)

# set blinds to something before starting
B1 = "UNKNOWN"
B2 = "UNKNOWN"
B3 = "UNKNOWN"

# loop forever checking status of the sensors
# my sensors return 0 when activated by a magnet
# and 1 when the magnet is moved away
# 
while (1):
	time.sleep(0.5)
	if g.input(23) == 0:
		B1 = "Triggered"
	if g.input(24) == 0:
		B2 = "Triggered"
	if g.input(25) == 0:
		B3 = "Triggered"
	
	if g.input(23) == 1:
		B1 = "Not Triggered"
	if g.input(24) == 1:
		B2 = "Not Triggered"
	if g.input(25) == 1:
		B3 = "Not Triggered"
	
	if g.input(23) != 1 and g.input(23) != 0:
		print "UNKNOWN RESPONSE FROM B1, EXITING..."
		sys.exit()
	if g.input(24) != 1 and g.input(24) != 0:
		print "UNKNOWN RESPONSE FROM B2, EXITING..."
		sys.exit()
	if g.input(25) != 1 and g.input(25) != 0:
		print "UNKNOWN RESPONSE FROM B3, EXITING..."
		sys.exit()
	
	
	print "B1: %s\tB2: %s \tB3: %s (Press Ctrl + C to quit)" % (B1, B2, B3)


