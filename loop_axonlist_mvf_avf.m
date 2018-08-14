
files = {'axonlist_full_image.mat'}
     
   

for index = 1 : length(files)
	thisfile = files{index}; 
	fprintf(1,'file name for index %d is %s\n',index,thisfile)
	axonlist_der_files_mozaic(thisfile)
end 
