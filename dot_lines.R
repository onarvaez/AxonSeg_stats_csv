data_file <- read.csv("C:/Users/Narvaez/Desktop/histologia_borrar/histologia_borrar/concat_all_first_dif.csv")
data_file$grupo <- as.factor(data_file$grupo)
library(ggplot2)
library(filesstrings)
library(plotly)
library(viridis)
library(cowplot)
library(gridExtra)
library(corrplot)

dir.create("C:/Users/Narvaez/Desktop/histologia_borrar/histologia_borrar/box_ind")
graph_dest <- "C:/Users/Narvaez/Desktop/histologia_borrar/histologia_borrar/box_ind"

rowname_data <- c("gRatio_mean","axon_diameter_mean","myelin_diameter_mean","mielyn_thickness_mean","myelin_area_mean","axon_area_mean","gRatio_median",	
                  "axon_diameter_median","myelin_diameter_median","myelin_thickness_median","myelin_area_median","axon_area_median","mvf","avf","total_axon_mean","axon_per_micra",
                  "AFD_mean", "AFD_median","AFDm_mean","AFDm_median","Cx_mean","Cx_median","Disp_mean","Disp_median","Peak_mean","Peak_median",	
                  "Ax_mrds_mean","Ax_mrds_median","Fa_mrds_mean","Fa_mrds_median","Md_mrds_mean","Md_mrds_median","Rd_mrds_mean","Rd_mrds_median",
                  "Sizes_mrds_mean","Sizes_mrds_median","Ax_tensor_mean","Ax_tensor_median","Fa_tensor_mean","Fa_tensor_median","Md_tensor_mean",
                  "Md_tensor_median","Rd_tensor_mean","Rd_tensor_median","AFD_mean_c","AFD_median_c","AFDm_mean_c","AFDm_median_c","Disp_mean_c","Disp_median_c","Peak_mean_c",	
                  "Peak_median_c","Ax_mrds_mean_c","Ax_mrds_median_c","Fa_mrds_mean_c","Fa_mrds_median_c","Md_mrds_mean_c","Md_mrds_median_c","Rd_mrds_mean_c","Rd_mrds_median_c","Sizes_mrds_mean_c","Sizes_mrds_median_c")

plot_name <- c("Tasa-g","Diametro axonal (\u03BCm)","Diametro axonal con mielina (\u03BCm)","Grosor de mielina (\u03BCm)","Area de mielina (\u03BCm\u00B2)","Area axonal (\u03BCm\u00B2)","Tasa-g","Diametro axonal (\u03BCm)","Diametro axonal con mielina (\u03BCm)",
               "Grosor de mielina (\u03BCm)","Area de mielina (\u03BCm\u00B2)","Area axonal (\u03BCm\u00B2)","Fracción de volumen de mielina","Fracción de volumen axonal","Número de axones","Densidad axonal (axones/\u03BCm\u00B2)",
               "AFD_mean", "AFD_median","AFDm_mean","AFDm_median","Cx_mean","Cx_median","Disp_mean","Disp_median","Peak_mean","Peak_median",	
               "Ax_mrds_mean","Ax_mrds_median","Fa_mrds_mean","Fa_mrds_median","Md_mrds_mean","Md_mrds_median","Rd_mrds_mean","Rd_mrds_median",
               "Sizes_mrds_mean","Sizes_mrds_median","Ax_tensor_mean","Ax_tensor_median","Fa_tensor_mean","Fa_tensor_median","Md_tensor_mean",
               "Md_tensor_median","Rd_tensor_mean","Rd_tensor_median","AFD_mean_c","AFD_median_c","AFDm_mean_c","AFDm_median_c","Disp_mean_c","Disp_median_c","Peak_mean_c",	
               "Peak_median_c","Ax_mrds_mean_c","Ax_mrds_median_c","Fa_mrds_mean_c","Fa_mrds_median_c","Md_mrds_mean_c","Md_mrds_median_c","Rd_mrds_mean_c","Rd_mrds_median_c","Sizes_mrds_mean_c","Sizes_mrds_median_c")

