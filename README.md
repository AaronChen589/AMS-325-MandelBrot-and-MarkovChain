# AMS-325-Homework-4
## MandelBrot.py
The MandelBrot function takes in the first argument, n, an integer, which determines how many points we want in our graph.
Usually, the greater the n, the more detailed the figure is.
The second argument the function takes is  N_max,an integer that is the stopping case for when we want to terminate the script
Lastly, the third argument,threshold, also an integer, will determines whether the value for z is too big and stores the appropriate boolean value to the mask array such
that if abs(z) > threshold, true is stored and vice versa.
Given the appropriate arguments, MandelBrot returns a figure that's saved onto your computer that will display the mandelbrot fractal
