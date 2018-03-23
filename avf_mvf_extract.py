#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:24:51 2018

@author: onarvaez
"""

import pandas as pd

col_chiasm_avf=["chiasm_avf"]
col_chiasm_mvf=["chiasm_mvf"]
col_nerve_a_ct_avf=["nerve_a_ct_avf"]
col_nerve_a_ct_mvf=["nerve_a_ct_mvf"]
col_nerve_b_ct_avf=["nerve_b_ct_avf"]
col_nerve_b_ct_mvf=["nerve_b_ct_mvf"]

col_chiasm_exp_avf=["chiasm_exp_avf"]
col_chiasm_exp_mvf=["chiasm_exp_mvf"]
col_nerve_degenerated_exp_avf=["nerve_degenerated_avf"]
col_nerve_degenerated_exp_mvf=["nerve_degenerated_mvf"]
col_nerve_intact_exp_avf=["nerve_intact_avf"]
col_nerve_intact_exp_mvf=["nerve_intact_mvf"]

#control chiasm
ct01_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct01/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_avf)
ct01_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct01/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_mvf)
ct02_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct02/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_avf)
ct02_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct02/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_mvf)
ct03_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct03/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_avf)
ct03_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct03/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_mvf)
ct04_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct04/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_avf)
ct04_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct04/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_mvf)
ct05_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct05/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_avf)
ct05_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct05/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_mvf)

#control nerve_a
ct01_a_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct01/histology/nerve_a_intact/proc/avf_cat.csv', names=col_nerve_a_ct_avf)
ct01_a_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct01/histology/nerve_a_intact/proc/mvf_cat.csv', names=col_nerve_a_ct_mvf)
ct02_a_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct02/histology/nerve_a_intact/proc/avf_cat.csv', names=col_nerve_a_ct_avf)
ct02_a_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct02/histology/nerve_a_intact/proc/mvf_cat.csv', names=col_nerve_a_ct_mvf)
ct03_a_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct03/histology/nerve_a_intact/proc/avf_cat.csv', names=col_nerve_a_ct_avf)
ct03_a_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct03/histology/nerve_a_intact/proc/mvf_cat.csv', names=col_nerve_a_ct_mvf)
ct04_a_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct04/histology/nerve_left_intact/proc/avf_cat.csv', names=col_nerve_a_ct_avf)
ct04_a_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct04/histology/nerve_left_intact/proc/mvf_cat.csv', names=col_nerve_a_ct_mvf)
ct05_a_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct05/histology/nerve_a_intact/proc/avf_cat.csv', names=col_nerve_a_ct_avf)
ct05_a_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct05/histology/nerve_a_intact/proc/mvf_cat.csv', names=col_nerve_a_ct_mvf)

#control nerve_b
ct01_b_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct01/histology/nerve_b_intact/proc/avf_cat.csv', names=col_nerve_b_ct_avf)
ct01_b_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct01/histology/nerve_b_intact/proc/mvf_cat.csv', names=col_nerve_b_ct_mvf)
ct02_b_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct02/histology/nerve_b_intact/proc/avf_cat.csv', names=col_nerve_b_ct_avf)
ct02_b_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct02/histology/nerve_b_intact/proc/mvf_cat.csv', names=col_nerve_b_ct_mvf)
ct03_b_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct03/histology/nerve_b_intact/proc/avf_cat.csv', names=col_nerve_b_ct_avf)
ct03_b_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct03/histology/nerve_b_intact/proc/mvf_cat.csv', names=col_nerve_b_ct_mvf)
ct04_b_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct04/histology/nerve_right_intact/proc/avf_cat.csv', names=col_nerve_b_ct_avf)
ct04_b_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct04/histology/nerve_right_intact/proc/mvf_cat.csv', names=col_nerve_b_ct_mvf)
ct05_b_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct05/histology/nerve_b_intact/proc/avf_cat.csv', names=col_nerve_b_ct_avf)
ct05_b_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/ct05/histology/nerve_b_intact/proc/mvf_cat.csv', names=col_nerve_b_ct_mvf)

#concatenate chiasm 

chiasm_ct_intact_avf = pd.concat([ct01_chiasm_avf, ct02_chiasm_avf, ct03_chiasm_avf, ct04_chiasm_avf, ct05_chiasm_avf])

chiasm_ct_intact_mvf = pd.concat([ct01_chiasm_mvf, ct02_chiasm_mvf, ct03_chiasm_mvf, ct04_chiasm_mvf, ct05_chiasm_mvf])

#concatenate nerve_a

nerve_a_ct_avf = pd.concat([ct01_a_avf, ct02_a_avf, ct03_a_avf, ct04_a_avf, ct05_a_avf])

nerve_a_ct_mvf = pd.concat([ct01_a_mvf, ct02_a_mvf, ct03_a_mvf, ct04_a_mvf, ct05_a_mvf])

#concatenate nerve_b

nerve_b_ct_avf = pd.concat([ct01_b_avf, ct02_b_avf, ct03_b_avf, ct04_b_avf, ct05_b_avf])

nerve_b_ct_mvf = pd.concat([ct01_b_mvf, ct02_b_mvf, ct03_b_mvf, ct04_b_mvf, ct05_b_mvf])

#saving_results

chiasm_ct_intact_avf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/control/chiasm/chiasm_ct_intact_avf.csv')
chiasm_ct_intact_mvf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/control/chiasm/chiasm_ct_intact_mvf.csv')
nerve_a_ct_avf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/control/nerve_a/nerve_a_ct_avf.csv')
nerve_a_ct_mvf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/control/nerve_a/nerve_a_ct_mvf.csv')
nerve_b_ct_avf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/control/nerve_b/nerve_b_ct_avf.csv')
nerve_b_ct_mvf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/control/nerve_b/nerve_b_ct_mvf.csv')


#experimental chiasm
is01_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is01/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is01_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is01/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is02_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is02/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is02_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is02/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is03_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is03/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is03_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is03/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is04_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is04/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is04_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is04/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is05_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is05/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is05_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is05/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is06_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is06/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is06_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is06/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is07_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is07/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is07_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is07/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is08_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is08/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is08_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is08/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is09_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is09/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is09_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is09/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)
is10_chiasm_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is10/histology/chiasm/proc/avf_cat.csv', names=col_chiasm_exp_avf)
is10_chiasm_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is10/histology/chiasm/proc/mvf_cat.csv', names=col_chiasm_exp_mvf)

#experimental nerve_degenerated
is01_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is01/histology/nerve_left_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is01_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is01/histology/nerve_left_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is02_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is02/histology/nerve_left_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is02_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is02/histology/nerve_left_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is03_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is03/histology/nerve_right_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is03_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is03/histology/nerve_right_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is04_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is04/histology/nerve_left_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is04_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is04/histology/nerve_left_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is05_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is05/histology/nerve_right_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is05_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is05/histology/nerve_right_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is06_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is06/histology/nerve_left_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is06_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is06/histology/nerve_left_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is07_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is07/histology/nerve_right_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is07_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is07/histology/nerve_right_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is08_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is08/histology/nerve_right_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is08_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is08/histology/nerve_right_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is09_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is09/histology/nerve_right_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is09_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is09/histology/nerve_right_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)
is10_degenerated_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is10/histology/nerve_right_degenerated/proc/avf_cat.csv', names=col_nerve_degenerated_exp_avf)
is10_degenerated_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is10/histology/nerve_right_degenerated/proc/mvf_cat.csv', names=col_nerve_degenerated_exp_mvf)

#experimental nerve_intact
is01_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is01/histology/nerve_right_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is01_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is01/histology/nerve_right_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is02_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is02/histology/nerve_right_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is02_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is02/histology/nerve_right_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is03_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is03/histology/nerve_left_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is03_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is03/histology/nerve_left_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is04_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is04/histology/nerve_right_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is04_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is04/histology/nerve_right_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is05_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is05/histology/nerve_left_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is05_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is05/histology/nerve_left_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is06_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is06/histology/nerve_right_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is06_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is06/histology/nerve_right_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is07_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is07/histology/nerve_left_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is07_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is07/histology/nerve_left_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is08_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is08/histology/nerve_left_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is08_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is08/histology/nerve_left_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is09_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is09/histology/nerve_left_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is09_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is09/histology/nerve_left_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)
is10_intact_avf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is10/histology/nerve_left_intact/proc/avf_cat.csv', names=col_nerve_intact_exp_avf)
is10_intact_mvf = pd.read_csv('/misc/torrey/onarvaez/Aqueronte_hist/is10/histology/nerve_left_intact/proc/mvf_cat.csv', names=col_nerve_intact_exp_mvf)

#concatenate chiasm 
chiasm_is_exp_avf = pd.concat([is01_chiasm_avf, is02_chiasm_avf, is03_chiasm_avf, is04_chiasm_avf, is05_chiasm_avf, is06_chiasm_avf, is07_chiasm_avf, is08_chiasm_avf, is09_chiasm_avf, is10_chiasm_avf])

chiasm_is_exp_mvf = pd.concat([is01_chiasm_mvf, is02_chiasm_mvf, is03_chiasm_mvf, is04_chiasm_mvf, is05_chiasm_mvf, is06_chiasm_mvf, is07_chiasm_mvf, is08_chiasm_mvf, is09_chiasm_mvf, is10_chiasm_mvf])


#concatenate degenerated
nerve_degenerated_is_exp_avf = pd.concat([is01_degenerated_avf, is02_degenerated_avf, is03_degenerated_avf, is04_degenerated_avf, is05_degenerated_avf, is06_degenerated_avf, is07_degenerated_avf, is08_degenerated_avf, is09_degenerated_avf, is10_degenerated_avf])

nerve_degenerated_is_exp_mvf = pd.concat([is01_degenerated_mvf, is02_degenerated_mvf, is03_degenerated_mvf, is04_degenerated_mvf, is05_degenerated_mvf, is06_degenerated_mvf, is07_degenerated_mvf, is08_degenerated_mvf, is09_degenerated_mvf, is10_degenerated_mvf])

#concatenate intact
nerve_intact_is_exp_avf = pd.concat([is01_intact_avf, is02_intact_avf, is03_intact_avf, is04_intact_avf, is05_intact_avf, is06_intact_avf, is07_intact_avf, is08_intact_avf, is09_intact_avf, is10_intact_avf])

nerve_intact_is_exp_mvf = pd.concat([is01_intact_mvf, is02_intact_mvf, is03_intact_mvf, is04_intact_mvf, is05_intact_mvf, is06_intact_mvf, is07_intact_mvf, is08_intact_mvf, is09_intact_mvf, is10_intact_mvf])

#saving degenerated
chiasm_is_exp_avf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/ischemic/chiasm/chiasm_is_exp_avf.csv')
chiasm_is_exp_mvf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/ischemic/chiasm/chiasm_is_exp_mvf.csv')
nerve_degenerated_is_exp_avf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/ischemic/degenerated/nerve_degenerated_avf.csv')
nerve_degenerated_is_exp_mvf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/ischemic/degenerated/nerve_degenerated_mvf.csv')
nerve_intact_is_exp_avf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/ischemic/intact/nerve_intact_avf.csv')
nerve_intact_is_exp_mvf.to_csv('/misc/torrey/onarvaez/Aqueronte_hist/avf_mvf/ischemic/intact/nerve_intact_mvf.csv')