graph_save <- c("gRatio_mean.svg","axon_diameter_mean.svg","myelin_diameter_mean.svg","mielyn_thickness_mean.svg","myelin_area_mean.svg","axon_area_mean.svg","gRatio_median.svg",	
                "axon_diameter_median.svg","myelin_diameter_median.svg","myelin_thickness_median.svg","myelin_area_median.svg","axon_area_median.svg","mvf.svg","avf.svg","total_axon_mean.svg","axon_per_micra.svg",
                "AFD_mean.svg", "AFD_median.svg","AFDm_mean.svg","AFDm_median.svg","Cx_mean.svg","Cx_median.svg","Disp_mean.svg","Disp_median.svg","Peak_mean.svg","Peak_median.svg",	
                "Ax_mrds_mean.svg","Ax_mrds_median.svg","Fa_mrds_mean.svg","Fa_mrds_median.svg","Md_mrds_mean.svg","Md_mrds_median.svg","Rd_mrds_mean.svg","Rd_mrds_median.svg",
                "Sizes_mrds_mean.svg","Sizes_mrds_median.svg","Ax_tensor_mean.svg","Ax_tensor_median.svg","Fa_tensor_mean.svg","Fa_tensor_median.svg","Md_tensor_mean.svg",
                "Md_tensor_median.svg","Rd_tensor_mean.svg","Rd_tensor_median.svg","AFD_mean_c.svg","AFD_median_c.svg","AFDm_mean_c.svg","AFDm_median_c.svg","Disp_mean_c.svg","Disp_median_c.svg","Peak_mean_c.svg",	
                "Peak_median_c.svg","Ax_mrds_mean_c.svg","Ax_mrds_median_c.svg","Fa_mrds_mean_c.svg","Fa_mrds_median_c.svg","Md_mrds_mean_c.svg","Md_mrds_median_c.svg","Rd_mrds_mean_c.svg","Rd_mrds_median_c.svg","Sizes_mrds_mean_c.svg","Sizes_mrds_median_c.svg")

gf <- c(1:97)
for (i in 1:length(gf)){
data_file$grupo <- as.factor(data_file$grupo)
p <- ggplot(data_file, aes_string(x="X", y=rowname_data[i], fill="grupo")) +
      geom_boxplot(position=position_dodge(.5), alpha=.6,width=0.7/length(unique(data_file$grupo)),aes(color = grupo)) +
      geom_boxplot(aes(color = grupo),
             fatten = NULL, fill = NA, coef = 0, outlier.alpha = 0,
             show.legend = F,width=0.7/length(unique(data_file$grupo)),position=position_dodge(.5))+
      geom_dotplot(binaxis='y', stackdir='center', 
                   position=position_dodge(.5),width=0.7/length(unique(data_file$grupo)),dotsize =.4,alpha=.4) +
  labs(x="Dias posteriores a la isquemia", y = plot_name[i])+
  scale_x_discrete(limits=c("ct","isq1d","isq7d","isq30d")) +
  scale_color_manual(values=c("#00BFC4", "#F8766D")) +
  scale_fill_manual(values=c("#00BFC4", "#F8766D")) +
  stat_summary(geom = "crossbar", position=position_dodge(.5),width=0.7/length(unique(data_file$grupo)), fatten=0, color="black", fun.data = function(x){ return(c(y=median(x), ymin=median(x), ymax=median(x))) })+
  stat_summary(fun.y=median, geom="line", position=position_dodge(.5),aes(group=grupo,color=grupo),size=.2)  + 
  #stat_summary(fun.y=median, geom="point",position=position_dodge(.5)) +
  theme_minimal(base_size = 12) 
  #theme(legend.position="none") 
  ggsave(graph_save[i],device = svg,height = 7, width = 10)
  file.move(graph_save[i],graph_dest)
print(p)    
}




