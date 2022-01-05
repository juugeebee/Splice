#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate splice

input='/media/jbogoin/Data1/Variants_introniques/CSM_05012022/SPIP/variants-pour-bioinfo-20211223_SpliceAI.vcf'
output='/media/jbogoin/Data1/Variants_introniques/CSM_05012022/SPIP/variants-pour-bioinfo-20211223_SPIP_output.txt'

cd ~/SPiP/
Rscript SPiPv2.1_main.r -I $input -O $output