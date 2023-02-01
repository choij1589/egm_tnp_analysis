from libPython.tnpClassUtils import tnpSample

SampleULv1 = {
    'data2016a': tnpSample('data2016a','/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016preVFP/data/SingleElectron', lumi=19.5),
    'mi2016a'  : tnpSample('mi2016a'  ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016preVFP/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos', isMC=True, mcTruth=True, weight='totWeight'),
    'amc2016a' : tnpSample('amc2016a' ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016preVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'mg2016a'  : tnpSample('mg2016a'  ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016preVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'data2016b': tnpSample('data2016b','/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016postVFP/data/SingleElectron', lumi=16.8),
    'mi2016b'  : tnpSample('mi2016b'  ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016postVFP/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos', isMC=True, mcTruth=True, weight='totWeight'),
    'amc2016b' : tnpSample('amc2016b' ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016postVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'mg2016b'  : tnpSample('mg2016b'  ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2016postVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'data2017' : tnpSample('data2017' ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2017/data/SingleElectron', lumi=41.5),
    'mi2017'   : tnpSample('mi2017'   ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2017/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos', isMC=True, mcTruth=True, weight='totWeight'),
    'amc2017'  : tnpSample('amc2017'  ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2017/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'mg2017'   : tnpSample('mg2017'   ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2017/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'data2018' : tnpSample('data2018' ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2018/data/EGamma', lumi=59.8),
    'mi2018'   : tnpSample('mi2018'   ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2018/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos', isMC=True, mcTruth=True, weight='totWeight'),
    'amc2018'  : tnpSample('amc2018'  ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'mg2018'   : tnpSample('mg2018'   ,'/gv0/Users/hsseo/EgammaTnP/2021-08-24/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
}

SampleULv2 = {
    'data2016a': tnpSample('data2016a','/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016preVFP/data/SingleElectron', lumi=19.5),
    'mi2016a'  : tnpSample('mi2016a'  ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016preVFP/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos', isMC=True, mcTruth=True, weight='totWeight'),
    'amc2016a' : tnpSample('amc2016a' ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016preVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'mg2016a'  : tnpSample('mg2016a'  ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016preVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'data2016b': tnpSample('data2016b','/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016postVFP/data/SingleElectron', lumi=16.8),
    'mi2016b'  : tnpSample('mi2016b'  ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016postVFP/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos', isMC=True, mcTruth=True, weight='totWeight'),
    'amc2016b' : tnpSample('amc2016b' ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016postVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'mg2016b'  : tnpSample('mg2016b'  ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016postVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'data2017' : tnpSample('data2017' ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2017/data/SingleElectron', lumi=41.5),
    'mi2017'   : tnpSample('mi2017'   ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2017/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos', isMC=True, mcTruth=True, weight='totWeight'),
    'amc2017'  : tnpSample('amc2017'  ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2017/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'mg2017'   : tnpSample('mg2017'   ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2017/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'data2018' : tnpSample('data2018' ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2018/data/EGamma', lumi=59.8),
    'mi2018'   : tnpSample('mi2018'   ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2018/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos', isMC=True, mcTruth=True, weight='totWeight'),
    'amc2018'  : tnpSample('amc2018'  ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
    'mg2018'   : tnpSample('mg2018'   ,'/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', isMC=True, mcTruth=True, weight='totWeight'),
}
