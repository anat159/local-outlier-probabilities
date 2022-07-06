#imports
import subprocess
import sys

#subprocess.check_call([sys.executable, "-m", "pip", "install", "sklearn"])
from sklearn.neighbors import NearestNeighbors

try:
    import matplotlib.pyplot as plt
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt
try:
    from pandas import read_csv
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    from pandas import read_csv
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np
try:
    import math
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "math"])
    import math
try:
    import os
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import os

#Param
K=20
Lambda=3

def d(o,s):
    """
    this function calculate the euclidean distance between points o,s
    input
    ------
    o: 1*D
    s: 1*D
    where D is the number of dimensions
    output
    -----
    ans: 1*1 -
    euclidean distance
    """
    return np.linalg.norm(o-s)

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
    #calculates all the distances in the data
    # calculates all the distances in the data
    neigh = NearestNeighbors(n_neighbors=K + 1)
    neigh.fit(X)
    distance_matrix = neigh.kneighbors(X)
    distance_matrix_sort_index = distance_matrix[1][:, 1:]
    distance_matrix_S = distance_matrix[0][:, 1:]

    #calculated std(o,S)
    std_o_S=np.power(np.power(distance_matrix_S,2).sum(axis=1)/K,0.5)
    #calculate pdist
    pdist=std_o_S*Lambda
    #calculate the mean pdist(lambda,s,s(S)) for s in S(o)
    E_pdist=np.mean(pdist[distance_matrix_sort_index],axis=1)
    #calculate PLOF
    PLOF=pdist/E_pdist-1
    nPLOF=Lambda*np.power(np.mean(np.power(PLOF,2)),0.5)
    #calculating erf
    args=PLOF/(nPLOF*np.power(2,0.5))
    y=np.zeros(len(X))
    for i,arg in enumerate(args):
        val=math.erf(arg)
        y[i]=np.max([0,val])
    return y
def main():
    """
    the main function
    calculate LoOP from the data store at 'data - 2022-04-22T091116.036.csv'
    """

    y=LoOP(X)
    plt.scatter(X[0],X[1])
    val=0.7
    plt.scatter(X[y>val][0], X[y>val][1],color='red')
    plt.show()

if __name__ == '__main__':
    main()