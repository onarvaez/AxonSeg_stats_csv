# AxonSeg_stats_csv

Neuropoly/AxonSeg_stats_extraction and total axon count

## Segmentación de mielina y axones con AxonSeg

1.- Utilizar loop_moz.m para realizar la segmentación con AxonSeg en todas las imágenes necesarias. Cada imagen generará una carpeta con el nombre de la imagen + Segmentation (e.g. mozaic_Segmentation) y tendrá: 

```
axonEquivDiameter_(axon)_0_xum.png
axonEquivDiameter_(myelin)_0_xum.png
axonlist_full_image.mat
```
## Extracción de métricas de axonlist

2.- Para extraer las métricas del archivo "axonlist_full_image.mat" utilizar "axonlist_der_files_mozaic.m" si es una imagen, o utilizar "loop_axonlist_der_files.m" si se requiere en varias. Este proceso generará una carpeta llamada "metrics" (dentro de imagen_Segmentation) por cada imagen, la cúal contendrá:

```
axonlist_image.csv
axon_pixel_area.csv
myelin_pixel_area.csv
stats_image.csv
total_axon.csv
avf.csv (solo si se quita el comentario de la linea 82 de axonlist_stats_mvf_avf.m)
mvf.csv (solo si se quita el comentario de la linea 91 de axonlist_stats_mvf_avf.m)
```
Los últimos dos archivos se omiten si el conteo axonal se realizó en un mozaico que abarca un área mayor a la de interés, de lo contrario, se puede quitar el comentario en esas líneas y obtener esos datos directamente.

## Obtención de avf y mvf para mozaicos 

3.-Para la obtención de la avf y mvf en mozaicos es necesario realizar una máscara del área total de interes. Dicha máscara se abre en ImageJ, se aplica un umbral (Image >> Adjust >> Threshold) y después se cuantifica la cantidad de pixeles correspondientes a la máscara del área de interés (Analize >> Analyze particles) y guardar el "summary" 

```
Summary_total_pix.csv
```
## Concatenar axonlist de imágenes (varios ensayos, misma muestra)

4.- Utilizar "stats_all_image.m" para concatenar los axonlist de las imagenes tomadas de la misma muestra para obtener el archivo de todos los "axonlist" y la "stat" de dicha concatenación, por lo tanto ahora habrán dos archivos más:
```
axonlist_image_all.csv
stats_image_all.csv
```
Nota. Por ahora es necesario cambiar de ruta cada que se generan estos dos nuevos archivos, sino se guardarán en la carpeta de alguna de las imágenes y creará una sobreescritura cada que corra

## Concatenar stats de imágenes (varios ensayos, misma muestra) - Ponderación

5.- Utilizar "stats_per_image.m" para concatenar las "stats" de las imágenes tomadas de la misma muestra para obtener el archivo de todos los "stats" y la stat ponderada de dicha concatenación, por lo tanto ahora habrán dos archivos más:
```
axonlist_stats_per_image.csv
stats_per_image.csv
```
Nota. Por ahora es necesario cambiar de ruta cada que se generan estos dos nuevos archivos, sino se guardarán en la carpeta de alguna de las imágenes y creará una sobreescritura cada que corra




![axonequivdiameter_ axon _0_3um](https://user-images.githubusercontent.com/32722299/44066222-ca730554-9f34-11e8-949a-b95e86780909.png) 
