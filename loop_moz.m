
files = {'image.tif'}
     
SegParameters = 'SegParameters.mat'


for index = 1 : length(files)
	thisfile = files{index}; 
    [this_dir, this_file, this_ext]= fileparts(thisfile);
 	fprintf(1,'file name for index %d is %s\n',index,thisfile)
    cd(this_dir)
	AxonSeg(thisfile, SegParameters, '-nogui')
end 
