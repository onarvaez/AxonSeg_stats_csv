#Metricas para nervio a 
vec_tap_a <- data.frame()
vec_axp_a <- data.frame()
vec_mp_a <- data.frame()
vec_totax_a <- data.frame()
vec_axlist_a <- data.frame()
for (i in c("ct01")){
  for (j in c("a")){
    for (k in c("1","2","3")){
      ###Aquí cargo todos los paths
      main_path <- ('/home/omar/Desktop/')
      exp_trat1 <- ("ct")
      sec_path <- (i)
      third_path <- (j)
      dir_path <- (k)
      dir_path_amxp <- ('img_t1_z1_c1_Segmentation/metrics/')
      file_name_tap <- ('Summary_total_pix.csv')
      file_name_axp <- ('axon_pixel_area.csv')
      file_name_mp <- ('myelin_pixel_area.csv')
      file_name_totax <- ('total_axon.csv')
      file_name_axlist <- ('axonlist_image.csv')
      full_path_tap_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',file_name_tap,sep = '')
      #print(full_path_tap)
      full_path_axp_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',dir_path_amxp,file_name_axp,sep = '')
      #print(full_path_axp)
      full_path_mp_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',dir_path_amxp,file_name_mp,sep = '')
      #print(full_path_mp)
      full_path_totax_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',dir_path_amxp,file_name_totax,sep = '')
      #print(full_path_totax)
      full_path_axlist_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',dir_path_amxp,file_name_axlist,sep = '')
      #print(full_path_axlist)
      
      ### Leer todos los archivos 
      file_a_tap <- read.csv(full_path_tap_a)
      file_a_axp <- read.csv(full_path_axp_a)
      file_a_mp <- read.csv(full_path_mp_a)
      file_a_totax <- read.csv(full_path_totax_a)
      file_a_axlist <- (read.csv(full_path_axlist_a))[-c(1,2,3,10)]
      
      ### Se colocan en su respectivo vector para ser concatenados
      vec_tap_a <- rbind(vec_tap_a,file_a_tap[1,])
      vec_axp_a <- rbind(vec_axp_a,file_a_axp[1,])
      vec_mp_a <- rbind(vec_mp_a,file_a_mp[1,])
      vec_totax_a <- rbind(vec_totax_a,file_a_totax[1,])
      vec_axlist_a <- rbind(vec_axlist_a,file_a_axlist)
      ### Se guardan los nuevos archivos concatenados de los 3 cortes de cada nervio
      final_tap_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"Summary_total_pix.csv",sep = '')
      final_axp_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"axon_pixel_cat.csv",sep = '')
      final_mp_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"myelin_pixel_cat.csv",sep = '')
      final_totax_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"total_axon_cat.csv",sep = '')
      final_axlist_a <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"axonlist_all_cat.csv",sep = '')
      write.csv(vec_tap_a,final_tap_a)
      write.csv(vec_axp_a,final_axp_a)
      write.csv(vec_mp_a,final_mp_a)
      write.csv(vec_totax_a,final_totax_a)
      write.csv(vec_axlist_a,final_axlist_a)
      
      ### Se hace la extracción de medias, medianas y ds de las concatenaciones
      mean_tap_a <- mean(vec_tap_a[,3])
      sum_tap_a <- sum(vec_tap_a[,3])
      mean_axp_a <- mean(vec_axp_a[,1])
      mean_mp_a <- mean(vec_mp_a[,1])
      mean_totax_a <- mean(vec_totax_a[,1])
      sum_totax_a <- sum(vec_totax_a[,1])
      std_totax_a <- sd(vec_totax_a[,1])
      axlist_mean_a <- apply(vec_axlist_a,2,mean)
      axlist_mean_a <- t(data.frame(axlist_mean_a))
      axlist_median_a <- apply(vec_axlist_a,2,median)
      axlist_median_a <- t(data.frame(axlist_median_a))
      axlist_sd_a <- apply(vec_axlist_a,2,sd)
      axlist_sd_a <- t(data.frame(axlist_sd_a))
      
      
      ### Las medias se colocan en variables como dataframes y se les asigna un nuevo nombre
      avf_a <- as.data.frame(mean_axp_a/mean_tap_a)
      colnames(avf_a) <- "avf"
      mvf_a <- as.data.frame(mean_mp_a/mean_tap_a)
      colnames(mvf_a) <- "mvf"
      total_axon_mean_a <- as.data.frame(mean_totax_a)
      colnames(total_axon_mean_a) <- "total_axon_mean"
      total_axon_std_a <- as.data.frame(std_totax_a)
      colnames(total_axon_std_a) <- "total_axon_std"
      axonlist_all_cat_mean_a <- as.data.frame(axlist_mean_a,optional = FALSE)
      colnames(axonlist_all_cat_mean_a) <- c("gRatio_mean","axon_diameter_mean","myelin_diameter_mean","mielyn_thickness_mean","myelin_area_mean","axon_area_mean")
      axonlist_all_cat_median_a <- as.data.frame(axlist_median_a,optional = FALSE)
      colnames(axonlist_all_cat_median_a) <- c("gRatio_median","axon_diameter_median","myelin_diameter_median","mielyn_thickness_median","myelin_area_median","axon_area_median")
      axonlist_all_cat_sd_a <- as.data.frame(axlist_sd_a,optional = FALSE)
      colnames(axonlist_all_cat_sd_a) <- c("gRatio_sd","axon_diameter_sd","myelin_diameter_sd","mielyn_thickness_sd","myelin_area_sd","axon_area_sd")
      axon_per_micra_a <- as.data.frame(sum_totax_a/(sum_tap_a*(.165*.165)),row.names = NULL)
      colnames(axon_per_micra_a) <- c("axon_per_micra")
      ### Se hace merge de todos los dataframes para que queden en un solo renglon
      axonlist_pre_a <- merge(axonlist_all_cat_mean_a,axonlist_all_cat_median_a)
      axonlist_all_par_ax_a <- merge(axonlist_pre_a,axonlist_all_cat_sd_a)
      axonlist_all_par_mvf_a <- merge(axonlist_all_par_ax_a,mvf_a)
      axonlist_all_par_mvf_avf_a <- merge(axonlist_all_par_mvf_a,avf_a)
      axonlist_all_par_mvf_avf_tot_m_a <- merge(axonlist_all_par_mvf_avf_a,total_axon_mean_a)
      axonlist_all_par_mvf_avf_tot_m_sd_a <- merge(axonlist_all_par_mvf_avf_tot_m_a,total_axon_std_a)
      axonlist_all_cat_a <- merge(axonlist_all_par_mvf_avf_tot_m_sd_a,axon_per_micra_a)
      
      rownames(axonlist_all_cat_a) <- "ct01"
      
      #Se guardan las medias, medianas, ds y concatenación final 
      write.csv(avf_a,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"avf.csv",sep = ''))
      write.csv(mvf_a,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"mvf.csv",sep = ''))
      write.csv(total_axon_mean_a,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"total_axon_mean.csv",sep = ''))
      write.csv(total_axon_std_a,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"total_axon_std.csv",sep = ''))
      write.csv(axonlist_all_cat_a,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"axonlist_stats_all.csv",sep = ''))
      
      
    }
  }
}

