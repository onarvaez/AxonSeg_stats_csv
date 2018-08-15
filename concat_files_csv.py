#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on 2018

@author: onarvaez
"""
import pandas as pd 
#Concatenar area axonal correspondiente a axon
axon_pixel_1 = pd.read_csv('/metrics/axon_pixel_area.csv')
axon_pixel_2 = pd.read_csv('/metrics/axon_pixel_area.csv')
axon_pixel_3 = pd.read_csv('/metrics/axon_pixel_area.csv')
    
axon_pixel_cat = pd.concat([axon_pixel_1,axon_pixel_2,axon_pixel_3])

axon_pixel_cat.to_csv('/analisis/axon_pixel_cat.csv')

#Concatenar area axonal correspondiente a mielina
myelin_pixel_1 = pd.read_csv('/metrics/myelin_pixel_area.csv')
myelin_pixel_2 = pd.read_csv('/metrics/myelin_pixel_area.csv')
myelin_pixel_3 = pd.read_csv('/metrics/myelin_pixel_area.csv')

myelin_pixel_cat = pd.concat([myelin_pixel_1,myelin_pixel_2,myelin_pixel_3])

myelin_pixel_cat.to_csv('/analisis/myelin_pixel_cat.csv')

#Concatenar número axonal
total_axon_1 = pd.read_csv('/metrics/total_axon.csv')
total_axon_2 = pd.read_csv('/metrics/total_axon.csv')
total_axon_3 = pd.read_csv('/metrics/total_axon.csv')
    
total_axon_cat = pd.concat([total_axon_1,total_axon_2,total_axon_3])

total_axon_cat.to_csv('/analisis/total_axon_cat.csv')
    

#ANOTHER NERVE

#Concatenar area axonal correspondiente a axon
axon_pixel_1 = pd.read_csv('/metrics/axon_pixel_area.csv')
axon_pixel_2 = pd.read_csv('/metrics/axon_pixel_area.csv')
axon_pixel_3 = pd.read_csv('/metrics/axon_pixel_area.csv')
    
axon_pixel_cat = pd.concat([axon_pixel_1,axon_pixel_2,axon_pixel_3])

axon_pixel_cat.to_csv('/analisis/axon_pixel_cat.csv')
#Concatenar area axonal correspondiente a mielina
myelin_pixel_1 = pd.read_csv('/metrics/myelin_pixel_area.csv')
myelin_pixel_2 = pd.read_csv('/metrics/myelin_pixel_area.csv')
myelin_pixel_3 = pd.read_csv('/metrics/myelin_pixel_area.csv')

myelin_pixel_cat = pd.concat([myelin_pixel_1,myelin_pixel_2,myelin_pixel_3])

myelin_pixel_cat.to_csv('/analisis/myelin_pixel_cat.csv')


#Concatenar número axonal
total_axon_1 = pd.read_csv('/metrics/total_axon.csv')
total_axon_2 = pd.read_csv('/metrics/total_axon.csv')
total_axon_3 = pd.read_csv('/metrics/total_axon.csv')
    
total_axon_cat = pd.concat([total_axon_1,total_axon_2,total_axon_3])

total_axon_cat.to_csv('/analisis/total_axon_cat.csv')
    
