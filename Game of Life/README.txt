A Naive Implementation of 'Game of Life'

This is a naive implementation. A lot of memory optimizations can and will be made
in days to come.

#################

Files:

csplot.py (graphics library)
life.py (main file)
README (this file)

All these files should be in the same directory (import dependencies)

FUNCTIONING:

1). Install python if not done so already (Linux distributions come preinstalled with it).
	Check python installation by typing "python" (without quotes) on the command line.
	Python interpreter will show up.
	
2). Run the main file(life.py) as follows on command line:
	python life.py
	
3). You will see the following message:
	enter the dimensions of the board separated by comma: 
	just input two numbers separated by comma as follows:
	
	enter the dimensions of the board separated by comma: 50,50
	
4). A graphical grid of 50 by 50 will show up.

5). Keep the keyboard key "S" pressed and click on the cells you want to be alive
	(initially all cells are dead). 
	
6). Once you have selected the cells you want to be alive, close the window.
	At this point game of life will begin.
	
7). It is an infinite loop at present. If you want to stop the simulation or test
	another pattern, just do CTRL+C on command prompt. To test other interesting 
	patterns follow steps 2-6.
	

This is the basic game of life. In future versions I will try to make it more memory 
efficient, plus explore other life rules for Cellular Automata.


Patterns at on this video are good place to start testing the working of this code:
http://www.youtube.com/watch?v=23MBR2pZoDQ&noredirect=1
	