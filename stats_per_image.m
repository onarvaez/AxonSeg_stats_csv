function stats_per_image(filename,filename1,filename2)
[this_dir,this_file,this_ext] = fileparts(filename);
[this_dir1,this_file1,this_ext1] = fileparts(filename1);
[this_dir2,this_file2,this_ext2] = fileparts(filename2);

statsimage = readtable(filename)
statsimage1 = readtable(filename1)
statsimage2 = readtable(filename2)

vertcat(statsimage,statsimage1,statsimage2)
axonlist = table2struct(ans)

AxDiamMean = cat(1,axonlist.axon_diameter_mean);
AxDiamMedian = cat(1,axonlist.axon_diameter_median);
AxDiamStd = cat(1,axonlist.axon_diameter_std);
AxDiamMax = cat(1,axonlist.axon_diameter_max)
AxDiamMin = cat(1,axonlist.axon_diameter_min)

MyDiamMean = cat(1,axonlist.myelin_diameter_mean);
MyDiamMedian = cat(1,axonlist.myelin_diameter_median);
MyDiamStd = cat(1,axonlist.myelin_diameter_std);
MyDiamMax = cat(1,axonlist.myelin_diameter_max)
MyDiamMin = cat(1,axonlist.myelin_diameter_min)

AxAreaMean = cat(1,axonlist.axon_area_mean);
AxAreaMedian = cat(1,axonlist.axon_area_median);
AxAreaStd = cat(1,axonlist.axon_area_std);
AxAreaMax = cat(1,axonlist.axon_area_max)
AxAreaMin = cat(1,axonlist.axon_area_min)

MyAreaMean = cat(1,axonlist.myelin_area_mean);
MyAreaMedian = cat(1,axonlist.myelin_area_median);
MyAreaStd = cat(1,axonlist.myelin_area_std);
MyAreaMax = cat(1,axonlist.myelin_area_max)
MyAreaMin = cat(1,axonlist.myelin_area_min)

MyThiMean = cat(1,axonlist.myelin_thickness_mean);
MyThiMedian = cat(1,axonlist.myelin_thickness_median);
MyThiStd = cat(1,axonlist.myelin_thickness_std);
MyThiMax = cat(1,axonlist.myelin_thickness_max)
MyThiMin = cat(1,axonlist.myelin_thickness_min)

gRatioMean = cat(1,axonlist.gRatio_mean);
gRatioMedian = cat(1,axonlist.gRatio_median);
gRatioStd = cat(1,axonlist.gRatio_std);
gRatioMax = cat(1,axonlist.gRatio_max)
gRatioMin = cat(1,axonlist.gRatio_min)

% Mean, median, std, max, min

axon_diameter_Mean = mean(AxDiamMean)
axon_diameter_Median = median(AxDiamMedian)
axon_diameter_Std = std(AxDiamStd)
axon_diameter_Max = max(AxDiamMax)
axon_diameter_Min = min(AxDiamMin)

myelin_diameter_Mean = mean(MyDiamMean)
myelin_diameter_Median = median(MyDiamMedian)
myelin_diameter_Std = std(MyDiamStd)
myelin_diameter_Max = max(MyDiamMax)
myelin_diameter_Min = min(MyDiamMin)

axon_area_Mean = mean(AxAreaMean)
axon_area_Median = median(AxAreaMedian)
axon_area_Std = std(AxAreaStd)
axon_area_Max = max(AxAreaMax)
axon_area_Min = min(AxAreaMin)

myelin_area_Mean = mean(MyAreaMean)
myelin_area_Median = median(MyAreaMedian)
myelin_area_Std = std(MyAreaStd)
myelin_area_Max = max(MyAreaMax)
myelin_area_Min = min(MyAreaMin)

myelin_thickness_Mean = mean(MyThiMean) 
myelin_thickness_Median = median(MyThiMedian) 
myelin_thickness_Std = std(MyThiStd) 
myelin_thickness_Max = max(MyThiMax) 
myelin_thickness_Min = min(MyThiMin) 

gRatio_Mean=mean(gRatioMean);
gRatio_Median=median(gRatioMedian);
gRatio_Std=std(gRatioStd);
gRatio_Max=max(gRatioMax);
gRatio_Min=min(gRatioMin);

%store data list and stats
stats = struct('axon_diameter_mean',axon_diameter_Mean,'axon_diameter_median',axon_diameter_Median,'axon_diameter_std',axon_diameter_Std,'axon_diameter_max',axon_diameter_Max,'axon_diameter_min',axon_diameter_Min,'myelin_diameter_mean',myelin_diameter_Mean,'myelin_diameter_median',myelin_diameter_Median,'myelin_diameter_std',myelin_diameter_Std,'myelin_diameter_max',myelin_diameter_Max,'myelin_diameter_min',myelin_diameter_Min,'axon_area_mean',axon_area_Mean,'axon_area_median',axon_area_Median,'axon_area_std',axon_area_Std,'axon_area_max',axon_area_Max,'axon_area_min',axon_area_Min,'myelin_area_mean',myelin_area_Mean,'myelin_area_median',myelin_area_Median,'myelin_area_std',myelin_area_Std,'myelin_area_max',myelin_area_Max,'myelin_area_min',myelin_area_Min,'myelin_thickness_mean',myelin_thickness_Mean,'myelin_thickness_median',myelin_thickness_Median,'myelin_thickness_std',myelin_thickness_Std,'myelin_thickness_max',myelin_thickness_Max,'myelin_thickness_min',myelin_thickness_Min,'gRatio_mean',gRatio_Mean,'gRatio_median',gRatio_Median,'gRatio_std',gRatio_Std,'gRatio_max',gRatio_Max,'gRatio_min',gRatio_Min)

axontable = struct2table(axonlist);
writetable(axontable,'axonlist_stats_per_image.csv');

temp_table = struct2table(stats);
writetable(temp_table,'stats_per_image.csv');
end

