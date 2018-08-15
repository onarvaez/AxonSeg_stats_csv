#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:05:45 2018

@author: onarvaez
"""

import pandas as pd
from scipy import stats 

stats_all_a = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/stats_per_image.csv')

avf_for_cat_a = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/avf.csv')
mvf_for_cat_a = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/mvf.csv')

avf_for_cat_good_a = avf_for_cat_a.drop('Unnamed: 0', axis=1)
mvf_for_cat_good_a = mvf_for_cat_a.drop('Unnamed: 0', axis=1)

Mean_axon_count_a=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/Total_axon_mean.csv')
Mean_axon_count_good_a=Mean_axon_count_a.drop('Unnamed: 0', axis=1)

Std_axon_count_a=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/Total_axon_std.csv')
Std_axon_count_good_a=Std_axon_count_a.drop('Unnamed: 0', axis=1)

frames_a=[stats_all_a, avf_for_cat_good_a, mvf_for_cat_good_a, Mean_axon_count_good_a, Std_axon_count_good_a]
result_a =pd.concat(frames_a, axis=1)

print(result_a)
result_a.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/stats_per_concat_PI.csv')






#ANOTHER NERVE

stats_all_b = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/intact_b/analisis/stats_per_image.csv')

avf_for_cat_b = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/intact_b/analisis/avf.csv')
mvf_for_cat_b = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/intact_b/analisis/mvf.csv')

avf_for_cat_good_b = avf_for_cat_b.drop('Unnamed: 0', axis=1)
mvf_for_cat_good_b = mvf_for_cat_b.drop('Unnamed: 0', axis=1)

Mean_axon_count_b=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/intact_b/analisis/Total_axon_mean.csv')
Mean_axon_count_good_b=Mean_axon_count_b.drop('Unnamed: 0', axis=1)

Std_axon_count_b=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/intact_b/analisis/Total_axon_std.csv')
Std_axon_count_good_b=Std_axon_count_b.drop('Unnamed: 0', axis=1)

frames_b=[stats_all_b, avf_for_cat_good_b, mvf_for_cat_good_b, Mean_axon_count_good_b, Std_axon_count_good_b]
result_b =pd.concat(frames_b, axis=1)

print(result_b)
result_b.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq04/intact_b/analisis/stats_per_concat_PI.csv')

