#############################################################
########## General settings
#############################################################
Era=Nom
Type='ID'

# Tag & General Cuts
VetoGap      = '(abs(el_sc_eta)<1.444 || abs(el_sc_eta)>1.566)'
VetoGapTag   = '(abs(tag_sc_eta)<1.444 || abs(tag_sc_eta)>1.566)'
MTCutTag     = 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
TagCutBase27 = 'tag_Ele_pt > 30 && el_q*tag_Ele_q<0 && '+VetoGapTag+' && '+VetoGap
TagCutBase32 = 'tag_Ele_pt > 35 && el_q*tag_Ele_q<0 && '+VetoGapTag+' && '+VetoGap
AltTagCut = ''
if '2016' in Era: AltTagCut = TagCutBase27+' && tag_Ele_pt > 35 && abs(tag_sc_eta)<2.1'
else            : AltTagCut = TagCutBase32+' && tag_Ele_pt > 40 && abs(tag_sc_eta)<2.1'

#ID to test
HLTSafeEl_NoEA = '( (abs(el_sc_eta) < 1.479 && el_5x5_sieie < 0.013 && abs(el_dEtaSeed) < 0.01 && abs(el_dPhiIn) < 0.07 && el_hoe < 0.13 && el_ecalIso < 0.5*el_pt && el_hcalIso < 0.3*el_pt && el_dr03TkSumPt < 0.2*el_pt) || (abs(el_sc_eta) > 1.479 && el_5x5_sieie < 0.035 && abs(el_dEtaSeed) < 0.015 && abs(el_dPhiIn) < 0.1 && el_hoe < 0.13 && el_ecalIso < 0.5*el_pt && el_hcalIso < 0.3*el_pt && el_dr03TkSumPt < 0.2*el_pt) )'
HLTSafeEl      = '( (abs(el_sc_eta) < 1.479 && el_5x5_sieie < 0.013 && abs(el_dEtaSeed) < 0.01 && abs(el_dPhiIn) < 0.07 && el_hoe < 0.13 && (el_ecalIso-event_rho*0.16544 < 0.5*el_pt) && (el_hcalIso-event_rho*0.05956 < 0.3*el_pt) && el_dr03TkSumPt < 0.2*el_pt) || (abs(el_sc_eta) > 1.479 && el_5x5_sieie < 0.035 && abs(el_dEtaSeed) < 0.015 && abs(el_dPhiIn) < 0.1 && el_hoe < 0.13 && (el_ecalIso-event_rho*0.13212 < 0.5*el_pt) && (el_hcalIso-event_rho*0.13052 < 0.3*el_pt) && el_dr03TkSumPt < 0.2*el_pt) )'
TopHNT   = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_mHits<2 && el_hasMatchedConversion == 0 && '+HLTSafeEl+' && '+VetoGap
TopHNSST = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_mHits<2 && el_hasMatchedConversion == 0 && el_3charge && '+HLTSafeEl+' && '+VetoGap
#TopHNSST_NoMHitCut = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_hasMatchedConversion == 0 && el_3charge && '+HLTSafeEl+' && '+VetoGap
#TopHNT_NoHLT = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_mHits==0 && el_hasMatchedConversion == 0 && '+VetoGap
POGCBM     = 'passingCutBasedMedium94XV2 && '+VetoGap
POGMVAni90 = 'passingMVA94Xwp90noisoV2 && '+VetoGap

#HLT to test
HLTEl23 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match && el_l1et > L1ThesholdHLTEle23Ele12CaloIdLTrackIdLIsoVL'
HLTEl23v2 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match'
HLTEl12 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2'

# flag to be Tested
flags = {
  'POGMVAni90_'+Era : POGMVAni90,
  'POGCBM_'+Era : POGCBM,
  'TopHNSST_'+Era : TopHNSST,
  'TopHNT_'+Era : TopHNT,
  'Ele23Leg1_TopHNSST_'+Era : HLTEl23,
  'Ele12Leg2_TopHNSST_'+Era : HLTEl12,
}

baseOutDir = 'results/'
if   Type=='ID'     : baseOutDir+='EleID/TopHNID/MiNNLO/Binv3/'
#if   Type=='ID'     : baseOutDir+='EleID/ULv2/Validation/MiNNLO/'
elif 'Trig' in Type : baseOutDir+='EleTrig/TopHNID/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'
if 'Trig' in Type : tnpTreeDir='tnpEleTrig'

