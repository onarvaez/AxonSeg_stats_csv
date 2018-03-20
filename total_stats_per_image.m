vertcat(statsimage,statsimage1,statsimage2,statsimage3,statsimage4,statsimage5,statsimage6,statsimage7,statsimage8,statsimage9)
axonlist = table2struct(ans) 

AxDiam = cat(1,axonlist.axon_diameter_mean);
MyDiam = cat(1,axonlist.myelin_diameter_mean);
AxArea = cat(1,axonlist.axon_area_mean);
MyArea = cat(1,axonlist.myelin_area_mean);
MyThi = cat(1,axonlist.myelin_thickness_mean);
gRatio = cat(1,axonlist.gRatio_mean);

% Mean, median, std, max, min

axon_diameter_Mean = mean(AxDiam)
axon_diameter_Median = median(AxDiam)
axon_diameter_Std = std(AxDiam)

myelin_diameter_Mean = mean(MyDiam)
myelin_diameter_Median = median(MyDiam)
myelin_diameter_Std = std(MyDiam)

axon_area_Mean = mean(AxArea)
axon_area_Median = median(AxArea)
axon_area_Std = std(AxArea)

myelin_area_Mean = mean(MyArea)
myelin_area_Median = median(MyArea)
myelin_area_Std = std(MyArea)

myelin_thickness_Mean = mean(MyThi) 
myelin_thickness_Median = median(MyThi) 
myelin_thickness_Std = std(MyThi) 

gRatio_Mean=mean(gRatio);
gRatio_Median=median(gRatio);
gRatio_Std=std(gRatio);

%save data list and stats
stats = struct('axon_diameter_mean',axon_diameter_Mean,'axon_diameter_median',axon_diameter_Median,'axon_diameter_std',axon_diameter_Std,'myelin_diameter_mean',myelin_diameter_Mean,'myelin_diameter_median',myelin_diameter_Median,'myelin_diameter_std',myelin_diameter_Std,'axon_area_mean',axon_area_Mean,'axon_area_median',axon_area_Median,'axon_area_std',axon_area_Std,'myelin_area_mean',myelin_area_Mean,'myelin_area_median',myelin_area_Median,'myelin_area_std',myelin_area_Std,'myelin_thickness_mean',myelin_thickness_Mean,'myelin_thickness_median',myelin_thickness_Median,'myelin_thickness_std',myelin_thickness_Std,'gRatio_mean',gRatio_Mean,'gRatio_median',gRatio_Median,'gRatio_std',gRatio_Std)
axontable = struct2table(axonlist);
writetable(axontable,'axonlist_stats_per_image.csv');
temp_table = struct2table(stats);
writetable(temp_table,'stats_per_image.csv');



