#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:56:59 2022

@author: astro
"""

#H_alpha 6562.80

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from astropy.io import fits
from matplotlib.backends.backend_pdf import PdfPages
da=fits.open('ngc1366_5gas_fluxes_hr_line.fits')
d=da[0].data

p=np.zeros((585,588),float)
for i in range(7):
    p+=d[53+i,:,:] #to read the slice
for i in range(7):
    p+=d[170+i,:,:] #to read the slice
for i in range(9):
    p+=d[1419+i,:,:] #to read the slice
for i in range(7):
    p+=d[1436+i,:,:] #to read the slice
#p=p/7
p=np.transpose(p) 
#for i in range(588):
#	for j in range(585): 
#		if (p[i,j]<0 or p[i,j]>10):
#			p[i,j]=0
plt.imshow(p,norm=colors.LogNorm())
plt.show()
"""
pdf=PdfPages("flux.pdf")
for i in range(1,21):
	fig=plt.figure(figsize=(4,5))
	plt.imshow(p)#, levels=50 )#, norm=colors.LogNorm())
	#plt.colorbar()
	pdf.savefig(fig)
	plt.close()
pdf.close()
"""