weightName = 'totWeight'

samplesDef = {
  'data'   : tnpSamples.SampleULv2['data'+Era].clone(),
  'mcNom'  : tnpSamples.SampleULv2['mi'+Era].clone(),
  'mcAlt'  : tnpSamples.SampleULv2['amc'+Era].clone(),
  'tagSel' : tnpSamples.SampleULv2['mi'+Era].clone(),
  #'mcNom'  : tnpSamples.SampleULv2['amc'+Era].clone(),
  #'mcAlt'  : tnpSamples.SampleULv2['mg'+Era].clone(),
  #'tagSel' : tnpSamples.SampleULv2['amc'+Era].clone(),
}

for sample in samplesDef:
  if sample !='data' and not samplesDef[sample] is None:
    samplesDef[sample].set_mcTruth()
    samplesDef[sample].set_weight(weightName)
    #for miNNLO unphysical weights
    if sample != 'mcAlt' :
      samplesDef[sample].set_maxWeight(2E4)

if not samplesDef['tagSel'] is None:
  samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
  samplesDef['tagSel'].set_cut(AltTagCut)

bin_POGID = [
    #{ 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.566, -1.444, -0.8, 0., 0.8, 1.444, 1.566, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.479, -0.8, 0., 0.8, 1.479, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 20, 35, 50, 100, 200, 500], 'title':'p_{T} [GeV]' },
]
bin_ID = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.479, -0.8, 0.0, 0.8, 1.479, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 20, 35, 50, 100, 200, 500], 'title':'p_{T} [GeV]' },#v3
]
bin_Ele23 = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.479, -0.8, 0.0, 0.8, 1.479, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 19, 21, 23, 25, 30, 35, 50, 70, 100, 200], 'title':'p_{T} [GeV]' },
]
bin_Ele12 = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.479, -0.8, 0.0, 0.8, 1.479, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 12, 15, 20, 25, 30, 35, 50, 70, 100, 200], 'title':'p_{T} [GeV]' },
]

biningDef = []
if   Type=='ID'        : biningDef = bin_ID
elif Type=='TrigEle23' : biningDef = bin_Ele23
elif Type=='TrigEle12' : biningDef = bin_Ele12
else                   : biningDef = bin_POGID

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase = TagCutBase27 if '2016' in Era else TagCutBase32

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCutBase = {}
if 'Trig' in Type :
  additionalCutBase = {
    'Ele23Leg1_TopHNT_'+Era : TopHNT,
    'Ele23Leg1_TopHNSST_'+Era : TopHNSST,
    'Ele12Leg2_TopHNT_'+Era : TopHNT,
    'Ele12Leg2_TopHNSST_'+Era : TopHNSST,
  }
additionalCuts={}
#if Type=='ID':
#  for i in range(8):
#    additionalCuts[i]=MTCutTag

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
#nominal: Sig:Conv(MCtemplate(Reco), Gaussian(mean, sigma)) / Bkg: RooCMS: Erfc(beta(alpha-x))*exp(-gamma(x-peak))
#altSig:  Sig:Conv(M(ee(Z))template(GEN),CBExGauss(mean, sigma1, sigma2, alpha, n, sos))
#         CBExGauss: TailLeft: exp(nx) (x<|-alpha|), gaussian(mean, sigma2) ([|-alpha|,0]), gaussian(mean,sigma1) (x>0)
#         CBExGauss:!TailLeft: gaussian(mean, sigma2) (x<0), gaussian(mean,sigma1) ([0,|alpha|]), exp(-nx) (>|alpha|)
#altBkg: exp(alpha*x) 
tnpParNomFit = [
  ##default
  "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]","meanF[-0.0,-5.0,5.0]","sigmaF[2.,0.1,5.0]",
  "acmsP[60.,50.,80.]","betaP[0.05,0.0,0.08]","gammaP[0.1, 0, 1]","peakP[90.0]",
  "acmsF[60.,50.,80.]","betaF[0.05,0.0,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",

  #POGCBM-BinFix-amc
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.015,0.01,0.03]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]", #16a-bin2,32,42
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]","meanF[-0.,-5.,5.]","sigmaF[0.2,0.1,1.]", #16a-bin7
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.2,0.05,0.7]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]", #18-bin39,43
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.18,0.05,0.2]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]", #18-bin44,45

  #POGCBM-BinFix-mi
  #"acmsF[60.,50.,80.]","betaF[0.05,0.0,0.08]","gammaF[0.1,0.02,1]","peakF[90.0]", #16a-bin0,6, 16b-bin5,29, 17-bin2, 18-bin1
 
  #Main ID-Binv3
  #"acmsF[60.,50.,80.]","betaF[0.02,0.0,0.04]","gammaF[0.1, 0, 1]","peakF[90.0]",#16b-2,
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.2,0.01,0.5]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]", #16b-4
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.2,0.1,0.5]","meanF[-0.,-5.,5.]","sigmaF[0.2,0.1,0.5]", #16b-8

]

