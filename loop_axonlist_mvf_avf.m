
files = {'axonlist_full_image.mat'}
     
   

for index = 1 : length(files)
	thisfile = files{index}; 
	fprintf(1,'file name for index %d is %s\n',index,thisfile)
	axonlist_stats_mvf_avf_mozaic(thisfile)
end 
