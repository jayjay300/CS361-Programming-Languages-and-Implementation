import numpy as np
import matplotlib.pyplot as plt

def formula(x):
	sinval = x-2
	eexp = -1 * x**2
	sin = (np.sin(sinval))
	sin = sin ** 2
	eval = np.exp(eexp)
	sin = sin * eval
	return sin
	
def graph(formula):
	x = np.linspace(0, 2, 50)
	y = formula(x)
	plt.plot(x,y)
	plt.xlabel('x value')
	plt.ylabel('y=sin^2(x-2)e^(-x^2)')
	plt.title('Equation for Problem 10')
	plt.show()

graph(formula)