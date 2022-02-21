#hltGetConfiguration /online/collisions/2017/2e34/v2.0/HLT/V16 --full --offline --data --process MYHLT --globaltag 92X_dataRun2_HLT_v4  --no-output --max-events -1 --l1-emulator "uGT" > hlt_Phlegyas_online_v16_reEmul_uGT.py

#/users/kakwok/CSCCluster_12_3_X_signalsPath/V2

#hltGetConfiguration /users/kakwok/CSCCluster_12_3_X_signalsPath/V2\
#   --globaltag auto:run3_hlt \
#   --data \
#   --unprescale \
#   --eras Run2_2018 \
#   --output minimal \
#   --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input \
#   > hltData.py

hltGetConfiguration /users/kakwok/CSCCluster_12_3_X_signalsPath/V2\
 --mc --full --offline --unprescale --globaltag auto:phase1_2021_realistic\
 --setup /dev/CMSSW_12_3_0/HLT/V21\
 --process MYHLT --no-output \
 --l1Xml L1Menu_Collisions2022_v0_1_2.xml --l1-emulator FullMC\
 --input root://xrootd-cms.infn.it///store/mc/Run3Summer21DRPremix/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/e28c777d-10fd-4100-b230-c42b0160ad8a.root >& hlt.py