# data_file$grupo <- as.factor(data_file$grupo)
# p <- ggplot(data_file, aes(x=X, y=Ax_tensor_median, fill=grupo)) +
#   geom_boxplot(position=position_dodge(.5), alpha=.6,width=0.7/length(unique(data_file$grupo)),aes(color = grupo)) +
#   geom_boxplot(aes(color = grupo),
#                fatten = NULL, fill = NA, coef = 0, outlier.alpha = 0,
#                show.legend = F,width=0.7/length(unique(data_file$grupo)),position=position_dodge(.5))+
#   geom_dotplot(binaxis='y', stackdir='center', 
#                position=position_dodge(.5),width=0.7/length(unique(data_file$grupo)),dotsize =.4,alpha=.4) +
#   labs(x="Dias posteriores a la isquemia", y ="plot_name[i]")+
#   scale_x_discrete(limits=c("ct","isq1d","isq7d","isq30d")) +
#   scale_color_manual(values=c("#00BFC4", "#F8766D")) +
#   scale_fill_manual(values=c("#00BFC4", "#F8766D")) +
#   stat_summary(geom = "crossbar", position=position_dodge(.5),width=0.7/length(unique(data_file$grupo)), fatten=0, color="black", fun.data = function(x){ return(c(y=median(x), ymin=median(x), ymax=median(x))) })+
#   stat_summary(fun.y=median, geom="line", position=position_dodge(.5),aes(group=grupo,color=grupo),size=.2)  + 
#   #stat_summary(fun.y=median, geom="point",position=position_dodge(.5)) +
#   theme_minimal(base_size = 12) 
# #theme(legend.position="none") 
# #ggsave(graph_save[i],device = svg)
# #file.move(graph_save[i],graph_dest)
# p
#ggplotly(p)    
#"Axon density (axons/\u03BCm\u00B2)","Axon volume fraction (AVF)","Myelin volume fraction (MVF)","g-Ratio","Axon diameter (\u03BCm)","Myelin thickness (\u03BCm)"




dir.create("C:/Users/Narvaez/Desktop/histologia_borrar/histologia_borrar/dot_both")
graph_dest1 <- "C:/Users/Narvaez/Desktop/histologia_borrar/histologia_borrar/dot_both"


hist <- c("gRatio_mean","axon_diameter_mean","myelin_diameter_mean","mielyn_thickness_mean","myelin_area_mean","axon_area_mean",	
          "mvf","avf","total_axon_mean","axon_per_micra")
diff <- c("AFD_mean","AFDm_mean","Cx_mean","Disp_mean","Peak_mean",	
          "Ax_mrds_mean","Fa_mrds_mean","Md_mrds_mean","Rd_mrds_mean",
          "Sizes_mrds_mean","Ax_tensor_mean","Fa_tensor_mean","Md_tensor_mean",
          "Rd_tensor_mean","AFD_mean_c","AFDm_mean_c","Disp_mean_c","Peak_mean_c",	
          "Ax_mrds_mean_c","Fa_mrds_mean_c","Md_mrds_mean_c","Rd_mrds_mean_c","Sizes_mrds_mean_c")


####works but mejorara

for (i in hist){
  for (j in diff){
p <- ggplot(data =data_file,aes_string(x="X", y=i, color="grupo", size = j))+
  geom_point(alpha=.8,aes_string(size= j),position = position_jitter(w = 0.1, h = 0))+
  scale_color_manual(breaks = c("Intacto", "Lesionado"),
                     values=c("#00BFC4", "#F8766D")) +
  scale_x_discrete(limits=c("ct","isq1d","isq7d","isq30d")) +
  labs(x="Dias posteriores a la isquemia", y = i) +
  theme_minimal(base_size = 12)
print(p)
ggsave(paste(i,"_",j,".svg",sep = ""),device = svg, height = 7, width = 10)
file.move(paste(i,"_",j,".svg",sep = ""),graph_dest1)
  }
}


