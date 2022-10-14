NON_MEAN_WORDS=["THE","AND","OF",'LE','LA','LES','DE','AT','FOR','UND']

CORP=['COMPANY','COMPANY,','INCORPORATED','CORPORATION','CORP.','CORP','INC',
 'INC.','S.P.A.','N.V.','A.G.','AG','NUF','S.A.','S.F.','OAO','CO.',
 'CO','CO.,','CO,','KABUSHIKI','KAISHA','KABUSHIKIKAISHA','KK','K.K.','K.K',
 'KABUSHIKI-KAISHA','AKTIENGESELLSCHAFT','SPA','INCORP','AKTIENGESELLSCHRAFT']


LLC=['PLLC','LLC','L.L.C.','PLC.','PLC','HF.','OYJ','A.E.','NYRT.','S/A',
'P.L.C.','SH.A.','S.A.','S.R.L.','SRL.','SRL','AAT','3AT','D.D.',
'S.R.O.','SPOL.','S R.O.','S.M.B.A.','SMBA','SARL','NV','SA','APS','A/S',
'P/S','SAE','SASU','EURL','AE','CPT','AS','AB','ASA','OOO','DAT','VAT',
'ZAT','MCHJ','A.D.','A.B.','AKTIEBOLAG']

LIMITED=['PTY. LTD.','PTY LTD','LTD','L.T.D.','LTD.','BVBA','D.O.O.','LTDA',
 'GMBH','G.M.B.H','KFT.','KHT.','ZRT.','EHF.','S.A.R.L.','D.O.O.E.L.','S.','DE','R.L.',
 'B.V.','TAPUI','SP.','Z O.O.','Z.O.O.','S.R.L.','S.L.','S,R.L.','S.L.N.E.','OOD','OY',
 'RT.','TEO','UAB','SCS','SPRL','LIMITED','BHD.','SDN. BHD.',
 'SDN','BHD','AS','LDA.', 'TOV','PP']

LLLP=['LLLP', 'L.L.L.P.']

LLP=['LLP', 'L.L.P.', 'SP.P.', 'S.C.A.', 'S.C.S.']

LP=['GMBH','&','CO.','KG','LP','L.P.','KOMMANDITGESELLSCHAFT'
 'S.C.S.','S.C.P.A','COMM.V','MIT','BESCHRANKTER',
 'K.D.','K.D.A.','S.','EN','C.','HAFTUNG','K.G.'
 'E.E.','S.A.S.','C.V.','S.K.A.',
 'SP.K.','S.CRA.','KY','SCS','KG',
 'KD','K/S','EE','SECS','KDA','KS',
 'KB','KT','MIT',' BESCHRAENKTER','HAFTUNG',
 'BESCHRÄNKTER','GESELLSCHAFT','M.B.H.','G.M.B.H.']

PTE=['PRIVATE', 'PTE', 'XK']

PLLC=['PLLC', 'P.L.L.C.']

ORG_UNIT=['GOVERMMENT','UNIVERSITY','UNIV','UNIVERSITE','SCH','SCHOOL','GRP','GROUP','FDN','FOUNDATION',
'ASSOC','ASSOCIATION','ORG','ORGANIZATION','CTR','CENTER','OBSERV','OBSERVATORY','INST','INSTITUTE',
'COLLEGE','COLL','HOST','HOSPITAL','NATIONAL','NAIL','LAB','LABORATORY','RESEARCH','DEPARTMENT','BANK']

INVENTER_NAME_CLEAN=['DR','DE','DA','DI','MC','VON','DER','VAN', 'DEN']

COUNTRY=['US','UNITED','STATE','CHINA','GERMANY','CHINA MAINLAND','FRANCE','JAPAN','ITALY',
'SPAIN','CANADA','KINGDOM','UK','AUSTRALIA','NETHERLANDS','SWITZERLAND','SAUDI ARABIA','AUSTRIA',
'SWISS','DENMARK','TAIWAN','BELGIUM','FINLAND','INDIA','SINGAPORE','SWEDEN','NORWAY']