#Ahora para b

vec_tap_b <- data.frame()
vec_axp_b <- data.frame()
vec_mp_b <- data.frame()
vec_totax_b <- data.frame()
vec_axlist_b <- data.frame()
for (i in c("ct01")){
  for (j in c("b")){
    for (k in c("1","2","3")){
      ###Aquí cargo todos los paths
      main_path <- ('/home/omar/Desktop/')
      exp_trat1 <- ("ct")
      sec_path <- (i)
      third_path <- (j)
      dir_path <- (k)
      dir_path_amxp <- ('img_t1_z1_c1_Segmentation/metrics/')
      file_name_tap <- ('Summary_total_pix.csv')
      file_name_axp <- ('axon_pixel_area.csv')
      file_name_mp <- ('myelin_pixel_area.csv')
      file_name_totax <- ('total_axon.csv')
      file_name_axlist <- ('axonlist_image.csv')
      full_path_tap_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',file_name_tap,sep = '')
      #print(full_path_tap)
      full_path_axp_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',dir_path_amxp,file_name_axp,sep = '')
      #print(full_path_axp)
      full_path_mp_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',dir_path_amxp,file_name_mp,sep = '')
      #print(full_path_mp)
      full_path_totax_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',dir_path_amxp,file_name_totax,sep = '')
      #print(full_path_totax)
      full_path_axlist_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',dir_path,'/',dir_path_amxp,file_name_axlist,sep = '')
      #print(full_path_axlist)
      
      ### Leer todos los archivos 
      file_b_tap <- read.csv(full_path_tap_b)
      file_b_axp <- read.csv(full_path_axp_b)
      file_b_mp <- read.csv(full_path_mp_b)
      file_b_totax <- read.csv(full_path_totax_b)
      file_b_axlist <- (read.csv(full_path_axlist_b))[-c(1,2,3,10)]
      
      ### Se colocan en su respectivo vector para ser concatenados
      vec_tap_b <- rbind(vec_tap_b,file_b_tap[1,])
      vec_axp_b <- rbind(vec_axp_b,file_b_axp[1,])
      vec_mp_b <- rbind(vec_mp_b,file_b_mp[1,])
      vec_totax_b <- rbind(vec_totax_b,file_b_totax[1,])
      vec_axlist_b <- rbind(vec_axlist_b,file_b_axlist)
      ### Se guardan los nuevos archivos concatenados de los 3 cortes de cada nervio
      final_tap_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"Summary_total_pix.csv",sep = '')
      final_axp_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"axon_pixel_cat.csv",sep = '')
      final_mp_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"myelin_pixel_cat.csv",sep = '')
      final_totax_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"total_axon_cat.csv",sep = '')
      final_axlist_b <- paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"axonlist_all_cat.csv",sep = '')
      write.csv(vec_tap_b,final_tap_b)
      write.csv(vec_axp_b,final_axp_b)
      write.csv(vec_mp_b,final_mp_b)
      write.csv(vec_totax_b,final_totax_b)
      write.csv(vec_axlist_b,final_axlist_b)
      
      ### Se hace la extracción de medias, medianas y ds de las concatenaciones
      mean_tap_b <- mean(vec_tap_b[,3])
      sum_tap_b <- sum(vec_tap_b[,3])
      mean_axp_b <- mean(vec_axp_b[,1])
      mean_mp_b <- mean(vec_mp_b[,1])
      mean_totax_b <- mean(vec_totax_b[,1])
      sum_totax_b <- sum(vec_totax_b[,1])
      std_totax_b <- sd(vec_totax_b[,1])
      axlist_mean_b <- apply(vec_axlist_b,2,mean)
      axlist_mean_b <- t(data.frame(axlist_mean_b))
      axlist_median_b <- apply(vec_axlist_b,2,median)
      axlist_median_b <- t(data.frame(axlist_median_b))
      axlist_sd_b <- apply(vec_axlist_b,2,sd)
      axlist_sd_b <- t(data.frame(axlist_sd_b))
      
      
      ### Las medias se colocan en variables como dataframes y se les asigna un nuevo nombre
      avf_b <- as.data.frame(mean_axp_b/mean_tap_b)
      colnames(avf_b) <- "avf"
      mvf_b <- as.data.frame(mean_mp_b/mean_tap_b)
      colnames(mvf_b) <- "mvf"
      total_axon_mean_b <- as.data.frame(mean_totax_b)
      colnames(total_axon_mean_b) <- "total_axon_mean"
      total_axon_std_b <- as.data.frame(std_totax_b)
      colnames(total_axon_std_b) <- "total_axon_std"
      axonlist_all_cat_mean_b <- as.data.frame(axlist_mean_b,optional = FALSE)
      colnames(axonlist_all_cat_mean_b) <- c("gRatio_mean","axon_diameter_mean","myelin_diameter_mean","mielyn_thickness_mean","myelin_area_mean","axon_area_mean")
      axonlist_all_cat_median_b <- as.data.frame(axlist_median_b,optional = FALSE)
      colnames(axonlist_all_cat_median_b) <- c("gRatio_median","axon_diameter_median","myelin_diameter_median","mielyn_thickness_median","myelin_area_median","axon_area_median")
      axonlist_all_cat_sd_b <- as.data.frame(axlist_sd_b,optional = FALSE)
      colnames(axonlist_all_cat_sd_b) <- c("gRatio_sd","axon_diameter_sd","myelin_diameter_sd","mielyn_thickness_sd","myelin_area_sd","axon_area_sd")
      axon_per_micra_b <- as.data.frame(sum_totax_b/(sum_tap_b*(.165*.165)),row.names = NULL)
      colnames(axon_per_micra_b) <- c("axon_per_micra")
      ### Se hace merge de todos los dataframes para que queden en un solo renglon
      axonlist_pre_b <- merge(axonlist_all_cat_mean_b,axonlist_all_cat_median_b)
      axonlist_all_par_ax_b <- merge(axonlist_pre_b,axonlist_all_cat_sd_b)
      axonlist_all_par_mvf_b <- merge(axonlist_all_par_ax_b,mvf_b)
      axonlist_all_par_mvf_avf_b <- merge(axonlist_all_par_mvf_b,avf_b)
      axonlist_all_par_mvf_avf_tot_m_b <- merge(axonlist_all_par_mvf_avf_b,total_axon_mean_b)
      axonlist_all_par_mvf_avf_tot_m_sd_b <- merge(axonlist_all_par_mvf_avf_tot_m_b,total_axon_std_b)
      axonlist_all_cat_b <- merge(axonlist_all_par_mvf_avf_tot_m_sd_b,axon_per_micra_b)
      
      rownames(axonlist_all_cat_b) <- "ct01"
      
      #Se guardan las medias, medianas, ds y concatenación final 
      write.csv(avf_b,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"avf.csv",sep = ''))
      write.csv(mvf_b,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"mvf.csv",sep = ''))
      write.csv(total_axon_mean_b,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"total_axon_mean.csv",sep = ''))
      write.csv(total_axon_std_b,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"total_axon_std.csv",sep = ''))
      write.csv(axonlist_all_cat_b,paste(main_path,exp_trat1,'/',sec_path,'/',third_path,'/',"axonlist_stats_all.csv",sep = ''))
      
      
    }
  }
}




##invoke library(purrr)