im = imread('/misc/torrey/onarvaez/Omar-C13/21-03-18/INB-00-0007/INB-00-0007_p20.TIF',1);
fondo = imread('/misc/torrey/onarvaez/Omar-C13/21-03-18/INB-00-0009-2/INB-00-0009-2_p20.TIF',1);

imf = single(im);
fondof = single(fondo);
%
biasfield = fondof ./ max(fondof(:));
im_final = uint8(imf ./ biasfield) 
colorbar
set(gca,'CLim',[0 255]);
imwrite(im_final, 'image_div20.tif')



%imagesc(imf)
%colorbar
%set(gca,'CLim',[0 255]);


%imagesc(fondof)
%colorbar
%set(gca,'CLim',[0 255]);
