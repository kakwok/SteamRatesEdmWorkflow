# hltGetConfiguration /users/kakwok/CSCCluster_12_3_X_signalsPath/V2 --mc --full --offline --unprescale --globaltag auto:phase1_2021_realistic --setup /dev/CMSSW_12_3_0/HLT/V21 --process MYHLT --no-output --l1Xml L1Menu_Collisions2022_v0_1_2.xml --l1-emulator FullMC --input root://xrootd-cms.infn.it///store/mc/Run3Summer21DRPremix/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/e28c777d-10fd-4100-b230-c42b0160ad8a.root

# /users/kakwok/CSCCluster_12_3_X_signalsPath/V2 (CMSSW_12_3_0_pre3)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "MYHLT" )
process.load("setup_dev_CMSSW_12_3_0_HLT_V21_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/kakwok/CSCCluster_12_3_X_signalsPath/V2')
)

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    verbose = cms.untracked.bool( False ),
    toGet = cms.VPSet( 
    )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltPSetMap = cms.EDProducer( "ParameterSetBlobProducer" )
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    FedIds = cms.vint32( 1404 ),
    Setup = cms.string( "stage2::GTSetup" ),
    FWId = cms.uint32( 0 ),
    DmxFWId = cms.uint32( 0 ),
    FWOverride = cms.bool( False ),
    TMTCheck = cms.bool( True ),
    CTP7 = cms.untracked.bool( False ),
    MTF7 = cms.untracked.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    debug = cms.untracked.bool( False ),
    MinFeds = cms.uint32( 0 )
)
process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    MuonShowerInputTag = cms.InputTag( "" ),
    EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    AlgoBlkInputTag = cms.InputTag( "hltGtStage2Digis" ),
    GetPrescaleColumnFromData = cms.bool( False ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    RequireMenuToMatchAlgoBlkInput = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    useMuonShowers = cms.bool( False ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    L1DataBxInEvent = cms.int32( 5 ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    BstLengthBytes = cms.int32( -1 ),
    PrescaleSet = cms.uint32( 1 ),
    Verbosity = cms.untracked.int32( 0 ),
    PrintL1Menu = cms.untracked.bool( False ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineMetaDataDigis = cms.EDProducer( "OnlineMetaDataRawToDigi",
    onlineMetaDataInputLabel = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    changeToCMSCoordinates = cms.bool( False ),
    maxZ = cms.double( 40.0 ),
    setSigmaZ = cms.double( 0.0 ),
    beamMode = cms.untracked.uint32( 11 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    maxRadius = cms.double( 2.0 ),
    useTransientRecord = cms.bool( False )
)
process.hltL1sMuShowerOneNominal = cms.EDFilter( "HLTL1TSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_MuShower_OneNominal OR L1_MuShower_OneTight" ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' )
)
process.hltPreCscClusterLoose = cms.EDFilter( "HLTPrescaler",
    offset = cms.uint32( 0 ),
    L1GtReadoutRecordTag = cms.InputTag( "L1_MuShower_OneNominal OR L1_MuShower_OneTight" )
)
process.hltMuonDTDigis = cms.EDProducer( "DTuROSRawToDigi",
    inputLabel = cms.InputTag( "rawDataCollector" ),
    debug = cms.untracked.bool( False )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    recAlgoConfig = cms.PSet( 
      maxTime = cms.double( 420.0 ),
      debug = cms.untracked.bool( False ),
      stepTwoFromDigi = cms.bool( False ),
      tTrigModeConfig = cms.PSet( 
        debug = cms.untracked.bool( False ),
        tofCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        wirePropCorrType = cms.int32( 0 ),
        doTOFCorrection = cms.bool( True ),
        vPropWire = cms.double( 24.4 ),
        doT0Correction = cms.bool( True ),
        doWirePropCorrection = cms.bool( True ),
        t0Label = cms.string( "" )
      ),
      useUncertDB = cms.bool( True ),
      doVdriftCorr = cms.bool( True ),
      minTime = cms.double( -3.0 ),
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      readLegacyTTrigDB = cms.bool( True ),
      readLegacyVDriftDB = cms.bool( True )
    ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
    debug = cms.untracked.bool( False ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    Reco4DAlgoConfig = cms.PSet( 
      Reco2DAlgoConfig = cms.PSet( 
        AlphaMaxPhi = cms.double( 1.0 ),
        debug = cms.untracked.bool( False ),
        segmCleanerMode = cms.int32( 2 ),
        AlphaMaxTheta = cms.double( 0.9 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        recAlgoConfig = cms.PSet( 
          maxTime = cms.double( 420.0 ),
          debug = cms.untracked.bool( False ),
          stepTwoFromDigi = cms.bool( False ),
          tTrigModeConfig = cms.PSet( 
            debug = cms.untracked.bool( False ),
            tofCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            wirePropCorrType = cms.int32( 0 ),
            doTOFCorrection = cms.bool( True ),
            vPropWire = cms.double( 24.4 ),
            doT0Correction = cms.bool( True ),
            doWirePropCorrection = cms.bool( True ),
            t0Label = cms.string( "" )
          ),
          useUncertDB = cms.bool( True ),
          doVdriftCorr = cms.bool( True ),
          minTime = cms.double( -3.0 ),
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          readLegacyTTrigDB = cms.bool( True ),
          readLegacyVDriftDB = cms.bool( True )
        ),
        MaxAllowedHits = cms.uint32( 50 ),
        nUnSharedHitsMin = cms.int32( 2 ),
        nSharedHitsMax = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      debug = cms.untracked.bool( False ),
      segmCleanerMode = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      recAlgoConfig = cms.PSet( 
        maxTime = cms.double( 420.0 ),
        debug = cms.untracked.bool( False ),
        stepTwoFromDigi = cms.bool( False ),
        tTrigModeConfig = cms.PSet( 
          debug = cms.untracked.bool( False ),
          tofCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          wirePropCorrType = cms.int32( 0 ),
          doTOFCorrection = cms.bool( True ),
          vPropWire = cms.double( 24.4 ),
          doT0Correction = cms.bool( True ),
          doWirePropCorrection = cms.bool( True ),
          t0Label = cms.string( "" )
        ),
        useUncertDB = cms.bool( True ),
        doVdriftCorr = cms.bool( True ),
        minTime = cms.double( -3.0 ),
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        readLegacyTTrigDB = cms.bool( True ),
        readLegacyVDriftDB = cms.bool( True )
      ),
      nUnSharedHitsMin = cms.int32( 2 ),
      nSharedHitsMax = cms.int32( 2 ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    ),
    debug = cms.untracked.bool( False ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    InputObjects = cms.InputTag( "rawDataCollector" ),
    UseExaminer = cms.bool( True ),
    ExaminerMask = cms.uint32( 535558134 ),
    UseSelectiveUnpacking = cms.bool( True ),
    ErrorMask = cms.uint32( 0 ),
    UnpackStatusDigis = cms.bool( False ),
    UseFormatStatus = cms.bool( True ),
    useRPCs = cms.bool( False ),
    useGEMs = cms.bool( False ),
    useCSCShowers = cms.bool( False ),
    Debug = cms.untracked.bool( False ),
    PrintEventNumber = cms.untracked.bool( False ),
    runDQM = cms.untracked.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    VisualFEDShort = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    SuppressZeroLCT = cms.untracked.bool( True ),
    DisableMappingCheck = cms.untracked.bool( False ),
    B904Setup = cms.untracked.bool( False )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    CSCStripPeakThreshold = cms.double( 10.0 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    UseAverageTime = cms.bool( False ),
    UseParabolaFit = cms.bool( False ),
    UseFivePoleFit = cms.bool( True ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseStaticPedestals = cms.bool( False ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    readBadChannels = cms.bool( False ),
    readBadChambers = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCUseGasGainCorrections = cms.bool( False ),
    CSCDebug = cms.untracked.bool( False ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 ),
    CSCUseReducedWireTimeWindow = cms.bool( False ),
    CSCWireTimeWindowLow = cms.int32( 0 ),
    CSCWireTimeWindowHigh = cms.int32( 15 )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_type = cms.int32( 1 ),
    algo_psets = cms.VPSet( 
      cms.PSet(  parameters_per_chamber_type = cms.vint32( 1, 2, 3, 4, 5, 6, 5, 6, 5, 6 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  wideSeg = cms.double( 3.0 ),
            chi2Norm_2D_ = cms.double( 35.0 ),
            dRIntMax = cms.double( 2.0 ),
            doCollisions = cms.bool( True ),
            dPhiMax = cms.double( 0.006 ),
            dRMax = cms.double( 1.5 ),
            dPhiIntMax = cms.double( 0.005 ),
            minLayersApart = cms.int32( 1 ),
            chi2Max = cms.double( 100.0 ),
            chi2_str = cms.double( 50.0 ),
            enlarge = cms.bool( False )
          ),
          cms.PSet(  wideSeg = cms.double( 3.0 ),
            chi2Norm_2D_ = cms.double( 35.0 ),
            dRIntMax = cms.double( 2.0 ),
            doCollisions = cms.bool( True ),
            dPhiMax = cms.double( 0.005 ),
            dRMax = cms.double( 1.5 ),
            dPhiIntMax = cms.double( 0.004 ),
            minLayersApart = cms.int32( 1 ),
            chi2Max = cms.double( 100.0 ),
            chi2_str = cms.double( 50.0 ),
            enlarge = cms.bool( False )
          ),
          cms.PSet(  wideSeg = cms.double( 3.0 ),
            chi2Norm_2D_ = cms.double( 35.0 ),
            dRIntMax = cms.double( 2.0 ),
            doCollisions = cms.bool( True ),
            dPhiMax = cms.double( 0.004 ),
            dRMax = cms.double( 1.5 ),
            dPhiIntMax = cms.double( 0.003 ),
            minLayersApart = cms.int32( 1 ),
            chi2Max = cms.double( 100.0 ),
            chi2_str = cms.double( 50.0 ),
            enlarge = cms.bool( False )
          ),
          cms.PSet(  wideSeg = cms.double( 3.0 ),
            chi2Norm_2D_ = cms.double( 20.0 ),
            dRIntMax = cms.double( 2.0 ),
            doCollisions = cms.bool( True ),
            dPhiMax = cms.double( 0.003 ),
            dRMax = cms.double( 1.5 ),
            dPhiIntMax = cms.double( 0.002 ),
            minLayersApart = cms.int32( 1 ),
            chi2Max = cms.double( 60.0 ),
            chi2_str = cms.double( 30.0 ),
            enlarge = cms.bool( False )
          ),
          cms.PSet(  wideSeg = cms.double( 3.0 ),
            chi2Norm_2D_ = cms.double( 60.0 ),
            dRIntMax = cms.double( 2.0 ),
            doCollisions = cms.bool( True ),
            dPhiMax = cms.double( 0.007 ),
            dRMax = cms.double( 1.5 ),
            dPhiIntMax = cms.double( 0.005 ),
            minLayersApart = cms.int32( 1 ),
            chi2Max = cms.double( 180.0 ),
            chi2_str = cms.double( 80.0 ),
            enlarge = cms.bool( False )
          ),
          cms.PSet(  wideSeg = cms.double( 3.0 ),
            chi2Norm_2D_ = cms.double( 35.0 ),
            dRIntMax = cms.double( 2.0 ),
            doCollisions = cms.bool( True ),
            dPhiMax = cms.double( 0.006 ),
            dRMax = cms.double( 1.5 ),
            dPhiIntMax = cms.double( 0.004 ),
            minLayersApart = cms.int32( 1 ),
            chi2Max = cms.double( 100.0 ),
            chi2_str = cms.double( 50.0 ),
            enlarge = cms.bool( False )
          )
        ),
        algo_name = cms.string( "CSCSegAlgoRU" ),
        chamber_types = cms.vstring( 'ME1/a',
          'ME1/b',
          'ME1/2',
          'ME1/3',
          'ME2/1',
          'ME2/2',
          'ME3/1',
          'ME3/2',
          'ME4/1',
          'ME4/2' )
      )
    )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskSource = cms.string( "File" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    deadSource = cms.string( "File" ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" )
)
process.hltMuonGEMDigis = cms.EDProducer( "GEMRawToDigiModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    useDBEMap = cms.bool( False ),
    keepDAQStatus = cms.bool( False ),
    readMultiBX = cms.bool( False ),
    fedIdStart = cms.uint32( 1467 ),
    fedIdEnd = cms.uint32( 1478 )
)
process.hltGemRecHits = cms.EDProducer( "GEMRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    recAlgo = cms.string( "GEMRecHitStandardAlgo" ),
    gemDigiLabel = cms.InputTag( "hltMuonGEMDigis" ),
    applyMasking = cms.bool( False )
)
process.hltGemSegments = cms.EDProducer( "GEMSegmentProducer",
    gemRecHitLabel = cms.InputTag( "hltGemRecHits" ),
    ge0_name = cms.string( "GE0SegAlgoRU" ),
    algo_name = cms.string( "GEMSegmentAlgorithm" ),
    ge0_pset = cms.PSet( 
      maxChi2GoodSeg = cms.double( 50.0 ),
      maxChi2Prune = cms.double( 50.0 ),
      maxNumberOfHitsPerLayer = cms.uint32( 100 ),
      maxETASeeds = cms.double( 0.1 ),
      maxPhiAdditional = cms.double( 0.001096605744 ),
      minNumberOfHits = cms.uint32( 4 ),
      doCollisions = cms.bool( True ),
      maxPhiSeeds = cms.double( 0.001096605744 ),
      requireCentralBX = cms.bool( True ),
      maxChi2Additional = cms.double( 100.0 ),
      allowWideSegments = cms.bool( True ),
      maxNumberOfHits = cms.uint32( 300 ),
      maxTOFDiff = cms.double( 25.0 )
    ),
    algo_pset = cms.PSet( 
      dYclusBoxMax = cms.double( 5.0 ),
      dXclusBoxMax = cms.double( 1.0 ),
      maxRecHitsInCluster = cms.int32( 4 ),
      preClustering = cms.bool( True ),
      preClusteringUseChaining = cms.bool( True ),
      dEtaChainBoxMax = cms.double( 0.05 ),
      clusterOnlySameBXRecHits = cms.bool( True ),
      minHitsPerSegment = cms.uint32( 2 ),
      dPhiChainBoxMax = cms.double( 0.02 )
    )
)
process.hltCSCrechitClusters = cms.EDProducer( "CSCrechitClusterProducer",
    nRechitMin = cms.int32( 50 ),
    rParam = cms.double( 0.4 ),
    nStationThres = cms.int32( 10 ),
    recHitLabel = cms.InputTag( "hltCsc2DRecHits" )
)
process.hltCscClusterLoose = cms.EDFilter( "HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag( "hltCSCrechitClusters" ),
    MinN = cms.int32( 1 ),
    MinSize = cms.int32( -1 ),
    MinSizeMinusMB1 = cms.int32( -1 ),
    MinSizeRegionCutEtas = cms.vdouble( -1.0, -1.0, 1.9, 1.9 ),
    MaxSizeRegionCutEtas = cms.vdouble( 1.9, 1.9, -1.0, -1.0 ),
    MinSizeRegionCutNstations = cms.vint32( -1, 1, -1, 1 ),
    MaxSizeRegionCutNstations = cms.vint32( 1, -1, 1, -1 ),
    MinSizeRegionCutClusterSize = cms.vint32( 200, 100, 500, 500 ),
    Max_nMB1 = cms.int32( -1 ),
    Max_nMB2 = cms.int32( -1 ),
    Max_nME11 = cms.int32( -1 ),
    Max_nME12 = cms.int32( -1 ),
    Max_nME41 = cms.int32( -1 ),
    Max_nME42 = cms.int32( -1 ),
    MinNstation = cms.int32( 0 ),
    MinAvgStation = cms.double( 0.0 ),
    MinTime = cms.double( -999.0 ),
    MaxTime = cms.double( 999.0 ),
    MinEta = cms.double( -1.0 ),
    MaxEta = cms.double( -1.0 ),
    MaxTimeSpread = cms.double( -1.0 )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltPreCscClusterMedium = cms.EDFilter( "HLTPrescaler",
    offset = cms.uint32( 0 ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltCscClusterMedium = cms.EDFilter( "HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag( "hltCSCrechitClusters" ),
    MinN = cms.int32( 1 ),
    MinSize = cms.int32( -1 ),
    MinSizeMinusMB1 = cms.int32( -1 ),
    MinSizeRegionCutEtas = cms.vdouble( -1.0, -1.0, 1.9, 1.9 ),
    MaxSizeRegionCutEtas = cms.vdouble( 1.9, 1.9, -1.0, -1.0 ),
    MinSizeRegionCutNstations = cms.vint32( -1, 1, -1, 1 ),
    MaxSizeRegionCutNstations = cms.vint32( 1, -1, 1, -1 ),
    MinSizeRegionCutClusterSize = cms.vint32( 300, 100, 800, 500 ),
    Max_nMB1 = cms.int32( -1 ),
    Max_nMB2 = cms.int32( -1 ),
    Max_nME11 = cms.int32( -1 ),
    Max_nME12 = cms.int32( -1 ),
    Max_nME41 = cms.int32( -1 ),
    Max_nME42 = cms.int32( -1 ),
    MinNstation = cms.int32( 0 ),
    MinAvgStation = cms.double( 0.0 ),
    MinTime = cms.double( -999.0 ),
    MaxTime = cms.double( 999.0 ),
    MinEta = cms.double( -1.0 ),
    MaxEta = cms.double( -1.0 ),
    MaxTimeSpread = cms.double( -1.0 )
)
process.hltPreCscClusterTight = cms.EDFilter( "HLTPrescaler",
    offset = cms.uint32( 0 ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltCscClusterTight = cms.EDFilter( "HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag( "hltCSCrechitClusters" ),
    MinN = cms.int32( 1 ),
    MinSize = cms.int32( -1 ),
    MinSizeMinusMB1 = cms.int32( -1 ),
    MinSizeRegionCutEtas = cms.vdouble( -1.0, -1.0, 1.9, 1.9 ),
    MaxSizeRegionCutEtas = cms.vdouble( 1.9, 1.9, -1.0, -1.0 ),
    MinSizeRegionCutNstations = cms.vint32( -1, 1, -1, 1 ),
    MaxSizeRegionCutNstations = cms.vint32( 1, -1, 1, -1 ),
    MinSizeRegionCutClusterSize = cms.vint32( 500, 100, 800, 500 ),
    Max_nMB1 = cms.int32( -1 ),
    Max_nMB2 = cms.int32( -1 ),
    Max_nME11 = cms.int32( -1 ),
    Max_nME12 = cms.int32( -1 ),
    Max_nME41 = cms.int32( -1 ),
    Max_nME42 = cms.int32( -1 ),
    MinNstation = cms.int32( 0 ),
    MinAvgStation = cms.double( 0.0 ),
    MinTime = cms.double( -999.0 ),
    MaxTime = cms.double( 999.0 ),
    MinEta = cms.double( -1.0 ),
    MaxEta = cms.double( -1.0 ),
    MaxTimeSpread = cms.double( -1.0 )
)
process.hltPreL1CSCShowerDTCluster50 = cms.EDFilter( "HLTPrescaler",
    offset = cms.uint32( 0 ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltDTrechitClusters = cms.EDProducer( "DTrechitClusterProducer",
    nRechitMin = cms.int32( 50 ),
    rParam = cms.double( 0.4 ),
    nStationThres = cms.int32( 10 ),
    recHitLabel = cms.InputTag( "hltDt1DRecHits" )
)
process.hltDTCluster50NoMB1 = cms.EDFilter( "HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag( "hltDTrechitClusters" ),
    MinN = cms.int32( 1 ),
    MinSize = cms.int32( 50 ),
    MinSizeMinusMB1 = cms.int32( -1 ),
    MinSizeRegionCutEtas = cms.vdouble( -1.0, -1.0, 1.9, 1.9 ),
    MaxSizeRegionCutEtas = cms.vdouble( 1.9, 1.9, -1.0, -1.0 ),
    MinSizeRegionCutNstations = cms.vint32( -1, 1, -1, 1 ),
    MaxSizeRegionCutNstations = cms.vint32( 1, -1, 1, -1 ),
    MinSizeRegionCutClusterSize = cms.vint32( -1, -1, -1, -1 ),
    Max_nMB1 = cms.int32( 0 ),
    Max_nMB2 = cms.int32( -1 ),
    Max_nME11 = cms.int32( -1 ),
    Max_nME12 = cms.int32( -1 ),
    Max_nME41 = cms.int32( -1 ),
    Max_nME42 = cms.int32( -1 ),
    MinNstation = cms.int32( 0 ),
    MinAvgStation = cms.double( 0.0 ),
    MinTime = cms.double( -999.0 ),
    MaxTime = cms.double( 999.0 ),
    MinEta = cms.double( -1.0 ),
    MaxEta = cms.double( -1.0 ),
    MaxTimeSpread = cms.double( -1.0 )
)
process.hltPreL1CSCShowerDTCluster75 = cms.EDFilter( "HLTPrescaler",
    offset = cms.uint32( 0 ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltDTCluster75NoMB1 = cms.EDFilter( "HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag( "hltDTrechitClusters" ),
    MinN = cms.int32( 1 ),
    MinSize = cms.int32( 75 ),
    MinSizeMinusMB1 = cms.int32( -1 ),
    MinSizeRegionCutEtas = cms.vdouble( -1.0, -1.0, 1.9, 1.9 ),
    MaxSizeRegionCutEtas = cms.vdouble( 1.9, 1.9, -1.0, -1.0 ),
    MinSizeRegionCutNstations = cms.vint32( -1, 1, -1, 1 ),
    MaxSizeRegionCutNstations = cms.vint32( 1, -1, 1, -1 ),
    MinSizeRegionCutClusterSize = cms.vint32( -1, -1, -1, -1 ),
    Max_nMB1 = cms.int32( 0 ),
    Max_nMB2 = cms.int32( -1 ),
    Max_nME11 = cms.int32( -1 ),
    Max_nME12 = cms.int32( -1 ),
    Max_nME41 = cms.int32( -1 ),
    Max_nME42 = cms.int32( -1 ),
    MinNstation = cms.int32( 0 ),
    MinAvgStation = cms.double( 0.0 ),
    MinTime = cms.double( -999.0 ),
    MaxTime = cms.double( 999.0 ),
    MinEta = cms.double( -1.0 ),
    MaxEta = cms.double( -1.0 ),
    MaxTimeSpread = cms.double( -1.0 )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    throw = cms.bool( False ),
    processName = cms.string( "@" ),
    moduleLabelPatternsToMatch = cms.vstring( 'hlt*' ),
    moduleLabelPatternsToSkip = cms.vstring(  )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtStage2Digis + process.hltGtStage2ObjectMap )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineMetaDataDigis + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTMuonLocalRecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits + process.hltMuonGEMDigis + process.hltGemRecHits + process.hltGemSegments )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltPSetMap + process.hltBoolFalse )
process.HLT_CscCluster_Loose_v0 = cms.Path( process.HLTBeginSequence + process.hltL1sMuShowerOneNominal + process.hltPreCscClusterLoose + process.HLTMuonLocalRecoSequence + process.hltCSCrechitClusters + process.hltCscClusterLoose + process.HLTEndSequence )
process.HLT_CscCluster_Medium_v0 = cms.Path( process.HLTBeginSequence + process.hltL1sMuShowerOneNominal + process.hltPreCscClusterMedium + process.HLTMuonLocalRecoSequence + process.hltCSCrechitClusters + process.hltCscClusterMedium + process.HLTEndSequence )
process.HLT_CscCluster_Tight_v0 = cms.Path( process.HLTBeginSequence + process.hltL1sMuShowerOneNominal + process.hltPreCscClusterTight + process.HLTMuonLocalRecoSequence + process.hltCSCrechitClusters + process.hltCscClusterTight + process.HLTEndSequence )
process.HLT_L1CSCShower_DTCluster50_v0 = cms.Path( process.HLTBeginSequence + process.hltL1sMuShowerOneNominal + process.hltPreL1CSCShowerDTCluster50 + process.HLTMuonLocalRecoSequence + process.hltDTrechitClusters + process.hltDTCluster50NoMB1 + process.HLTEndSequence )
process.HLT_L1CSCShower_DTCluster75_v0 = cms.Path( process.HLTBeginSequence + process.hltL1sMuShowerOneNominal + process.hltPreL1CSCShowerDTCluster75 + process.HLTMuonLocalRecoSequence + process.hltDTrechitClusters + process.hltDTCluster75NoMB1 + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtStage2Digis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )


process.schedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_CscCluster_Loose_v0, process.HLT_CscCluster_Medium_v0, process.HLT_CscCluster_Tight_v0, process.HLT_L1CSCShower_DTCluster50_v0, process.HLT_L1CSCShower_DTCluster75_v0, process.HLTriggerFinalPath, ))


# source module (EDM inputs)
process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        'root://xrootd-cms.infn.it///store/mc/Run3Summer21DRPremix/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/e28c777d-10fd-4100-b230-c42b0160ad8a.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# override the GlobalTag's L1T menu from an Xml file
from HLTrigger.Configuration.CustomConfigs import L1XML
process = L1XML(process,"L1Menu_Collisions2022_v0_1_2.xml")

# run the Full L1T emulator, then repack the data into a new RAW collection, to be used by the HLT
from HLTrigger.Configuration.CustomConfigs import L1REPACK
process = L1REPACK(process,"FullMC")

# avoid PrescaleService error due to missing HLT paths
if 'PrescaleService' in process.__dict__:
    for pset in reversed(process.PrescaleService.prescaleTable):
        if not hasattr(process,pset.pathName.value()):
            process.PrescaleService.prescaleTable.remove(pset)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

# enable TrigReport, TimeReport and MultiThreading
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    numberOfThreads = cms.untracked.uint32( 4 ),
    numberOfStreams = cms.untracked.uint32( 0 ),
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'auto:phase1_2021_realistic')

# show summaries from trigger analysers used at HLT
if 'MessageLogger' in process.__dict__:
    process.MessageLogger.TriggerSummaryProducerAOD = cms.untracked.PSet()
    process.MessageLogger.L1GtTrigReport = cms.untracked.PSet()
    process.MessageLogger.L1TGlobalSummary = cms.untracked.PSet()
    process.MessageLogger.HLTrigReport = cms.untracked.PSet()
    process.MessageLogger.FastReport = cms.untracked.PSet()
    process.MessageLogger.ThroughputService = cms.untracked.PSet()

# load the DQMStore and DQMRootOutputModule
process.load( "DQMServices.Core.DQMStore_cfi" )

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)

process.DQMOutput = cms.EndPath( process.dqmOutput )
process.schedule.append( process.DQMOutput )

# add specific customizations
#_customInfo = {}
#_customInfo['menuType'  ]= "GRun"
#_customInfo['globalTags']= {}
#_customInfo['globalTags'][True ] = "auto:run3_hlt_GRun"
#_customInfo['globalTags'][False] = "auto:run3_mc_GRun"
#_customInfo['inputFiles']={}
#_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
#_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
#_customInfo['maxEvents' ]=  100
#_customInfo['globalTag' ]= "auto:phase1_2021_realistic"
#_customInfo['inputFile' ]=  ['root://xrootd-cms.infn.it///store/mc/Run3Summer21DRPremix/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/e28c777d-10fd-4100-b230-c42b0160ad8a.root']
#_customInfo['realData'  ]=  False
#
#from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
#process = customizeHLTforAll(process,"GRun",_customInfo)

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
process = customizeHLTforCMSSW(process,"GRun")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(process)

