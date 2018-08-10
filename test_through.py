#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:22:21 2018

@author: onarvaez
"""

# importing libraries
import os

# defining location of parent folder
BASE_DIRECTORY = '/misc/torrey/onarvaez/prueba'
output_file = open('avf.csv', 'w')
output = {}
file_list = []

# scanning through sub folders
for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
    for f in filenames:
        if 'csv' in str(f):
            e = os.path.join(str(dirpath), str(f))
            file_list.append(e)

for f in file_list:
    print f
    txtfile = open(f, 'r')
    output[f] = []
    for line in txtfile:
        if 'AVF:' in line:
            output[f].append(line)
#        elif 'Format' in line:
#            output[f].append(line)
#        elif 'Resolution' in line:
#            output[f].append(line)
tabs = []
for tab in output:
    tabs.append(tab)


import pandas as pd
x0 = (pd.read_csv((tabs[0])).drop('Unnamed: 0', axis=1))
x1 = (pd.read_csv((tabs[1])).drop('Unnamed: 0', axis=1))
x3 = (pd.read_csv((tabs[2])).drop('Unnamed: 0', axis=1))

avf_concat=pd.concat([x0,x1,x3])
   
