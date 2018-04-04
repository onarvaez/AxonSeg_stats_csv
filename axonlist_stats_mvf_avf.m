function axonlist_stats_mvf_avf(filename)
%AxonSeg_stats_csv
%Neuropoly/AxonSeg_Stats

[this_dir,this_file,this_ext] = fileparts(filename);

%Extract each parameter from axonlist and delete axons below 0.005 micras

load(filename)
axonlist([axonlist.axonEquivDiameter]<0.005)=[];
Axon_diameters = cat(1,axonlist.axonEquivDiameter);
myelin_diameters = cat(1,axonlist.myelinEquivDiameter);
axonArea = cat(1,axonlist.axonArea);
myelinArea = cat(1,axonlist.myelinArea);
myelin_thickness = cat(1,axonlist.myelinThickness);
gRatio = cat(1,axonlist.gRatio);
 
%Obtain mean, median, standard deviation, max and min of each parameter

axon_diam_mean=mean(Axon_diameters);
axon_diam_median=median(Axon_diameters);
axon_diam_std=std(Axon_diameters);
axon_diam_max=max(Axon_diameters);
axon_diam_min=min(Axon_diameters);

myelin_diam_mean=mean(myelin_diameters);
myelin_diam_median=median(myelin_diameters);
myelin_diam_std=std(myelin_diameters);
myelin_diam_max=max(myelin_diameters);
myelin_diam_min=min(myelin_diameters);

axonArea_mean=mean(axonArea);
axonArea_median=median(axonArea);
axonArea_std=std(axonArea);
axonArea_max=max(axonArea);
axonArea_min=min(axonArea);

myelinArea_mean=mean(myelinArea);
myelinArea_median=median(myelinArea);
myelinArea_std=std(myelinArea);
myelinArea_max=max(myelinArea);
myelinArea_min=min(myelinArea);

myelinThickness_mean=mean(myelin_thickness);
myelinThickness_median=median(myelin_thickness);
myelinThickness_std=std(myelin_thickness);
myelinThickness_max=max(myelin_thickness);
myelinThickness_min=min(myelin_thickness);

gRatio_mean=mean(gRatio);
gRatio_median=median(gRatio);
gRatio_std=std(gRatio);
gRatio_max=max(gRatio);
gRatio_min=min(gRatio);
 
%Make a struct with all parameters headers and values and save new axonlist file and stats to csv

stats = struct('axon_diameter_mean',axon_diam_mean,'axon_diameter_median',axon_diam_median,'axon_diameter_std',axon_diam_std,'axon_diameter_max',axon_diam_max,'axon_diameter_min',axon_diam_min,'myelin_diameter_mean',myelin_diam_mean,'myelin_diameter_median',myelin_diam_median,'myelin_diameter_std',myelin_diam_std,'myelin_diameter_max',myelin_diam_max,'myelin_diameter_min',myelin_diam_min,'axon_area_mean',axonArea_mean,'axon_area_median',axonArea_median,'axon_area_std',axonArea_std,'axon_area_max',axonArea_max,'axon_area_min',axonArea_min,'myelin_area_mean',myelinArea_mean,'myelin_area_median',myelinArea_median,'myelin_area_std',myelinArea_std,'myelin_area_max',myelinArea_max,'myelin_area_min',myelinArea_min,'myelin_thickness_mean',myelinThickness_mean,'myelin_thickness_median',myelinThickness_median,'myelin_thickness_std',myelinThickness_std,'myelin_thickness_max',myelinThickness_max,'myelin_thickness_min',myelinThickness_min,'gRatio_mean',gRatio_mean,'gRatio_median',gRatio_median,'gRatio_std',gRatio_std,'gRatio_max',gRatio_max,'gRatio_min',gRatio_min)
axontable = struct2table(axonlist);
axontable.axonID=[];
axontable.data=[];
%Make new directory
savedir=[this_dir filesep 'misc' filesep];
mkdir(savedir);
%currentdir=pwd;
%cd(savedir);
% save SegParameters
    writetable(axontable,fullfile(savedir,'axonlist_image.csv'));
    temp_table = struct2table(stats);
    writetable(temp_table,fullfile(savedir,'stats_image.csv'));
 

%Obtain Myelin/Axon Volume Fraction, then, manually change the name of MVF and AVF if you are going to analyze several images

total_area=size(img,1)*size(img,2);
bw_axonseg=as_display_label(axonlist,size(img),'axonEquivDiameter','myelin');
img_BW_myelins=im2bw(bw_axonseg,0);
myelin_area=nnz(img_BW_myelins);
MVF_1=myelin_area/total_area;
struct_mvf = struct('MVF',MVF_1);
mvf_2 = struct2table(struct_mvf)
writetable(mvf_2,fullfile(savedir,'mvf.csv'));

total_area=size(img,1)*size(img,2);
bw_axonseg=as_display_label(axonlist,size(img),'axonEquivDiameter','axon');
img_BW_axons=im2bw(bw_axonseg,0);
axon_area=nnz(img_BW_axons);
AVF_1=axon_area/total_area;
struct_avf = struct('AVF',AVF_1);
avf_2 = struct2table(struct_avf)
writetable(avf_2,fullfile(savedir,'avf.csv'));

axon_area_1 = struct('axon_pixel_area', axon_area) 
axon_area_2 = struct2table(axon_area_1) 
writetable(axon_area_2,fullfile(savedir,'axon_pixel_area.csv')) 

myelin_area_1 = struct('myelin_pixel_area', myelin_area) 
myelin_area_2 = struct2table(myelin_area_1) 
writetable(myelin_area_2,fullfile(savedir,'myelin_pixel_area.csv'))


total_axon_almost = length(Axon_diameters)
total_axon_1 = num2str(total_axon_almost)
struct_total = struct('total_axon', total_axon_1)
total_axon_final = struct2table(struct_total)
writetable(total_axon_final,fullfile(savedir,'total_axon.csv'));
end 