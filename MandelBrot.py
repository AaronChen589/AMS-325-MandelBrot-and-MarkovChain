import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(n, N_max,threshold): 
    """
    Parameters
    ----------
    n : Integer
        This argument determines how many points we want in our graph.
        Usually, the greater the n, the more detailed the figure is.
    N_max : Integer
        N_max is the stopping case for when we want to terminate the script
    threshold : Integer
        threshold determines whether the value for z is too big and
        stores the appropriate boolean value to the mask array.
        (if abs(z) > threshold, true) (else, false)

    Returns
    -------
    A figure is saved onto your computer that will display the mandelbrot
    fractal
    
    Examples For Good Graphs
    mandelbrot(100,100,100)
    mandelbrot(80,50,50)
    mandelbrot(500,50,50)

    """
    # creates the arrays x with bounds of [-2,1] and y with bounds of [-1.5,1.5]
    # where each have n points
    x = np.linspace(-2, 1, n)
    y = np.linspace(-1.5,1.5,n)
    # meshgrid makes xv into a matrix from -2 to 1 horizontally
    # while making yv into a matrix from -1.5 to 1.5 vertically
    xv, yv = np.meshgrid(x, y)
    # creates a mask boolean array
    mask = np.zeros((n,n))
    # Create a matrix C such that each index of c is equal to
    # the sum of the elements of xv and yv * 1j at their respective index 
    c = xv + yv * 1j
    # iterate through the c matrix and Mask array
    for x in range(n):
        for y in range(n):
            z = 0
            for j in range(N_max):
                #if abs(z) is >= threshold, we make z = threshold to 
                #prevent overflow
                if (abs(z) >= threshold):
                    z = threshold
                else:
                    z = z**2 + c[x][y]
                #Mask array should be an boolean array containing true 
                #at the index if abs(z) < threshold and otherwise false
                if(abs(z) < threshold):
                    mask[x][y] = True
                else:
                    mask[x][y] = False
    #Plots out the graph and saves the figure as a png
    plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    return

mandelbrot(100,100,100)



