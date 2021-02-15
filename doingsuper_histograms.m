close all 
clc
figure;
hold on
bins = 0.0:0.06:3; 
%ajuste de datos a una densidad de kernel
[f,xi] = ksdensity(axondiam_dam);
[g,hi] = ksdensity(axondiam_intact);
%histograma del intacto
h= histogram(axondiam_intact,bins);
%reescalamiento de densidad al tamaño de histograma
g=max(h.Values)*g/max(g);
%linea de densidad reescalada
plot(hi,g,'r','LineWidth',2)
%lo mismo que tres lineas anteriores pero para el dañado
t= histogram(axondiam_dam,bins);
f= max(t.Values)*f/max(f);
plot(xi,f,'g','LineWidth',2)
%maximo de densidad de datos dañados
[hg,hgi] = max(f);
%maximo de densidad de datos intact
[pg,pgi] = max(f);
%medianas
median_dam = median(axondiam_dam);
median_intact = median(axondiam_intact);
%medias
mean_dam = mean(axondiam_dam);
mean_intact = mean(axondiam_intact);
%obtener el indice de la posicion mas cercana a mediana 
fg = abs(xi-median_dam);
[fg_min, fg_idx]= min(fg);
%obtener el indice de la posicion mas cercana a mediana intact
hp = abs(hi-median_intact);
[hp_min, hp_idx]= min(hp);
%obtener el indice de la posicion mas cercana a media
tg = abs(xi-mean_dam);
[tg_min, tg_idx]= min(tg);
%obtener el indice de la posicion mas cercana a media intact
ht = abs(hi-mean_intact);
[ht_min, ht_idx]= min(ht);
%valor de la densidad en la posición más cercana a la mediana dañado
ti= f(fg_idx);
%valor de la densidad en la posición más cercana a la mediana intact
th= g(hp_idx);
%valor de la densidad en la posición más cercana a la media dañado
tip= f(tg_idx);
%valor de la densidad en la posición más cercana a la media intact
thp= g(ht_idx);
%dibujar linea en posición más cercana a la mediana con un tamaño del 10%
%del máximo de la densidad 
plot([median_dam median_dam], [ti-.2*hg ti+.2*hg], 'c','LineWidth',2)
plot([median_intact median_intact], [th-.2*pg th+.2*pg], 'c','LineWidth',2)

plot([mean_dam mean_dam], [tip-.2*hg tip+.2*hg], 'c','LineWidth',2)
plot([mean_intact mean_intact], [thp-.2*pg thp+.2*pg], 'c','LineWidth',2)



% ye = 10000
% hax=axes;
% meandas=0.0:0.06:3;
% plot(mean_dam,ye)
% SP=mean_dam; %your point goes here
% line([SP SP],get(hax,'YLim'),'Color',[1 0 0])

% hold on 
% [N,edges] = histcounts(axondiam_dam,bins,'Normalization','probability');
% histogram(axondiam_dam,bins,'Normalization','probability');
% hold on 
% plot(edges(1:end-1),N)
% histogram(axondiam_intact,bins,'Normalization','probability');







% format long

% folder = '/misc/torrey/onarvaez/ex_vivo/lps/lps01/past/stats/';
% stats = {'mean','median','std','min','max','count'};
% metric = {'fa','adc','rd','ad'};
% 
% nname = {'stats_op_l', 'stats_op_r'};
% ext   = '.txt';
% ns = length(stats);
% nm = length(metric);
% nn = length(nname);
% A = zeros(nm,ns,nn);
% for l = 1:nn 
% for k = 1:nm
% for i = 1:ns
%     fname = [folder nname{l} '_' metric{k} '_' stats{i} ext];
%     a = load(fname);
%     A(k,i,l) = a;
% end
% end
% end
% Al = A(:,:,1);
% Ar = A(:,:,2);
% 
% 
% rowNames = {'fa','adc','rd','ad'};
% colNames = {'mean','median','std', 'min','max','count'};
% sTable_l = array2table(Al,'RowNames',rowNames,'VariableNames',colNames)
% sTable_r = array2table(Ar,'RowNames',rowNames,'VariableNames',colNames)
% 
% % num2str
% % str2num
