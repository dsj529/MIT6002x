# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:33:38 2016

@author: dsj
"""

import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    growthProb = 1.0 - CURRENTRABBITPOP * 1.0 / MAXRABBITPOP
    newRabbits = 0
    for i in range(CURRENTRABBITPOP):
        if random.random() < growthProb:
#            print "new rabbit!"
            newRabbits += 1
    newPop = CURRENTRABBITPOP + newRabbits
    if newPop > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP
    else:
        CURRENTRABBITPOP=newPop
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    newFoxes = 0
    for i in range(CURRENTFOXPOP):
        if random.random() < (CURRENTRABBITPOP/float(MAXRABBITPOP)) \
           and CURRENTRABBITPOP > 10:  # eat a rabbit
#            print "munch!"
            CURRENTRABBITPOP -= 1
            if random.random() < (1.0/3): # new fox?
#                print "new fox!"
                newFoxes += 1
        else: # didn't
            if random.random() < 0.1 and CURRENTFOXPOP > 10:
#                print "RIP fox"
                newFoxes -= 1
    CURRENTFOXPOP += newFoxes
    
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations=[]
    fox_populations=[]
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
#        print [rabbit_populations, fox_populations]
        print [CURRENTRABBITPOP, CURRENTFOXPOP]

runSimulation(200)