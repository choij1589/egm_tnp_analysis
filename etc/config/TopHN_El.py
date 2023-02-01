from tnpConfig import tnpConfig

############## samples ################
samples={
    'data2016a':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016preVFP/data/SingleElectron',
    'mi2016a':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016preVFP/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'amc2016a':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016preVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mg2016a':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016preVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2016b':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016postVFP/data/SingleElectron',
    'mi2016b':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016postVFP/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'amc2016b':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016postVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mg2016b':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016postVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2017':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2017/data/SingleElectron',
    'mi2017':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2017/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'amc2017':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2017/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mg2017':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2017/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2018':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2018/data/EGamma',
    'mi2018':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2018/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'amc2018':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mg2018':'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
}
############## binning ################
bin_POGID = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.479, -0.8, 0., 0.8, 1.479, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 20, 35, 50, 100, 200, 500], 'title':'p_{T} [GeV]' },
]
bin_ID = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.479, -0.8, 0.0, 0.8, 1.479, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 50, 70, 100, 200, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele23 = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.479, -0.8, 0.0, 0.8, 1.479, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 19, 21, 23, 25, 30, 35, 50, 70, 100, 200], 'title':'p_{T} [GeV]' },
]
bin_Ele12 = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.479, -0.8, 0.0, 0.8, 1.479, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 12, 15, 20, 25, 30, 35, 50, 70, 100, 200], 'title':'p_{T} [GeV]' },
]


############### Expr ################
## selection
mcTrue='mcTrue'
mcTrue_dRp1='mcTrue && (el_eta-mc_probe_eta)*(el_eta-mc_probe_eta)+(el_phi-mc_probe_phi)*(el_phi-mc_probe_phi)<0.01'
medium_dRp1dPtRelp2='mcTrue && el_et/mc_probe_et>0.8 && el_et/mc_probe_et < 1.2 && (el_eta-mc_probe_eta)*(el_eta-mc_probe_eta)+(el_phi-mc_probe_phi)*(el_phi-mc_probe_phi)<0.01'

VetoGap    = '(abs(el_sc_eta)<1.444 || abs(el_sc_eta)>1.566)'
VetoGapTag = '(abs(tag_sc_eta)<1.444 || abs(tag_sc_eta)>1.566)'
MTCutTag = 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
TagCutBase27 = 'tag_Ele_pt > 30 && el_q*tag_Ele_q<0 && '+VetoGapTag
TagCutBase32 = 'tag_Ele_pt > 35 && el_q*tag_Ele_q<0 && '+VetoGapTag

#ID to test
HLTSafeEl_NoEA = '( (abs(el_sc_eta) < 1.479 && el_5x5_sieie < 0.013 && abs(el_dEtaSeed) < 0.01 && abs(el_dPhiIn) < 0.07 && el_hoe < 0.13 && el_ecalIso < 0.5*el_pt && el_hcalIso < 0.3*el_pt && el_dr03TkSumPt < 0.2*el_pt) || (abs(el_sc_eta) > 1.479 && el_5x5_sieie < 0.035 && abs(el_dEtaSeed) < 0.015 && abs(el_dPhiIn) < 0.1 && el_hoe < 0.13 && el_ecalIso < 0.5*el_pt && el_hcalIso < 0.3*el_pt && el_dr03TkSumPt < 0.2*el_pt) )'
HLTSafeEl = '( (abs(el_sc_eta) < 1.479 && el_5x5_sieie < 0.013 && abs(el_dEtaSeed) < 0.01 && abs(el_dPhiIn) < 0.07 && el_hoe < 0.13 && (el_ecalIso-event_rho*0.16544 < 0.5*el_pt) && (el_hcalIso-event_rho*0.05956 < 0.3*el_pt) && el_dr03TkSumPt < 0.2*el_pt) || (abs(el_sc_eta) > 1.479 && el_5x5_sieie < 0.035 && abs(el_dEtaSeed) < 0.015 && abs(el_dPhiIn) < 0.1 && el_hoe < 0.13 && (el_ecalIso-event_rho*0.13212 < 0.5*el_pt) && (el_hcalIso-event_rho*0.13052 < 0.3*el_pt) && el_dr03TkSumPt < 0.2*el_pt) )'
TopHNT = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_mHits==0 && el_hasMatchedConversion == 0 && '+HLTSafeEl+' && '+VetoGap
TopHNSST = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_mHits==0 && el_hasMatchedConversion == 0 && el_3charge && '+HLTSafeEl+' && '+VetoGap
TopHNSST_NMHit01 = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_mHits<2 && el_hasMatchedConversion == 0 && el_3charge && '+HLTSafeEl+' && '+VetoGap
TopHNSST_NoMHitCut = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_hasMatchedConversion == 0 && el_3charge && '+HLTSafeEl+' && '+VetoGap
TopHNT_NoHLT = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_mHits==0 && el_hasMatchedConversion == 0 && '+VetoGap
MediumID = 'passingCutBasedMedium94XV2 && '+VetoGap

