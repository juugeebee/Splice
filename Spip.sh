#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate splice

input='/media/jbogoin/Data1/Variants_introniques/CSM_05012022/SPIP/variants-pour-bioinfo-20211223_SpliceAI.vcf'
output_txt='/media/jbogoin/Data1/Variants_introniques/CSM_05012022/SPIP/variants-pour-bioinfo-20211223_SPIP_output_v1.0.txt'
output_vcf='/media/jbogoin/Data1/Variants_introniques/CSM_05012022/SPIP/variants-pour-bioinfo-20211223_SPIP_output_v1.0.vcf'
fasta='/media/jbogoin/Data1/References/fa_hg19/hg19_std_M-rCRS_Y-PAR-mask.fa'
sam='/usr/bin/samtools'

cd ~/SPiP/

Rscript SPiPv2.1_main.r -I $input -O $output_vcf --VCF
#Rscript SPiPv2.1_main.r -I $input -O $output_txt

Rscript SPiPv1.0.r -I $input \
    -O $output_vcf --VCF -f $fasta -s $sam

