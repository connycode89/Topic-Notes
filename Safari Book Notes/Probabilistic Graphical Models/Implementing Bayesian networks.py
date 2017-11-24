# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:20:35 2017

@author: cdonovan
"""

# Student getting late for school
# Each RV is discrete with 2 states (yes and no)

from IPython.display import Image
Image('https://www.safaribooksonline.com/library/view/mastering-probabilistic-graphical/9781784394684/graphics/B04016_01_64.jpg')

# Bayesian Model Representation
# Initialize empty model
# [Conda install scipy if this import doesn't work]
from pgmpy.models import BayesianModel
model = BayesianModel()

model.add_nodes_from(['rain','traffic_jam'])
model.add_edge('rain','traffic_jam')

model.add_edge('accident','traffic_jam') # these nodes are automatically added to model (despite accident not being specified)
model.nodes()
model.edges()

# Define some tabular CPDs
from pgmpy.factors.discrete import TabularCPD
cpd_rain = TabularCPD('rain',2,[[0.4],[0.6]])
cpd_accident = TabularCPD('accident',2,[[0.2],[0.8]])
cpd_traffic_jam = TabularCPD('traffic_jam', 2,[[0.9, 0.6, 0.7, 0.1],[0.1, 0.4, 0.3, 0.9]],
                             evidence=['rain', 'accident'],evidence_card=[2, 2])
model.add_cpds(cpd_rain, cpd_accident, cpd_traffic_jam)
model.get_cpds()

model.add_node('long_queues')
model.add_edge('traffic_jam','long_queues')
cpd_long_queues = TabularCPD('long_queues',2,[[0.9,0.2],[0.1,0.8]],
                             evidence=['traffic_jam'],evidence_card=[2])
model.add_cpds(cpd_long_queues)
model.add_nodes_from(['getting_up_late','late_for_school'])
model.add_edges_from([('getting_up_late','late_for_school'),('traffic_jam','late_for_school')])
cpd_getting_up_late = TabularCPD('getting_up_late',2,[[0.6],[0.4]])
cpd_late_for_school = TabularCPD('late_for_school',2,[[0.9,0.45,0.8,0.1],[0.1,0.55,0.2,0.9]],
                                 evidence=['getting_up_late','traffic_jam'],evidence_card=[2,2])
model.add_cpds(cpd_getting_up_late, cpd_late_for_school)

model.get_cpds()

# check consistency of model
model.check_model()

# we can remove CPDs
model.remove_cpds('late_for_school')
model.get_cpds()