WRONG_WORDS_CROP=['COPORATION','CORPORATON','COROPORATION','CORPORTAION','CORPORAION',
'CORPORTION','CORPORATI','CORPOTRATION','CORPORATIION','CORPROATION',"CROP",
'CORPORATIOB','CORPORATED','CORPORATIN','CORPPORATION','CORPORATION']

WRONG_WORDS_INC=['INCOPORATION','INCOROPORATION','INCORPORAION','INCORPORATI','INCORPORATIION','INCROP',
 'INCORPORATON','INCORPORTAION','INCORPORTION','INCORPOTRATION','INCORPROATION','INCORPORATION','INE','IN'
]
WRONG_WORDS_CO=['COMANY', 'COMAPNY', 'COMPAMY','CAMPANY','COMAPN','COMMPANY','COMPA','COMPAANY',
'EOMPANY','CORMPANY','COPMPANY','COMPAY','COMPANT','COMPANH','COMPANCY','COMPANAY','CMPANY']

WRONG_WORDS_KK=['KABUSHIKIKAISYA','KABISHIKI','KABUSHIJI','KAISYA','KABIUSHIKI','KAIGHA',
'KABKUSHIKI','KAISHI','LABUSHIKI','DABUSHIKI','KSIAHA','KAISAHA','KSBUSHIKI','KAUBSHIKI',
'KIASHA','GAISHA','KABUSHIKII','KA8USHIKI','KABUSHIKIK','KABASHIKI','KABUSHIKL','KABUSHIK',
'KABSHIKI','KABSUHIKI','KABUAHIK','KABUASHIKI','KABUBSHIKI','KABUHIKI','KABUHSHIKI','KABUHSIKI',
'KABUHSIKIKASHIA','KABUISHIKI','KABUKSHIKI','KABUSBIKI','KABUSGIKI','KABUSH1KI','KABUSHI',
'KABUSHIHI','KABUSHIHKI','KABUSHII','KABUSHIIKI','KABUSHIKA','KABUSHIKI','KABUSHIKIA',
'KABUSHIKIAKIASHA','KABUSHIKIKAISHA','KABUSHIKIKI','KABUSHIKKIASHA','KABUSHINKI',
'KABUSHISHI','KABUSHISKI','KABUSHKI','KABUSHKIK','KABUSHLKI','KABUSHSIKI','KABUSHUIKI',
'KABUSHUKI','KABUSIHI','KABUSIHIKI','KABUSIHKI','KABUSIKI','KABUSIKIKAISKA','KABUSKI',
'KABUSKIKI','KABUUSHIKI','KAGUSHIKI','KAIAHA','KAIHSA','KAIISHA','KAISA','KAISAH',
'KAISH','KAISHA','KAISHAI','KAISHHA','KAISHIA','KAISHSA','KAISKA','KAKBUSHIKI',
'KAKISHA','KAKUSHIKI','KALSHA','KANBUSHIKI','KANUSHIKI','KARSHA','KASBUSHIKI',
'KASEI','KASHA','KASHIA','KASIAH','KASIHA','KASISHA','KASUSHIKI',
'KAUBUSHIKI','KAUSHIKI','KBAUSHIKI','KUBUSHIKI','XAISHA','KABUSIKIKAISHA'
]
WRONG_WORDS_AG=['AKTIENGELLSCHAFT','AKTIENGESSELLSCHAFT']

WRONG_WORDS_GMBH=['GBMH','GMBJ','CCO.','DG','HG','CI,']

WRONG_WORDS_LLC=['LCC','LLP']

WRONG_WORDS_LTD=['LITD.','LDT',' LTE','LTP.','LTDL','LGD','LRD','TLD','LED','LID','LIMOTED']

