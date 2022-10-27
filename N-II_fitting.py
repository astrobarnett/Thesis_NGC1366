#This program fit all the N-I line with wavelength 6547.96 line using 10spaxel file. 
import numpy as np
import matplotlib.pyplot as plt 
from astropy.io import fits
from scipy import optimize as opt
from matplotlib.backends.backend_pdf import PdfPages
xpos1=1273
xpos2=1513
#for noise
xpos3=114
xpos4=161
xpos5=177
xpos6=223


data=np.zeros((3364,3272),float) #2D array with 121x3272 size
for i in range(1,3365):
	if i < 10 : sss='000'+str(i)
	if i >  9 : sss='00'+str(i)
	if i > 99 : sss='0'+str(i)
	if i > 999 : sss=''+str(i)	
	hdul = fits.open('vor/voron_spc'+sss+'.fits')
	data[i-1,:] = hdul[0].data #we used colon to slice

x=np.linspace(6400,6700,240) #range of the x-axis

#We wrote first fuction gausian, then residual and then did chisquare
#p0 is itensity , p1 lamda, p2 wavelength dispersion, p3 bg noise
#we create p as array with value intensity,sigma,lamda,position and backgroud noise
def fun1(p,x): 
	gauss=p[0]*np.exp(-0.5*((x-p[1])/(p[2]))**2)+p[3]
	return gauss

def fun2(p,x,y): #residual function y is data point 
	resid=fun1(p,x)-y
	return resid
def fun3(p,x,y): #chi2 function
	chi2=np.sum(fun2(p,x,y)*fun2(p,x,y))
	return chi2

#to save the output in pdf file.

pdf = PdfPages("N-II_fittingstd.pdf")
p=np.zeros((3364,6),float)

for i in range (3364):
	dat=data[i,:]
	dat=dat[xpos1:xpos2]
	r=np.mean(dat)
	sl=(dat[166]+4*dat[167]+dat[168])/6 #sl denotes the slice number, and we used here "weighted average" concept
	guess=[sl-r,6609,2.,r] #guess the value for peak of curve which is intensity,lamda,width of lamda,background
	res=opt.minimize(fun3,guess,args=(x,dat)) #y will take args
	noise_1=dat[xpos3:xpos4]
	noise_2=dat[xpos5:xpos6]
	noise1=np.concatenate((noise_1,noise_2))
	meann=np.mean(noise1)
	p[i,4]=np.std(noise1)
	#print(p[i,4])
	p[i,0:4]=res.x
	p[i,2]=abs(p[i,2])
	p[i,5]=((p[i,0]*p[i,2])*2.4835)
	q=fun1(p[i,0:4],x)
	fig = plt.figure(figsize =(6, 5))
	plt.plot(x,dat,label='Data')
	plt.xlabel('Wavelength $(A)$')
	plt.ylabel('Flux $(10^{-16}erg/s/cm^{-2}/A)$')
	plt.plot(x,q,label='Fit')	
	plt.legend(loc="upper right")
	pdf.savefig(fig)
	plt.close()
pdf.close()
np.savetxt('N-II_outstd.txt', np.column_stack([p]), fmt=b'%10.6f')






























