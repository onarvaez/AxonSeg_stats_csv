#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:49:53 2018

@author: onarvaez
"""
import pandas as pd 

axonlist_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/1/img_t1_z1_c1_Segmentation/misc/axonlist_image.csv')
axonlist_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/2/img_t1_z1_c1_Segmentation/misc/axonlist_image.csv')
axonlist_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/3/img_t1_z1_c1_Segmentation/misc/axonlist_image.csv')

axonlist_cat = pd.concat([axonlist_1,axonlist_2,axonlist_3])

axonlist_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/axonlist_cat.csv')

axon_pixel_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/1/img_t1_z1_c1_Segmentation/misc/axon_pixel_area.csv')
axon_pixel_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/2/img_t1_z1_c1_Segmentation/misc/axon_pixel_area.csv')
axon_pixel_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/3/img_t1_z1_c1_Segmentation/misc/axon_pixel_area.csv')
    
axon_pixel_cat = pd.concat([axon_pixel_1,axon_pixel_2,axon_pixel_3])

axon_pixel_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/axon_pixel_cat.csv')

myelin_pixel_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/1/img_t1_z1_c1_Segmentation/misc/myelin_pixel_area.csv')
myelin_pixel_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/2/img_t1_z1_c1_Segmentation/misc/myelin_pixel_area.csv')
myelin_pixel_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/3/img_t1_z1_c1_Segmentation/misc/myelin_pixel_area.csv')

myelin_pixel_cat = pd.concat([myelin_pixel_1,myelin_pixel_2,myelin_pixel_3])

myelin_pixel_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/myelin_pixel_cat.csv')

stats_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/1/img_t1_z1_c1_Segmentation/misc/stats_image.csv')
stats_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/2/img_t1_z1_c1_Segmentation/misc/stats_image.csv')
stats_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/3/img_t1_z1_c1_Segmentation/misc/stats_image.csv')
    
stats_cat = pd.concat([stats_1,stats_2,stats_3])
    
stats_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/stats_cat.csv')

total_axon_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/1/img_t1_z1_c1_Segmentation/misc/total_axon.csv')
total_axon_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/2/img_t1_z1_c1_Segmentation/misc/total_axon.csv')
total_axon_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/3/img_t1_z1_c1_Segmentation/misc/total_axon.csv')
    
total_axon_cat = pd.concat([total_axon_1,total_axon_2,total_axon_3])

total_axon_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/total_axon_cat.csv')
    

#ANOTHER NERVE



axonlist_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/1/img_t1_z1_c1_Segmentation/misc/axonlist_image.csv')
axonlist_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/2/img_t1_z1_c1_Segmentation/misc/axonlist_image.csv')
axonlist_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/3/img_t1_z1_c1_Segmentation/misc/axonlist_image.csv')

axonlist_cat = pd.concat([axonlist_1,axonlist_2,axonlist_3])

axonlist_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/axonlist_cat.csv')

axon_pixel_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/1/img_t1_z1_c1_Segmentation/misc/axon_pixel_area.csv')
axon_pixel_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/2/img_t1_z1_c1_Segmentation/misc/axon_pixel_area.csv')
axon_pixel_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/3/img_t1_z1_c1_Segmentation/misc/axon_pixel_area.csv')
    
axon_pixel_cat = pd.concat([axon_pixel_1,axon_pixel_2,axon_pixel_3])

axon_pixel_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/axon_pixel_cat.csv')

myelin_pixel_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/1/img_t1_z1_c1_Segmentation/misc/myelin_pixel_area.csv')
myelin_pixel_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/2/img_t1_z1_c1_Segmentation/misc/myelin_pixel_area.csv')
myelin_pixel_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/3/img_t1_z1_c1_Segmentation/misc/myelin_pixel_area.csv')

myelin_pixel_cat = pd.concat([myelin_pixel_1,myelin_pixel_2,myelin_pixel_3])

myelin_pixel_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/myelin_pixel_cat.csv')

stats_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/1/img_t1_z1_c1_Segmentation/misc/stats_image.csv')
stats_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/2/img_t1_z1_c1_Segmentation/misc/stats_image.csv')
stats_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/3/img_t1_z1_c1_Segmentation/misc/stats_image.csv')
    
stats_cat = pd.concat([stats_1,stats_2,stats_3])
    
stats_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/stats_cat.csv')

total_axon_1 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/1/img_t1_z1_c1_Segmentation/misc/total_axon.csv')
total_axon_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/2/img_t1_z1_c1_Segmentation/misc/total_axon.csv')
total_axon_3 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/3/img_t1_z1_c1_Segmentation/misc/total_axon.csv')
    
total_axon_cat = pd.concat([total_axon_1,total_axon_2,total_axon_3])

total_axon_cat.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/left_damaged/analisis/total_axon_cat.csv')
    