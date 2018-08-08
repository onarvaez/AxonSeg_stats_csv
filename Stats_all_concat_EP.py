#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:45:16 2018

@author: onarvaez
"""
import pandas as pd
from scipy import stats 
stats_all_a = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/stats_image_all.csv')

avf_for_cat_a = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/avf.csv')
mvf_for_cat_a = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/mvf.csv')

avf_for_cat_good_a = avf_for_cat_a.drop('Unnamed: 0', axis=1)
mvf_for_cat_good_a = mvf_for_cat_a.drop('Unnamed: 0', axis=1)



Total_axon_a = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/total_axon_cat.csv')
total_axon_mean_a = stats.tmean(Total_axon_a.total_axon)
mean_total_a=pd.DataFrame([total_axon_mean_a])
mean_total_axon_renamed_a=mean_total_a.rename(index=str, columns={0: "Total_axon_mean"})
mean_total_axon_renamed_a.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/Total_axon_mean.csv')
Mean_axon_count_a=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/Total_axon_mean.csv')
Mean_axon_count_good_a=Mean_axon_count_a.drop('Unnamed: 0', axis=1)


total_axon_std_a = stats.tstd(Total_axon_a.total_axon)
std_total_a=pd.DataFrame([total_axon_std_a])
std_total_axon_renamed_a=std_total_a.rename(index=str, columns={0: "Total_axon_std"})
std_total_axon_renamed_a.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/Total_axon_std.csv')
Std_axon_count_a=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/Total_axon_std.csv')
Std_axon_count_good_a=Std_axon_count_a.drop('Unnamed: 0', axis=1)





frames_a=[stats_all_a, avf_for_cat_good_a, mvf_for_cat_good_a, Mean_axon_count_good_a, Std_axon_count_good_a]
result_a =pd.concat(frames_a, axis=1)

print(result_a)
result_a.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/left_damaged/analisis/stats_all_concat_EP.csv')

#ANOTHER NERVE

stats_all_b = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/stats_image_all.csv')

avf_for_cat_b = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/avf.csv')
mvf_for_cat_b = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/mvf.csv')

avf_for_cat_good_b = avf_for_cat_b.drop('Unnamed: 0', axis=1)
mvf_for_cat_good_b = mvf_for_cat_b.drop('Unnamed: 0', axis=1)


Total_axon_b = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/total_axon_cat.csv')
total_axon_mean_b = stats.tmean(Total_axon_b.total_axon)
mean_total_b=pd.DataFrame([total_axon_mean_b])
mean_total_axon_renamed_b=mean_total_b.rename(index=str, columns={0: "Total_axon_mean"})
mean_total_axon_renamed_b.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/Total_axon_mean.csv')
Mean_axon_count_b=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/Total_axon_mean.csv')
Mean_axon_count_good_b=Mean_axon_count_b.drop('Unnamed: 0', axis=1)


total_axon_std_b = stats.tstd(Total_axon_b.total_axon)
std_total_b=pd.DataFrame([total_axon_std_b])
std_total_axon_renamed_b=std_total_b.rename(index=str, columns={0: "Total_axon_std"})
std_total_axon_renamed_b.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/Total_axon_std.csv')
Std_axon_count_b=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/Total_axon_std.csv')
Std_axon_count_good_b=Std_axon_count_b.drop('Unnamed: 0', axis=1)


frames_b=[stats_all_b, avf_for_cat_good_b, mvf_for_cat_good_b, Mean_axon_count_good_b, Std_axon_count_good_b]
result_b =pd.concat(frames_b, axis=1)

print(result_b)
result_b.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq01/right_intact/analisis/stats_all_concat_EP.csv')