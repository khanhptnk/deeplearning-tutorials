import pylab
import numpy as np

x = np.linspace(-10,10,100) # 100 linearly spaced numbers

y = x**3 + 2*x*2 + x + 3 # computing the values of sin(x)/x

# compose plot
pylab.plot(x,y) # sin(x)/x
pylab.plot([0],[0], marker='o', markersize=8, color='red')
pylab.show() # show the plot


x = np.linspace(-2.5,1.5,100) # 100 linearly spaced numbers
y = x**4 + x**3 - 2*x**2 + 1 # computing the values of sin(x)/x

# compose plot
pylab.plot(x,y) # sin(x)/x
pylab.plot([0.72],[0.60], marker='o', markersize=8, color='red')
pylab.show() # show the plot
