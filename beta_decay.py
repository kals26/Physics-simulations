import matplotlib.pyplot as plt
import numpy as np 

pi= np.pi
def sqrt(x): return np.sqrt(x)
def exp(x): return np.exp(x)

def qq(Ei, mB, mC ):
	Dms = pow(mB,2) - pow(mC,2)
	Sms = pow(mB,2) + pow(mC,2)
	
	num = pow(Ei,4) + pow(Dms,2) - 2 * pow(Ei,2) * Sms
	
	return num / (4.0 * pow(Ei,2))

def missing_mass(mA, mB, pB ):
	tmp = pow(mA,2) + pow(mB,2)
	tmp = tmp - 2* mA * sqrt(pow(mB,2) + pow(pB,2))
	return sqrt(tmp)
	
plt.figure(figsize=(9,10))

mA = 2
mB = 1
mD = .1

regen = 'n'
if regen =='y':
	Npoints = 1000
	mC, dmC = .2,.01
	mCs =  np.random.normal(mC,dmC, Npoints)
	print("mCfs",np.mean(mCs),np.std(mCs,ddof=1))
	Nbins=50
	hack ='n'
	if hack =="y":
		plt.subplot(311)
		plt.ylabel('mC',size=20)

		plt.hist(mCs, bins=50)  

		plt.axvline(x=mC,color='b',linewidth=1)
		plt.axvline(x=mC+dmC,color='b',linewidth=1,linestyle='dashed')
		plt.axvline(x=mC-dmC,color='b',linewidth=1,linestyle='dashed')

		plt.axvline(x=np.mean(mCs),color='k',linewidth=1)
		plt.axvline(x=np.mean(mCs)+np.std(mCs,ddof=1),color='k',linewidth=1,linestyle='dashed')
		plt.axvline(x=np.mean(mCs)-np.std(mCs,ddof=1),color='k',linewidth=1,linestyle='dashed')

	
	# Here I solve the inverse problem. 
	# Give then the masses, what is the momentum.
	
	if hack =="y":
		plt.subplot(312)
	plt.subplot(211)
	qqs = qq(mA, mB, mCs )
	qs = sqrt(qqs)
	plt.hist(sqrt(qqs), bins=50)  
	plt.ylabel('q',size=20)

	
	EB = sqrt(qqs + pow(mB,2))
	EC = sqrt(qqs + pow(mCs,2))
	print("EB + EC = ",np.mean(EB + EC))
	print("EB + EC - mA= ",np.mean(EB + EC)- mA)

	filename = 'pBs_2body_decay.txt'
	np.savetxt(filename,qs)



q0s = np.loadtxt('pBs_2body_decay.txt')
plt.subplot(211)
print("q0s +/- sigm_q0s = ",np.mean(q0s), '  +/- ',np.std(q0s,ddof=1))
plt.hist(q0s, bins=50)  
plt.axvline(x=np.mean(q0s),color='k',linewidth=1)
plt.axvline(x=np.mean(q0s)+np.std(q0s,ddof=1),color='k',linewidth=1,linestyle='dashed')
plt.axvline(x=np.mean(q0s)-np.std(q0s,ddof=1),color='k',linewidth=1,linestyle='dashed')
plt.xlabel('momentum',size=20)


plt.subplot(212)
mCfs = missing_mass(mA, mB, q0s )
print("mC +/- sigm_mC = ",np.mean(mCfs), '  +/- ',np.std(mCfs,ddof=1))
plt.hist(mCfs, bins=50)  
plt.axvline(x=np.mean(mCfs),color='k',linewidth=1)
plt.axvline(x=np.mean(mCfs)+np.std(mCfs,ddof=1),color='k',linewidth=1,linestyle='dashed')
plt.axvline(x=np.mean(mCfs)-np.std(mCfs,ddof=1),color='k',linewidth=1,linestyle='dashed')

plt.xlabel('recons. mC',size=20)

text_file = open("pBs_2body_decay_result.txt","w")
text_file.write("mCfs = " + str(np.mean(mCfs)) +"  +/-   " +str(np.std(mCfs,ddof=1)))
text_file.close()

plt.savefig('examplePlot.png',
				bbox_inches='tight', 
				transparent=True)

plt.show()


