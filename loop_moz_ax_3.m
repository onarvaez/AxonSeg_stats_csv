
files = {'/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/1/img_t1_z1_c1.tif'...
         '/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/2/img_t1_z1_c1.tif'...
         '/misc/torrey/onarvaez/M-isq/isq/isq04/right_intact/analisis/3/img_t1_z1_c1.tif'}
     
SegParameters = '/misc/torrey/onarvaez/M-isq/SegParameters.mat'


for index = 1 : length(files)
	thisfile = files{index}; 
    [this_dir, this_file, this_ext]= fileparts(thisfile);
%     savedir=[this_dir filesep 'output' filesep];
%     mkdir(savedir);
 	fprintf(1,'file name for index %d is %s\n',index,thisfile)
    cd(this_dir)
	AxonSeg(thisfile, SegParameters, '-nogui')
end 