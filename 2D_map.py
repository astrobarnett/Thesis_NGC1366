#for velocity dispersion we used p[2] and replace -1 and do not minus the 1180
#for relative velocity we used p[1] and put -1 and minus the 1180

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)
from astropy import units as u
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import colors

a=5006.83 #observed wavelength

b=np.loadtxt('O-II_outstd.txt',usecols=(5),unpack=True) # we have extract the flux 

rvel=np.loadtxt('O-II_outstd.txt',usecols=(1),unpack=True) # we have extract the relative velocity 
rvel=((rvel/a)-1)*299793.4 #v=(l1/l0-1)*c
rvel[:]=rvel[:]-1180

vdep=np.loadtxt('O-II_outstd.txt',usecols=(2),unpack=True) # we have extract the velocity dispersion 
vdep=((vdep/a))*299793.4 #v=(l1/l0)*c

ns1=np.loadtxt('O-II_outstd.txt',usecols=(4),unpack=True) # we have extract the noise 

sn=b/ns1

for i in range(len(b)):
	if sn[i]<3:
		b[i]=np.nan
		rvel[i]=np.nan
		vdep[i]=np.nan

p1=np.zeros([580,580],float) #grid
p2=np.zeros([580,580],float) #grid
p3=np.zeros([580,580],float) #grid

x,y,bin_num=np.genfromtxt('out_step1_sq.txt10',skip_header=1,usecols=(0,1,2),unpack=True)

for i in range(len(x)):
	p1[int(x[i]-1),int(y[i]-1)]=b[int(bin_num[i]-1)]
	p2[int(x[i]-1),int(y[i]-1)]=rvel[int(bin_num[i]-1)]
	p3[int(x[i]-1),int(y[i]-1)]=vdep[int(bin_num[i]-1)]


p1=np.transpose(p1)
p2=np.transpose(p2)
p3=np.transpose(p3)

fig,axs=plt.subplots(3,1)

####subplot 1
im=axs[0].imshow(p1,norm=colors.LogNorm())
axs[0].set_xlabel('Size(2")')
axs[0].set_ylabel('Size(2")')
axs[0].set_xticklabels([-38,-29,-20,-10,0,10,20,29])
axs[0].set_yticklabels([-38,-29,-20,-10,0,10,20,29])
axs[0].xaxis.set_major_locator(MultipleLocator(100))
axs[0].xaxis.set_minor_locator(MultipleLocator(10))
axs[0].yaxis.set_major_locator(MultipleLocator(100))
axs[0].yaxis.set_minor_locator(MultipleLocator(10))
axs[0].set_title(r'Flux ($[OIII], \lambda=5006$)')
plt.colorbar(im,ax=axs[0],fraction=0.046)#,label='Flux (10$^{-16}$erg/s/cm$^{-2}$/A')


####subplot 2
im=axs[1].imshow(p2,vmin=-250,vmax=250,cmap='RdBu_r')
axs[1].set_xticklabels([-38,-29,-20,-10,0,10,20,29])
axs[1].set_yticklabels([-38,-29,-20,-10,0,10,20,29])
axs[1].xaxis.set_major_locator(MultipleLocator(100))
axs[1].xaxis.set_minor_locator(MultipleLocator(10))
axs[1].yaxis.set_major_locator(MultipleLocator(100))
axs[1].yaxis.set_minor_locator(MultipleLocator(10))
axs[1].set_title(r'Relative velocity ($[OIII], \lambda=5006$)')
plt.colorbar(im,ax=axs[1],fraction=0.046)#,label='Relative velocity ($Kms^{-1}$)')

####subplot 3
im=axs[2].imshow(p3,vmin=42,vmax=200,cmap='hot_r')
axs[2].set_xticklabels([-38,-29,-20,-10,0,10,20,29])
axs[2].set_yticklabels([-38,-29,-20,-10,0,10,20,29])
axs[2].xaxis.set_major_locator(MultipleLocator(100))
axs[2].xaxis.set_minor_locator(MultipleLocator(10))
axs[2].yaxis.set_major_locator(MultipleLocator(100))
axs[2].yaxis.set_minor_locator(MultipleLocator(10))
axs[2].set_title(r'Velocity dispersion ($[OIII], \lambda=5006$)')
plt.colorbar(im,ax=axs[2],fraction=0.046)#,label='Velocity dispersion ($Kms^{-1}$)')


fig.tight_layout()
plt.subplots_adjust(wspace=0.2)
#plt.tight_layout()
plt.show()
















