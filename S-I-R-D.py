# Simulation
import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
import time
# define a function for coupled DE's
def f(x1,t1):
    s1= x1[0]
    i1=x1[1]
    r1=x1[2]
    d1=x1[3]
    N= s1+i1+r1+d1
    mu1= 0.0021 # Death rates due to the infection
    alpha1=0.0760 # Spread rates of infection
    beta1=0.02514 # Recovery coefficient
    N= 1380000000 # observation set 
    ds1dt= -alpha1*s1*i1/N 
    di1dt= -beta1*i1+ alpha1*s1*i1/N- mu1*i1
    dr1dt= beta1*i1
    dd1dt= mu1*i1
    return[ds1dt,di1dt,dr1dt,dd1dt]

# start counting time
begin = time.time()

# intialise
i10=89198.174
r10=34269.324
d10=3251.15
N= 1380000000
s10= N-(r10+i10+d10)

# initial conditions to solve the DEs
x10=[s10,i10,r10,d10]
# define time starting from XX day, end it on YY day, basically to evaluate coupled DEs
t1=np.linspace(112,1000,1000)
# solver.
x1= odeint(f,x10,t1)
# solutions
s1=x1[:,0]
i1=x1[:,1]
r1=x1[:,2]
d1=x1[:,3]
# This function is used to solve the DE's and generate the data for each leg.
'''for t in range(32,500):
    b= (x[:,1])
    b= np.array(b)
# (Addition to find peak number within the data set)
    def largest(arr,n): 
        max = arr[0] 
        for i in range(1, n): 
          if arr[i] > max: 
            max = arr[i] 
        return max
  
# Driver Code 
arr = b
n = len(b) 
Ans = largest(b,n) 
print ("Largest in given array is",Ans) '''

# import the data table from excel. This data sheet is from crowd sourcing.
import xlrd
import numpy as np
import matplotlib.pyplot as plt
file_location = "D:\PythonPrograms\data.xlsx" # change the file directory when you are working in your system. 
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

a = [first_sheet.cell_value(i, 0) for i in range(first_sheet.nrows)] # 1st column, represents cumulative t count.
b = [first_sheet.cell_value(i, 1) for i in range(first_sheet.nrows)] # 2nd column, represents cumulative i count.
c = [first_sheet.cell_value(i, 2) for i in range(first_sheet.nrows)]  # 3rd column, represents cumulative r count.
e = [first_sheet.cell_value(i, 3) for i in range(first_sheet.nrows)]  # 4th column, represents cumulative d count.
# Now, to plotting, stage 1 of data points
plt.errorbar(a,b,fmt='m.', markersize=3.5) # I data
plt.errorbar(a,c,fmt='y.', markersize=3.5) # R data
plt.errorbar(a,e,fmt='r.', markersize=3.5) # D data

# import the data table from excel. This data is I, R, D values obtained by operating alpha, beta and mu for each leg.
file_location = "D:\PythonPrograms\calculated.xlsx" # change the file directory when you are working in your system. 
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

a1 = [first_sheet.cell_value(i, 0) for i in range(first_sheet.nrows)] # 1st column, represents cumulative t count.
b1 = [first_sheet.cell_value(i, 1) for i in range(first_sheet.nrows)] # 2nd column, represents cumulative i count.
c1 = [first_sheet.cell_value(i, 2) for i in range(first_sheet.nrows)]  # 3rd column, represents cumulative r count.
e1 = [first_sheet.cell_value(i, 3) for i in range(first_sheet.nrows)]  # 4th column, represents cumulative d count.
# Now, to plotting, stage 2 of calculated data points
plt.semilogy(a1,b1,'b') # I data
plt.semilogy(a1,c1,'g') # R data
plt.semilogy(a1,e1,'k') # D data

# Now, to plotting, stage 3, the plotting of function itself:With a set of values of alpha, beta and mu.
plt.semilogy(t1,i1,'m') # plots i 
plt.semilogy(t1,r1,'g') # plots r 
plt.semilogy(t1,d1,'b') # plots d 
plt.semilogy(t1,s1,'c--') # plots s

plt.legend()
''' # This one is dashed lines of plots that represents all legs of period of ten days
q= np.linspace(0,N*10)
p1= 0*(q)+42
p2= 0*(q)+52
p3= 0*q+62
p4= 0*q+72
p5=0*q+82
p6=0*q+92
p7= 0*q+102
p8= 0*q+112
plt.plot(p1,q,'c--')
plt.plot(p2,q,'c--')
plt.plot(p3,q,'c--')
plt.plot(p4,q,'c--')
plt.plot(p5,q,'c--')
plt.plot(p6,q,'c--')
plt.plot(p7,q,'c--')
plt.plot(p8,q,'c--')'''

plt.xlabel()
plt.ylabel()
plt.title()
plt.xlim()
plt.ylim()
plt.show()

# note the execution time
end = time.time()-begin
print('total execution time took {0} s.'.format(end))

# end of basic structure of the program. 





















