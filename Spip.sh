#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate splice

input='/media/jbogoin/Data1/Variants_introniques/CSM_05012022/SPIP/variants-pour-bioinfo-20211223_SpliceAI.vcf'
output_txt='/media/jbogoin/Data1/Variants_introniques/CSM_05012022/SPIP/variants-pour-bioinfo-20211223_SPIP_output_v2.1.txt'
output_vcf='/media/jbogoin/Data1/Variants_introniques/CSM_05012022/SPIP/variants-pour-bioinfo-20211223_SPIP_output_v2.1.vcf'


cd ~/SPiP/

Rscript SPiPv2.1_main.r -I $input -O $output_vcf --VCF
#Rscript SPiPv2.1_main.r -I $input -O $output_txt