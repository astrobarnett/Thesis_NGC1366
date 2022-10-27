import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)



# Suppress/hide the warning
np.seterr(invalid='ignore')


#I have call the flux of Nitrogen 
N=np.loadtxt('N-II_outstd.txt',usecols=(5),unpack=True) # I have extract the flux
N1=np.loadtxt('N-II_outstd.txt',usecols=(4),unpack=True) # I have extract the flux

m=N/N1
for i in range(len(N)):
	if m[i]<3:
		N[i]=np.nan

#I have call the flux of Halpha 
Ha=np.loadtxt('H_alpha_outnew.txt',usecols=(5),unpack=True) # I have extract the flux 
Ha1=np.loadtxt('H_alpha_outnew.txt',usecols=(4),unpack=True) # I have extract the flux 

H=Ha/Ha1
for i in range(len(Ha)):
	if H[i]<3:
		Ha[i]=np.nan

#I have call the flux of oxygen 
o=np.loadtxt('O-II_outstd.txt',usecols=(5),unpack=True) # I have extract the flux 
o1=np.loadtxt('O-II_outstd.txt',usecols=(4),unpack=True) # I have extract the flux 

o3=o/o1
for i in range(len(o)):
	if o3[i]<3:
		o[i]=np.nan


#I have call the flux of hbeta 
Hb=np.loadtxt('H_beta_outnew.txt',usecols=(5),unpack=True) # I have extract the flux 
Hb1=np.loadtxt('H_beta_outnew.txt',usecols=(4),unpack=True) # I have extract the flux 

Hb3=Hb/Hb1
for i in range(len(Hb)):
	if Hb3[i]<3:
		Hb[i]=np.nan

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

d=np.log10(N/Ha) 
#f=np.log10(o/Hb)


p=np.zeros([580,580],float)

x,y,bin_num=np.genfromtxt('out_step1_sq.txt10',skip_header=1,usecols=(0,1,2),unpack=True)

"""
k=0
X=np.arange(0,58,1)
Y=np.arange(0,58,1)
r=np.zeros(3364,float)
k=0
for i in range(58):
	for j in range(58):
		r[k]=(X[i]-29)**2+(Y[j]-29)**2
		r[k]=np.sqrt(r[k])
		k+=1
r=r*0.1645 
"""

for i in range(len(x)):
	p[int(x[i]-1),int(y[i]-1)]=d[int(bin_num[i]-1)]
	
plt.imshow(p,vmax=0.4,vmin=-0.7)
x=[0,100,200,300,400,500,580]
y=[0,100,200,300,400,500,580]
l=[-29,-20,-10,0,10,20,29]
plt.xticks(x,l)
plt.yticks(y,l)
plt.xlabel('Size(2")')
plt.ylabel('Size(2")')
plt.minorticks_on()

plt.colorbar(label='log([NII] ($\lambda6583$)/H\u03B1 ($\lambda6562$))')
plt.savefig('NII_Halpha1111_map.png')
plt.show()

"""
#plt.scatter(r,d)

plt.scatter(r,f,color='black',s=10)
plt.ylim(-2,2)
plt.xlim(0,7)
plt.xlabel('Distance from center (Kpc)')
plt.ylabel('log([OIII] ($\lambda5006$)/H\u03B2 ($\lambda4861$))')
plt.savefig('OIII-Hbnew_Radius.png')
plt.show()
"""