tnpParAltSigFit = [
  "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]",
  "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]",
  "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
  "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
  "sosP[1,0.05,5.0]",
  "sosF[1,0.05,5.0]",

  #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[-2,-5,5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]",#16a-24-31,33-34,43/#16b-16-17,23,27-31/#17-16-17,23/#18-16-18,21-23,25
  #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2,1.,5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]",#16b-18,22/#17-21-22
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.2,1.5]","alphaP[-2,-10,5]" ,'nP[3,-5,5]',"sigmaP_2[0.5,0.2,1.5]",#16b-24-26/#17-18,24-31/#18-24,26-31,43
  #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]",#18-43

  #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[7,5,10]',"sigmaF_2[2.0,0.5,6.0]",#16a-20,21
  #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[-2,-10,5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]",#16a-24-31,33-38,42-44/#16b-24-31/#17-24-31/#18-24-31
  #"meanF[-0.0,-5.0,5.0]","sigmaF[1,0.2,2.0]","alphaF[-2,-10,5]",'nF[3,-5,5]',"sigmaF_2[1.0,0.2,2.0]",##16b-27-30/#18-19,39
  #"meanF[-0.0,-5.0,5.0]","sigmaF[1,0.1,2.]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1,0.1,2.0]",#16a-45/16b-19-20,32-39,41-42,45/#17-19-20/#18-19-20,32-38,41-45

  #"acmsF[60.,50.,80.]","betaF[0.05,0.0,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",#17-24-25,30-31/#18-24-25,30-31

  #"sosP[0.1,0.05,0.5]",#16a-25,30/#16b-16-18,23/#17-16-17,19-21,23/#18-16,20-21,23
  #"sosF[0.1,0.05,0.5]",#16a-35/#17-16,19-20/#18-16,20
  #"sosP[0.1,0.05,0.8]",#18-22
  #"sosP[0.1,0.05,1.]", "sosF[0.1,0.05,0.7]",#16b-30
  #"sosP[0.1,0.05,1.]",#16b-30/#17-18
  #"sosF[0.6,0.05,1.]",#18-21,23
  #"sosP[0.5,0.2,0.8]", "sosF[0.6,0.05,0.8]",#18-17-19
]

tnpParAltSigFit_addGaus = [
  "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
  "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
  "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
  "acmsF[60.,50.,85.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
  "meanGF[40.0,10.0,60.0]","sigmaGF[15,5.0,125.0]",#16a,b-2-6/#17-0-6/#18-0-6
]
     
tnpParAltBkgFit = [
  "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]", "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,5.0]",
  "alphaP[0.,-5.,5.]", "alphaF[0.,-5.,5.]",

  #Main ID (binv3)
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.2,0.1,0.5]","meanF[-0.,-5.,5.]","sigmaF[0.2,0.1,0.6]", #16b-4
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.2,0.1,0.5]","meanF[-0.,-5.,5.]","sigmaF[0.2,0.1,0.5]", #16b-8
  #"alphaP[0.,-5.,5.]", "alphaF[-0.03,-0.035,-0.01]",#18-3
  #"meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]", "meanF[-0.0,-5.0,5.0]","sigmaF[0.3,0.1,0.3]",#18-4
  #"alphaP[0.,-5.,5.]", "alphaF[-0.03,-0.036,-0.01]",#18-4
]
