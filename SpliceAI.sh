#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate splice

# cat vcf_header.txt 15920_ABCC8intronique_genomique_vcf_format.csv > 15920_ABCC8intronique_SpliceAI.vcf
# remplacer les , par des \t

input='/media/jbogoin/Data1/Variants_introniques/CSM/SpliceAI/variants-pour-bioinfo-20211223_SpliceAI.vcf'
output='//media/jbogoin/Data1/Variants_introniques/CSM/SpliceAI/variants-pour-bioinfo-20211223_SpliceAI_output.vcf'
genome='/media/jbogoin/Data1/References/fa_hg19/hg19_std_M-rCRS_Y-PAR-mask.fa'

# -D: Maximum distance between the variant and gained/lost splice site (default: 50)
# max 4999.

spliceai -I $input -O $output -R $genome -A grch37 -D 4999