OTHERS=['&QUOT;','&AMP;','&LT;','&GT;','&OELIG;','&SCARON;',
'&YUML;','&CIRC;','&TILDE;','&ENSP;','&EMSP;','&THINSP;','&ZWNJ;',
'&ZWJ;','&LRM;','&RLM;','&NDASH;','&MDASH;','&LSQUO;','&RSQUO;',
'&SBQUO;','&LDQUO;','&RDQUO;','&BDQUO;','&DAGGER;','&PERMIL;',
'&EACUTE;','&LSQUO;','&SHARP;','&LDQUO;','&AMP;','&QUOT;',
'&COMMAT;','&','&QUEST;','&ANGST;','&PRIME;','&AACUTE;','&COMMAT;','&OUML;',
'&EACTE;','&NUM;','&AGRAVE;','&AACUTE;','&ACIRC;','&ATILDE;','&AUML;',
'&ARING;','&AELIG;','&SZLIG;','&CCEDIL;','&EGRAVE;',
'&EACUTE;','&ECIRC;','&EUML;','&#131;','&IGRAVE;',
'&IACUTE;','&ICIRC;','&IUML;','&NTILDE;','&OGRAVE;',
'&OACUTE;','&OCIRC;','&OTILDE;','&OUML;','&OSLASH;',
'&#140;','&#156;','&#138;','&#154;','&UGRAVE;',
'&UACUTE;','&UCIRC;','&UUML;','&#181;','&#215;',
'&YACUTE;','&#159;','&YUML;','&#176;','&#134;',
'&#135;','&LT;','&GT;','&#177;','&#171;',
'&#187;','&#191;','&#161;','&#183;','&#149;',
'&#153;','&COPY;','&REG;','&#167;','&#182;'
'&#34;','&#38;','&#60;','&#62;','&#338;',
'&#339;','&#352;','&#353;','&#376;','&#710;',
'&#732;','&#8194;','&#8195;','&#8201;','&#8204;',
'&#8205;','&#8206;','&#8207;','&#8211;','&#8212;',
'&#8216;','&#8217;','&#8218;','&#8220;','&#8221;',
'&#8222;','&#8224;','&#8225;','&#8240;','&#8249;',
'&#8250;','&#8364;''&#x22;','&#x26;','&#x3C;','&#x3E;','&#x152;','&#x153;',
'&#x160;','&#x161;','&#x178;','&#x2C6;','&#x2DC;',
'&#x2002;','&#x2003;','&#x2009;','&#x200C;','&#x200D;',
'&#x200E;','&#x200F;','&#x2013;','&#x2014;',
'&#x2018;','&#x2019;','&#x201A;','&#x201C;',
'&#x201D;','&#x201E;','&#x2020;','&#x2021;',
'&#x2030;','&#x2039;','&#x203A;','&#x20AC;'
]

OTRHER_DIGIT=['(501)',"501","502",'509']

def WRONG_WORDS_ALL():
    WRONG_WORDS_ALL=[]
    WRONG_WORDS_ALL.append(WRONG_WORDS_CROP)
    WRONG_WORDS_ALL.append(WRONG_WORDS_INC)
    WRONG_WORDS_ALL.append(WRONG_WORDS_CO)
    WRONG_WORDS_ALL.append(WRONG_WORDS_KK)
    WRONG_WORDS_ALL.append(WRONG_WORDS_GMBH)
    WRONG_WORDS_ALL.append(WRONG_WORDS_AG)
    WRONG_WORDS_ALL.append(WRONG_WORDS_LLC)
    WRONG_WORDS_ALL=sum(WRONG_WORDS_ALL,[])
    return WRONG_WORDS_ALL


replace_words_dicts={
'Lin' :'Linear', 
'Accel' : 'Accelerator',
'Bioinformat' : 'Bioinformatics', 
'Inst' : 'Institute', 
'Neurosci':'Neuroscience',
'Med': 'Medical',
'Assoc':'Association',
'Metr':'Metrics', 
'Evaluat':'Evalua',
'Ist':'Istituto',
'Acc':'Accelerator',
'Observ':'Observatory',
'Grad':'Graduate',
'Mt':'Mount',
'Econ':'Economics',
'Nutr':'Nutrition',
}
