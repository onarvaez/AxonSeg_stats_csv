#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on 2018

@author: onarvaez
"""

import pandas as pd

#Importar concatenación del número de pixeles de mielina y axones
Axon_pixel = pd.read_csv('axon_pixel_cat.csv')
Myelin_pixel = pd.read_csv('myelin_pixel_cat.csv')
#Sumatoria de la concatenación 
sum_axon=sum(Axon_pixel.axon_pixel_area)
sum_myelin=sum(Myelin_pixel.myelin_pixel_area)
#Importar la concatenación de los pixeles de cada área de interes (máscara) 
Total_pixel = pd.read_csv('Summary_total_pix.csv')
Total_pixel.columns =['Slice', 'count', 'Total_area', 'Average_size', 'Percent_area', 'Mean']
#Sumatoria de la concatenación de los pixeles de cada área de interes (máscara) 
sum_total_pixel=sum(Total_pixel.Total_area)
#Obtener la AVF y MVF
avf_1=float(sum_axon)/(sum_total_pixel)
mvf_1=float(sum_myelin)/(sum_total_pixel)
print(avf_1)
print(mvf_1)
#Crear los dataframes para AVF y MVF
AVF=pd.DataFrame([avf_1])
MVF=pd.DataFrame([mvf_1])

avf_renamed=AVF.rename(index=str, columns={0: "AVF"})
mvf_renamed=MVF.rename(index=str, columns={0: "MVF"})
#Guardar los archivos
avf_renamed.to_csv('avf.csv')
mvf_renamed.to_csv('mvf.csv')
#Leer los archivos y eliminar columna "Unnamed: 0"
avf_for_cat = pd.read_csv('avf.csv')
mvf_for_cat = pd.read_csv('mvf.csv')

avf_for_cat_good = avf_for_cat.drop('Unnamed: 0', axis=1)
mvf_for_cat_good = mvf_for_cat.drop('Unnamed: 0', axis=1)
#Concatenar AVF y MVF
frames=[avf_for_cat_good, mvf_for_cat_good]
result =pd.concat(frames, axis=1)
#Listo! AVF y MVF en un archivo 
print(result)
result.to_csv('avf_mvf.csv')

###Lo mismo pero en otro nervio####


#Importar concatenación del número de pixeles de mielina y axones
Axon_pixel_2 = pd.read_csv('axon_pixel_cat.csv')
Myelin_pixel_2 = pd.read_csv('myelin_pixel_cat.csv')
#Sumatoria de la concatenación 
sum_axon_2=sum(Axon_pixel_2.axon_pixel_area)
sum_myelin_2=sum(Myelin_pixel_2.myelin_pixel_area)
#Importar la concatenación de los pixeles de cada área de interes (máscara) 
Total_pixel_2 = pd.read_csv('Summary_total_pix.csv')
Total_pixel_2.columns =['Slice', 'count', 'Total_area', 'Average_size', 'Percent_area', 'Mean']
#Sumatoria de la concatenación de los pixeles de cada área de interes (máscara) 
sum_total_pixel_2=sum(Total_pixel_2.Total_area)
#Obtener la AVF y MVF
avf_1_2=float(sum_axon_2)/(sum_total_pixel_2)
mvf_1_2=float(sum_myelin_2)/(sum_total_pixel_2)
print(avf_1_2)
print(mvf_1_2)
#Crear los dataframes para AVF y MVF
AVF_2=pd.DataFrame([avf_1_2])
MVF_2=pd.DataFrame([mvf_1_2])

avf_renamed_2=AVF_2.rename(index=str, columns={0: "AVF"})
mvf_renamed_2=MVF_2.rename(index=str, columns={0: "MVF"})
#Guardar los archivos
avf_renamed_2.to_csv('avf.csv')
mvf_renamed_2.to_csv('mvf.csv')

avf_for_cat_2 = pd.read_csv('avf.csv')
mvf_for_cat_2 = pd.read_csv('mvf.csv')
#Leer los archivos y eliminar columna "Unnamed: 0"
avf_for_cat_good_2 = avf_for_cat_2.drop('Unnamed: 0', axis=1)
mvf_for_cat_good_2 = mvf_for_cat_2.drop('Unnamed: 0', axis=1)
#Concatenar AVF y MVF
frames_2=[avf_for_cat_good_2, mvf_for_cat_good_2]
result_2 =pd.concat(frames_2, axis=1)
#Listo! AVF y MVF en un archivo 
print(result_2)
result_2.to_csv('avf_mvf.csv')
