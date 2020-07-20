import matplotlib.pyplot as plt
import numpy as np 

"""
This will determine pi using probability.

Consider a square of length 2, centered in the origin. 
This square has an area of As = l^2 = 4

Inside this square, put a circle of radius 1, 
which has an area of Ac = pi * r^2 = pi

Then, generate two random numbers inside the square:	
	x in [-1,1]
	y in [-1,1]

The probability that this number is inside the circle is equal to 
	Ac/As = pi / 4 

By calculating a bunch of these random numbers, Nt, 
label the ones that are inside the circle as Nc, 
then then probability is also approximately equal to Nc/Nt

So solve for pi = 4 * Nc/Nt

"""


pi= np.pi
def sqrt(x): return np.sqrt(x)
def exp(x): return np.exp(x)

def calcpi(Nt):
	# this generates Nt random numbers from 0 to 1
	x0=np.random.random(Nt)
	y0=np.random.random(Nt)
	
	# next let's shift these, so they are between -1 and 1
	x = x0*2.0 - 1.0 
	y = y0*2.0 - 1.0 
	
	# let r be distance away from the center"
	r = sqrt( pow(x,2) + pow(y,2) )
	
	
	# if r <1 it's inside the circle with radius 1 otherwise, it's outside the circle
	
	
	condition0 = r <1	
	
	
	# This function then extracts all elements in x (or y), for which the condition is True
	
	xin = np.extract(condition0, x)
	yin = np.extract(condition0, y)

	
	# here we repeat this, but for elements outside of the circle
	
	condition1 = r >=1	
	xout = np.extract(condition1, x)
	yout = np.extract(condition1, y)

	pi_ran = 4.0* len(xin)/float(Nt)
	return xin,yin, xout,yout, pi_ran
	

method1 = 'y'
if method1 == 'y':
	plt.figure(figsize=(9,10))

	for exp0 in np.arange(1,7,.2):
		Nt = int(pow(10,exp0))

		plt.subplot(222)
		plt.axhline(y=pi,color='b',linewidth=1,linestyle='dashed')

		xin,yin, xout,yout, pi_ran = calcpi(Nt) 
		print("pi_ran",pi_ran)
		plt.subplot(222)
		plt.errorbar(exp0, pi_ran,markersize=8,fmt='o',color='r',mfc='white',mec='r', elinewidth=2, capsize=4, mew=1.4)	
		
		plt.xticks([0,2,4,6],['$1$','$10^2$','$10^4$','$10^6$'],size=15)
		plt.ylim([3.04,3.24])

	Nt = 10000
	xin,yin, xout,yout, pi_ran = calcpi(Nt) 
	plt.subplot(221)
	plt.errorbar(xin,yin,markersize=8,fmt='s',color='b',mfc='white',mec='b', elinewidth=2, capsize=4, mew=1.4)	
	plt.errorbar(xout,yout,markersize=8,fmt='o',color='r',mfc='white',mec='r', elinewidth=2, capsize=4, mew=1.4)	
plt.savefig('./pi_1pcnt_part1.pdf',
				bbox_inches='tight', 
				transparent=True)
method2 = 'y'
if method2 == 'y':
	plt.figure(figsize=(10,5))
	plt.subplot(223)
	plt.axhline(y=pi,color='b',linewidth=1,linestyle='dashed')
	
	for exp0 in np.arange(1,7,1):
		Nt = int(pow(10,exp0))
		pis = [] 
		attempts =500 

		for attempt in np.arange(attempts):
			xin,yin, xout,yout, pi0 = calcpi(Nt)
			pis.append(pi0)

		pi0 = np.mean(np.array(pis))
		dpi0 = np.std(np.array(pis),ddof=1)
		plt.subplot(223)
		plt.errorbar(exp0,pi0,yerr=dpi0,markersize=8,fmt='s',color='b',mfc='white',mec='b', elinewidth=2, capsize=4, mew=1.4)	

	plt.xticks([0,2,4,6],['$1$','$10^2$','$10^4$','$10^6$'],size=15)
	print("pi0, dpi0",pi0, dpi0)
	plt.ylim([2.94,3.34])
	plt.subplot(222)

	x=np.arange(7)
	ym = np.ones(7)*(pi0-dpi0)
	yp = np.ones(7)*(pi0+dpi0)
	plt.fill_between(x,ym,yp,facecolor='b',alpha=.3)
	
	pis = np.array(pis)
	plt.subplot(224)
	Nbins=30
	plt.hist(pis, bins=Nbins)  

	plt.axvline(x=pi0,color='b',linewidth=1)
	plt.axvline(x=pi0+dpi0,color='b',linewidth=1,linestyle='dashed')
	plt.axvline(x=pi0-dpi0,color='b',linewidth=1,linestyle='dashed')


plt.savefig('./pi_1pcnt_final.pdf',
				bbox_inches='tight', 
				transparent=True)
plt.show()
