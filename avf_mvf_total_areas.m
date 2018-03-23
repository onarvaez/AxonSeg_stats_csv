%Neuropoly/AxonSeg_Stats

%Concatenate all MVF and AVF results from "axonlist_stats_mvf_avf.m" 
avf_cat = vertcat(AVF_1,AVF_2,AVF_3,AVF_4,AVF_5,AVF_6,AVF_7,AVF_8,AVF_9,AVF_10)
axon_area_cat = vertcat(axon_area_1,axon_area_2,axon_area_3,axon_area_4,axon_area_5,axon_area_6,axon_area_7,axon_area_8,axon_area_9,axon_area_10)
mvf_cat = vertcat(MVF_1,MVF_2,MVF_3,MVF_4,MVF_5,MVF_6,MVF_7,MVF_8,MVF_9,MVF_10)
myelin_area_cat = vertcat(myelin_area_1,myelin_area_2,myelin_area_3,myelin_area_4,myelin_area_5,myelin_area_6,myelin_area_7,myelin_area_8,myelin_area_9,myelin_area_10)
%Multiply total area for total number of images of interest
total_area_image = total_area*10

%axon volume fraction stats
avf_sum = sum(avf_cat)
avf_mean = mean(avf_cat)
avf_median = median(avf_cat)
avf_std = std(avf_cat)

axon_por_sum = sum(axon_area_cat)
axon_por_mean = mean(axon_area_cat)
axon_por_median = median(axon_area_cat)
axon_por_std = std(axon_area_cat)
axon_por_all_images = axon_por_sum/total_area_image

%myelin volume fraction stats
mvf_sum = sum(mvf_cat)
mvf_mean = mean(mvf_cat)
mvf_median = median(mvf_cat)
mvf_std = std(mvf_cat)

myelin_por_sum = sum(myelin_area_cat)
myelin_por_mean = mean(myelin_area_cat)
myelin_por_median = median(myelin_area_cat)
myelin_por_std = std(myelin_area_cat)
myelin_por_all_images = myelin_por_sum/total_area_image

%save avf and mvf cat 
csvwrite('avf_cat.csv', avf_cat)
csvwrite('axon_pixel_area_cat.csv', axon_area_cat)
csvwrite('mvf_cat.csv', mvf_cat)
csvwrite('myelin_pixel_area_cat.csv', myelin_area_cat)
