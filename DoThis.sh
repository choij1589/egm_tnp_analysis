#!/bin/bash

declare -a EraList=('2016a' '2016b' '2017' '2018')
#ID- 'POGCBM' 'TopHNSST' 'TopHNT' / HLT - 'Ele23Leg1_TopHNSST' 'Ele12Leg2_TopHNSST'
#declare -a MeasList=('TopHNT')
#declare -a MeasList=('Ele23Leg1_TopHNT', 'Ele12Leg2_TopHNT') 
declare -a MeasList=('Ele23Leg1_TopHNT')
MeasType="HLT" #'ID'/'HLT'
DoNominal="True"
DoSyst="True"
DoBinFix="False"
for Era in "${EraList[@]}"
do
  for Meas in "${MeasList[@]}"
  do
    sed -i "s:Era=Nom:Era='${Era}':g" etc/config/settings_UL_${MeasType}.py
    if [[ ${DoNominal} == "True" ]]; then
      python tnpEGM_fitter.py etc/config/settings_UL_${MeasType}.py --flag ${Meas}_${Era} --createBins
      python tnpEGM_fitter.py etc/config/settings_UL_${MeasType}.py --flag ${Meas}_${Era} --createHists -n 30
      python tnpEGM_fitter.py etc/config/settings_UL_${MeasType}.py --flag ${Meas}_${Era} --doFit -n 20
    fi
    if [[ ${DoSyst} == "True" ]]; then
      python tnpEGM_fitter.py etc/config/settings_UL_${MeasType}.py --flag ${Meas}_${Era} --doFit --mcSig --altSig -n 30
      python tnpEGM_fitter.py etc/config/settings_UL_${MeasType}.py --flag ${Meas}_${Era} --doFit --altSig -n 30
      python tnpEGM_fitter.py etc/config/settings_UL_${MeasType}.py --flag ${Meas}_${Era} --doFit --altBkg -n 30
    fi
    python tnpEGM_fitter.py etc/config/settings_UL_${MeasType}.py --flag ${Meas}_${Era} --sumUp
    sed -i "s:Era='${Era}':Era=Nom:g" etc/config/settings_UL_${MeasType}.py
  done
done
#--doPlot --iBin 18
