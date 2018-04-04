# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:14:51 2018

@author: Omar
"""

import pandas as pd 

#chiasm avf_mvf_totalaxon cat

avf_1 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x1_Segmentation/misc/avf.csv')
avf_2 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x2_Segmentation/misc/avf.csv')
avf_3 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x3_Segmentation/misc/avf.csv')
avf_4 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x4_Segmentation/misc/avf.csv')
avf_5 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x5_Segmentation/misc/avf.csv')
avf_6 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x6_Segmentation/misc/avf.csv')
avf_7 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x7_Segmentation/misc/avf.csv')
avf_8 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x8_Segmentation/misc/avf.csv')
avf_9 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x9_Segmentation/misc/avf.csv')
avf_10 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x10_Segmentation/misc/avf.csv')


avf_cat = pd.concat([avf_1, avf_2, avf_3, avf_4, avf_5, avf_6, avf_7, avf_8, avf_9, avf_10])

avf_cat.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/avf_cat.csv')

#------
mvf_1 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x1_Segmentation/misc/mvf.csv')
mvf_2 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x2_Segmentation/misc/mvf.csv')
mvf_3 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x3_Segmentation/misc/mvf.csv')
mvf_4 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x4_Segmentation/misc/mvf.csv')
mvf_5 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x5_Segmentation/misc/mvf.csv')
mvf_6 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x6_Segmentation/misc/mvf.csv')
mvf_7 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x7_Segmentation/misc/mvf.csv')
mvf_8 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x8_Segmentation/misc/mvf.csv')
mvf_9 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x9_Segmentation/misc/mvf.csv')
mvf_10 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x10_Segmentation/misc/mvf.csv')


mvf_cat = pd.concat([mvf_1, mvf_2, mvf_3, mvf_4, mvf_5, mvf_6, mvf_7, mvf_8, mvf_9, mvf_10])

mvf_cat.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/mvf_cat.csv')
#------

total_1 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x1_Segmentation/misc/total_axon.csv')
total_2 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x2_Segmentation/misc/total_axon.csv')
total_3 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x3_Segmentation/misc/total_axon.csv')
total_4 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x4_Segmentation/misc/total_axon.csv')
total_5 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x5_Segmentation/misc/total_axon.csv')
total_6 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x6_Segmentation/misc/total_axon.csv')
total_7 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x7_Segmentation/misc/total_axon.csv')
total_8 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x8_Segmentation/misc/total_axon.csv')
total_9 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x9_Segmentation/misc/total_axon.csv')
total_10 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x10_Segmentation/misc/total_axon.csv')

total_axon_cat = pd.concat([total_1, total_2, total_3, total_4, total_5, total_6, total_7, total_8, total_9, total_10])

total_axon_cat.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/total_axon_cat.csv')

#--------
axonlist_1 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x1_Segmentation/misc/axonlist_image.csv')
axonlist_2 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x2_Segmentation/misc/axonlist_image.csv')
axonlist_3 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x3_Segmentation/misc/axonlist_image.csv')
axonlist_4 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x4_Segmentation/misc/axonlist_image.csv')
axonlist_5 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x5_Segmentation/misc/axonlist_image.csv')
axonlist_6 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x6_Segmentation/misc/axonlist_image.csv')
axonlist_7 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x7_Segmentation/misc/axonlist_image.csv')
axonlist_8 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x8_Segmentation/misc/axonlist_image.csv')
axonlist_9 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x9_Segmentation/misc/axonlist_image.csv')
axonlist_10 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x10_Segmentation/misc/axonlist_image.csv')

axonlist_cat = pd.concat([axonlist_1, axonlist_2, axonlist_3, axonlist_4, axonlist_5, axonlist_6, axonlist_7, axonlist_8, axonlist_9, axonlist_10])

axonlist_cat.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/axonlist_cat.csv')

#-----

axonstats_1 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x1_Segmentation/misc/stats_image.csv')
axonstats_2 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x2_Segmentation/misc/stats_image.csv')
axonstats_3 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x3_Segmentation/misc/stats_image.csv')
axonstats_4 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x4_Segmentation/misc/stats_image.csv')
axonstats_5 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x5_Segmentation/misc/stats_image.csv')
axonstats_6 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x6_Segmentation/misc/stats_image.csv')
axonstats_7 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x7_Segmentation/misc/stats_image.csv')
axonstats_8 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x8_Segmentation/misc/stats_image.csv')
axonstats_9 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x9_Segmentation/misc/stats_image.csv')
axonstats_10 = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/x10_Segmentation/misc/stats_image.csv')

axonstats_cat = pd.concat([axonstats_1, axonstats_2, axonstats_3, axonstats_4, axonstats_5, axonstats_6, axonstats_7, axonstats_8, axonstats_9, axonstats_10])

axonstats_cat.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/chiasm/axonstats_cat.csv')

#nerve_1 avf_mvf cat

avf_1_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x1_Segmentation/misc/avf.csv')
avf_2_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x2_Segmentation/misc/avf.csv')
avf_3_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x3_Segmentation/misc/avf.csv')
avf_4_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x4_Segmentation/misc/avf.csv')
avf_5_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x5_Segmentation/misc/avf.csv')
avf_6_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x6_Segmentation/misc/avf.csv')
avf_7_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x7_Segmentation/misc/avf.csv')
avf_8_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x8_Segmentation/misc/avf.csv')
avf_9_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x9_Segmentation/misc/avf.csv')
avf_10_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x10_Segmentation/misc/avf.csv')


avf_cat_n = pd.concat([avf_1_n, avf_2_n, avf_3_n, avf_4_n, avf_5_n, avf_6_n, avf_7_n, avf_8_n, avf_9_n, avf_10_n])

avf_cat_n.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/avf_cat.csv')

#-------
mvf_1_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x1_Segmentation/misc/mvf.csv')
mvf_2_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x2_Segmentation/misc/mvf.csv')
mvf_3_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x3_Segmentation/misc/mvf.csv')
mvf_4_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x4_Segmentation/misc/mvf.csv')
mvf_5_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x5_Segmentation/misc/mvf.csv')
mvf_6_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x6_Segmentation/misc/mvf.csv')
mvf_7_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x7_Segmentation/misc/mvf.csv')
mvf_8_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x8_Segmentation/misc/mvf.csv')
mvf_9_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x9_Segmentation/misc/mvf.csv')
mvf_10_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x10_Segmentation/misc/mvf.csv')


mvf_cat_n = pd.concat([mvf_1_n, mvf_2_n, mvf_3_n, mvf_4_n, mvf_5_n, mvf_6_n, mvf_7_n, mvf_8_n, mvf_9_n, mvf_10_n])

mvf_cat_n.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/mvf_cat.csv')
#-------
total_1_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x1_Segmentation/misc/total_axon.csv')
total_2_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x2_Segmentation/misc/total_axon.csv')
total_3_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x3_Segmentation/misc/total_axon.csv')
total_4_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x4_Segmentation/misc/total_axon.csv')
total_5_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x5_Segmentation/misc/total_axon.csv')
total_6_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x6_Segmentation/misc/total_axon.csv')
total_7_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x7_Segmentation/misc/total_axon.csv')
total_8_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x8_Segmentation/misc/total_axon.csv')
total_9_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x9_Segmentation/misc/total_axon.csv')
total_10_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x10_Segmentation/misc/total_axon.csv')

total_axon_cat_n = pd.concat([total_1_n, total_2_n, total_3_n, total_4_n, total_5_n, total_6_n, total_7_n, total_8_n, total_9_n, total_10_n])

total_axon_cat_n.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/total_axon_cat.csv')
#-------
axonlist_1_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x1_Segmentation/misc/axonlist_image.csv')
axonlist_2_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x2_Segmentation/misc/axonlist_image.csv')
axonlist_3_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x3_Segmentation/misc/axonlist_image.csv')
axonlist_4_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x4_Segmentation/misc/axonlist_image.csv')
axonlist_5_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x5_Segmentation/misc/axonlist_image.csv')
axonlist_6_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x6_Segmentation/misc/axonlist_image.csv')
axonlist_7_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x7_Segmentation/misc/axonlist_image.csv')
axonlist_8_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x8_Segmentation/misc/axonlist_image.csv')
axonlist_9_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x9_Segmentation/misc/axonlist_image.csv')
axonlist_10_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x10_Segmentation/misc/axonlist_image.csv')

axonlist_cat_n = pd.concat([axonlist_1_n, axonlist_2_n, axonlist_3_n, axonlist_4_n, axonlist_5_n, axonlist_6_n, axonlist_7_n, axonlist_8_n, axonlist_9_n, axonlist_10_n])

axonlist_cat_n.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/axonlist_cat.csv')
#-------

axonstats_1_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x1_Segmentation/misc/stats_image.csv')
axonstats_2_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x2_Segmentation/misc/stats_image.csv')
axonstats_3_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x3_Segmentation/misc/stats_image.csv')
axonstats_4_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x4_Segmentation/misc/stats_image.csv')
axonstats_5_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x5_Segmentation/misc/stats_image.csv')
axonstats_6_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x6_Segmentation/misc/stats_image.csv')
axonstats_7_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x7_Segmentation/misc/stats_image.csv')
axonstats_8_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x8_Segmentation/misc/stats_image.csv')
axonstats_9_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x9_Segmentation/misc/stats_image.csv')
axonstats_10_n = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/x10_Segmentation/misc/stats_image.csv')

axonstats_cat_n = pd.concat([axonstats_1_n, axonstats_2_n, axonstats_3_n, axonstats_4_n, axonstats_5_n, axonstats_6_n, axonstats_7_n, axonstats_8_n, axonstats_9_n, axonstats_10_n])

axonstats_cat_n.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_right_degenerated/axonstats_cat.csv')

#nerve_2 avf_mvf cat

avf_1_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x1_Segmentation/misc/avf.csv')
avf_2_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x2_Segmentation/misc/avf.csv')
avf_3_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x3_Segmentation/misc/avf.csv')
avf_4_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x4_Segmentation/misc/avf.csv')
avf_5_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x5_Segmentation/misc/avf.csv')
avf_6_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x6_Segmentation/misc/avf.csv')
avf_7_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x7_Segmentation/misc/avf.csv')
avf_8_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x8_Segmentation/misc/avf.csv')
avf_9_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x9_Segmentation/misc/avf.csv')
avf_10_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x10_Segmentation/misc/avf.csv')


avf_cat_m = pd.concat([avf_1_m, avf_2_m, avf_3_m, avf_4_m, avf_5_m, avf_6_m, avf_7_m, avf_8_m, avf_9_m, avf_10_m])

avf_cat_m.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/avf_cat.csv')
#-------

mvf_1_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x1_Segmentation/misc/mvf.csv')
mvf_2_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x2_Segmentation/misc/mvf.csv')
mvf_3_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x3_Segmentation/misc/mvf.csv')
mvf_4_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x4_Segmentation/misc/mvf.csv')
mvf_5_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x5_Segmentation/misc/mvf.csv')
mvf_6_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x6_Segmentation/misc/mvf.csv')
mvf_7_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x7_Segmentation/misc/mvf.csv')
mvf_8_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x8_Segmentation/misc/mvf.csv')
mvf_9_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x9_Segmentation/misc/mvf.csv')
mvf_10_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x10_Segmentation/misc/mvf.csv')


mvf_cat_m = pd.concat([mvf_1_m, mvf_2_m, mvf_3_m, mvf_4_m, mvf_5_m, mvf_6_m, mvf_7_m, mvf_8_m, mvf_9_m, mvf_10_m])

mvf_cat_m.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/mvf_cat.csv')
#-------
total_1_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x1_Segmentation/misc/total_axon.csv')
total_2_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x2_Segmentation/misc/total_axon.csv')
total_3_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x3_Segmentation/misc/total_axon.csv')
total_4_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x4_Segmentation/misc/total_axon.csv')
total_5_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x5_Segmentation/misc/total_axon.csv')
total_6_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x6_Segmentation/misc/total_axon.csv')
total_7_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x7_Segmentation/misc/total_axon.csv')
total_8_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x8_Segmentation/misc/total_axon.csv')
total_9_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x9_Segmentation/misc/total_axon.csv')
total_10_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x10_Segmentation/misc/total_axon.csv')

total_axon_cat_m = pd.concat([total_1_n, total_2_n, total_3_n, total_4_n, total_5_n, total_6_n, total_7_n, total_8_n, total_9_n, total_10_n])

total_axon_cat_m.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/total_axon_cat.csv')

#-------
axonlist_1_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x1_Segmentation/misc/axonlist_image.csv')
axonlist_2_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x2_Segmentation/misc/axonlist_image.csv')
axonlist_3_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x3_Segmentation/misc/axonlist_image.csv')
axonlist_4_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x4_Segmentation/misc/axonlist_image.csv')
axonlist_5_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x5_Segmentation/misc/axonlist_image.csv')
axonlist_6_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x6_Segmentation/misc/axonlist_image.csv')
axonlist_7_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x7_Segmentation/misc/axonlist_image.csv')
axonlist_8_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x8_Segmentation/misc/axonlist_image.csv')
axonlist_9_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x9_Segmentation/misc/axonlist_image.csv')
axonlist_10_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x10_Segmentation/misc/axonlist_image.csv')

axonlist_cat_m = pd.concat([axonlist_1_m, axonlist_2_m, axonlist_3_m, axonlist_4_m, axonlist_5_m, axonlist_6_m, axonlist_7_m, axonlist_8_m, axonlist_9_m, axonlist_10_m])

axonlist_cat_m.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/axonlist_cat.csv')
#-------
axonstats_1_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x1_Segmentation/misc/axonlist_image.csv')
axonstats_2_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x2_Segmentation/misc/axonlist_image.csv')
axonstats_3_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x3_Segmentation/misc/axonlist_image.csv')
axonstats_4_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x4_Segmentation/misc/axonlist_image.csv')
axonstats_5_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x5_Segmentation/misc/axonlist_image.csv')
axonstats_6_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x6_Segmentation/misc/axonlist_image.csv')
axonstats_7_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x7_Segmentation/misc/axonlist_image.csv')
axonstats_8_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x8_Segmentation/misc/axonlist_image.csv')
axonstats_9_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x9_Segmentation/misc/axonlist_image.csv')
axonstats_10_m = pd.read_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/x10_Segmentation/misc/axonlist_image.csv')

axonstats_cat_m = pd.concat([axonstats_1_m, axonstats_2_m, axonstats_3_m, axonstats_4_m, axonstats_5_m, axonstats_6_m, axonstats_7_m, axonstats_8_m, axonstats_9_m, axonstats_10_m])

axonstats_cat_m.to_csv('/misc/torrey/onarvaez/ha/histologias_automaticas/histologias_automaticas/is/10_17-14/nerve_left_intact/axonstats_cat.csv')