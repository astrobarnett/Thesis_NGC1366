import numpy as np
import matplotlib.pyplot as plt

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

d=np.zeros(len(N),float)

d=np.log10((N/Ha)) #nitrogen/halpha
g=np.log10(o/Hb)  #oxygen/Hbeta



a=np.arange(-3,6,0.01)
q=((0.61)/(a-(0.05)))+1.30

plt.scatter(d,g,color='black',s=10)
plt.plot(a,q,'r')
plt.xlabel('log(N[II]6584/H\u03B1)')
plt.ylabel('log(O[III]5007/H\u03B2)')
plt.xlim(-1.5,0)
plt.ylim(-2,2)
plt.savefig('BPT.png')
plt.show()

np.savetxt('BPT_5.txt', np.column_stack([N,Ha,o,Hb,d,g]), fmt=b'%10.6f')



#np.savetxt('BPT_2.txt', np.column_stack([a,q]), fmt=b'%10.6f')
#d=np.nan_to_num(d)
#g=np.nan_to_num(g)
#f=np.nan_to_num(f)

#d=np.nan_to_num(d)
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
"""


"""
for i in range(len(Ha)):
	if Ha[i]>20 and N[i]>20:
		d[i]=np.log(N[i]/Ha[i])
d=d[d!=0]
g=np.zeros(len(N),float)

for i in range(len(Ha)):
	if o[i]>20 and Hb[i]>20:
		g[i]=np.log(o[i]/Hb[i])
g=g[g!=0]

print(len(d),len(g))
d=d[:len(g)]

a=np.linspace(-3,4,len(g))
q=((0.61)/(a-(3)))+1.30
plt.scatter(d,g)
plt.plot(a,q)
plt.xlabel('log(N[II]6584/H\u03B1)')
plt.ylabel('log(O[III]5007/H\u03B2)')
plt.xlim(-2,0)
plt.ylim(-2,2)
plt.show()
"""



































