import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

def plot_f(x):
    plt.plot(x, f(x))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def df(x, h=1e-5):
    return (f(x+h)-f(x))/h

def plot_df(x):
    plt.plot(x, df(x))
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.show()

def ddf(x, h=1e-5): 
    return (df(x+h)-df(x))/h

def plot_ddf(x):
    plt.plot(x, ddf(x))
    plt.xlabel('x')
    plt.ylabel("f''(x)")
    plt.show()

def dddf(x, h=1e-5):
    return (ddf(x+h)-ddf(x))/h

def plot_dddf(x):
    plt.plot(x, dddf(x))
    plt.xlabel('x')
    plt.ylabel("f'''(x)")
    plt.show()
