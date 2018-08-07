#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:45:16 2018

@author: onarvaez
"""
import pandas as pd
import numpy as np
from scipy import stats as sts
stats_all = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/stats_image_all.csv')

avf_for_cat = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/avf.csv')
mvf_for_cat = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/mvf.csv')

avf_for_cat_good = avf_for_cat.drop('Unnamed: 0', axis=1)
mvf_for_cat_good = mvf_for_cat.drop('Unnamed: 0', axis=1)



Total_axon_a = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/total_axon_cat.csv')
total_axon_mean_a = np.mean(Total_axon_a.total_axon)
mean_total_a=pd.DataFrame([total_axon_mean_a])
mean_total_axon_renamed_a=mean_total_a.rename(index=str, columns={0: "Total_axon_mean"})
mean_total_axon_renamed_a.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/Total_axon_mean.csv')
Mean_axon_count_a=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/Total_axon_mean.csv')
Mean_axon_count_good_a=Mean_axon_count_a.drop('Unnamed: 0', axis=1)


total_axon_std_a = sts.tstd(Total_axon_a.total_axon)
std_total_a=pd.DataFrame([total_axon_std_a])
std_total_axon_renamed_a=std_total_a.rename(index=str, columns={0: "Total_axon_std"})
std_total_axon_renamed_a.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/Total_axon_std.csv')
Std_axon_count_a=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/Total_axon_std.csv')
Std_axon_count_good_a=Std_axon_count_a.drop('Unnamed: 0', axis=1)





frames=[stats_all, avf_for_cat_good, mvf_for_cat_good, Mean_axon_count_good_a, Std_axon_count_good_a]
result =pd.concat(frames, axis=1)

print(result)
result.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/right_damaged/analisis/stats_all_concat_EP.csv')

#ANOTHER NERVE

stats_all = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/stats_image_all.csv')

avf_for_cat = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/avf.csv')
mvf_for_cat = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/mvf.csv')

avf_for_cat_good = avf_for_cat.drop('Unnamed: 0', axis=1)
mvf_for_cat_good = mvf_for_cat.drop('Unnamed: 0', axis=1)


Total_axon_b = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/total_axon_cat.csv')
total_axon_mean_b = np.mean(Total_axon_b.total_axon)
mean_total_b=pd.DataFrame([total_axon_mean_a])
mean_total_axon_renamed_b=mean_total_b.rename(index=str, columns={0: "Total_axon_mean"})
mean_total_axon_renamed_b.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/Total_axon_mean.csv')
Mean_axon_count_b=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/Total_axon_mean.csv')
Mean_axon_count_good_b=Mean_axon_count_b.drop('Unnamed: 0', axis=1)


total_axon_std_b = sts.tstd(Total_axon_b.total_axon)
std_total_b=pd.DataFrame([total_axon_std_b])
std_total_axon_renamed_b=std_total_b.rename(index=str, columns={0: "Total_axon_std"})
std_total_axon_renamed_b.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/Total_axon_std.csv')
Std_axon_count_b=pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/Total_axon_std.csv')
Std_axon_count_good_b=Std_axon_count_b.drop('Unnamed: 0', axis=1)


frames_b=[stats_all, avf_for_cat_good, mvf_for_cat_good, Mean_axon_count_good_b, Std_axon_count_good_b]
result_b =pd.concat(frames_b, axis=1)

print(result_b)
result_b.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq03/left_intact/analisis/stats_all_concat_EP.csv')