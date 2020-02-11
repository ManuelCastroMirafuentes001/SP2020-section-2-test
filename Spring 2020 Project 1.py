"""
EE 381 Spring 2020 Project 1
Name: Manuel Castro-Mirafuentes
I.D. #: 016418712
Start Dtae: 01-27-2020
End Date: 
Discription: This is the code for a pseudorandom number generator, RNG.
It will output a uniform distribution of numbers in the set [0,1).
"""
# -----------------------------------------------------------------------------
# Constants
N = 10000 #The norm.
A = 4857 #The adder.
M = 8601 #The multiplier.
# -----------------------------------------------------------------------------
#Get seed from clock.
import time
S = time.time_ns - time.process_time_ns()
#print(t)
#------------------------------------------------------------------------------
#S = 0 #This will be removed from the final program.

for i in range(100):
    S = (M * S + A) % N #RNG Formula
    #print(S)\
    r = S / N #Numebrs in [0,1)
    #print(format(r, '.4f'))
    die = math.floor(6 * r + 1)
    print(die)
