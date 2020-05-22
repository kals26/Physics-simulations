import numpy as np 

from datetime import datetime # Measures time of execution

def IsPrime(n):
    # Return True if prime.
    # This function uses the trick that
    # Prime numbers >= 5 can only be of the form 6k+1 or 6k-1.
    if n ==2:
        return True
    if n ==3 :
        return True
    if n%2 == 0:
        return False
    if n%3 == 0:
        return False
    i = 5
    w = 2

    while i*i <= n:
        if n% i == 0:
            return False
        i +=w
        w = 6-w
    return True

# Now, we simply generate a list of prime numbers 
# Let's generate a list of 1 million primes. That should be enought ot start with.
primes = [] # empty list
counter = 2 # start from the first prime number.
while True:
    # create infinite loop until the list is as long as we need it to be.
    # StartTime = datetime.now()
    if IsPrime(counter):
        primes.append(counter)
        print(len(primes),': \t Added',counter) # At the loss of a few microseconds, this will show the latest added prime
    counter += 1    # Check the next number
    if len(primes) == 10000 : 
        break # Yay! Generated 1 million primes!
    # EndTime = datetime.now()
# print('Execution Time: ' ,datetime.timedelta(EndTime - StartTime))

# Now, save them into a file. Easiest is the numpy save
np.array(primes).tofile('PrimesDataFile.py')

# Now, to plotting!
# We'll do this in a different file, after reading the data from this file. 
# For now, we'll just see how long this took.


