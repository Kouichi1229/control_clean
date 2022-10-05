import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

Corporation=['company', 'incorporated', 'corporation', 'corp.', 'corp', 'inc',
      '& co.', '& co', 'inc.', 's.p.a.', 'n.v.', 'a.g.', 'ag', 'nuf', 's.a.', 's.f.',
      'oao', 'co.', 'co','kabushiki kaisha','kk','k.k.','k.k'
    ]

General_Partnership=['soc.col.', 'stg', 'd.n.o.', 'ltda.', 'v.o.s.', 'a spol.',
      u've\xc5\x99. obch. spol.', 'kgaa', 'o.e.', 's.f.', 's.n.c.', 's.a.p.a.', 'j.t.d.',
      'v.o.f.', 'sp.j.', 'og', 'sd', ' i/s', 'ay', 'snc', 'oe', 'bt.', 's.s.', 'mb',
      'ans', 'da', 'o.d.', 'hb', 'pt'
    ]

Unlimited=['unltd', 'ultd', 'sal', 'unlimited', 'saog', 'saoc', 'aj',
      'yoaj', 'oaj', 'akc. spol.', 'a.s.'
    ]

Joint_Venture=['esv', 'gie', 'kv.', 'qk']

Limited=['pty. ltd.', 'pty ltd', 'ltd', 'l.t.d.','ltd.', 'bvba', 'd.o.o.', 'ltda', 'gmbh',
      'g.m.b.h', 'kft.', 'kht.', 'zrt.', 'ehf.', 's.a.r.l.', 'd.o.o.e.l.', 's. de r.l.',
      'b.v.', 'tapui',
      'sp. z.o.o.', 'sp. z o.o.', 'spółka z o.o.',
      's.r.l.', 's.l.', 's.l.n.e.', 'ood', 'oy', 'rt.',
      'teo', 'uab', 'scs', 'sprl', 'limited', 'bhd.', 'sdn. bhd.', 'sdn bhd', 'as',
      'lda.', 'tov', 'pp'
   ]

Limited_Liability_Company=['pllc', 'llc', 'l.l.c.', 'plc.', 'plc', 'hf.', 'oyj',
      'a.e.', 'nyrt.', 'p.l.c.', 'sh.a.', 's.a.', 's.r.l.', 'srl.', 'srl', 'aat', '3at', 'd.d.',
      's.r.o.', 'spol. s r.o.', 's.m.b.a.', 'smba', 'sarl', 'nv', 'sa', 'aps',
      'a/s', 'p/s', 'sae', 'sasu', 'eurl', 'ae', 'cpt', 'as', 'ab', 'asa', 'ooo', 'dat',
      'vat', 'zat', 'mchj', 'a.d.'
    ]

Limited_Liability_Limited_Partnership= ['lllp', 'l.l.l.p.']
Limited_Liability_Partnership=['llp', 'l.l.p.', 'sp.p.', 's.c.a.', 's.c.s.']
Limited_Partnership=['gmbh & co. kg', 'lp', 'l.p.', 's.c.s.',
      's.c.p.a', 'comm.v', 'k.d.', 'k.d.a.', 's. en c.', 'e.e.', 's.a.s.', 's. en c.',
      'c.v.', 's.k.a.', 'sp.k.', 's.cra.', 'ky', 'scs', 'kg', 'kd', 'k/s', 'ee', 'secs',
      'kda', 'ks', 'kb','kt'
    ]

Mutual_Fund= ['sicav']
No_Liability= ['nl']
Non_Profit= ['vzw', 'ses.', 'gte.']
Private_Company= ['private', 'pte', 'xk']
Professional_Corporation=['p.c.', 'vof', 'snc']
Professional_Limited_Liability_Company= ['pllc', 'p.l.l.c.']
Sole_Proprietorship=['e.u.', 's.p.', 't:mi', 'tmi', 'e.v.', 'e.c.', 'et', 'obrt',
      'fie', 'ij', 'fop', 'xt']

    
    
TAKE_OUT_CORP_LLC_LTD =['COMPANY',
 'INCORPORATED','CORPORATION','CORP.','CORP','INC',
 'INC.','S.P.A.','N.V.','A.G.','AG','NUF','S.A.',
 'S.F.','OAO','CO.','CO','KABUSHIKI','KAISHA','KABUSHIKIKAISHA',
 'KK','K.K.','K.K','KABUSHIKI-KAISHA','PLLC','LLC','L.L.C.','PLC.','PLC',
 'HF.','OYJ','A.E.','NYRT.','P.L.C.','SH.A.','S.A.',
 'S.R.L.','SRL.','SRL','AAT','3AT','D.D.','S.R.O.',
 'SPOL. S R.O.','S.M.B.A.','SMBA','SARL','NV','SA',
 'APS','A/S','P/S','SAE','SASU','EURL','AE','CPT',
 'AS','AB','ASA','OOO','DAT','VAT', 'ZAT','MCHJ',
 'A.D.','PTY. LTD.','PTY LTD','LTD',
 'L.T.D.','LTD.','BVBA','D.O.O.','LTDA',
 'GMBH','G.M.B.H','KFT.','KHT.','ZRT.','EHF.',
 'S.A.R.L.','D.O.O.E.L.','S. DE R.L.',
 'B.V.','TAPUI','SP. Z.O.O.','SP. Z O.O.',
 'S.R.L.','S.L.','S.L.N.E.','OOD','OY',
 'RT.','TEO','UAB','SCS','SPRL',
 'LIMITED','BHD.','SDN. BHD.',
 'SDN BHD','AS','LDA.', 'TOV',
 'PP','THE','AND','OF']

TAKE_OUT_CORP_LLC_LTD_GERMANY =['COMPANY',
 'INCORPORATED','CORPORATION','CORP.','CORP','INC',
 'INC.','S.P.A.','N.V.','A.G.','AG','NUF','S.A.',
 'S.F.','OAO','CO.','CO','KABUSHIKI','KAISHA','KK','KABUSHIKIKAISHA',
 'K.K.','K.K','PLLC','LLC','L.L.C.','PLC.','PLC',
 'HF.','OYJ','A.E.','NYRT.','P.L.C.','SH.A.','S.A.',
 'S.R.L.','SRL.','SRL','AAT','3AT','D.D.','S.R.O.',
 'SPOL. S R.O.','S.M.B.A.','SMBA','SARL','NV','SA',
 'APS','A/S','P/S','SAE','SASU','EURL','AE','CPT',
 'AS','AB','ASA','OOO','DAT','VAT', 'ZAT','MCHJ',
 'A.D.','PTY. LTD.','PTY LTD','LTD',
 'L.T.D.','LTD.','BVBA','D.O.O.','LTDA',
 'GMBH','G.M.B.H','KFT.','KHT.','ZRT.','EHF.',
 'S.A.R.L.','D.O.O.E.L.','S. DE R.L.',
 'B.V.','TAPUI','SP. Z.O.O.','SP. Z O.O.',
 'S.R.L.','S.L.','S.L.N.E.','OOD','OY',
 'RT.','TEO','UAB','SCS','SPRL',
 'LIMITED','BHD.','SDN. BHD.',
 'SDN BHD','AS','LDA.', 'TOV',
 'PP','THE','AND','OF','E.G.',
 'E.V.','GBR','OHG','PARTG',
 'KGAA','GMBH','G.M.B.H.','AG','KG'
]
