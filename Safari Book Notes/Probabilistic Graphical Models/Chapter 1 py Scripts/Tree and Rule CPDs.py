# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:28:10 2017

@author: cdonovan
"""

from pgmpy.factors.discrete.CPD import TreeCPD
from pgmpy.factors.discrete import DiscreteFactor
tree_cpd = TreeCPD([('B', Factor(['A'], [2], [0.8, 0.2]), '0'),
                    ('B', 'C', '1'),
                    ('C', Factor(['A'], [2], [0.1, 0.9]), '0'),
                    ('C', 'D', '1'),
                    ('D', Factor(['A'], [2], [0.9, 0.1]), '0'),
                    ('D', Factor(['A'], [2], [0.4, 0.6]), '1')])

from pgmpy.factors.discrete.CPD import RuleCPD
rule = RuleCPD('A', {('A_0', 'B_0'): 0.8,
                     ('A_1', 'B_0'): 0.2,
                     ('A_0', 'B_1', 'C_0'): 0.4,
                     ('A_1', 'B_1', 'C_0'): 0.6,
                     ('A_0', 'B_1', 'C_1'): 0.9,
                     ('A_1', 'B_1', 'C_1'): 0.1})