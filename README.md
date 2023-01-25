# AMS-325 MandelBrot-and-MarkovChain
## MandelBrot.py
The MandelBrot function takes in the first argument, n, an integer, which determines how many points we want in our graph.
Usually, the greater the n, the more detailed the figure is.
The second argument the function takes is  N_max,an integer that is the stopping case for when we want to terminate the script
Lastly, the third argument,threshold, also an integer, will determines whether the value for z is too big and stores the appropriate boolean value to the mask array such
that if abs(z) > threshold, true is stored and vice versa.
Given the appropriate arguments, MandelBrot returns a figure that's saved onto your computer that will display the mandelbrot fractal

## markov_chain.py

markov_chain is a function that takes the integer n, which allows the function to create an n by 1 dimension vector, P. 
P's elements are randomly generated  and rescaled so that its sum adds up to 1.
Additionally, n will create an n by n dimension matrix P such that adding each row individually result in 1. 
P is crucial in computing its transposed form, PT, which can then be used to find the largest eigen vector. 
The resulting eigen vector will be stored in p_stationary and we can find the norm of p - p_stationary, 
which allows us to plot the return graph.

markov_chain allow takes the integer, N, which determines the number of transition/iterations for which we compute the 
dot product of PT and P. Then we utilize that P for the next iteration and so on till the Nth interation

The function then returns the a graph that's saved onto your computer that will display i-th iteration plotted
against the norm of p - p_stationary.
