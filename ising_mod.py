import matplotlib.pyplot as plt
import numpy as np 
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

"""
"""

"first, define some basic functions"
pi= np.pi
def sqrt(x): return np.sqrt(x)
def exp(x): return np.exp(x)

def rotate_vec(vec0):
	"""
	this piece of code rotates an array (vec0)
	by one to the left
	"""
	N=len(vec0)
	tmp = np.zeros(N)
	
	tmp[0:N-1]=vec0[1:N]                                                   
	tmp[N-1]=vec0[0]
	
	return tmp
	
	
def Eising(St,a,b,c):
	"rotate the spins by one"
	Stp1 = rotate_vec(St)
	"rotate the spins by two"
	Stp2 = rotate_vec(Stp1)
	
	"nearest neighbors"
	dEa = a * sum(St * Stp1)
	"next-to-nearest neighbors"
	dEb = b * sum(St * Stp2)
	"background field"
	dEc = c * sum(St)
	
	return dEa + dEb + dEc
	
def ising_lists(N):
	"""
	if we N possible spins, 
	we have 2^N possible states
	
	we will put these into lists,
	starting with a single spin that is
	either up or down
	"""
	TOT=[[1],[-1]]
	
	for n in range(N-1):
		
		Nt = len(TOT)


		for j0 in range(Nt):


			state1 = TOT[j0][:]
			state2 = TOT[j0][:]

			"we add 1 to the first one"
			state1.append(1)
			"we add -1 to the first one"
			state2.append(-1)

			"here we replace the previous value of TOT[j0] with state1"
			TOT[j0]=state1
			"here we add state2 to the end of TOT"
			TOT.append(state2)
			
		
	return TOT
	
debug='y'
if debug == 'y':
	"""
	here we test that we are recovering the expected
	number of states for N=2,3,4
	"""
	print("")
	print("###########################")
	N=2
	states = ising_lists(N)
	print("N = ", N)
	print("number of states = ", len(states))
	print("expected number of states = ", pow(2,N))
	for state0 in states:
		print(state0)

	print("")
	print("###########################")
	N=3
	states = ising_lists(N)
	print("N = ", N)
	print("number of states = ", len(states))
	print("expected number of states = ", pow(2,N))
	for state0 in states:
		print(state0)
		
	print("")
	print("###########################")
	N=4
	states = ising_lists(N)
	print("N = ", N)
	print("number of states = ", len(states))
	print("expected number of states = ", pow(2,N))
	for state0 in states:
		print(state0)

	
"""
this code evaluate the energies of all the possible 
spin states, and then sorts them from smallest value to biggest.
"""
def ising_sort(N):
	
	TOT = ising_lists(N)
	
	if print_opt=='y':
		print("")
		print("############################################")
		print("total number of elements = ",len(TOT))		
		print("expected number is = ", pow(2,N))		
	
	Es = []
	for tot in TOT:
		St = np.array(tot)
		E0 = Eising(St,a,b,c)
		if E0 not in Es:
			Es.append(E0)
		
	Es_sorted = np.sort(Es)
	
	if det_opt=='tot':
		for E0 in Es_sorted:
			print("E0",E0)
			Ndeg=0
			for tot in TOT:
				St = np.array(tot)
				Es = Eising(St,a,b,c)
				if Es == E0:
					Ndeg+=1
			print("degeneracy = ",Ndeg)
			
	if det_opt=='gs':
		E0 = Es_sorted[0]
		if print_opt=='y':
			print("ground state energy = ",E0)
		Ndeg=0
		for tot in TOT:
			St = np.array(tot)
			Es = Eising(St,a,b,c)
			if Es == E0:
				if print_opt=='y':
					print(tot)
				Ndeg+=1
		if print_opt=='y':
			print("degeneracy for the ground state = ",Ndeg)
			print("############################################")
			print("")
		return Es_sorted

"""
here we use the code above to consider different possible scenarios
"""
examples3to6 = 'n'
if examples3to6 =='y':
	det_opt='gs'
	print_opt = 'y'

	a,b,c = 5,1,.01
	ising_sort(3)

	a,b,c = -5,1,.0
	ising_sort(10)


	a,b,c = -5,1,.01
	ising_sort(10)

	a,b,c = 15,-.2,.02
	ising_sort(15)


plot_example='y'

if plot_example=='y':
	print_opt = 'n'

	a,b,c = 1,.1,0

	cs= - np.arange(-1,2.5,.001)
	E0s=[]
	N=10
	
	"the assumed ground state is for c=0"
	St0=[]
	for j0 in range(N):
		St0.append(pow(-1,j0))


	"the assumed ground state is for c=infty"
	Stinfty=[]
	for j0 in range(N):
		Stinfty.append(1)

	print("guess for gs =", St0)
	Egs_vec=[]
	E0_vec=[]
	Einfty_vec=[]
	for c in cs:
		print("a,b,c",a,b,c)
		" ground state energy of the system"
		Egs = ising_sort(N)[0]
		Egs_vec.append(Egs)

		"energy for St0"
		E0 = Eising(St0,a,b,c)
		E0_vec.append(E0)

		"energy for Stinfty"
		Einfty = Eising(Stinfty,a,b,c)
		Einfty_vec.append(Einfty)
	
	plt.plot(cs,np.array(Egs_vec),color='k')
	plt.plot(cs,np.array(E0_vec),color='r')
	plt.plot(cs,np.array(Einfty_vec),color='g')
		
		
	#plt.ylim(-20,-8)
