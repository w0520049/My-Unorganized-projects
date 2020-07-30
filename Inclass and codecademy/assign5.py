# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:24:34 2019

@author: MM
"""

#Test
# HR = [83,92,100,95,92,74,119,94,118,79,73,65,106,117,83,89,109,68,80,94,88,116,68,67,75,90,78,94,85 ]
# RR = [10,11,11,13,12,24,13,14,14,22,22,15,15,16,22,18,22,24,18,22,15,14,13,20,11,21,24,17,16]

HR = []
RR = []

#Import modules
import matplotlib.pyplot as plt



#Function that calcs max & mean
def analyzeHRAndRR(HR, RR):

    #mean of HH & RR
    meanHR = sum(HR)/len(HR)
    meanRR = sum(RR)/len(RR)


    maxHR = 0
    maxRR = 0

    #Find max HR & RR
    for rate in HR:
        if maxHR < rate:
            maxHR = rate
        elif maxHR >= rate:
            continue
    
    for rate in RR:
        if maxRR < rate:
            maxRR = rate
        elif maxRR >= rate:
            continue
       
    return (maxHR, maxRR, meanHR, meanRR) 
    

 
(maxHR, maxRR, meanHR, meanRR) = analyzeHRAndRR(HR, RR)
 
print(maxHR, maxRR, meanHR, meanRR)



plt.plot(range(0,len(HR)), HR, label = 'Heart Rate')
plt.plot(range(0,len(RR)), RR, label = 'Resting Rate')
plt.legend()
plt.show()
