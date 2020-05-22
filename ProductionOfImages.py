import numpy as np
import matplotlib.pyplot as plt

# This file will read the file that the earlier one created and then 
# try and save the images

# First, read the file and save the array
primes = np.fromfile('PrimesDataFile.py',dtype=int)

# Now, visualise them in plots and save them. 
# 1 million is 10^6, so we'll need around 60 files to save our data. 
# Definitely less than 100. 
counter = 1 # File counter
baseNumber = 1 # Limit counter
while True : # We'll break this loop automatically later
    for i in np.arange(start=baseNumber,stop = 10*(baseNumber), step=baseNumber): 
        # check in terms of the numbers - this loop will ALWAYS have 10 iterations.
        selectedRange = primes[:i] # How many primes we want for this file
        xData = [prime*np.cos(prime) for prime in selectedRange] # calculates x- coordinate of each prime
        yData = [prime*np.sin(prime) for prime in selectedRange] # calculates y- coordinate of each prime
        filename = ''.join([str(counter).zfill(4),'.png'])  # filename string

        #save the file!
        plt.figure(figsize=(12,12)) # Uniform size for each figure
        plt.plot(xData,yData,'ro',markersize='2') # I prefer red circles, you choose your style to be different if you want.
        plt.title('A Galaxy of Primes')
        plt.savefig(''.join(['Plots',filename]), format='png', dpi=600)
        plt.close() # Close figure before exiting!
        print('Done with: ',filename, flush=True, end='\r')
        counter += 1
        if i == 9*baseNumber:
            # last iteration - increment baseNumber!
            baseNumber *= 10