#HLT to test
HLTEl23 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match && el_l1et > L1ThesholdHLTEle23Ele12CaloIdLTrackIdLIsoVL'
HLTEl12 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2'

## fits
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, 0, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, 0, 1],peakF[90.0])",
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.3,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant alphaP nP alphaF nF",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, 0, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, 0, 1],peakF[90.0])",
]

fit_altbkg = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]

fit_nominal_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_random,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, 0, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, 0, 1],peakF[90.0])",
]

fit_altsig_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass_random,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.3,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant alphaP nP alphaF nF",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, 0, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, 0, 1],peakF[90.0])",
]

fit_altbkg_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_random,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]



########### Configs ##############
Configs={}

#### 2016a
## ID
config=tnpConfig(
    data=samples['data2016a'],
    sim=samples['amc2016a'],
    sim_weight='totWeight',
    sim_maxweight=10000.,
    sim_genmatching=mcTrue,
    sim_genmass="mcMass",
    tree='tnpEleIDs/fitter_tree',
    mass="pair_mass",
    bins=bin_ID,
    expr='( '+TagCutBase27+' )',
    test='passingCutBasedMedium94XV2',
    hist_nbins=62,
    hist_range=(59,121),
    method="fit",
    fit_parameter=fit_nominal,
    fit_range=(60,120),
    systematic=[
#        [{'title':'altbkg','fit_parameter':fit_altbkg}],
#        [{'title':'altsig','fit_parameter':fit_altsig}],
#        [{'title':'alttag','expr.replace':('tag_Ele_pt>30','tag_Ele_pt>35')}],
#        [{'title':'altmc','sim.replace':('DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8')}],
    ],
    option="", #"fix_ptbelow20",
)
Configs['TopHNSST_2016a']=config.clone(test=TopHNSST, bins=bin_ID)
Configs['TopHNSST_NMHit01_2016a']=config.clone(test=TopHNSST_NMHit01, bins=bin_ID)
#Configs['TopHNSST_NoMHitCut_2016a']=config.clone(test=TopHNSST_NoMHitCut, bins=bin_ID)
Configs['MediumID_2016a']=config.clone(test=MediumID, bins=bin_ID)


### trigger ###
config=config.clone( tree='tnpEleTrig/fitter_tree' )
Configs['Ele23Leg1_TopHNSST_2016a']=config.clone(bins=bin_Ele23, test=HLTEl23, expr='( '+TagCutBase27+' && '+TopHNSST+' )')
Configs['Ele23Leg1_MediumID_2016a']=config.clone(bins=bin_Ele23, test=HLTEl23, expr='( '+TagCutBase27+' && '+MediumID+' )')
Configs['Ele12Leg2_TopHNSST_2016a']=config.clone(bins=bin_Ele12, test=HLTEl12, expr='( '+TagCutBase27+' && '+TopHNSST+' )')
Configs['Ele12Leg2_MediumID_2016a']=config.clone(bins=bin_Ele12, test=HLTEl12, expr='( '+TagCutBase27+' && '+MediumID+' )')


### 2016b, 2017, 2018 #################################################
Configs_2016b={}
Configs_2017 ={}
Configs_2018 ={}
for key in Configs:
  if not "_2016a" in key: continue

  Configs_2016b[key.replace("_2016a","_2016b")]=Configs[key].clone(data=samples["data2016b"],sim=samples["amc2016b"])
  if 'Ele23Leg1_' in key or 'Ele12Leg2_' in key:
    Configs_2017[key.replace("_2016a","_2017" )]=Configs[key].clone(
       data=samples["data2017"],
       sim=samples["amc2017"],
       expr='( '+TagCutBase32+' && '+globals()[key.replace('_2016a','').replace('Ele23Leg1_','').replace('Ele12Leg2_','')]+')',
    )
    Configs_2018[key.replace("_2016a","_2018" )]=Configs[key].clone(
       data=samples["data2018"],
       sim=samples["amc2018"],
       expr='( '+TagCutBase32+' && '+globals()[key.replace('_2016a','').replace('Ele23Leg1_','').replace('Ele12Leg2_','')]+')',
    )
  else:
    Configs_2017[key.replace("_2016a","_2017" )]=Configs[key].clone(data=samples["data2017"], sim=samples["amc2017"], expr='('+TagCutBase32+')')
    Configs_2018[key.replace("_2016a","_2018" )]=Configs[key].clone(data=samples["data2018"], sim=samples["amc2018"], expr='('+TagCutBase32+')')

Configs.update(Configs_2016b)
Configs.update(Configs_2017)
Configs.update(Configs_2018)
#######################################################################



if __name__=="__main__":
    for key in sorted(Configs.keys()):
        print key
