
files = {'/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/1/img_t1_z1_c1_Segmentation/axonlist_full_image.mat'}
         %'/misc/torrey/onarvaez/M-isq/ct/PQR-ISQ-01/PQR-ISQ-01_b/INB-00-0041/img_t1_z1_c1_Segmentation/axonlist_full_image.mat'...
         %'/misc/torrey/onarvaez/M-isq/ct/PQR-ISQ-01/PQR-ISQ-01_b/INB-00-0043/img_t1_z1_c1_Segmentation/axonlist_full_image.mat'...
     
   

for index = 1 : length(files)
	thisfile = files{index}; 
	fprintf(1,'file name for index %d is %s\n',index,thisfile)
	axonlist_stats_mvf_avf_mozaic(thisfile)
end 