 #Simple quantum walk
 #Define measurement, aka, probabilties. Later, define what state post measurement looks like.
 #Define the hadamard transformation you wish to do (45'). Define shift operator.
 #Initialise all the values for the variables mentioned before
 #Run for some steps
 #Plot your graph
import math
import matplotlib.pylab as plt 


def probabilities(posn):
    return [sum([abs(probamp) ** 2 for probamp in ofstep]) for ofstep in posn]
#Returns the probabilities for each place where step is taken

def postmeasurement(posn):
   N = math.sqrt(sum(probabilities(posn)))
   return [[probamp /N for probamp in ofstep] for ofstep in posn]
#Returns what the state collapses into post measurement

def coin(posn):
    return postmeasurement([[x[0] + x[1], x[0] - x[1]] for x in posn])
#Coin operator fixed at 45.

def shift(pos):
    newposn = [[0, 0] for i in range(len(pos))]
    for j in range(1, len(posn)-1):
        newposn[j + 1][0] += pos[j][0]
        newposn[j - 1][1] += pos[j][1]
    return postmeasurement(newposn)

# Initialise lists.
Nl,Nr = -100, 100 #Taking 0 as mid point and extend -N,N
posn = [[0, 0] for i in range(Nl+1, Nr+1)]
#phi changes initial rotation
phi=math.radians(45)
posn[Nr] = [math.cos(phi), 1j*math.sin(phi)]
#input state

# Run for some steps...
for time in range(Nr):
    posn = shift(coin(posn))
#Output state


#a=math.floor(Nr*math.cos(phi))
#print('a is:\n',a)
# Checking if peak is alright.

#Plot
x=range(Nl+1,Nr+1)
y=probabilities(posn)
plt.plot(x,y,c='m')
plt.title("Probability distribution in a Discrete Time Quantum Walk", loc='center')
plt.xlabel("Position, coin rotation= 45 deg")
plt.ylabel("Probability amplitudes, walker rotation=45 deg")
#plt.axvline(a,0,1,color='r')
#plt.axvline(-1*a,0,1,color='r')
plt.savefig('qw1.png')









