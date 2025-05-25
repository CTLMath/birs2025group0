import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, exp, log

def graph(f,a,b,N=200,color="b"):
    "Plot the graph of y = f(x) on [a,b] using N points."
    f = np.vectorize(f)
    x = np.linspace(a,b,N)
    y = f(x)
    plt.plot(x,y,c=color)
    plt.grid(True)

def point(x,y,color="b"):
    "Plot point (x,y)."
    plt.scatter(x,y,s=50,c=color)
    plt.grid(True)

def matrix(A):
    return np.matrix(A,dtype=float)

print("Welcome to the UBC MATH 100 development environment!")
print("Mathematical functions: sin, cos, exp, log")
print("Plot the graph y = f(x) over [a,b] with graph(f,a,b)")
print("Create a matrix from a list of rows of numbers such as matrix([[a,b],[c,d]])")