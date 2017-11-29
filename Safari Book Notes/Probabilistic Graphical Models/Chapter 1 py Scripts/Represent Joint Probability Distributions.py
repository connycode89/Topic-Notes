# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:20:35 2017

@author: cdonovan
"""

# joint distribution over the outcomes of tossing 2 fair coins
from pgmpy.factors.discrete import JointProbabilityDistribution as Joint

# first arg -> names of RVs
# second arg -> number of states of each RV
# third arg -> list of probability values (assuming 1st variable changes state the slowest)
distribution = Joint(['coin1','coin2'],[2,2],[0.25,0.25,0.25,0.25])
print distribution

# Independence Queries
distribution.check_independence(['coin1'],['coin2']) # are coin1 and coin2 independent RVs?