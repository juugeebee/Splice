import pandas

##### 15029
df_15029 = pandas.read_csv('/media/jbogoin/Data1/Variants_introniques/15029.txt',\
    sep='\t', header=[0])

df_15029['Transcrits'] = 'NM_001287174.1'

df_15029_spip = pandas.DataFrame()
df_15029_spip['gene'] = df_15029['Gene']
df_15029_spip['varID'] = df_15029['Transcrits'] + ':' + df_15029['c.HGVS']

df_15029_spip.to_csv('15029_spip_input.txt', sep='\t', index=False)


##### 15383
df_15383 = pandas.read_csv('/media/jbogoin/Data1/Variants_introniques/15383.txt',\
    sep='\t', header=[0])

df_15383['Transcrits'] = 'NM_001287174.1'

df_15383_spip = pandas.DataFrame()
df_15383_spip['gene'] = df_15383['Gene']
df_15383_spip['varID'] = df_15383['Transcrits'] + ':' + df_15383['c.HGVS']

df_15383_spip.to_csv('15383_spip_input.txt', sep='\t', index=False)

df_15383_vv = pandas.DataFrame()
df_15383_vv['varID'] = df_15383['Transcrits'] + ':' + df_15383['c.HGVS']

df_15383_vv.to_csv('15383_vv_input.txt', sep='\t', index=False, header=False)



##### 15814
df_15814 = pandas.read_csv('/media/jbogoin/Data1/Variants_introniques/15814.txt',\
    sep='\t', header=[0])

df_15814_spip = pandas.DataFrame()   
df_15814_spip['gene'] = df_15814['Gene']
df_15814_spip['varID'] = df_15814['Transcrits'] + ':' + df_15814['c.HGVS']

df_15814_spip.to_csv('15814_spip_input.txt', sep='\t', index=False)


##### 15920
df_15920 = pandas.read_csv('/media/jbogoin/Data1/Variants_introniques/15920.txt',\
    sep='\t', header=[0])

df_15920['Transcrits'] = 'NM_001287174.1'

df_15920_spip = pandas.DataFrame()   
df_15920_spip['gene'] = df_15920['Gene']
df_15920_spip['varID'] = df_15920['Transcrits'] + ':' + df_15920['c.HGVS']

df_15920_spip.to_csv('15920_spip_input.txt', sep='\t', index=False)


##### 15092
df_15092 = pandas.read_csv('/media/jbogoin/Data1/Variants_introniques/15092.txt',\
    sep='\t', header=[0])

df_15092['Transcrits'] = 'NM_001287174.1' 

df_15092_spip = pandas.DataFrame()   
df_15092_spip['gene'] = df_15092['Gene']
df_15092_spip['varID'] = df_15092['Transcrits'] + ':' + df_15092['c.HGVS']

df_15092_spip.to_csv('15092_spip_input.txt', sep='\t', index=False)


