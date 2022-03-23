import pandas
import vcf
import subprocess
import os

print("\nSPlice - curation_alamut GO!\n")

print('IMPORT FICHIER INPUT BRUT')
df = pandas.read_csv('EXPORT_3genes_SPIP_SPLICEAI.txt',\
    sep='\t', header=[0])

print('CREATION INPUT SPIP')
df_spip = pandas.DataFrame()
df_spip['gene'] = df['gene']
df_spip['varID'] = df['transcript'] + ':' + df['cNomen']
df_spip.to_csv('spip_input.txt', index=None, sep='\t')

print('CREATION INPUT SPLICEAI')
df_spliceai = pandas.DataFrame(columns=\
    ['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO'])
df_spliceai['#CHROM'] = df['chrom']
df_spliceai['ID'] = df['gNomen']
df_spliceai['FILTER'] = '.'
df_spliceai['INFO'] = '.'
df_spliceai['QUAL'] = '.'
df_spliceai['POS'] = df['gDNAstart']
df_spliceai['REF'] = df['wtNuc']
df_spliceai['ALT'] = df['varNuc']
df_spliceai.to_csv('spliceai_input_no_header.txt', index=None, sep='\t')

subprocess.call("cat /media/jbogoin/Data1/References/SpliceAI/spliceai_header.txt\
    spliceai_input_no_header.txt \
    > spliceai_input.vcf", shell="/bin/bash")

print("LANCEMENT SPIP")

subprocess.call("Rscript ~/SPiP/SPiPv2.1_main.r -I spip_input.txt \
    -O spip_output.txt", shell="/bin/bash")

print("LANCEMENT SPLICEAI")

subprocess.call("spliceai -I spliceai_input.vcf \
    -O spliceai_output.vcf \
    -R /media/jbogoin/Data1/References/fa_hg19/hg19_std_M-rCRS_Y-PAR-mask.fa \
    -A grch37 -D 4999", shell="/bin/bash")

print("AJOUT DES COLONNES DANS LE FICHIER OUTPUT")

print('** SPiP')
df_spip_output = pandas.read_csv('spip_output.txt',\
    sep='\t', header=[0])

df['Interpretation_SPiP_v2.1'] = df_spip_output['Interpretation']
df['InterConfident_SPiP_v2.1'] = df_spip_output['InterConfident']

print("** SpliceAI")
vcf_reader = vcf.Reader(open('spliceai_output.vcf', 'r'))

spliceai_list = [] 

for record in vcf_reader:
    spliceai_list.append(record.INFO)

df['SpliceAI_v1.3'] = pandas.Series(spliceai_list)
df.to_csv('EXPORT_3genes_SPIP_SPLICEAI_results.txt', index=None, sep='\t')

print("\nJob done!\n")