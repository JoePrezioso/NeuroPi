NeuroPi
=======

An experiment in reading data from a NeuroSky Mindwave into a Raspberry Pi.

We intend to use the Mindwave to do send data to the Pi, based upon the 
readings it gets from the user, whether that be by using it to manipulate
the mouse, send key input, or do something else to use the user's brain 
as a means of interaction with the Pi.

Dependencies:
We are using a modified version of https://github.com/cttoronto/python-mindwave-mobile to interface with the mindwave mobile, and from that we have their dependencies; Install python-bluetooth to remove the import error.
All graphical pieces use pygame. (http://www.pygame.org)
