#./cmsCondorData.py run_steamflow_cfg.py /afs/cern.ch/user/k/kakwok/work/public/LLP/HLT/jobs/CMSSW_12_0_1/src/ /afs/cern.ch/user/k/kakwok/work/public/LLP/HLT/jobs/CMSSW_12_0_1/src/SteamRatesEdmWorkflow/Prod/tuples  -n 2 -q longlunch
#./cmsCondorData.py run_steamflow_cfg.py /afs/cern.ch/user/k/kakwok/work/public/LLP/HLT/jobs/CMSSW_12_0_1/src/ /afs/cern.ch/user/k/kakwok/work/public/LLP/HLT/jobs/CMSSW_12_0_1/src/SteamRatesEdmWorkflow/Prod/tuples  -n 2 -q longlunch -p /afs/cern.ch/user/k/kakwok/private/x509up_u41277

#cmssw="/afs/cern.ch/user/k/kakwok/work/public/LLP/HLT/L1emul/CMSSW_12_3_X_2022-02-07-1100/src/"
cmssw="/afs/cern.ch/user/k/kakwok/work/public/LLP/HLT/L1emul/CMSSW_12_3_5/src/"

#./cmsCondorData.py run_steamflow_cfg.py $cmssw /eos/cms/store/user/kakwok/HLT/signal_123X/signal_1  -n 10 -q longlunch -p /afs/cern.ch/user/k/kakwok/private/x509up_u41277 -i signal_1
#./cmsCondorData.py runCSCShowerAnalyzer_cfg.py $cmssw /eos/cms/store/user/kakwok/HLT/Commissioning2022/run353018_full  -n 5 -q workday -p /afs/cern.ch/user/k/kakwok/private/x509up_u41277 -i list_353018_zball
#./sub_total.jobb

#./cmsCondorData.py runCSCShowerAnalyzer_cfg.py $cmssw /eos/cms/store/user/kakwok/HLT/Commissioning2022/run355100  -n 5 -q workday -p /afs/cern.ch/user/k/kakwok/private/x509up_u41277 -i list_355100
#./sub_total.jobb

#./cmsCondorData.py runCSCShowerAnalyzer_cfg.py $cmssw /eos/cms/store/user/kakwok/HLT/Commissioning2022/run355135  -n 20 -q workday -p /afs/cern.ch/user/k/kakwok/private/x509up_u41277 -i list_355135
#./sub_total.jobb

./cmsCondorData.py runCSCShowerAnalyzer_cfg.py $cmssw /eos/cms/store/user/kakwok/HLT/Commissioning2022/run355404  -n 5 -q workday -p /afs/cern.ch/user/k/kakwok/private/x509up_u41277 -i list_355404
./sub_total.jobb
