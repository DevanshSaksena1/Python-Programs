import numpy as np
import matplotlib.pyplot as plt


inlinks = []
inpackages = []
#reading data from file
with open('in_squeeze.dat') as inData:
    for line in inData:
        data = line.split()
        inlinks.append(float(data[0]))
        inpackages.append(float(data[1]))
#dividing the inData file into inlinks array and inpackages array
#Similary for the outlinks
outlinks =[]
outpackages =[]
with open('out_squeeze.dat') as inData:
    for line in inData:
        data = line.split()
        #Adding the type casting from string to integer
        outlinks.append(float(data[0]))
        outpackages.append(float(data[1]))

#main formula for the calculation
def N(x, nu, c, lamda):
    return nu+(c*c)*((x+lamda)**(-2))

#till 47 it fits properly with the curve
X1 = np.linspace(start=1, stop=47, num=1000)
X2 = np.linspace(start=1, stop=300, num=1000)

nuinlinks, cinlinks, lamdainlinks = -28.0 ,265.0 ,2.2 
Ninlinks = N(X1, nuinlinks, cinlinks, lamdainlinks)

nuoutlinks, coutlinks, lamdaoutlinks = 1.0 ,110.0  ,0.45
Noutlinks = N(X2, nuoutlinks, coutlinks, lamdaoutlinks)

plt.figure(1)
plt.plot(inlinks, inpackages, '+')
plt.xscale('log')
plt.yscale('log')
plt.title('Input-links for the pakages')
plt.plot(X1, Ninlinks, linestyle='dashed' ,color='red', lw=1)


plt.figure(2)
plt.plot(outlinks, outpackages, '+')
plt.xscale('log')
plt.yscale('log')
plt.title('Output-links for the pakages')
plt.plot(X2, Noutlinks,linestyle='dashed' ,color='red', lw=1)

plt.show()
