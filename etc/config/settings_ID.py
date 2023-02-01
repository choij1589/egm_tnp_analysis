#############################################################
########## General settings
#############################################################
# Tag & General Cuts
VetoGap = '(abs(el_sc_eta)<1.444 || abs(el_sc_eta)>1.566)'
MTCutTag = 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
TagCutBase = 'tag_Ele_pt > 32 && abs(tag_Ele_eta)<2.1 && el_q*tag_Ele_q<0'+' && '+VetoGap

#ID to test
HLTSafeEl = '( (abs(el_sc_eta) < 1.479 && el_5x5_sieie < 0.012 && abs(el_dEtaSeed) < 0.01 && abs(el_dPhiIn) < 0.07 && el_hoe < 0.09 && el_ecalIso < 0.37*el_pt && el_hcalIso < 0.25*el_pt && el_dr03TkSumPt < 0.2*el_pt) || (abs(el_sc_eta) > 1.479 && el_5x5_sieie < 0.033 && abs(el_dEtaSeed) < 0.015 && abs(el_dPhiIn) < 0.1 && el_hoe < 0.09 && el_ecalIso < 0.45*el_pt && el_hcalIso < 0.28*el_pt && el_dr03TkSumPt < 0.2*el_pt) )'
TopHNID = 'passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip < 4 && abs(el_dz) < 0.1 && el_mHits < 2 && el_passConversionVeto == 1 '+' && '+HLTSafeEl+' && '+VetoGap 

#Ineff. & SF diff src study
CutMVA = 'passingMVA94Xwp90noisoV2 && '+VetoGap
CutMVA_Sieie = CutMVA+' && ( (abs(el_sc_eta) < 1.479 && el_5x5_sieie < 0.012) || (abs(el_sc_eta) > 1.479 && el_5x5_sieie < 0.033) )'
CutMVA_SieiedEta = CutMVA_Sieie+' && ( (abs(el_sc_eta) < 1.479 && abs(el_dEtaSeed) < 0.01) || (abs(el_sc_eta) > 1.479 && abs(el_dEtaSeed) < 0.015) )'
CutMVA_SieiedEtaPhi = CutMVA_SieiedEta+' && ( (abs(el_sc_eta) < 1.479 && abs(el_dPhiIn) < 0.07) || (abs(el_sc_eta) > 1.479 && abs(el_dPhiIn) < 0.1) )'
CutMVA_SieiedEtaPhiHoE = CutMVA_SieiedEtaPhi+' && ( (abs(el_sc_eta) < 1.479 && el_hoe < 0.09) || (abs(el_sc_eta) > 1.479 && el_hoe < 0.09) )'
CutMVAHLT = CutMVA+' && '+HLTSafeEl
CutMVAHLTConv = CutMVAHLT+' && el_passConversionVeto == 1'
CutMVAHLTConvmHit = CutMVAHLTConv+' && el_mHits < 2'
CutMVAHLTConvmHitDZ = CutMVAHLTConvmHit+' && abs(el_dz) < 0.1'
CutMVAHLTConvmHitDZSIP = CutMVAHLTConvmHitDZ+' && el_sip<4'
CutMVAHLTConvmHitDZSIPmIso = CutMVAHLTConvmHitDZSIP+' && el_miniIsoAll_fall17 < 0.1*el_pt'

CutMVAIP_NoDZ = CutMVA+' && el_sip<4'
CutMVAIP = CutMVA+' && el_sip<4 && abs(el_dz)<0.1'
CutMVAHLTConv = CutMVAHLT+' && el_mHits < 2 && el_passConversionVeto == 1'
CutMVAHLTConvIP = CutMVAHLTConv+' && el_sip < 4 && abs(el_dz) < 0.1'


