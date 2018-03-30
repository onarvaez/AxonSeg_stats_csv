# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import pandas as pd
from scipy import stats

data = pd.read_csv('C:/Users/Sergio/Documents/AxonSeg_stats_csv_master/t_test.csv')

vector_intact=[]
for i in range(21):
    vector_intact.append(data.iloc[i,0])
vector_degenerated=[]
for i in range(21):
    vector_degenerated.append(data.iloc[i,1])    

stats.ttest_ind(vector_intact,vector_degenerated)