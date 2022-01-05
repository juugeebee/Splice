import pandas
import numpy

entree = 'variants-pour-bioinfo-20211223.txt'
sortie = './SpliceAI/variants-pour-bioinfo-20211223_vcf_format.txt'

dfi = pandas.read_csv(entree, sep='\t', names=['CHROM','POS', 'REF', 'ALT'])

vcf = pandas.DataFrame(columns=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO'])
vcf['CHROM'] = dfi['CHROM'].str.split('chr').str[1]
vcf['ID'] = '.'
vcf['POS'] = dfi['POS']
vcf['REF'] = dfi['REF'].replace(numpy.nan, '.')
vcf['ALT'] = dfi['ALT'].replace(numpy.nan, '.')
# vcf['REF'] = vcf['REF'].replace('dup', '.')
# vcf['REF'] = vcf['REF'].replace('ins', '.')
# vcf['REF'] = vcf['REF'].replace('del', '.')
# vcf['REF'] = vcf['REF'].replace('_', '.')
vcf['QUAL'] = '.'
vcf['FILTER'] = '.'
vcf['INFO'] = '.'

vcf.to_csv(sortie, sep='\t', header=False, index=False)

print('\n' + sortie + ' genere !\n')