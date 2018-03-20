 #AxonSeg_stats_csv
 Neuropoly/AxonSeg-Stats
 
 #Extract each parameter from axonlist and delete axons below 0.005 micras

 axonlist([axonlist.axonEquivDiameter]<0.005)=[];
 Axon_diameters = cat(1,axonlist.axonEquivDiameter);
 myelin_diameters = cat(1,axonlist.myelinEquivDiameter);
 myelin_thickness = cat(1,axonlist.myelinThickness);
 gRatio = cat(1,axonlist.gRatio);
 
#Obtain mean, median, standard deviation, max and min of each parameter

 axon_diam_mean=mean(Axon_diameters);
 axon_diam_median=median(Axon_diameters);
 axon_diam_std=std(Axon_diameters);
 gRatio_max=max(gRatio);
 gRatio_min=min(gRatio);
 
#Make a struct with all parameters headers and values and save new axonlist file and stats to csv
 stats = struct('axon_diameter_mean',axon_diam_mean,'axon_diameter_median',axon_diam_median,'axon_diameter_std',axon_diam_std,'axon_diameter_max',axon_diam_max,'axon_diameter_min',axon_diam_min,'myelin_diameter_mean',myelin_diam_mean,'myelin_diameter_median',myelin_diam_median,'myelin_diameter_std',myelin_diam_std,'myelin_diameter_max',myelin_diam_max,'myelin_diameter_min',myelin_diam_min,'axon_area_mean',axonArea_mean,'axon_area_median',axonArea_median,'axon_area_std',axonArea_std,'axon_area_max',axonArea_max,'axon_area_min',axonArea_min,'myelin_area_mean',myelinArea_mean,'myelin_area_median',myelinArea_median,'myelin_area_std',myelinArea_std,'myelin_area_max',myelinArea_max,'myelin_area_min',myelinArea_min,'myelin_thickness_mean',myelinThickness_mean,'myelin_thickness_median',myelinThickness_median,'myelin_thickness_std',myelinThickness_std,'myelin_thickness_max',myelinThickness_max,'myelin_thickness_min',myelinThickness_min,'gRatio_mean',gRatio_mean,'gRatio_median',gRatio_median,'gRatio_std',gRatio_std,'gRatio_max',gRatio_max,'gRatio_min',gRatio_min)
 axontable = struct2table(axonlist);
 axontable.axonID=[];
 axontable.data=[];
 writetable(axontable,'axonlist_image.csv');
 temp_table = struct2table(stats);
 writetable(temp_table,'stats_image.csv');

#Obtain Myelin/Axon volume fraction, then, manually change the name of MVF and AVF if you are going to analyze several images
 total_area=size(img,1)*size(img,2);
 bw_axonseg=as_display_label(axonlist,size(img),'axonEquivDiameter','myelin');
 img_BW_myelins=im2bw(bw_axonseg,0);