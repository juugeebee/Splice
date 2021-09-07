#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate splice

# cat vcf_header.txt 15920_ABCC8intronique_genomique_vcf_format.csv > 15920_ABCC8intronique_SpliceAI.vcf
# remplacer les , par des \t

input='/media/jbogoin/Sep2020-JGB/Donnees_brutes/hg19/Metabo/variants_introniques/SpliceAI/15814_ABCC8intronique_SpliceAI.vcf'
output='/media/jbogoin/Sep2020-JGB/Donnees_brutes/hg19/Metabo/variants_introniques/SpliceAI/15814_ABCC8intronique_SpliceAI_output.vcf'
genome='/media/Data1/jbogoin/ref/fa_hg19/hg19.fa'

# -D: Maximum distance between the variant and gained/lost splice site (default: 50)
# max 4999.

spliceai -I $input -O $output -R $genome -A grch37 -D 4999