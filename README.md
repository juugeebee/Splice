# Splice

1. Fichier_brut .xlsx

2. Fichier brut modifié  .xlsx

suppression mise en forme
ajout transcrit

noms de colonne:
FAMILLE	Prélèvement d'origine	Gene	Location	Type	c. HGVS	Transcrit

3. Fichier .csv

format:
NM_001287174.1:c.-549_-547dupCAC

formule:
=CONCAT(Feuil2.G2;":";$Feuil2.F2)

4. VARIANTVALIDATOR

~/SCRIPTS/c_to_g/VariantValidator.py > Génération du fichier *_genomique.txt

création manuelle des fichier *_snp.txt & *_deldupinsinv.txt

5. SPIP

a. Fichier input à partir du fichier .csv
noms de colonne: gene varID (c.) A ECRIRE EN 1ERE LIGNE
séparateur: \t > *.SPIP_input.txt

b. Lancement SPIP
bash ~/SCRIPTS/Splice/Spip.sh > *.SPIP_output.txt

6. SpliceAI

a. Coordonnées génomiques 
~/SCRIPTS/c_to_g/g_to_vcf.py > Génération fichier vcf.csv

b. Concaténation avec l'entete du vcf
cat cat vcf_header.txt *_genomique_vcf_format.csv > *_ABCC8intronique_SpliceAI.vcf
vérification du séparateur /t

c. Lancement SpliceAI
bash ~/SCRIPTS/Splice/SpliceAI.sh






 







