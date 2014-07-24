from __future__ import division
import io
import numpy as np
import matplotlib.pylab as p;
import matplotlib.pyplot as plt
from matplotlib import rc


# public global variables
Niter = 50000 #iterations in algorithm
tempHigh= 40  #kelvin
tempLow = 20  #kelvin
radius = 1
xmax = 100 #x-scaling of the surface
ymax = 100 #y-scaling of the surface
#privates
x = range(xmax)
y = range(ymax)
X, Y = p.meshgrid(x,y) 
#use only for xmax,ymax = 100 or 10 cm
def gridFill(xmax,ymax):
	T = np.zeros((xmax, ymax), float)
	for k in range(xmax):
		for l in range(ymax):
			if((k==30 and l ==30) or (k == 70 and l == 30) or (k==30 and l == 70) or (k==70 and l ==70)):
				T[k,l] = tempHigh
			else:
				T[k,l] = tempLow
	return T

def radialFill(xmax, ymax):
	T = gridFill(xmax,ymax)
	lx,ly = np.shape(T)
	for k in range(xmax):
		for l in range(ymax):
			if(T[k,l] == tempHigh):
				i= 0
				j = 0
				while(i<= radius and k+i<=lx-1 and k-i>=0):
					while(j<= radius and j+l<=ly-1  and l-j>=0):
						T[k+i, l+j] = 0
						T[k-i, l-j] = 0
						T[k-i,l+j] = 0
						T[k+i,l-j] = 0
						j= j+1
					j=0
					i = i+1
			else:
				pass
	return T
def reFill(xmax,ymax):
	T = radialFill(xmax,ymax)
	for k in range(xmax):
		for l in range(ymax):
			if(T[k,l]==0):
				T[k,l] = tempHigh
			if(k== 0 or l ==0 or k ==xmax-1 or l==ymax-1):
				T[k,l] = tempLow
			else:
				None
	return T

def relaxation(Niter):
	T = reFill(xmax,ymax)
	for iter in range(Niter): # iterations over algorithm
		for i in range(1, xmax-1):
			for j in range(1, ymax-1):
				if(T[i,j] == tempHigh):
					None
				else:
					T[i,j] = 0.25*(T[i+1,j]+T[i-1,j]+T[i,j+1]+T[i,j-1])
	return T

dT_x, dT_y = np.gradient(relaxation(Niter), 1,1)

def functz(X,Y):
	T = relaxation(Niter)
	z = T[X,Y]
	return z

def functx(X,Y):
	fx = dT_x[X,Y]
	return fx
def functy(X,Y):
	fy = dT_y[X,Y]
	return fy

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# X Derivative
plt.subplot(131)
plt.pcolor(X, Y, functx(X,Y),  cmap='jet',  vmin = np.min(dT_x), vmax = np.max(dT_x))
plt.title(r"$\displaystyle\partial_xT(x,y)$", fontsize = 12, color ='black')
plt.colorbar()
# Y Derivative
plt.subplot(132)
plt.pcolor(X, Y, functy(X,Y),  cmap='jet',  vmin = np.min(dT_y) , vmax = np.max(dT_y))
plt.title( r"$\displaystyle\partial_yT(x,y)$", fontsize = 12, color ='black')
plt.colorbar()

# Surface Temperature
plt.subplot(133)
plt.pcolor(X, Y, functz(X,Y),  cmap='jet',  vmin = tempLow , vmax = tempHigh)
plt.title(r'\textit {Surface Temperature}')
plt.colorbar()

plt.show()

