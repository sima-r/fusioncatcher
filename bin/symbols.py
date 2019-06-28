#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
It handles the loci and gene symbols and their synonyms.



Author: Daniel Nicorici, Daniel.Nicorici@gmail.com

Copyright (c) 2009-2018 Daniel Nicorici

This file is part of FusionCatcher.

FusionCatcher is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

FusionCatcher is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with FusionCatcher (see file 'COPYING.txt').  If not, see
<http://www.gnu.org/licenses/>.

By default, FusionCatcher is running BLAT aligner
<http://users.soe.ucsc.edu/~kent/src/> but it offers also the option to disable
all its scripts which make use of BLAT aligner if you choose explicitly to do so.
BLAT's license does not allow to be used for commercial activities. If BLAT
license does not allow to be used in your case then you may still use
FusionCatcher by forcing not use the BLAT aligner by specifying the option
'--skip-blat'. Fore more information regarding BLAT please see its license.

Please, note that FusionCatcher does not require BLAT in order to find
candidate fusion genes!

This file is not running/executing/using BLAT.
"""
import os
import sys

# hard coded gene synonyms
synonym = {
'C15ORF21':'HMGN2P46',
'MYST3':'KAT6A',
'ODZ4':'TENM4',
'TMEM49':'VMP1',
'CXORF15':'TXLNG',
'SFRS11':'SRSF11',
'RAD51L1':'RAD51B',
'CYTSB':'SPECC1',
'MYST4':'KAT6B',
'BCL8':'NBEAP1',
'SFRS3':'SRSF3',
'RPL22P1':'RP11-641D5.1',
'LOC204010':'RPSAP52',
'BRWD2':'WDR11',
'C14ORF161':'CATSPERB',
'MTAC2D1':'TC2N',
'SKP1A':'SKP1',
'ZNHIT4':'INO80B',
'C11ORF64':'LINC00301',
'C20ORF3':'APMAP',
'CRSP7':'MED26',
'C6ORF159':'RIPPLY2',
'NO145':'SYCP2L',
'L3MBTL':'L3MBTL1',
'ACY1L2':'PM20D2',
'C1ORF175':'HEATR8',
'C16ORF53':'PAGR1',
'C6ORF111':'PNISR',
'C14ORF156':'SLIRP',
'ISGF3G':'IRF9',
'LOC51149':'C5ORF45',
'CYORF14':'TTTY14',
'C1ORF176':'EXO5',
'MGC33212':'TCTEX1D2',
'KIAA0367':'PRUNE2',
'C14ORF112':'COX16',
'MAGMAS':'PAM16',
'SIKE':'SIKE1',
'FLJ20054':'DENND1B',
'KRT6L':'KRT79',
'FLJ14397':'CCDC142',
'C1ORF151':'MINOS1',
'C11ORF66':'PPP1R32',
'C9ORF75':'TPRN',
'CYORF15A':'TXLNG2P',
'CYORF15B':'TXLNG2P',
'C14ORF58':'FLVCR2',
'C21ORF69':'C21ORG67',
'C9ORF102':'ERCC6L2',
'C6ORF60':'FAM184A',
'C6ORF130':'OARD1',
'C3ORF10':'BRK1',
'C14ORF143':'EFCAB11',

'BC047782':'TEN1',
'MOBKL1A':'MOB1B',
'FAM62A':'ESYT1',
'APBA2BP':'NECAB3',
'KSP37':'FGFBP2',
'HNRPUL2':'HNRNPUL2',
'TXNDC14':'TMX2',
'URG4':'URGCP',
'3TM12':'SLCO1B7',
'FLJ42258':'ORAOV1',
'TMEM170':'TMEM170A',
'KUA':'TMEM189',
'CIP29':'SARNP',
'CLCA3':'CLCA3P',
'FAM119B':'METTL21B',
'ZADH1':'PTGR2',
'LOC286187':'PPP1R42',
'RUTBC3':'SGSM3',
'FLJ20487':'SDHAF2',
'RCP9':'CRCP',
'STK23':'SRPK3',
'MGC14327':'TMEM203',
'RAD51L3':'RAD51D',
'UQCR':'UQCR11',
'LOC162073':'ITPRIPL2',
'NYD':'TTLL2',
'FLJ13611':'C5ORF44',
'BRUNOL6':'CELF6',
'RBM21':'TUT1',
'TMEM142B':'ORAI2',
'TNRC5':'CNPY3',
'MDP':'DPEP1',
'C21ORF69':'C21ORF67',
'MGC57346':'CRHR1-IT1',
'LSM8':'NAA38',
'MCMDC1':'MCM9',
'PRR8':'RBM33',
'FLJ39779':'ZFP36L1',
'LOC145757':'RP11-66B24.1',
'MTP18':'MTFP1',
'MGC51025':'TBC1D26',
'ZNF286':'ZNF286A',
'GCN5L2':'KAT2A',
'PSCD2':'CYTH2',
'CHES1':'FOXN3',
'PLZF':'ZBTB16',
'NUT':'C15ORF55',
'TEL':'ETV6',
'AML1':'RUNX1',
'ETO':'RUNX1T1',
'NUT':'C15ORF55',
'EVI1':'MECOM',
'C6ORF204':'CEP85L',
'C2ORF3':'GCFC2',
'C15ORF21':'HMGN2P46',
'C11ORF41':'KIAA1549L',
'C4ORF18':'FAM198B',
'C14ORF124':'SDR39U1',
'C21ORF34':'LINC00478',
'C14ORF21':'NOP9',
'C3ORF10':'BRK1',
'ZNFN1A1':'IKZF1',
'NKAIN21':'NKAIN2',
'KIAA1618':'RNF213',
'CEP110':'CNTRL',
'NOL1':'NOP2',
'JARID1A':'KDM5A',
'AF4':'AFF1',
'AF9':'MLLT3',
'PTD':'BCS1L',
'ENL':'MLLT1',
'AF10':'MLLT10',
'AF6':'MLLT4',
'AF1P':'EPS15',
'AF17':'MLLT6',
'CIP2A':'KIAA1524',
'ATP50':'ATP5O',
'ZNF9':'CNBP',
'SCL45A3':'SLC45A3',
'EWS':'EWSR1',
'CTLC':'CLTCL1',
'LEDGF':'PSIP1',
'BX648577':'FLJ27352',
'NSD3':'WHSC1L1',
'NPM':'NPM1',
'TK14':'FGFR2',
'ASPL':'ASPSCR1',
'AFX':'FOXO4',
'EIAF':'ETV4',
'E1AF':'ETV4',
'ZSG':'PATZ1',
'CHOP':'DDIT3',
'PSF':'SFPQ',
'RBP56':'TAF15',
'FKHR':'FOXO1',
'TLS':'FUS',
'SYT':'SS18',
'TEF3':'TEAD4',
'FOXO1A':'FOXO1',
'ZNF278':'PATZ1',
'SEC31L1':'SEC31A',
'MLLT7':'FOXO4',
'MECT1':'CRTC1',
'RFG8':'NCOA4',
'RAB6IP2':'ERC1',
'TMP3':'TPM3',
'TMP4':'TPM4',
'TAFII68':'TAF15',
'HOX11':'TLX1',
'C2ORF22':'PQLC3',
'RUNXBP2':'KAT6A',
'CBFA2T1':'RUNX1T1',
'C16ORF75':'RMI2',
'AF1Q':'MLLT11',
'AF15Q14':'CASC5',
'AF3P21':'NCKIPSD',
'AF5Q31':'AFF4',
'ALO17':'RNF213',
'ARHH':'RHOH',
'BCL5':'BCL6',
'CD273':'PDCD1LG2',
'CEP1':'CNTRL',
'CMKOR1':'CXCR7',
'D10S170':'CCDC6',
'ELKS':'ERC1',
'FACL6':'ACSL6',
'FOXO3A':'FOXO3',
'FVT1':'KDSR',
'GRAF':'ARHGAP26',
'HCMOGT-1':'SPECC1',
'HEAB':'CLP1',
'HLXB9':'MNX1',
'HSPCA':'HSP90AA1',
'HSPCB':'HSP90AB1',
'IRTA1':'FCRL4',
'LAF4':'AFF3',
'LCX':'TET1',
'MDS1':'MECOM',
'MLLT2':'AFF1',
'PMX1':'PRRX1',
'PNUTL1':'SEPT5',
'PRO1073':'MALAT1',
'PSIP2':'PSIP1',
'RAB5EP':'RABEP1',
'RUNDC2A':'SNX29',
'SIL':'SIL1',
'SSH3BP1':'ABI1',
'STL':'RP11-510H23.1',
'TIF1':'TRIM24',
'ZNF145':'ZBTB16',
'ZNF198':'ZMYM2',
'C18ORF45':'TMEM241',
'CCDC46':'CEP112',
'CCDC49':'CWC25',
'CHGN':'CSGALNACT1',
'CRKRS':'CDK12',
'DEPDC6':'DEPTOR',
'HER2':'ERBB2',
'KIAA0134':'DHX34',
'KIAA1267':'KANSL1',
'PERLD1':'PGAP3',
'PGCP':'CPQ',
'PLDN':'BLOC1S6',
'PLEC1':'PLEC',
'PREI3':'MOB4',
'PSCD1':'CYTH1',
'TEM7':'PLXDC1',
'WDR68':'DCAF7',
'AFAR3':'AKR7L',
'ALF':'GTF2A1L',
'ARD1A':'NAA10',
'ATPBD1C':'GPN3',
'BAT1':'DDX39B',
'BCDO2':'BCO2',
'CREBL1':'ATF6B',
'CRSP9':'MED7',
'DCDC1':'DCDC5',
'DMA':'HLA-DMA',
'DULLARD':'CTDNEP1',
'ECGF1':'TYMP',
'F25965':'LIN37',
'FLJ10324':'RADIL',
'C11ORF47':'DNHD1',
'C14ORF179':'IFT43',
'C14ORF94':'HAUS4',
'C16ORF34':'HN1L',
'C16ORF48':'ENKD1',
'C19ORF51':'DNAAF3',
'C1ORF49':'TEX35',
'C6ORF21':'LY6G6F',
'C9ORF164':'SEMA4D',
'C9ORF30':'MSANTD3',
'FLJ13611':'C5ORF44',
'FLJ14154':'NAA60',
'FLJ14213':'PRR5L',
'FLJ35530':'C1PRF220',
'FLJ45224':'LCNL1',
'GOLPH2':'GOLM1',
'GPIAP1':'CAPRIN1',
'GRINL1A':'GCOM1',
'GUP1':'HHATL',
'HBLD2':'ISCA1',
'HIG2':'HILPDA',
'HNRPH2':'HNRNPH2',
'JUB':'AJUBA',
'KIAA1787':'NEURL4',
'KRT222P':'KRT222',
'LBXCOR1':'SKOR1',
'LSDP5':'PLIN5',
'MAP3K7IP1':'TAB1',
'MGC12966':'FAM220A',
'MGC19604':'FDX1L',
'MGC24975':'PRR22',
'MGC35402':'ZNF321P',
'MGC52110':'COA5',
'MGC71993':'RNASEK',
'MOBKL2A':'MOB3A',
'MUTED':'BLOC1S5',
'NYD-SP21':'MS4A14',
'OATL1':'TBC1D25',
'PLEKHQ1':'PLEKHO2',
'PSCD3':'CYTH3',
'PTK9L':'TWF2',
'RY1':'SNRNP27',
'SPINLW1':'EPPIN',
'SURF5':'MED22',
'TMEM4':'CNPY2',
'UNC84B':'SUN2',
'UNQ2446':'NRN1L',
'VARSL':'VARS2',
'VPS24':'CHMP3',
'WDR23':'DCAF11',
'ZFHX1B':'ZEB2',
'ZNF816A':'ZNF816',
'ACCN3':'ASIC3',
'AY251274':'FLJ00104',
'AYTL1':'LPCAT2',
'BA16L21.2.1':'DNAJC25',
'C14ORF109':'TMEM251',
'C14ORF125':'HEATR5A',
'C14ORF126':'DTD2',
'C14ORF130':'UBR7',
'C16ORF28':'UNKL',
'C17ORF83':'SPEM1',
'C17ORF86':'LINC00338',
'C19ORF16':'FAM71E2',
'C1ORF188':'RNF207',
'C20ORF106':'FAM209A',
'C20ORF29':'AP5S1',
'C2ORF13':'APLF',
'C3ORF26':'CMSS1',
'C3ORF41':'FAM198A',
'C4ORF15':'HAUS3',
'C6ORF114':'GFOD1',
'C6ORF174':'SOGA3',
'C6ORF26':'SAPCD1',
'C9ORF105':'TOMM5',
'C9ORF86':'RABL6',
'CDC2L1':'CDK11B',
'CDC2L2':'CDK11A',
'CENTD2':'ARAP1',
'DAGLBETA':'DAGLB',
'DGCR13':'DGCR14',
'DJ222E13.2':'RRP7B',
'DUSP5P':'DUSP5P1',
'EXOD1':'ERI2',
'FLJ22167':'TMEM231',
'FLJ22374':'FAM188B',
'FLJ22531':'C11ORF80',
'FLJ23867':'QSOX1',
'FLJ35530':'C1ORF220',
'FLJ37614':'CARD8',
'FLJ41309':'ATP6AP1L',
'FLJ46481':'C4ORF50',
'FLJ46838':'AC073082.1',
'GAGE2':'GAGE2A',
'GEFT':'ARHGEF25',
'GIYD1':'SLX1A',
'GIYD2':'SLX1B',
'HNRPD':'HNRNPD',
'HSPC047':'AC093668.1',
'LASS1':'CERS1',
'LOC115648':'ZNF493',
'LOC128977':'C22ORF39',
'LOC284371':'ZNF841',
'LOC285498':'RNF212',
'LOC339524':'RP5-1052I5.1',
'LOC389458':'RBAK',
'LOC57228':'SMAGP',
'LOC606495':'CYB5RL',
'MAP2K1IP1':'LAMTOR3',
'MCART1':'SLC25A51',
'MDP-1':'MDP1',
'MGC39821':'LINC00663',
'NOS2A':'NOS2',
'NSUN5B':'NSUN5P1',
'OSAP':'MGARP',
'PAPD1':'MTPAP',
'QSCN6':'QSOX1',
'RBM16':'SCAF8',
'SALF':'STON1',
'TESSP5':'PRSS45',
'TMEM137':'RBM14',
'TMEM149':'IGFLR1',
'TSP50':'PRSS50',
'TXNDC3':'NME8',
'U2AF1L1':'ZRSR1',
'U92992':'RP11-451M19.3',
'UIP1':'HAUS7',
'WDR51B':'POC1B',
'KIAA1509':'CCDC88C',
'CEV14':'TRIP11',
'FGFR1OP1':'FGFR1OP',
'HNRPA2B1':'HNRNPA2B1',
'RAD51L1':'RAD51B',
'SIP1':'GEMIN2',
'ROD1':'PTBP3',
'ACCN1':'ASIC2',
'P11':'S100A10',
'TROP2':'TACSTD2',
'DNMT2':'TRDMT1',
'ALS2CR16':'NBEAL1',
'AK126539':'CTD-3088G3.8',
'C11ORF20':'TEX40',
'TMCO7':'TANGO6',
'KIAA0284':'CEP170B',
'MTCP1NB':'CMC4',
'HELIOS':'IKZF2',
'DAB21P':'DAB2IP',
'C2ORF18':'SLC35F6',
'ASB3':'GPR75-ASB3',
'BAGE3':'BAGE5',
'C17ORF61':'TMEM256',
'C19ORF42':'SMIM7',
'C1ORF175':'MROH7',
'C2ORF18':'SLC35F6',
'C6ORF162':'SMIM8',
'FAM18B2':'TVP23C',
'FAM54B':'MTFR1L',
'KIAA0494':'EFCAB14',
'LST-3TM12':'SLCO1B7',
'NBPF8':'NBPF8P',
'PLAC2':'TINCR',
'ZNF167':'ZKSCAN7',
'ZNF673':'KRBOX4',
'CTL4':'SLC44A4',
'C17ORF106':'TEN1',
'ACSLS':'ACSL3',
'AK096045':'SHANK2',
'AX747739':'RP5-1043L13.1',
'AX747623':'RP11-399D6.2',
'AK128161':'RP11-100L22.2',
'AK024242':'RP11-758M4.4',
'EU154352':'C1ORF132',
'FLJ00268':'RP11-108K14.4',
'LOC284100':'RP11-115K3.2',
'UNQ2998':'C1ORF159',
'BC017255':'AC099850.1',
'BC035340':'MCF2L',
'BC038786':'AC084018.1',
'BC041478':'AC012309.5',
'BC016484':'LINC00617',
'BC044946':'AC006552.1',
'BX248273':'RP11-129M6.1',
'BC041441':'RP5-952N6.1',
'BX537644':'RP11-18C24.6',
'EST14':'AL121790.1',
'RCC17':'ASPSCR1',
'BF104016':'CCDC26',
'HCMOGT1':'SPECC1',
'RP11-721F8':'RN7SL167P',
'PPP2RA':'PPP2CA',
'BX004987.7':'RP11-435B5.7',
'RP11-715D1.1':'MORC1',
'RP11-322M19.1':'NUTM2A-AS1',
'LPPR1':'RP11-35N6.1',
'RFX1':'HGNC:9982',
'RNA28S5':'CTD-2328D6.1',
'DKFZP586I1420':'AC006978.6',
'CHDC2':'CXORF22',
'AC126544.2':'CRHR1-IT1',
'ACBD6':'LHX4-AS1',
'FAM75A4':'SPATA31A7',
'C6ORF164':'RP1-102H19.7',
'IG':'IG@',
'IGH':'IGH@',
'IGL':'IGL@',
'IGK':'IGK@',
'HLA':'HLA@',
'AC008279.1':'RPL5P8',
'AC096579.7':'AC096579.13',
'AK125726':'KIAA1257',
'AC138031.1':'RPL23AP45',
'AL672183.2':'RPL23AP25',
'AC090627.1':'THRA1/BTR',
'STBD1':'FAM47E-STBD1',
'KIAA0660':'G3BP2',
'MIR143':'CARMN',
'ERVK3-1':'AC020915.1',
'HERVK':'AC020915.1',
'HERVK17':'AC129492.2',
'RNF213':'AC124319.1',
'ALO17':'AC124319.1',
'KIAA1618':'AC124319.1',
'TGFB1':'AC011462.1',
'USP3':'AC007950.1',
'LMTK3':'AC008403.1',
'CDR2':'AC092338.1',
'TCL1A':'AL139020.1',
'N4BP1':'AC026470.1',
'MIR3687':'MIR3687-1',
'MIR3687-1':'FP671120.1',
'MRC2':'AC080038.1',
'EML5':'AL121768.1'
}

# see here for more: http://www.genenames.org/genefamilies/TR#TRG
locus = {
'TRA@':set(['TRAV1-1','TRAV1-2','TRAV2','TRAV3','TRAV4','TRAV5','TRAV6','TRAV7','TRAV8-1',
'TRAV8-2','TRAV8-3','TRAV8-4','TRAV8-5','TRAV8-6','TRAV8-7','TRAV9-1','TRAV9-2',
'TRAV10','TRAV11','TRAV12-1','TRAV12-2','TRAV12-3','TRAV13-1','TRAV13-2',
'TRAV14DV4','TRAV15','TRAV16','TRAV17','TRAV18','TRAV19','TRAV20','TRAV21',
'TRAV22','TRAV23DV6','TRAV24','TRAV25','TRAV26-1','TRAV26-2','TRAV27','TRAV28',
'TRAV29DV5','TRAV30','TRAV31','TRAV32','TRAV33','TRAV34','TRAV35','TRAV36DV7',
'TRAV37','TRAV38-1','TRAV38-2DV8','TRAV39','TRAV40','TRAV41','TRAJ1','TRAJ2',
'TRAJ3','TRAJ4','TRAJ5','TRAJ6','TRAJ7','TRAJ8','TRAJ9','TRAJ10','TRAJ11',
'TRAJ12','TRAJ13','TRAJ14','TRAJ15','TRAJ16','TRAJ17','TRAJ18','TRAJ19',
'TRAJ20','TRAJ21','TRAJ22','TRAJ23','TRAJ24','TRAJ25','TRAJ26','TRAJ27',
'TRAJ28','TRAJ29','TRAJ30','TRAJ31','TRAJ32','TRAJ33','TRAJ34','TRAJ35',
'TRAJ36','TRAJ37','TRAJ38','TRAJ39','TRAJ40','TRAJ41','TRAJ42','TRAJ43',
'TRAJ44','TRAJ45','TRAJ46','TRAJ47','TRAJ48','TRAJ49','TRAJ50','TRAJ51','TRAJ52'
,'TRAJ53','TRAJ54','TRAJ55','TRAJ56','TRAJ57','TRAJ58','TRAJ59','TRAJ60',
'TRAJ61','TRAC']),

'TRB@':set(['TRBV1','TRBV2','TRBV3-1','TRBV3-2','TRBV4-1','TRBV4-2','TRBV4-3','TRBV5-1',
'TRBV5-2','TRBV5-3','TRBV5-4','TRBV5-5','TRBV5-6','TRBV5-7','TRBV6-2','TRBV6-3',
'TRBV6-4','TRBV6-5','TRBV6-6','TRBV6-7','TRBV6-8','TRBV6-9','TRBV7-1','TRBV7-2',
'TRBV7-3','TRBV7-4','TRBV7-5','TRBV7-6','TRBV7-7','TRBV7-8','TRBV7-9','TRBV8-1',
'TRBV8-2','TRBV9','TRBV10-1','TRBV10-2','TRBV10-3','TRBV11-1','TRBV11-2',
'TRBV11-3','TRBV12-1','TRBV12-2','TRBV12-3','TRBV12-4','TRBV12-5','TRBV13',
'TRBV14','TRBV15','TRBV16','TRBV17','TRBV18','TRBV19','TRBV20-1','TRBV21-1',
'TRBV22-1','TRBV23-1','TRBV24-1','TRBV25-1','TRBV26','TRBV27','TRBV28',
'TRBV29-1','TRBV30','TRBVA','TRBVB','TRBV5-8','TRBV6-1','TRBD1','TRBD2',
'TRBJ1-1','TRBJ1-2','TRBJ1-3','TRBJ1-4','TRBJ1-5','TRBJ1-6','TRBJ2-1','TRBJ2-2',
'TRBJ2-2P','TRBJ2-3','TRBJ2-4','TRBJ2-5','TRBJ2-6','TRBJ2-7','TRBC1','TRBC2']),

'TRD@':set(['TRDV1','TRDV2','TRDV3','TRDD1','TRDD2','TRDD3','TRDJ1','TRDJ2',
'TRDJ3','TRDJ4','TRDC']),

'TRG@':set(['TRGV1','TRGV2','TRGV3','TRGV4','TRGV5','TRGV5P','TRGV6','TRGV7',
'TRGV8','TRGV9','TRGV10','TRGV11','TRGVA','TRGVB','TRGJ1','TRGJ2','TRGJP',
'TRGJP1','TRGJP2','TRGC1','TRGC2']),

'IGH@':set(['IGHV1-2','IGHV1-3','IGHV1-8','IGHV1-12','IGHV1-14','IGHV1-17','IGHV1-18',
'IGHV1-24','IGHV1-45','IGHV1-46','IGHV1-58','IGHV1-67','IGHV1-68','IGHV1-69',
'IGHV1-C','IGHV1-F','IGHV2-5','IGHV2-10','IGHV2-26','IGHV2-70','IGHV3-6',
'IGHV3-7','IGHV3-9','IGHV3-11','IGHV3-13','IGHV3-15','IGHV3-16','IGHV3-19',
'IGHV3-20','IGHV3-21','IGHV3-22','IGHV3-23','IGHV3-25','IGHV3-29','IGHV3-30',
'IGHV3-30-2','IGHV3-30-3','IGHV3-30-5','IGHV3-32','IGHV3-33','IGHV3-33-2',
'IGHV3-35','IGHV3-36','IGHV3-37','IGHV3-38','IGHV3-41','IGHV3-42','IGHV3-43',
'IGHV3-47','IGHV3-48','IGHV3-49','IGHV3-50','IGHV3-52','IGHV3-53','IGHV3-54',
'IGHV3-57','IGHV3-60','IGHV3-62','IGHV3-63','IGHV3-64','IGHV3-65','IGHV3-66',
'IGHV3-71','IGHV3-72','IGHV3-73','IGHV3-74','IGHV3-75','IGHV3-76','IGHV3-79',
'IGHV3-D','IGHV3-H','IGHV4-4','IGHV4-28','IGHV4-30-1','IGHV4-30-2','IGHV4-30-4',
'IGHV4-31','IGHV4-34','IGHV4-39','IGHV4-55','IGHV4-59','IGHV4-61','IGHV4-80',
'IGHV4-B','IGHV5-51','IGHV5-78','IGHV5-A','IGHV6-1','IGHV7-4-1','IGHV7-27',
'IGHV7-34-1','IGHV7-40','IGHV7-56','IGHV7-81','IGHVII-1-1','IGHVII-15-1',
'IGHVII-20-1','IGHVII-22-1','IGHVII-26-2','IGHVII-28-1','IGHVII-31-1',
'IGHVII-30-1','IGHVII-33-1','IGHVII-40-1','IGHVII-43-1','IGHVII-44-2',
'IGHVII-46-1','IGHVII-49-1','IGHVII-51-2','IGHVII-53-1','IGHVII-60-1',
'IGHVII-62-1','IGHVII-65-1','IGHVII-67-1','IGHVII-74-1','IGHVII-78-1',
'IGHVIII-2-1','IGHVIII-5-1','IGHVIII-5-2','IGHVIII-11-1','IGHVIII-13-1',
'IGHVIII-16-1','IGHVIII-22-2','IGHVIII-25-1','IGHVIII-26-1','IGHVIII-38-1',
'IGHVIII-44','IGHVIII-47-1','IGHVIII-51-1','IGHVIII-67-2','IGHVIII-67-3',
'IGHVIII-67-4','IGHVIII-76-1','IGHVIII-82','IGHVIV-44-1','IGHD1-1',
'IGHD1-7','IGHD1-14','IGHD1-20','IGHD1-26','IGHD2-2','IGHD2-8','IGHD2-15',
'IGHD2-21','IGHD3-3','IGHD3-9','IGHD3-10','IGHD3-16','IGHD3-22','IGHD4-4',
'IGHD4-11','IGHD4-17','IGHD4-23','IGHD5-5','IGHD5-12','IGHD5-18','IGHD5-24',
'IGHD6-6','IGHD6-13','IGHD6-19','IGHD6-25','IGHD7-27','IGHJ1','IGHJ1P',
'IGHJ2','IGHJ2P','IGHJ3','IGHJ3P','IGHJ4','IGHJ5','IGHJ6','IGHA1','IGHA2',
'IGHG1','IGHG2','IGHG3','IGHG4','IGHGP','IGHD','IGHE','IGHEP1','IGHM']),

'IGHV@':set(['IGHV1-2','IGHV1-3','IGHV1-8','IGHV1-12','IGHV1-14','IGHV1-17','IGHV1-18',
'IGHV1-24','IGHV1-45','IGHV1-46','IGHV1-58','IGHV1-67','IGHV1-68','IGHV1-69',
'IGHV1-C','IGHV1-F','IGHV2-5','IGHV2-10','IGHV2-26','IGHV2-70','IGHV3-6',
'IGHV3-7','IGHV3-9','IGHV3-11','IGHV3-13','IGHV3-15','IGHV3-16','IGHV3-19',
'IGHV3-20','IGHV3-21','IGHV3-22','IGHV3-23','IGHV3-25','IGHV3-29','IGHV3-30',
'IGHV3-30-2','IGHV3-30-3','IGHV3-30-5','IGHV3-32','IGHV3-33','IGHV3-33-2',
'IGHV3-35','IGHV3-36','IGHV3-37','IGHV3-38','IGHV3-41','IGHV3-42','IGHV3-43',
'IGHV3-47','IGHV3-48','IGHV3-49','IGHV3-50','IGHV3-52','IGHV3-53','IGHV3-54',
'IGHV3-57','IGHV3-60','IGHV3-62','IGHV3-63','IGHV3-64','IGHV3-65','IGHV3-66',
'IGHV3-71','IGHV3-72','IGHV3-73','IGHV3-74','IGHV3-75','IGHV3-76','IGHV3-79',
'IGHV3-D','IGHV3-H','IGHV4-4','IGHV4-28','IGHV4-30-1','IGHV4-30-2','IGHV4-30-4',
'IGHV4-31','IGHV4-34','IGHV4-39','IGHV4-55','IGHV4-59','IGHV4-61','IGHV4-80',
'IGHV4-B','IGHV5-51','IGHV5-78','IGHV5-A','IGHV6-1','IGHV7-4-1','IGHV7-27',
'IGHV7-34-1','IGHV7-40','IGHV7-56','IGHV7-81','IGHVII-1-1','IGHVII-15-1',
'IGHVII-20-1','IGHVII-22-1','IGHVII-26-2','IGHVII-28-1','IGHVII-31-1',
'IGHVII-30-1','IGHVII-33-1','IGHVII-40-1','IGHVII-43-1','IGHVII-44-2',
'IGHVII-46-1','IGHVII-49-1','IGHVII-51-2','IGHVII-53-1','IGHVII-60-1',
'IGHVII-62-1','IGHVII-65-1','IGHVII-67-1','IGHVII-74-1','IGHVII-78-1',
'IGHVIII-2-1','IGHVIII-5-1','IGHVIII-5-2','IGHVIII-11-1','IGHVIII-13-1',
'IGHVIII-16-1','IGHVIII-22-2','IGHVIII-25-1','IGHVIII-26-1','IGHVIII-38-1',
'IGHVIII-44','IGHVIII-47-1','IGHVIII-51-1','IGHVIII-67-2','IGHVIII-67-3',
'IGHVIII-67-4','IGHVIII-76-1','IGHVIII-82','IGHVIV-44-1','IGHD1-1',
'IGHD1-7','IGHD1-14','IGHD1-20','IGHD1-26','IGHD2-2','IGHD2-8','IGHD2-15',
'IGHD2-21','IGHD3-3','IGHD3-9','IGHD3-10','IGHD3-16','IGHD3-22','IGHD4-4',
'IGHD4-11','IGHD4-17','IGHD4-23','IGHD5-5','IGHD5-12','IGHD5-18','IGHD5-24',
'IGHD6-6','IGHD6-13','IGHD6-19','IGHD6-25','IGHD7-27','IGHJ1','IGHJ1P',
'IGHJ2','IGHJ2P','IGHJ3','IGHJ3P','IGHJ4','IGHJ5','IGHJ6','IGHA1','IGHA2',
'IGHG1','IGHG2','IGHG3','IGHG4','IGHGP','IGHD','IGHE','IGHEP1','IGHM']),

'IGK@':set(['IGKV1-5','IGKV1-6','IGKV1-8','IGKV1-9','IGKV1-12','IGKV1-13','IGKV1-16',
'IGKV1-17','IGKV1-22','IGKV1-27','IGKV1-32','IGKV1-33','IGKV1-35','IGKV1-37',
'IGKV1-39','IGKV1D-8','IGKV1D-12','IGKV1D-13','IGKV1D-16','IGKV1D-17',
'IGKV1D-22','IGKV1D-27','IGKV1D-32','IGKV1D-33','IGKV1D-35','IGKV1D-37',
'IGKV1D-39','IGKV1D-42','IGKV1D-43','IGKV2-4','IGKV2-10','IGKV2-14','IGKV2-18',
'IGKV2-19','IGKV2-23','IGKV2-24','IGKV2-26','IGKV2-28','IGKV2-29','IGKV2-30',
'IGKV2-36','IGKV2-38','IGKV2-40','IGKV2D-10','IGKV2D-14','IGKV2D-18',
'IGKV2D-19','IGKV2D-23','IGKV2D-24','IGKV2D-26','IGKV2D-28','IGKV2D-29',
'IGKV2D-30','IGKV2D-36','IGKV2D-38','IGKV2D-40','IGKV3-7','IGKV3-11','IGKV3-15',
'IGKV3-20','IGKV3-25','IGKV3-31','IGKV3-34','IGKV3D-7','IGKV3D-11','IGKV3D-15',
'IGKV3D-20','IGKV3D-25','IGKV3D-31','IGKV3D-34','IGKV4-1','IGKV5-2','IGKV6-21',
'IGKV6D-21','IGKV6D-41','IGKV7-3','IGKJ1','IGKJ2','IGKJ3','IGKJ4','IGKJ5',
'IGKC']),

'IGKV@':set(['IGKV1-5','IGKV1-6','IGKV1-8','IGKV1-9','IGKV1-12','IGKV1-13','IGKV1-16',
'IGKV1-17','IGKV1-22','IGKV1-27','IGKV1-32','IGKV1-33','IGKV1-35','IGKV1-37',
'IGKV1-39','IGKV1D-8','IGKV1D-12','IGKV1D-13','IGKV1D-16','IGKV1D-17',
'IGKV1D-22','IGKV1D-27','IGKV1D-32','IGKV1D-33','IGKV1D-35','IGKV1D-37',
'IGKV1D-39','IGKV1D-42','IGKV1D-43','IGKV2-4','IGKV2-10','IGKV2-14','IGKV2-18',
'IGKV2-19','IGKV2-23','IGKV2-24','IGKV2-26','IGKV2-28','IGKV2-29','IGKV2-30',
'IGKV2-36','IGKV2-38','IGKV2-40','IGKV2D-10','IGKV2D-14','IGKV2D-18',
'IGKV2D-19','IGKV2D-23','IGKV2D-24','IGKV2D-26','IGKV2D-28','IGKV2D-29',
'IGKV2D-30','IGKV2D-36','IGKV2D-38','IGKV2D-40','IGKV3-7','IGKV3-11','IGKV3-15',
'IGKV3-20','IGKV3-25','IGKV3-31','IGKV3-34','IGKV3D-7','IGKV3D-11','IGKV3D-15',
'IGKV3D-20','IGKV3D-25','IGKV3D-31','IGKV3D-34','IGKV4-1','IGKV5-2','IGKV6-21',
'IGKV6D-21','IGKV6D-41','IGKV7-3','IGKJ1','IGKJ2','IGKJ3','IGKJ4','IGKJ5',
'IGKC']),

'IGL@':set(['IGLV1-36','IGLV1-40','IGLV1-41','IGLV1-44','IGLV1-47','IGLV1-50',
'IGLV1-51','IGLV1-62','IGLV2-5','IGLV2-8','IGLV2-11','IGLV2-14','IGLV2-18',
'IGLV2-23','IGLV2-28','IGLV2-33','IGLV2-34','IGLV3-1','IGLV3-2','IGLV3-4',
'IGLV3-6','IGLV3-7','IGLV3-9','IGLV3-10','IGLV3-12','IGLV3-13','IGLV3-15',
'IGLV3-16','IGLV3-17','IGLV3-19','IGLV3-21','IGLV3-22','IGLV3-24','IGLV3-25',
'IGLV3-26','IGLV3-27','IGLV3-29','IGLV3-30','IGLV3-31','IGLV3-32','IGLV4-3',
'IGLV4-60','IGLV4-69','IGLV5-37','IGLV5-39','IGLV5-45','IGLV5-48','IGLV5-52',
'IGLV6-57','IGLV7-35','IGLV7-43','IGLV7-46','IGLV8-61','IGLV9-49','IGLV10-54',
'IGLV10-67','IGLV11-55','IGLVI-20','IGLVI-38','IGLVI-42','IGLVI-56','IGLVI-63',
'IGLVI-68','IGLVI-70','IGLVIV-53','IGLVIV-59','IGLVIV-64','IGLVIV-65',
'IGLVIV-66-1','IGLVV-58','IGLVV-66','IGLVVI-22-1','IGLVVI-25-1','IGLVVII-41-1',
'IGLJ1','IGLJ2','IGLJ3','IGLJ4','IGLJ5','IGLJ6','IGLJ7','IGLC1','IGLC2',
'IGLC3','IGLC4','IGLC5','IGLC6','IGLC7']),

'IGLV@':set(['IGLV1-36','IGLV1-40','IGLV1-41','IGLV1-44','IGLV1-47','IGLV1-50',
'IGLV1-51','IGLV1-62','IGLV2-5','IGLV2-8','IGLV2-11','IGLV2-14','IGLV2-18',
'IGLV2-23','IGLV2-28','IGLV2-33','IGLV2-34','IGLV3-1','IGLV3-2','IGLV3-4',
'IGLV3-6','IGLV3-7','IGLV3-9','IGLV3-10','IGLV3-12','IGLV3-13','IGLV3-15',
'IGLV3-16','IGLV3-17','IGLV3-19','IGLV3-21','IGLV3-22','IGLV3-24','IGLV3-25',
'IGLV3-26','IGLV3-27','IGLV3-29','IGLV3-30','IGLV3-31','IGLV3-32','IGLV4-3',
'IGLV4-60','IGLV4-69','IGLV5-37','IGLV5-39','IGLV5-45','IGLV5-48','IGLV5-52',
'IGLV6-57','IGLV7-35','IGLV7-43','IGLV7-46','IGLV8-61','IGLV9-49','IGLV10-54',
'IGLV10-67','IGLV11-55','IGLVI-20','IGLVI-38','IGLVI-42','IGLVI-56','IGLVI-63',
'IGLVI-68','IGLVI-70','IGLVIV-53','IGLVIV-59','IGLVIV-64','IGLVIV-65',
'IGLVIV-66-1','IGLVV-58','IGLVV-66','IGLVVI-22-1','IGLVVI-25-1','IGLVVII-41-1',
'IGLJ1','IGLJ2','IGLJ3','IGLJ4','IGLJ5','IGLJ6','IGLJ7','IGLC1','IGLC2',
'IGLC3','IGLC4','IGLC5','IGLC6','IGLC7']),

'HOXA@':set(['HOXA-AS2','HOXA-AS3','HOXA-AS4','HOXA11-AS','HOXA1','HOXA2',
'HOXA3','HOXA4','HOXA5','HOXA6','HOXA7','HOXA9','HOXA10','HOXA11','HOXA13']),

'HLA@':set(['HLA-AS1','HLA-DRA','HLA-DRB5','HLA-DRB1','HLA-DQA1','HLA-DQB1','HLA-DQA2',
'HLA-DQB2','HLA-DOB','HLA-DOA','HLA-DPA1','HLA-DPB1','HLA-DMB','HLA-DMB',
'HLA-DMA','HLA-F-AS1','HLA-V','HLA-P','HLA-H','HLA-T','HLA-K','HLA-U','HLA-W',
'HLA-J','HLA-L','HLA-N','HLA-A','HLA-S','HLA-F','HLA-DRB9','HLA-DRB6','HLA-G',
'HLA-DQB1-AS1','HLA-DQB3','HLA-Z','HLA-A','HLA-DPA2','HLA-DPB2','HLA-DPA3',
'HLA-E','HLA-V','HLA-P','HLA-F','HLA-DRB9','HLA-H','HLA-DQB1-AS1','HLA-T',
'HLA-K','HLA-DQB3','HLA-U','HLA-W','HLA-G','HLA-Z','HLA-DPA2','HLA-DPB2',
'HLA-A','HLA-J','HLA-L','HLA-N','HLA-S','HLA-DRB9','HLA-DRB2','HLA-DQB1-AS1',
'HLA-DQB3','HLA-Z','HLA-DPA2','HLA-DPB2','HLA-DPA3','HLA-E','HLA-F','HLA-DRA',
'HLA-G','HLA-DRB3','HLA-A','HLA-DRB1','HLA-DQA1','HLA-F-AS1','HLA-DQB1',
'HLA-DRB3','HLA-DQA2','HLA-DQB2','HLA-V','HLA-C','HLA-DQA2','HLA-P','HLA-DQB2',
'HLA-DOB','HLA-H','HLA-T','HLA-K','HLA-U','HLA-W','HLA-F','HLA-F-AS1','HLA-V',
'HLA-P','HLA-H','HLA-J','HLA-T','HLA-K','HLA-U','HLA-W','HLA-J','HLA-L','HLA-L',
'HLA-DMB','HLA-N','HLA-N','HLA-DMA','HLA-S','HLA-DRB9','HLA-DRB2',
'HLA-DQB1-AS1','HLA-DQB3','HLA-S','HLA-DMB','HLA-Z','HLA-DPA2','HLA-DOA',
'HLA-DPB2','HLA-DPA3','HLA-DPA1','HLA-DMA','HLA-DPB1','HLA-DRB9','HLA-DRB8',
'HLA-DRB7','HLA-DQB1-AS1','HLA-DQB3','HLA-Z','HLA-DPA2','HLA-DPB2','HLA-DPA3',
'HLA-E','HLA-DOA','HLA-DPA1','HLA-DPB1','HLA-H','HLA-T','HLA-K','HLA-U','HLA-W',
'HLA-J','HLA-DRA','HLA-DRB3','HLA-DRB1','HLA-DQB1','HLA-L','HLA-DQA2',
'HLA-DQB2','HLA-DOB','HLA-N','HLA-DRB9','HLA-DRB7','HLA-DQB1-AS1','HLA-DQB3',
'HLA-DMB','HLA-DMA','HLA-Z','HLA-DPA2','HLA-DPB2','HLA-DPA3','HLA-F-AS1',
'HLA-F-AS1','HLA-V','HLA-V','HLA-P','HLA-H','HLA-T','HLA-P','HLA-K','HLA-H',
'HLA-T','HLA-W','HLA-DOA','HLA-U','HLA-W','HLA-J','HLA-DPA1','HLA-DPB1','HLA-J',
'HLA-L','HLA-DRA','HLA-F-AS1','HLA-N','HLA-DRB4','HLA-DRB1','HLA-DQA1','HLA-S',
'HLA-DQB1','HLA-DRB9','HLA-DRB9','HLA-DRB9','HLA-DRB8','HLA-DRB8','HLA-DRB8',
'HLA-DRB7','HLA-DRB7','HLA-DRB7','HLA-DQB1-AS1','HLA-DQA2','HLA-DQB3',
'HLA-DQB2','HLA-Z','HLA-DPA2','HLA-DOB','HLA-DPB2','HLA-DPA3','HLA-DMB',
'HLA-DMA','HLA-DOA','HLA-DPA1','HLA-DPB1','HLA-DRA','HLA-DRB4','HLA-DQA1',
'HLA-DQB1','HLA-G','HLA-A','HLA-DQA2','HLA-F','HLA-DQB2','HLA-DOB','HLA-DMB',
'HLA-G','HLA-A','HLA-DMA','HLA-DPA1','HLA-DPB1','HLA-V','HLA-P','HLA-H','HLA-T',
'HLA-K','HLA-U','HLA-W','HLA-E','HLA-J','HLA-E','HLA-N','HLA-DRB9','HLA-DQB3',
'HLA-Z','HLA-DPA2','HLA-F','HLA-DPB2','HLA-DPA3','HLA-G','HLA-F','HLA-A',
'HLA-G','HLA-A','HLA-E','HLA-C','HLA-E','HLA-B','HLA-C','HLA-B','HLA-C','HLA-B',
'HLA-C','HLA-B','HLA-C','HLA-B','HLA-DRA','HLA-DRB1','HLA-DQA1','HLA-DQB1',
'HLA-C','HLA-DQA2','HLA-DQB2','HLA-DOB','HLA-B','HLA-DMB','HLA-DMA','HLA-DOA',
'HLA-DPA1','HLA-DPB1','HLA-DRA','HLA-DRA','HLA-DRA','HLA-DRB4','HLA-DRB4',
'HLA-DRB4','HLA-DRB1','HLA-DQA1','HLA-DQB1','HLA-DQA2','HLA-DQB2','HLA-DMB',
'HLA-DMA','HLA-DOA','HLA-DPA1','HLA-DPB1','HLA-F-AS1','HLA-V','HLA-P','HLA-G',
'HLA-T','HLA-K','HLA-U','HLA-A','HLA-W']),

'HOXB@':set(['HOXB-AS1','HOXB-AS2','HOXB-AS4','HOXB-AS5','HOXB1','HOXB2',
'HOXB3','HOXB-AS3','HOXB4','HOXB5','HOXB6','HOXB7','HOXB8','HOXB9','HOXB13'])

}

# read the gene symbols
def read_genes_symbols(gene_symbols_filename = 'synonyms.txt'):
    genes = [line.rstrip('\r\n').split('\t') for line in file(gene_symbols_filename,'r').readlines()]
    g = dict()
    for line in genes:
        k = line[0].upper() # ensembl
        v = line[1].upper() # symbol
        if not g.has_key(v):
            g[v] = set()
        g[v].add(k)
    return g

def find_starts(txt,gs):
    r = []
    for t in txt:
        r.extend([el for el in gs if el.upper().startswith(t.upper())])
    return list(set(r))

# read the gene symbols and generate loci
def generate_loci(gene_symbols_filename = 'genes_symbols.txt'):
    genes = [line.rstrip('\r\n').split('\t') for line in file(gene_symbols_filename,'r').readlines()]
    genes = list(set([v.upper() for (k,v) in genes]))

    loci = dict()
    loci['HOXA@'] = find_starts(['HOXA'],genes)
    loci['HOXB@'] = find_starts(['HOXB'],genes)
    loci['HOXC@'] = find_starts(['HOXC'],genes)
    loci['HOXD@'] = find_starts(['HOXD'],genes)
    loci['HOX@'] = loci['HOXA@'] + loci['HOXB@'] + loci['HOXC@'] + loci['HOXD@']
    
    loci['HLA@'] = find_starts(['HLA-'],genes)

    loci['IGL@'] = find_starts(['IGLV','IGLJ','IGLC','IGLL','IGL_locus','IGH_locus'],genes)
    loci['IGLV@'] = loci['IGL@']
    loci['IGK@'] = find_starts(['IGKV','IGKJ','IGKC','IGK_locus'],genes)
    loci['IGKV@'] = loci['IGK@']
    loci['IGH@'] = find_starts(['IGHV','IGHD','IGHJ','IGHA','IGHG','IGHE','IGHM','IGH_locus','IGL_locus'],genes)
    loci['IGHV@'] = loci['IGH@']
    loci['IG@'] = loci['IGL@'] + loci['IGK@'] + loci['IGH@']

    loci['TRA@'] = find_starts(['TRAC','TRAV','TRAJ','TRA_locus'],genes)
    loci['TCRA@'] = loci['TRA@']
    loci['TRB@'] = find_starts(['TRBV','TRBD','TRBJ','TRBC','TRB_locus'],genes)
    loci['TCRB@'] = loci['TRB@']
    loci['TRBV@'] = find_starts(['TRBV'],genes)
    loci['TCRVB@'] = loci['TRBV@']
    loci['TCRBV@'] = loci['TRBV@']
    loci['TRD@'] = find_starts(['TRDV','TRDD','TRDJ','TRDC','TRD_locus'],genes)
    loci['TCRB@'] = loci['TRD@']
    loci['TRG@'] = find_starts(['TRGV','TRGJ','TRGC','TRG_locus'],genes)
    loci['TCRG@'] = loci['TRG@']
    loci['TCR@'] = loci['TRG@'] + loci['TRD@'] + loci['TRBV@'] + loci['TRB@'] + loci['TRA@']
    return loci

# converts only gene symbol to ensembl id

def ensembl(g,genes):
    ens = None
    if g.endswith('@'):
        e = []
        for ex in locus.get(g.upper(),None):
            e.extend(ensembl(ex,genes))
        ens = list(set(e))
    else:
        ens = genes.get(g.upper(),None)
        if not ens:
            ens = genes.get(synonym.get(g.upper(),None),None)
            # I let it pass if it is and Ensembl id
            if (not ens) and g.upper().startswith('ENS'):
                ens = [g.upper()]
    if not ens:
        print >>sys.stderr,"Warning: Could not find Ensembl gene id for gene '%s' [synonym: %s]!" % (g,synonym.get(g,None))
    else:
        ens = list(ens)
    return ens

def ensembl(g,genes,loci):
    ens = None
    if g.endswith('@'):
        e = []
        for ex in loci.get(g.upper(),None):
            e.extend(ensembl(ex,genes,loci))
        ens = list(set(e))
    else:
        ens = genes.get(g.upper(),None)
        if not ens:
            ens = genes.get(synonym.get(g.upper(),None),None)
            # I let it pass if it is and Ensembl id
            if (not ens) and g.upper().startswith('ENS'):
                ens = [g.upper()]
    if not ens:
        print >>sys.stderr,"Warning: Could not find Ensembl gene id for gene '%s' [synonym: %s]." % (g,synonym.get(g,None))
    else:
        ens = list(ens)
    return ens
#
