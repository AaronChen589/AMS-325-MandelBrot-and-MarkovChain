import numpy as np
import matplotlib.pyplot as plt

def markov_chain(n,N): 
    """
    Parameters
    ----------
    n : Integer
        This argument will create an n by 1 dimension vector P with randomly
        generated states/elements adding up to 1.
        Additionally, n will create an n by n dimension matrix P such that
        adding each rows result in 1. 
        P can be used to compute it's transposed form, PT. This can then be 
        used to find the largest eigen vector, which can be stored in 
        p_stationary. Lastly, we can find the norm of p - p_stationary and
        utilize it to plot the graph.
    N : Integer
        This argument determines the number of transition/iterations
        for which we compute the dot product of PT (P.transposed()) 
        and P. Then we utilize that P for the next iteration and so on. 

    Returns
    -------
    A graph is saved on your computer that will display i-th iteration plotted
    against the norm of p - p_stationary

    """
# Probability Distribution P is made by creating an array where each index is a 
# randomly generated number from 0 to 1 and divided by the sum of all numbers 
# to scale them so that their sum is equal to 1. 
# To begin, we want to generate random # in a 1-D vector
    p = np.random.rand(1,n) 
    sum = p.sum()
    p = (p / sum)   # normalize the vector
    p = p.transpose() # we transpose the p so that dot product is possible later
    
# P_transition is the transition matrix 
# where each adding element of a row is equal to 1
    P_transition = np.random.rand(n,n)
    for i in range(n):
        rowSum = 0
        for j in range(n):
            rowSum = rowSum + P_transition[i][j]
            if(j == n - 1):
                for k in range(n):
                    P_transition[i][k] = P_transition[i][k] / rowSum                
    PT = P_transition.transpose() #PT is P transposed

# w contains the indices of each eigenvector while
# v contains the normalized length of a specific vector

    w,v = np.linalg.eig(PT)

# argmax returns the index of the largest eigen vector and we find 
# the eigenvector corresponding to the largest eigenvalue
    p_stationary = v[:,(np.argmax(w))]
  
    eigenSum = p_stationary.sum()
    p_stationary = (p_stationary / eigenSum) #normalize the vector
   
# norm_array will represent the norm of p-p_stationary such that for each iteration,
# p is updated by doing the dot product of PT and the current iteration's p
    norm_array = []
    # outer for loops determines N numbers of iterations
    for i in range(N):
        x=np.random.rand(n,1) # create an array x of size n by 1 dimension 
        for j in range(n):
            x[j]=p[j]-p_stationary[j] # store each element of p and p_stationary into x
        norm_array.append(np.linalg.norm(x)) #append the norm of x into array
        p = np.dot(PT,p) # update P as the dot product of PT and P
    print(p-p_stationary)
    
# i_array will be the x-axis, representing all i-th iteration up till N        
    i_array = np.arange(1,N+1,1)
    plt.plot(i_array, norm_array)
    plt.xlabel("i-th iteration")
    plt.ylabel("norm( p - p_stationary )")
    plt.title("i-th iteration vs norm(p - p_stationary) ")
    plt.show()
    return
markov_chain(10,50)

