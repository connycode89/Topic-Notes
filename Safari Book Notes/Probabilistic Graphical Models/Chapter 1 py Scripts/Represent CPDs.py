# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:20:35 2017

@author: cdonovan
"""

# joint distribution over the outcomes of tossing 2 fair coins
from pgmpy.factors.discrete import TabularCPD

# first arg -> variable name
# second arg -> variable cardinality = no. of states of RV
# third arg -> probability for each state
quality = TabularCPD(variable='Quality', variable_card=3, values=[[0.3],[0.5],[0.2]])
print quality

quality.variables
quality.cardinality
quality.values

location = TabularCPD(variable='Location', variable_card=2, values=[[0.6],[0.4]])
print location

# If we have conditional variables, need to specify these too and their cardinality
cost = TabularCPD(variable='Cost', variable_card=2,
                  values=[[0.8, 0.6, 0.1, 0.6, 0.6, 0.05], [0.2, 0.4, 0.9, 0.4, 0.4, 0.95]],
                  evidence=['Q','L'], evidence_card=[3,2])
print cost