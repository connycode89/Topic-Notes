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
from pgmpy.models import BayesianModel
model = BayesianModel()