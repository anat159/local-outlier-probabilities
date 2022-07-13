#imports
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import numpy as np
from math import erf
from sklearn.datasets import make_blobs

#Param
K=50 #number of neighbors
Lambda=3 #control over the approximation of the density.
val = 0.7 #  threshold for LoOP values


def LoOP(X):
    """
    this function calculate LoOP
    input
    ------
    X : n*D
    the data,
    where n is the number of samples and D is the number of dimensions
    output
    ------
    y : n*1
    the score,
    where n is the number of samples
    """
    #calculates distances
    neigh = NearestNeighbors(n_neighbors=K+1)
    neigh.fit(X)
    distance_matrix = neigh.kneighbors(X)
    distance_matrix_sort_index = distance_matrix[1][:, 1:]
    distance_matrix_S = distance_matrix[0][:, 1:]
    #calculated std(o,S)
    std_o_S=(np.sum(distance_matrix_S**2,axis=1)/K)**0.5
    #calculate pdist
    pdist=std_o_S*Lambda
    #calculate the mean pdist(lambda,s,s(S)) for s in S(o)
    E_pdist=np.mean(pdist[distance_matrix_sort_index],axis=1)
    #calculate PLOF
    PLOF=pdist/E_pdist-1
    nPLOF=Lambda*(np.mean(PLOF**2))**0.5
    #calculating erf
    args=PLOF/(nPLOF*(2**0.5))
    y=np.zeros(len(X))
    for i,arg in enumerate(args):
        val=erf(arg)
        y[i]=np.max([0,val])
    return y

def main():
    """
    the main function
    """
    centers = [[-3, -3], [0,0],[4,0]]
    X, y = make_blobs(n_samples=[20,1000,200], centers=centers, n_features=2, cluster_std=[0.1,1,0.5],random_state = 0) #Generate isotropic Gaussian blobs.
    y=LoOP(X) #calculate LoOP
    plt.scatter(X[y<=val,0],X[y<=val,1],color='blue')
    plt.scatter(X[y>val,0], X[y>val,1],color='red')
    plt.title('LoOP')
    plt.show()

if __name__ == '__main__':
    main()