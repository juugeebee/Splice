#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate splice

input='/media/jbogoin/Sep2020-JGB/Donnees_brutes/hg19/Metabo/variants_introniques_17062021/SPIP/15383_15029_ABCC8intronique_SPIP_input.txt'
output='/media/jbogoin/Sep2020-JGB/Donnees_brutes/hg19/Metabo/variants_introniques_17062021/SPIP/15383_15029_ABCC8intronique_SPIP_output.txt'


cd ~/SPiP/
Rscript SPiPv2.1_main.r -I $input -O $output