# flag to be Tested
flags = {
    'passingMedium' : '(passingMedium == 1)',
    'passingTopHNID' : TopHNID,
    #Ineff. & SF diff. src. study
    'passingMVA' : CutMVA,
    'passingMVA_Sieie' : CutMVA_Sieie,
    'passingMVA_SieiedEta' : CutMVA_SieiedEta, #negligible effect for both eff & SF
    'passingMVA_SieiedEtaPhi' : CutMVA_SieiedEtaPhi,
    'passingMVA_SieiedEtaPhiHoE' : CutMVA_SieiedEtaPhiHoE,
    'passingMVAHLT' : CutMVAHLT,
    'passingMVAHLTConv' : CutMVAHLTConv, #ConVeto negligible impact on eff,SF
    'passingMVAHLTConvmHit' : CutMVAHLTConvmHit, #mHit negligible impact on eff,SF
    'passingMVAHLTConvmHitDZ' : CutMVAHLTConvmHitDZ, #DZ negligible impact on eff,SF (~1%)
    'passingMVAHLTConvmHitDZSIP' : CutMVAHLTConvmHitDZSIP, #SIP impact: ~-5% on eff. / +5% on SF.
    'passingMVAHLTConvmHitDZSIPmIso' : CutMVAHLTConvmHitDZSIPmIso, #mIso impact negligible on eff, SF
    'passingMVAIP_NoDZ' : CutMVAIP_NoDZ, #SIP cut has large impact ~10% on endcap eff., but largely correlated with HLT cut. After HLT cut, eff loss is 1-5%
    }
baseOutDir = 'results/EleID/TopHNID/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
#tnpTreeDir = 'GsfElectronToEleID'
tnpTreeDir = 'tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.Sample2017['data2017'].clone(),
    'mcNom'  : tnpSamples.Sample2017['amc2017'].clone(),
    'mcAlt'  : tnpSamples.Sample2017['mg2017'].clone(),
    'tagSel' : tnpSamples.Sample2017['amc2017'].clone(),
}
## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.ICHEP2016['data_2016_runC_ele'] )
#samplesDef['data'].add_sample( tnpSamples.ICHEP2016['data_2016_runD_ele'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
    samplesDef['tagSel'].set_cut(TagCutBase+' && tag_Ele_pt>35 && tag_Ele_noIsoMVA94XV2>0.9')

## set MC weight, simple way (use tree weight) 
weightName = 'totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.5, -0.8, 0.0, 0.8, 1.5, 2.0, 2.5] },
   { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 20, 35, 50, 100, 200, 500] },
]
#   { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase = TagCutBase

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCutBase = None
additionalCuts={}
for i in range(8):
    additionalCuts[i]=MTCutTag
#additionalCuts = None

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

    #Main ID
    #"acmsF[60.,50.,80.]","betaF[0.05,-0.08,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",#bin0,1,2,5,7
    #"acmsF[60.,0.,180.]","betaF[0.05,-0.1,0.1]","gammaF[0.1,0,1]","peakF[90.0]",#bin4
    #"acmsF[60.,50.,80.]","betaF[0.05,-0.1,0.1]","gammaF[0.1, 0, 1]","peakF[90.0]",#bin6
    #"acmsP[60.,50.,80.]","betaP[0.05,-0.5,0.5]","gammaP[0.1, 0, 1]","peakP[90.0]","acmsF[60.,50.,90.]","betaF[0.05,-0.5,0.5]","gammaF[0.1, 0, 1]","peakF[90.0]",#bin31
    #"meanP[0.,-5.,5.]","sigmaP[0.8,0.7,0.9]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]","acmsF[60.,50.,90.]","betaF[0.05,-0.5,0.5]","gammaF[0.1, 0, 1]","peakF[90.0]",#bin34
    #"meanP[0.,-5.,5.]","sigmaP[0.5,0.4,0.6]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]",#bin35,44
    #"meanP[0.,-5.,5.]","sigmaP[0.6,0.4,0.7]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]",#bin36
    #"meanP[0.,-5.,5.]","sigmaP[0.8,0.7,0.9]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]",#bin37,43
    #"meanP[0.,-5.,5.]","sigmaP[0.5,0.4,1.]","meanF[-0.,-5.,5.]","sigmaF[2.,0.1,5.]",#bin42,45


    #MVAHLT
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1.,0.1,5.0]","meanF[-0.0,-5.0,5.0]","sigmaF[2.,0.1,5.0]",#bin9

    #MVAHLTConv/MVAHLTConvmHit/
    #"acmsF[60.,50.,80.]","betaF[0.05,-0.08,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",#bin2

    #MVASieie(dEta)(dPhi)
    #"acmsF[60.,50.,90.]","betaF[0.05,-0.08,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",#bin3,4,5
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1.0,0.5,5.0]","meanF[-0.0,-5.0,5.0]","sigmaF[2.,0.1,5.0]",#bin24

    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
