from __future__ import division
import io
import numpy as np
import matplotlib.pylab as p;
import matplotlib.pyplot as plt
from matplotlib import rc

#global variables
#Nmax = 100 # array length in one dimension
xspacing = 40  #spacing between in each charge
yspacing =  40
Niter = 1000 #iterations in algorithm
tempHigh= 40 #celcius
tempLow = 20 #celcius
radius = 1
xmax = 100 #millimeter scaling
ymax = 100 #millimeter scaling
T = np.zeros((xmax, ymax), float) # float
#end defining constants
lx,ly = np.shape(T)
# boundary values
#two dimensional grid spacing function
for k in range(xmax):
    for l in range(ymax):
        if((k==30 and l ==30) or (k == 70 and l == 30) or (k==30 and l == 70) or (k==70 and l ==70)):
            T[k,l] = tempHigh
        else:
            T[k,l] = tempLow
for k in range(xmax):
	for l in range(ymax):
		i= 0
		j = 0
		if(T[k,l] == tempHigh):
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
for k in range(xmax):
    for l in range(ymax):
        if(T[k,l]==0):
            T[k,l] = tempHigh
        else:
            None
for k in range(xmax):
    for l in range(ymax):
		if(k== 0 or l ==0 or k ==xmax-1 or l==ymax-1):
			T[k,l] = tempLow
		else:
			pass
#end grid filling and boundary conditions
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
x = range(xmax)
y = range(ymax)
X, Y = p.meshgrid(x,y)
#relaxation algorithm block
for iter in range(Niter): # iterations over algorithm
    for i in range(1, xmax-1):
        for j in range(1, ymax-1):
            if(T[i,j] == tempHigh):
                None
            else:
                T[i,j] = 0.25*(T[i+1,j]+T[i-1,j]+T[i,j+1]+T[i,j-1])
	Z = T[X,Y]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.pcolor(X, Y, Z,  cmap='jet',  vmin = tempLow , vmax = tempHigh)
	ax.title(r'\textit {Surface Temperature}')
	plt.colorbar()
	plt.savefig('%d.png' % iter)
	plt.close(fig)
#end relaxation
