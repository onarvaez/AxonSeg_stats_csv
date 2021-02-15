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
[gh,ghi] = max(g);
%medianas dañado e intacto
median_dam = median(axondiam_dam);
median_intact = median(axondiam_intact);
%obtener el indice de la posicion mas cercana a mediana dañado
fg = abs(xi-median_dam);
[fg_min, fg_idx]= min(fg);
%obtener el indice de la posicion mas cercana a mediana intacto
gg = abs(hi-median_intact);
[gg_min, gg_idx]= min(gg);
%valor de la densidad en la posición más cercana a la mediana 
ti= f(fg_idx);
gi= g(gg_idx);
%dibujar linea en posición más cercana a la mediana con un tamaño del 10%
%del máximo de la densidad 
plot([median_dam median_dam], [ti-.2*hg ti+.2*hg], 'c','LineWidth',2)
plot([median_intact median_intact], [gi-.05*gh gi+.05*gh], 'c','LineWidth',2)