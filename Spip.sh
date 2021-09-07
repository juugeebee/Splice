#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate splice

input='/media/jbogoin/Sep2020-JGB/Donnees_brutes/hg19/Metabo/variants_introniques/SPIP/15814_ABCC8intronique_SPIP_input.txt'
output='/media/jbogoin/Sep2020-JGB/Donnees_brutes/hg19/Metabo/variants_introniques/SPIP/15814_ABCC8intronique_SPIP_output.txt'


cd ~/SPiP/
Rscript SPiPv2.1_main.r -I $input -O $output