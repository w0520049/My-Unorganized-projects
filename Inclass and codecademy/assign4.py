# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:23:27 2019

@author: Mashrura
"""
#Program meant to detect if HR goes above and RR goes below at the same time

#HR = Heart Rate
# RR stands for Respiration Rate
# HRThreshold is the threshold for HR
# RRThreshold is the threshold for RR

#The specification of the function goes here
def getInstanceCount(HR, RR, HRThreshold, RRThreshold):
    
    #Looks for when both 'HRates' and 'RRates' pass their thresholds and ads the pair in the 'Instances' List
    Instances = [HRates for HRates, RRates in zip(HR, RR) if HRates > HRThreshold and RRates < RRThreshold]


    #Returns the final number of instances
    return len(Instances)

