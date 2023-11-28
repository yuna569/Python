# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:45:14 2023

@author: yjeon
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#pd.read_csv('경기도_안성시_어린이보호구역_20230321.csv')

all_list=[]

all_list.append({'date':'2022-10-08', 'dayofweek':'sat'})
all_list.append({'date':'2022-10-09', 'dayofweek':'sun'})
all_list.append({'date':'2022-10-10', 'dayofweek':'mon'})

print(pd.DataFrame(all_list))