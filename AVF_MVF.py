#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:54:48 2018

@author: onarvaez
"""

import pandas as pd

Axon_pixel = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/axon_pixel_cat.csv')
Myelin_pixel = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/myelin_pixel_cat.csv')
sum_axon=sum(Axon_pixel.axon_pixel_area)
sum_myelin=sum(Myelin_pixel.myelin_pixel_area)
Total_pixel = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/Summary_total_pix.csv')
Total_pixel.columns =['Slice', 'count', 'Total_area', 'Average_size', 'Percent_area', 'Mean']
sum_total_pixel=sum(Total_pixel.Total_area)
avf_1=float(sum_axon)/(sum_total_pixel)
mvf_1=float(sum_myelin)/(sum_total_pixel)
print(avf_1)
print(mvf_1)

stats_per = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/stats_per_image.csv')

AVF=pd.DataFrame([avf_1])
MVF=pd.DataFrame([mvf_1])

avf_renamed=AVF.rename(index=str, columns={0: "AVF"})
mvf_renamed=MVF.rename(index=str, columns={0: "MVF"})

avf_renamed.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/avf.csv')
mvf_renamed.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/mvf.csv')

avf_for_cat = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/avf.csv')
mvf_for_cat = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/mvf.csv')

avf_for_cat_good = avf_for_cat.drop('Unnamed: 0', axis=1)
mvf_for_cat_good = mvf_for_cat.drop('Unnamed: 0', axis=1)

frames=[stats_per, avf_for_cat_good, mvf_for_cat_good]
result =pd.concat(frames, axis=1)

print(result)
result.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/right_damaged/analisis/stats_avf_mvf.csv')

#ANOTHER NERVE


Axon_pixel_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/axon_pixel_cat.csv')
Myelin_pixel_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/myelin_pixel_cat.csv')
sum_axon_2=sum(Axon_pixel_2.axon_pixel_area)
sum_myelin_2=sum(Myelin_pixel_2.myelin_pixel_area)
Total_pixel_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/Summary_total_pix.csv')
Total_pixel_2.columns =['Slice', 'count', 'Total_area', 'Average_size', 'Percent_area', 'Mean']
sum_total_pixel_2=sum(Total_pixel_2.Total_area)
avf_1_2=float(sum_axon_2)/(sum_total_pixel_2)
mvf_1_2=float(sum_myelin_2)/(sum_total_pixel_2)
print(avf_1_2)
print(mvf_1_2)

stats_per_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/stats_per_image.csv')

AVF_2=pd.DataFrame([avf_1_2])
MVF_2=pd.DataFrame([mvf_1_2])

avf_renamed_2=AVF_2.rename(index=str, columns={0: "AVF"})
mvf_renamed_2=MVF_2.rename(index=str, columns={0: "MVF"})

avf_renamed_2.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/avf.csv')
mvf_renamed_2.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/mvf.csv')

avf_for_cat_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/avf.csv')
mvf_for_cat_2 = pd.read_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/mvf.csv')

avf_for_cat_good_2 = avf_for_cat_2.drop('Unnamed: 0', axis=1)
mvf_for_cat_good_2 = mvf_for_cat_2.drop('Unnamed: 0', axis=1)

frames_2=[stats_per_2, avf_for_cat_good_2, mvf_for_cat_good_2]
result_2 =pd.concat(frames_2, axis=1)

print(result_2)
result_2.to_csv('/misc/torrey/onarvaez/M-isq/isq/isq10/left_intact/analisis/stats_avf_mvf.csv')