#######

p <- ggplot(data =data_file,aes(x=X, y=avf, size = AFD_mean_c,color=grupo))+
  geom_point(alpha=.8,aes(size= AFD_mean_c),position = position_jitter(w = 0.1, h = 0))+
  #scale_color_gradientn(colours = plasma(100))+
  scale_color_manual(breaks = c("Intacto", "Lesionado"),
                     values=c("#00BFC4", "#F8766D")) +
  scale_x_discrete(limits=c("ct","isq1d","isq7d","isq30d")) +
  ggsave(paste("avf","_","AFD_mean_c",".svg",sep = ""),device = svg, height = 9, width = 12) +
  theme_minimal(base_size = 12)
print(p)

#ggplotly(p)


# Make a basic scatter plot :




# color_row_bubble_median <- c("AFD_median","AFDm_median","Cx_median","Disp_median","Peak_median",	
#                       "Ax_mrds_median","Fa_mrds_median","Md_mrds_median","Rd_mrds_median",
#                       "Sizes_mrds_median","Ax_tensor_median","Fa_tensor_median",
#                       "Md_tensor_median","Rd_tensor_median","AFD_median_c","AFDm_median_c","Disp_median_c",	
#                       "Peak_median_c","Ax_mrds_median_c","Fa_mrds_median_c","Md_mrds_median_c","Rd_mrds_median_c","Sizes_mrds_median_c")
# 
#dft_nerve
dft <- data_file[,-c(1,3,25,28,29,31,32,34,35,37,38,40,41,43,44,46,47,49,50,52,53,55,56,58,59,61,62,64,65,67,68,c(10:21),c(69:95))]
#dft_chiasm
#dft <- data_file[,-c(1,3,25,c(10:21),c(27:68),70,71,73,74,76,77,79,80,82,83,85,86,88,89,91,92,94,95)]

rows <- as.matrix(dft[1])
dft <- dft[-1]
dft_col <- t(matrix(c(1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)))
dft_col <- as.numeric(dft_col)

M <- cor(dft)
res1 <- cor.mtest(dft, conf.level = .95)

Mp <- corrplot::cor.mtest(M)$p
corrplot(M, p.mat = res1$p, method = "color", type = "lower", title = "",
         sig.level =.05,
         insig = "blank",outline = T, addgrid.col = "white", tl.srt = 45, tl.col = "black",bg="gray86",tl.cex = .7, col = viridis(200))



#Interactive corplot
library(qtlcharts)
#spearman <- cor(dft, use="pairwise.complete.obs", method="spearman")

corrplot_nerve <- iplotCorr(dft,dft_col,reorder=FALSE,
                            chartOpts=list(scatcolors=c("Deepskyblue", "mediumseagreen", "tomato"),rectcolor = "#EFF5FB",pointsize = 5,
                                           margin = list(left=260, top=40, right=50, bottom=80, inner=20),cortitle = "Correlations",
                                           corcolors=c("steelblue", "white", "orange"),
                                           scattitle = "Scatter", height=600, width=1600, caption=paste("Click on the heatmap on the left to see",
                                                                                                        "corresponding scatterplots on the right.")))
corrplot_nerve



#some normality tests
cts <- dft[-c(5,6,7,8,9),]
cts_2 <- dft[-c(1,2,3,4,10,11,12,13,14,15,16,17,18),]
library(ggpubr)
ggqqplot(cts$avf)
ggdensity(cts$avf, 
          main = "Density plot of tooth length",
          xlab = "Tooth length")
shapiro.test(cts$avf)

ggqqplot(cts_2$AFD_median)
ggdensity(cts_2$AFD_median, 
          main = "Density plot of tooth length",
          xlab = "Tooth length")
shapiro.test(cts_2$AFD_median)


