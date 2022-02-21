# L1T WARN:  L1REPACK:FullMC (intended for MC events with RAW eventcontent) only supports Stage 2 eras for now.
# L1T WARN:  Use a legacy version of L1REPACK for now.
import FWCore.ParameterSet.Config as cms

process = cms.Process("MYHLT")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://xrootd-cms.infn.it///store/mc/Run3Summer21DRPremix/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/e28c777d-10fd-4100-b230-c42b0160ad8a.root'),
    inputCommands = cms.untracked.vstring('keep *')
)
process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/users/kakwok/CSCCluster_12_3_X_signalsPath/V2')
)

process.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter1GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(False),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3MuonPSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(False),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3MuonPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3MuonPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter3PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter3PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter3PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter4PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkf3HitTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfTrajectoryFilterIterL3OI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHI')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(0.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(0.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(0.701),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(0.701),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(8.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedQuadStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedQuadStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedQuadStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedQuadStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilterBase')
    ))
)

process.HLTPSetDetachedStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedTripletStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedTripletStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetGroupedCkfTrajectoryBuilderIterL3ForOI = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfTrajectoryFilterIterL3OI')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    requireSeedHitsInRebuild = cms.bool(False),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfTrajectoryFilterIterL3OI')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(5),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.5),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.7),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetInitialCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.6),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingForDmesonPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.HLTPSetJetCoreStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetJetCoreStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.49),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(1),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.49),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.05),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.4),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiEffTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(9),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(10.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(True)
)

process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonTrackingRegionBuilder8356 = cms.PSet(
    DeltaEta = cms.double(0.2),
    DeltaPhi = cms.double(0.2),
    DeltaR = cms.double(0.2),
    DeltaZ = cms.double(15.9),
    EtaR_UpperLimit_Par1 = cms.double(0.25),
    EtaR_UpperLimit_Par2 = cms.double(0.15),
    Eta_fixed = cms.bool(False),
    Eta_min = cms.double(0.1),
    MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
    OnDemand = cms.int32(-1),
    PhiR_UpperLimit_Par1 = cms.double(0.6),
    PhiR_UpperLimit_Par2 = cms.double(0.2),
    Phi_fixed = cms.bool(False),
    Phi_min = cms.double(0.1),
    Pt_fixed = cms.bool(False),
    Pt_min = cms.double(1.5),
    Rescale_Dz = cms.double(3.0),
    Rescale_eta = cms.double(3.0),
    Rescale_phi = cms.double(3.0),
    UseVertex = cms.bool(False),
    Z_fixed = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    input = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    maxRegions = cms.int32(2),
    precise = cms.bool(True),
    vertexCollection = cms.InputTag("pixelVertices")
)

process.HLTPSetPixelLessStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelLessStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.05),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelLessStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHI')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelPairCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelPairCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(100),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(100),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(8.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterInOut')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterInOutForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterInOutPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterInOutForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterInOutPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPvClusterComparer = cms.PSet(
    track_chi2_max = cms.double(9999999.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(10.0),
    track_pt_min = cms.double(2.5)
)

process.HLTPSetPvClusterComparerForBTag = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(0.1)
)

process.HLTPSetPvClusterComparerForIT = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(1.0)
)

process.HLTPSetTobTecStepInOutTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilterPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryBuilderForElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(-1),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryFilterL3 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(1000000000),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.5),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    propagator = cms.string('PropagatorWithMaterial')
)

process.HLTSeedFromConsecutiveHitsCreatorIT = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSeedFromProtoTracks = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSiStripClusterChargeCutForHI = cms.PSet(
    value = cms.double(2069.0)
)

process.HLTSiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.HLTSiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.HLTSiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.HLTSiStripClusterChargeCutTiny = cms.PSet(
    value = cms.double(800.0)
)

process.datasets = cms.PSet(
    AlCaLumiPixelCountsExpress = cms.vstring('AlCa_LumiPixelsCounts_Random_v2'),
    AlCaLumiPixelCountsPrompt = cms.vstring('AlCa_LumiPixelsCounts_ZeroBias_v2'),
    AlCaP0 = cms.vstring(
        'AlCa_EcalEtaEBonlyForHI_v1',
        'AlCa_EcalEtaEBonly_v13',
        'AlCa_EcalEtaEEonlyForHI_v1',
        'AlCa_EcalEtaEEonly_v13',
        'AlCa_EcalPi0EBonlyForHI_v1',
        'AlCa_EcalPi0EBonly_v13',
        'AlCa_EcalPi0EEonlyForHI_v1',
        'AlCa_EcalPi0EEonly_v13',
        'AlCa_HIEcalEtaEBonly_v1',
        'AlCa_HIEcalEtaEEonly_v1',
        'AlCa_HIEcalPi0EBonly_v1',
        'AlCa_HIEcalPi0EEonly_v1'
    ),
    AlCaPPS = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v1',
        'HLT_PPSMaxTracksPerRP4_v1'
    ),
    AlCaPhiSym = cms.vstring(
        'AlCa_EcalPhiSymForHI_v1',
        'AlCa_EcalPhiSym_v9'
    ),
    BTagMu = cms.vstring(
        'HLT_BTagMu_AK4DiJet110_Mu5_v13',
        'HLT_BTagMu_AK4DiJet170_Mu5_v12',
        'HLT_BTagMu_AK4DiJet20_Mu5_v13',
        'HLT_BTagMu_AK4DiJet40_Mu5_v13',
        'HLT_BTagMu_AK4DiJet70_Mu5_v13',
        'HLT_BTagMu_AK4Jet300_Mu5_v12',
        'HLT_BTagMu_AK8DiJet170_Mu5_v9',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v2',
        'HLT_BTagMu_AK8Jet300_Mu5_v12'
    ),
    Charmonium = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v5',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v7',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_v8',
        'HLT_Dimuon0_Jpsi_v8',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v7',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v8',
        'HLT_Dimuon0_LowMass_L1_4R_v7',
        'HLT_Dimuon0_LowMass_L1_4_v8',
        'HLT_Dimuon0_LowMass_v8',
        'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v7',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v6',
        'HLT_Dimuon18_PsiPrime_v14',
        'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v7',
        'HLT_Dimuon25_Jpsi_noCorrL1_v6',
        'HLT_Dimuon25_Jpsi_v14',
        'HLT_DoubleMu2_Jpsi_DoubleTkMu0_Phi_v5',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v6',
        'HLT_DoubleMu4_3_Bs_v14',
        'HLT_DoubleMu4_3_Jpsi_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v7',
        'HLT_DoubleMu4_JpsiTrk_Displaced_v15',
        'HLT_DoubleMu4_Jpsi_Displaced_v7',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v7',
        'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v15',
        'HLT_Mu30_TkMu0_Psi_v1',
        'HLT_Mu7p5_L2Mu2_Jpsi_v10',
        'HLT_Mu7p5_Track2_Jpsi_v11',
        'HLT_Mu7p5_Track3p5_Jpsi_v11',
        'HLT_Mu7p5_Track7_Jpsi_v11'
    ),
    Commissioning = cms.vstring(
        'HLT_IsoTrackHB_v4',
        'HLT_IsoTrackHE_v4',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v2'
    ),
    Cosmics = cms.vstring(
        'HLT_L1SingleMu3_v1',
        'HLT_L1SingleMu5_v1',
        'HLT_L1SingleMu7_v1',
        'HLT_L1SingleMuCosmics_v1',
        'HLT_L1SingleMuOpen_DT_v2',
        'HLT_L1SingleMuOpen_v2',
        'HLT_L2DoubleMu23_NoVertex_v2'
    ),
    DQMOnlineBeamspot = cms.vstring(
        'HLT_HIHT80_Beamspot_ppRef5TeV_v3',
        'HLT_HT300_Beamspot_v11',
        'HLT_HT450_Beamspot_v11',
        'HLT_HT60_Beamspot_v1',
        'HLT_ZeroBias_Beamspot_v4'
    ),
    DisplacedJet = cms.vstring(
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT425_v9',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT430_DisplacedDijet60_DisplacedTrack_v13',
        'HLT_HT500_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT550_DisplacedDijet60_Inclusive_v13',
        'HLT_HT650_DisplacedDijet60_Inclusive_v13'
    ),
    DoubleMuon = cms.vstring(
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_NoL2Matched_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_NoL2Matched_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_NoL2Matched_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_NoL2Matched_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v2',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v2',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v2',
        'HLT_DoubleL2Mu50_v2',
        'HLT_DoubleMu33NoFiltersNoVtxDisplaced_v1',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v10',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v10',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v10',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v10',
        'HLT_DoubleMu40NoFiltersNoVtxDisplaced_v1',
        'HLT_DoubleMu43NoFiltersNoVtx_v4',
        'HLT_DoubleMu48NoFiltersNoVtx_v4',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v8',
        'HLT_HIL1DoubleMu0ForPPRef_v4',
        'HLT_HIL1DoubleMu10ForPPRef_v4',
        'HLT_HIL2DoubleMu0_NHitQForPPRef_v5',
        'HLT_HIL3DoubleMu0_OS_m2p5to4p5ForPPRef_v6',
        'HLT_HIL3DoubleMu0_OS_m7to14ForPPRef_v6',
        'HLT_L1DoubleMu0_v1',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v14',
        'HLT_Mu17_TrkIsoVVL_v13',
        'HLT_Mu17_v13',
        'HLT_Mu18_Mu9_DZ_v4',
        'HLT_Mu18_Mu9_SameSign_DZ_v4',
        'HLT_Mu18_Mu9_SameSign_v4',
        'HLT_Mu18_Mu9_v4',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v3',
        'HLT_Mu19_TrkIsoVVL_v4',
        'HLT_Mu19_v4',
        'HLT_Mu20_Mu10_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_v4',
        'HLT_Mu20_Mu10_v4',
        'HLT_Mu23_Mu12_DZ_v4',
        'HLT_Mu23_Mu12_SameSign_DZ_v4',
        'HLT_Mu23_Mu12_SameSign_v4',
        'HLT_Mu23_Mu12_v4',
        'HLT_Mu37_TkMu27_v5',
        'HLT_Mu8_TrkIsoVVL_v12',
        'HLT_Mu8_v12',
        'HLT_TripleMu_10_5_5_DZ_v10',
        'HLT_TripleMu_12_10_5_v10',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v3',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v8',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v6',
        'HLT_TrkMu16_DoubleTrkMu6NoFiltersNoVtx_v12',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v13'
    ),
    DoubleMuonLowMass = cms.vstring(
        'HLT_Dimuon0_LowMass_L1_TM530_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v4',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_v12',
        'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v15',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v4'
    ),
    EGamma = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v4',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v13',
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_NoPixelVeto_Mass55_v13',
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_PixelVeto_Mass55_v15',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto_Mass55_v2',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto_v2',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v13',
        'HLT_DoubleEle25_CaloIdL_MW_v4',
        'HLT_DoubleEle27_CaloIdL_MW_v4',
        'HLT_DoubleEle33_CaloIdL_MW_v17',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v20',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v20',
        'HLT_DoublePhoton33_CaloIdL_v6',
        'HLT_DoublePhoton70_v6',
        'HLT_DoublePhoton85_v14',
        'HLT_ECALHT800_v10',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v14',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v7',
        'HLT_Ele145_CaloIdVT_GsfTrkIdT_v8',
        'HLT_Ele15_CaloIdL_TrackIdL_IsoVL_PFJet30_v3',
        'HLT_Ele15_Ele8_CaloIdL_TrackIdL_IsoVL_v3',
        'HLT_Ele15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v8',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v16',
        'HLT_Ele15_IsoVVVL_PFHT450_v16',
        'HLT_Ele15_IsoVVVL_PFHT600_v20',
        'HLT_Ele15_WPLoose_Gsf_v3',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v9',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v16',
        'HLT_Ele17_WPLoose_Gsf_v3',
        'HLT_Ele200_CaloIdVT_GsfTrkIdT_v8',
        'HLT_Ele20_WPLoose_Gsf_v6',
        'HLT_Ele20_WPTight_Gsf_v6',
        'HLT_Ele20_eta2p1_WPLoose_Gsf_v6',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v19',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele250_CaloIdVT_GsfTrkIdT_v13',
        'HLT_Ele27_Ele37_CaloIdL_MW_v4',
        'HLT_Ele27_WPTight_Gsf_v16',
        'HLT_Ele28_HighEta_SC20_Mass55_v13',
        'HLT_Ele28_WPTight_Gsf_v1',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v13',
        'HLT_Ele300_CaloIdVT_GsfTrkIdT_v13',
        'HLT_Ele30_WPTight_Gsf_v1',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v9',
        'HLT_Ele32_WPTight_Gsf_v15',
        'HLT_Ele35_WPTight_Gsf_L1EGMT_v5',
        'HLT_Ele35_WPTight_Gsf_v9',
        'HLT_Ele38_WPTight_Gsf_v9',
        'HLT_Ele40_WPTight_Gsf_v9',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v18',
        'HLT_Ele50_IsoVVVL_PFHT450_v16',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v16',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Photon100EBHE10_v2',
        'HLT_Photon100EB_TightID_TightIso_v2',
        'HLT_Photon100EEHE10_v2',
        'HLT_Photon100EE_TightID_TightIso_v2',
        'HLT_Photon110EB_TightID_TightIso_v2',
        'HLT_Photon120EB_TightID_TightIso_v2',
        'HLT_Photon120_R9Id90_HE10_IsoM_v14',
        'HLT_Photon120_v13',
        'HLT_Photon150_v6',
        'HLT_Photon165_R9Id90_HE10_IsoM_v15',
        'HLT_Photon175_v14',
        'HLT_Photon200_v13',
        'HLT_Photon20_HoverELoose_v10',
        'HLT_Photon20_v2',
        'HLT_Photon25_v4',
        'HLT_Photon300_NoHE_v12',
        'HLT_Photon30_HoverELoose_v10',
        'HLT_Photon33_v5',
        'HLT_Photon40_HoverELoose_v10',
        'HLT_Photon50_HoverELoose_v10',
        'HLT_Photon50_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_PFMET50_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_v14',
        'HLT_Photon50_v13',
        'HLT_Photon60_HoverELoose_v10',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350MinPFJet15_v11',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_v5',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_CaloMJJ300_PFJetsMJJ400DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_CaloMJJ400_PFJetsMJJ600DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ600DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_v14',
        'HLT_Photon75_v13',
        'HLT_Photon90_CaloIdL_PFHT700_v16',
        'HLT_Photon90_R9Id90_HE10_IsoM_v14',
        'HLT_Photon90_v13',
        'HLT_TriplePhoton_20_20_20_CaloIdLV2_R9IdVL_v3',
        'HLT_TriplePhoton_20_20_20_CaloIdLV2_v3',
        'HLT_TriplePhoton_30_30_10_CaloIdLV2_R9IdVL_v4',
        'HLT_TriplePhoton_30_30_10_CaloIdLV2_v4',
        'HLT_TriplePhoton_35_35_5_CaloIdLV2_R9IdVL_v4'
    ),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v4'),
    EmptyBX = cms.vstring(
        'HLT_HIL1NotBptxORForPPRef_v2',
        'HLT_HIL1UnpairedBunchBptxMinusForPPRef_v2',
        'HLT_HIL1UnpairedBunchBptxPlusForPPRef_v2',
        'HLT_L1NotBptxOR_v3',
        'HLT_L1UnpairedBunchBptxMinus_v2',
        'HLT_L1UnpairedBunchBptxPlus_v2'
    ),
    EphemeralHLTPhysics1 = cms.vstring('HLT_Physics_part0_v7'),
    EphemeralHLTPhysics2 = cms.vstring('HLT_Physics_part1_v7'),
    EphemeralHLTPhysics3 = cms.vstring('HLT_Physics_part2_v7'),
    EphemeralHLTPhysics4 = cms.vstring('HLT_Physics_part3_v7'),
    EphemeralHLTPhysics5 = cms.vstring('HLT_Physics_part4_v7'),
    EphemeralHLTPhysics6 = cms.vstring('HLT_Physics_part5_v7'),
    EphemeralHLTPhysics7 = cms.vstring('HLT_Physics_part6_v7'),
    EphemeralHLTPhysics8 = cms.vstring('HLT_Physics_part7_v7'),
    EphemeralZeroBias1 = cms.vstring('HLT_ZeroBias_part0_v6'),
    EphemeralZeroBias2 = cms.vstring('HLT_ZeroBias_part1_v6'),
    EphemeralZeroBias3 = cms.vstring('HLT_ZeroBias_part2_v6'),
    EphemeralZeroBias4 = cms.vstring('HLT_ZeroBias_part3_v6'),
    EphemeralZeroBias5 = cms.vstring('HLT_ZeroBias_part4_v6'),
    EphemeralZeroBias6 = cms.vstring('HLT_ZeroBias_part5_v6'),
    EphemeralZeroBias7 = cms.vstring('HLT_ZeroBias_part6_v6'),
    EphemeralZeroBias8 = cms.vstring('HLT_ZeroBias_part7_v6'),
    EventDisplay = cms.vstring(
        'HLT_AK4PFJet100_v19',
        'HLT_DoublePhoton85_v14',
        'HLT_L1SingleMu7_v1',
        'HLT_PFJet500_v21'
    ),
    ExpressAlignment = cms.vstring(
        'HLT_HIHT80_Beamspot_ppRef5TeV_v3',
        'HLT_HT300_Beamspot_v11',
        'HLT_HT450_Beamspot_v11',
        'HLT_HT60_Beamspot_v1',
        'HLT_ZeroBias_Beamspot_v4'
    ),
    ExpressCosmics = cms.vstring(
        'HLT_L1SingleMuCosmics_v1',
        'HLT_L1SingleMuOpen_DT_v2',
        'HLT_L1SingleMuOpen_v2',
        'HLT_Random_v3'
    ),
    ExpressPhysics = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_HIL1DoubleMu0ForPPRef_v4',
        'HLT_IsoMu20_v15',
        'HLT_IsoMu24_v13',
        'HLT_IsoMu27_v16',
        'HLT_L1MinimumBiasHF1AND_v4',
        'HLT_L1RomanPot_part0_v1',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v15',
        'HLT_Physics_v7',
        'HLT_Random_v3',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part0_v1',
        'HLT_ZeroBias_Alignment_v1',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v5',
        'HLT_ZeroBias_IsolatedBunches_v5',
        'HLT_ZeroBias_v6'
    ),
    FSQJet1 = cms.vstring(
        'HLT_DiPFJet15_NoCaloMatched_v16',
        'HLT_DiPFJet25_NoCaloMatched_v16'
    ),
    FSQJet2 = cms.vstring(
        'HLT_DiPFJet15_FBEta3_NoCaloMatched_v17',
        'HLT_DiPFJet25_FBEta3_NoCaloMatched_v17',
        'HLT_DiPFJetAve15_HFJEC_v17',
        'HLT_DiPFJetAve25_HFJEC_v17',
        'HLT_DiPFJetAve35_HFJEC_v17'
    ),
    FullTrack = cms.vstring(
        'HLT_FullTrack18ForPPRef_v11',
        'HLT_FullTrack24ForPPRef_v11',
        'HLT_FullTrack34ForPPRef_v11',
        'HLT_FullTrack45ForPPRef_v11',
        'HLT_FullTrack53ForPPRef_v11'
    ),
    HFvetoTOTEM = cms.vstring('HLT_L1HFveto_v1'),
    HICastor = cms.vstring(
        'HLT_HICastor_HighJet_BptxAND_v1',
        'HLT_HICastor_HighJet_MBHF1AND_BptxAND_v1',
        'HLT_HICastor_HighJet_MBHF1OR_BptxAND_v1',
        'HLT_HICastor_HighJet_MBHF2AND_BptxAND_v1',
        'HLT_HICastor_HighJet_NotMBHF2AND_v1',
        'HLT_HICastor_HighJet_NotMBHF2OR_v1',
        'HLT_HICastor_HighJet_v1',
        'HLT_HICastor_MediumJet_BptxAND_v1',
        'HLT_HICastor_MediumJet_MBHF1OR_BptxAND_v1',
        'HLT_HICastor_MediumJet_NotMBHF2AND_v1',
        'HLT_HICastor_MediumJet_NotMBHF2OR_v1',
        'HLT_HICastor_MediumJet_SingleEG5_MBHF1OR_BptxAND_v1',
        'HLT_HICastor_MediumJet_SingleMu0_MBHF1OR_BptxAND_v1',
        'HLT_HICastor_MediumJet_v1',
        'HLT_HICastor_Muon_BptxAND_v1',
        'HLT_HICastor_Muon_v1',
        'HLT_HIL1_ZDC_AND_OR_MinimumBiasHF1_AND_BptxAND_v1',
        'HLT_HIL1_ZDC_AND_OR_MinimumBiasHF2_AND_BptxAND_v1'
    ),
    HIDQMOnlineBeamspot = cms.vstring(
        'HLT_HICentralityVeto_Beamspot_v1',
        'HLT_HICsAK4PFJet100Eta1p5_Beamspot_v1'
    ),
    HIDoubleMuon = cms.vstring(
        'HLT_HIL1DoubleMu0_v1',
        'HLT_HIL1DoubleMu10_v1',
        'HLT_HIL1DoubleMuOpen_OS_er1p6_v1',
        'HLT_HIL1DoubleMuOpen_er1p6_v1',
        'HLT_HIL1DoubleMuOpen_v1',
        'HLT_HIL2DoubleMuOpen_v1',
        'HLT_HIL2_L1DoubleMu10_v1',
        'HLT_HIL3DoubleMuOpen_M60120_v1',
        'HLT_HIL3DoubleMuOpen_Upsi_v1',
        'HLT_HIL3DoubleMuOpen_v1',
        'HLT_HIL3Mu0_L2Mu0_v1',
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_M7toinf_v1',
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_v1',
        'HLT_HIL3Mu2p5_L1DoubleMu0_v1',
        'HLT_HIL3Mu3NHitQ10_L1DoubleMuOpen_v1',
        'HLT_HIL3Mu3_L1DoubleMuOpen_OS_v1',
        'HLT_HIL3Mu3_L1TripleMuOpen_v1',
        'HLT_HIL3_L1DoubleMu10_v1'
    ),
    HIDoubleMuonPsiPeri = cms.vstring(
        'HLT_HIL1DoubleMuOpen_Centrality_30_100_v1',
        'HLT_HIL1DoubleMuOpen_Centrality_40_100_v1',
        'HLT_HIL1DoubleMuOpen_Centrality_50_100_v1',
        'HLT_HIL1DoubleMuOpen_OS_Centrality_30_100_v1',
        'HLT_HIL1DoubleMuOpen_OS_Centrality_40_100_v1',
        'HLT_HIL3DoubleMuOpen_JpsiPsi_v1',
        'HLT_HIL3Mu0NHitQ10_L2Mu0_MAXdR3p5_M1to5_v1'
    ),
    HIEmptyBX = cms.vstring(
        'HLT_HIL1NotBptxOR_v1',
        'HLT_HIL1UnpairedBunchBptxMinus_v1',
        'HLT_HIL1UnpairedBunchBptxPlus_v1'
    ),
    HIExpressAlignment = cms.vstring(
        'HLT_HICentralityVeto_v1',
        'HLT_HICsAK4PFJet100Eta1p5_v1'
    ),
    HIExpressPhysics = cms.vstring(
        'HLT_HICastor_MediumJet_NotMBHF2AND_v1',
        'HLT_HICentrality30100_FirstCollisionAfterAbortGap_v1',
        'HLT_HICentralityVeto_v1',
        'HLT_HICsAK4PFJet100Eta1p5_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt50_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt50_v1',
        'HLT_HIEle20Gsf_v1',
        'HLT_HIFullTracks2018_HighPt56_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF1OR_v1',
        'HLT_HIGEDPhoton40_v1',
        'HLT_HIIslandPhoton40_Eta2p4_v1',
        'HLT_HIL1DoubleMu0_v1',
        'HLT_HIL1DoubleMu10_v1',
        'HLT_HIL1DoubleMuOpen_Centrality_50_100_v1',
        'HLT_HIL1NotBptxOR_v1',
        'HLT_HIL1UnpairedBunchBptxMinus_v1',
        'HLT_HIL1UnpairedBunchBptxPlus_v1',
        'HLT_HIL1_ETT10_ETTAsym50_MinimumBiasHF1_OR_BptxAND_v1',
        'HLT_HIL2DoubleMuOpen_v1',
        'HLT_HIL2Mu3_NHitQ15_v1',
        'HLT_HIL2_L1DoubleMu10_v1',
        'HLT_HIL3DoubleMuOpen_v1',
        'HLT_HIL3Mu0NHitQ10_L2Mu0_MAXdR3p5_M1to5_v1',
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_M7toinf_v1',
        'HLT_HIL3_L1DoubleMu10_v1',
        'HLT_HILcPPTrackingGlobal_Dpt50_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part0_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part0_v1',
        'HLT_HIMinimumBias_part0_v1',
        'HLT_HIPhysics_v1',
        'HLT_HIPuAK4CaloJet100Eta5p1_v1',
        'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p4_v1',
        'HLT_HIRandom_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_v1',
        'HLT_HIUPC_ZeroBias_SinglePixelTrack_v1',
        'HLT_HIZeroBias_FirstCollisionAfterAbortGap_v1',
        'HLT_HIZeroBias_v1'
    ),
    HIForward = cms.vstring(
        'HLT_HIUPC_DoubleEG2_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_v1',
        'HLT_HIUPC_DoubleEG5_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_v1',
        'HLT_HIUPC_DoubleMu0_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMu0_NotMBHF2AND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMu0_NotMBHF2AND_v1',
        'HLT_HIUPC_DoubleMu0_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMu0_NotMBHF2OR_v1',
        'HLT_HIUPC_DoubleMuOpen_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMuOpen_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMuOpen_NotMBHF2OR_v1',
        'HLT_HIUPC_ETT5_Asym50_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_ETT5_Asym50_NotMBHF2OR_v1',
        'HLT_HIUPC_Mu8_Mu13_MaxPixelTrack_v1',
        'HLT_HIUPC_Mu8_Mu13_v1',
        'HLT_HIUPC_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_NotMBHF2AND_v1',
        'HLT_HIUPC_NotMBHF2OR_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_NotMBHF2OR_BptxAND_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG3_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG3_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_v1',
        'HLT_HIUPC_SingleEG5_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG5_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_v1',
        'HLT_HIUPC_SingleMu0_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2AND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2AND_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2OR_v1',
        'HLT_HIUPC_SingleMu3_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu3_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu3_NotMBHF2OR_v1',
        'HLT_HIUPC_SingleMuOpen_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2OR_v1',
        'HLT_HIUPC_ZeroBias_MaxPixelCluster_v1',
        'HLT_HIUPC_ZeroBias_SinglePixelTrack_v1',
        'HLT_HIZeroBias_v1'
    ),
    HIHLTPhysics = cms.vstring('HLT_HIPhysics_v1'),
    HIHardProbes = cms.vstring(
        'HLT_HICsAK4PFJet100Eta1p5_v1',
        'HLT_HICsAK4PFJet120Eta1p5_v1',
        'HLT_HICsAK4PFJet80Eta1p5_v1',
        'HLT_HIDoubleEle10GsfMass50_v1',
        'HLT_HIDoubleEle10Gsf_v1',
        'HLT_HIDoubleEle15GsfMass50_v1',
        'HLT_HIDoubleEle15Gsf_v1',
        'HLT_HIEle10Gsf_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIEle10Gsf_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIEle10Gsf_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIEle10Gsf_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIEle10Gsf_v1',
        'HLT_HIEle15Ele10GsfMass50_v1',
        'HLT_HIEle15Ele10Gsf_v1',
        'HLT_HIEle15Gsf_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIEle15Gsf_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIEle15Gsf_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIEle15Gsf_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIEle15Gsf_v1',
        'HLT_HIEle20Gsf_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIEle20Gsf_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIEle20Gsf_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIEle20Gsf_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIEle20Gsf_v1',
        'HLT_HIEle30Gsf_v1',
        'HLT_HIEle40Gsf_v1',
        'HLT_HIEle50Gsf_v1',
        'HLT_HIGEDPhoton30_EB_HECut_v1',
        'HLT_HIGEDPhoton30_EB_v1',
        'HLT_HIGEDPhoton30_HECut_v1',
        'HLT_HIGEDPhoton30_v1',
        'HLT_HIGEDPhoton40_EB_HECut_v1',
        'HLT_HIGEDPhoton40_EB_v1',
        'HLT_HIGEDPhoton40_HECut_v1',
        'HLT_HIGEDPhoton40_v1',
        'HLT_HIGEDPhoton50_EB_HECut_v1',
        'HLT_HIGEDPhoton50_EB_v1',
        'HLT_HIGEDPhoton50_HECut_v1',
        'HLT_HIGEDPhoton50_v1',
        'HLT_HIGEDPhoton60_EB_HECut_v1',
        'HLT_HIGEDPhoton60_EB_v1',
        'HLT_HIGEDPhoton60_HECut_v1',
        'HLT_HIGEDPhoton60_v1',
        'HLT_HIIslandPhoton30_Eta1p5_v1',
        'HLT_HIIslandPhoton30_Eta2p4_v1',
        'HLT_HIIslandPhoton40_Eta1p5_v1',
        'HLT_HIIslandPhoton40_Eta2p4_v1',
        'HLT_HIIslandPhoton50_Eta1p5_v1',
        'HLT_HIIslandPhoton50_Eta2p4_v1',
        'HLT_HIIslandPhoton60_Eta1p5_v1',
        'HLT_HIIslandPhoton60_Eta2p4_v1',
        'HLT_HIL1Mu3Eta2p5_Ele10Gsf_v1',
        'HLT_HIL1Mu3Eta2p5_Ele15Gsf_v1',
        'HLT_HIL1Mu3Eta2p5_Ele20Gsf_v1',
        'HLT_HIL1Mu5Eta2p5_Ele10Gsf_v1',
        'HLT_HIL1Mu5Eta2p5_Ele15Gsf_v1',
        'HLT_HIL1Mu5Eta2p5_Ele20Gsf_v1',
        'HLT_HIL1Mu7Eta2p5_Ele10Gsf_v1',
        'HLT_HIL1Mu7Eta2p5_Ele15Gsf_v1',
        'HLT_HIL1Mu7Eta2p5_Ele20Gsf_v1',
        'HLT_HIL3Mu3_EG10HECut_v1',
        'HLT_HIL3Mu3_EG15HECut_v1',
        'HLT_HIL3Mu3_EG20HECut_v1',
        'HLT_HIL3Mu3_EG30HECut_v1',
        'HLT_HIL3Mu5_EG10HECut_v1',
        'HLT_HIL3Mu5_EG15HECut_v1',
        'HLT_HIL3Mu5_EG20HECut_v1',
        'HLT_HIL3Mu5_EG30HECut_v1',
        'HLT_HIL3Mu7_EG10HECut_v1',
        'HLT_HIL3Mu7_EG15HECut_v1',
        'HLT_HIL3Mu7_EG20HECut_v1',
        'HLT_HIL3Mu7_EG30HECut_v1',
        'HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p75_v1',
        'HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p4_v1',
        'HLT_HIPuAK4CaloJet100Eta5p1_v1',
        'HLT_HIPuAK4CaloJet100Fwd_v1',
        'HLT_HIPuAK4CaloJet100_35_Eta0p7_v1',
        'HLT_HIPuAK4CaloJet100_35_Eta1p1_v1',
        'HLT_HIPuAK4CaloJet120Eta5p1_v1',
        'HLT_HIPuAK4CaloJet120Fwd_v1',
        'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p75_v1',
        'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p4_v1',
        'HLT_HIPuAK4CaloJet60Fwd_v1',
        'HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p75_v1',
        'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p4_v1',
        'HLT_HIPuAK4CaloJet80Eta5p1_v1',
        'HLT_HIPuAK4CaloJet80Fwd_v1',
        'HLT_HIPuAK4CaloJet80_35_Eta0p7_v1',
        'HLT_HIPuAK4CaloJet80_35_Eta1p1_v1',
        'HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v1'
    ),
    HIHardProbesLower = cms.vstring(
        'HLT_HICsAK4PFJet60Eta1p5_v1',
        'HLT_HIGEDPhoton10_EB_HECut_v1',
        'HLT_HIGEDPhoton10_EB_v1',
        'HLT_HIGEDPhoton10_HECut_v1',
        'HLT_HIGEDPhoton10_v1',
        'HLT_HIGEDPhoton20_EB_HECut_v1',
        'HLT_HIGEDPhoton20_EB_v1',
        'HLT_HIGEDPhoton20_HECut_v1',
        'HLT_HIGEDPhoton20_v1',
        'HLT_HIIslandPhoton10_Eta1p5_v1',
        'HLT_HIIslandPhoton10_Eta2p4_v1',
        'HLT_HIIslandPhoton20_Eta1p5_v1',
        'HLT_HIIslandPhoton20_Eta2p4_v1',
        'HLT_HIPuAK4CaloJet40Eta5p1_v1',
        'HLT_HIPuAK4CaloJet40Fwd_v1',
        'HLT_HIPuAK4CaloJet60Eta5p1_v1'
    ),
    HIHardProbesPeripheral = cms.vstring(
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_30_100_v1',
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_50_100_v1',
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_30_100_v1',
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_50_100_v1',
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_30_100_v1',
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_50_100_v1',
        'HLT_HIGEDPhoton10_Cent30_100_v1',
        'HLT_HIGEDPhoton10_Cent50_100_v1',
        'HLT_HIGEDPhoton20_Cent30_100_v1',
        'HLT_HIGEDPhoton20_Cent50_100_v1',
        'HLT_HIGEDPhoton30_Cent30_100_v1',
        'HLT_HIGEDPhoton30_Cent50_100_v1',
        'HLT_HIGEDPhoton40_Cent30_100_v1',
        'HLT_HIGEDPhoton40_Cent50_100_v1',
        'HLT_HIIslandPhoton10_Eta2p4_Cent30_100_v1',
        'HLT_HIIslandPhoton10_Eta2p4_Cent50_100_v1',
        'HLT_HIIslandPhoton20_Eta2p4_Cent30_100_v1',
        'HLT_HIIslandPhoton20_Eta2p4_Cent50_100_v1',
        'HLT_HIIslandPhoton30_Eta2p4_Cent30_100_v1',
        'HLT_HIIslandPhoton30_Eta2p4_Cent50_100_v1',
        'HLT_HIIslandPhoton40_Eta2p4_Cent30_100_v1',
        'HLT_HIIslandPhoton40_Eta2p4_Cent50_100_v1',
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_30_100_v1',
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_50_100_v1',
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_30_100_v1',
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_50_100_v1',
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_30_100_v1',
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_50_100_v1',
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_30_100_v1',
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_50_100_v1'
    ),
    HIHcalNZS = cms.vstring(
        'HLT_HIHcalNZS_v1',
        'HLT_HIHcalPhiSym_v1'
    ),
    HIHeavyFlavor = cms.vstring(
        'HLT_HIDmesonPPTrackingGlobal_Dpt15_NoIter10_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt15_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt20_NoIter10_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt20_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt30_NoIter10_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt30_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt40_NoIter10_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt40_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt50_NoIter10_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt50_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt60_NoIter10_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt60_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt20_NoIter10_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt20_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt30_NoIter10_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt30_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt40_NoIter10_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt40_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt50_NoIter10_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt50_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt60_NoIter10_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt60_v1',
        'HLT_HIFullTracks2018_HighPt18_NoIter10_v1',
        'HLT_HIFullTracks2018_HighPt18_v1',
        'HLT_HIFullTracks2018_HighPt24_NoIter10_v1',
        'HLT_HIFullTracks2018_HighPt24_v1',
        'HLT_HIFullTracks2018_HighPt34_NoIter10_v1',
        'HLT_HIFullTracks2018_HighPt34_v1',
        'HLT_HIFullTracks2018_HighPt45_NoIter10_v1',
        'HLT_HIFullTracks2018_HighPt45_v1',
        'HLT_HIFullTracks2018_HighPt56_NoIter10_v1',
        'HLT_HIFullTracks2018_HighPt56_v1',
        'HLT_HIFullTracks2018_HighPt60_NoIter10_v1',
        'HLT_HIFullTracks2018_HighPt60_v1',
        'HLT_HILcPPTrackingGlobal_Dpt20_NoIter10_v1',
        'HLT_HILcPPTrackingGlobal_Dpt20_v1',
        'HLT_HILcPPTrackingGlobal_Dpt30_NoIter10_v1',
        'HLT_HILcPPTrackingGlobal_Dpt30_v1',
        'HLT_HILcPPTrackingGlobal_Dpt40_NoIter10_v1',
        'HLT_HILcPPTrackingGlobal_Dpt40_v1',
        'HLT_HILcPPTrackingGlobal_Dpt50_NoIter10_v1',
        'HLT_HILcPPTrackingGlobal_Dpt50_v1',
        'HLT_HILcPPTrackingGlobal_Dpt60_NoIter10_v1',
        'HLT_HILcPPTrackingGlobal_Dpt60_v1'
    ),
    HIHighMultiplicityETTAsym = cms.vstring(
        'HLT_HIL1_ETT10_ETTAsym50_MinimumBiasHF1_OR_BptxAND_v1',
        'HLT_HIL1_ETT60_ETTAsym65_MinimumBiasHF2_OR_PixelTracks10_v1',
        'HLT_HIL1_ETT65_ETTAsym80_MinimumBiasHF2_OR_PixelTracks10_v1',
        'HLT_HIL1_ETT8_ETTAsym50_MinimumBiasHF1_OR_BptxAND_v1'
    ),
    HILowMultiplicity = cms.vstring(
        'HLT_HIFullTracks_Multiplicity020_HF1AND_v1',
        'HLT_HIFullTracks_Multiplicity020_HF1OR_v1',
        'HLT_HIFullTracks_Multiplicity020_HF2OR_v1',
        'HLT_HIFullTracks_Multiplicity020_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF1AND_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF1OR_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF2OR_v1',
        'HLT_HIFullTracks_Multiplicity2040_v1',
        'HLT_HIFullTracks_Multiplicity335_HF1OR_v1',
        'HLT_HIFullTracks_Multiplicity4060_v1',
        'HLT_HIFullTracks_Multiplicity6080_v1',
        'HLT_HIFullTracks_Multiplicity80100_v1'
    ),
    HILowMultiplicityReducedFormat = cms.vstring(
        'HLT_HIFullTracks_Multiplicity020_HF1AND_v1',
        'HLT_HIFullTracks_Multiplicity020_HF1OR_v1',
        'HLT_HIFullTracks_Multiplicity020_HF2OR_v1',
        'HLT_HIFullTracks_Multiplicity020_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF1AND_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF1OR_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF2OR_v1',
        'HLT_HIFullTracks_Multiplicity2040_v1',
        'HLT_HIFullTracks_Multiplicity4060_v1',
        'HLT_HIFullTracks_Multiplicity6080_v1',
        'HLT_HIFullTracks_Multiplicity80100_v1'
    ),
    HIMinimumBias0 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part0_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part0_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part0_v1',
        'HLT_HIMinimumBias_part0_v1'
    ),
    HIMinimumBias1 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part1_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part1_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part1_v1',
        'HLT_HIMinimumBias_part1_v1'
    ),
    HIMinimumBias10 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part10_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part10_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part10_v1',
        'HLT_HIMinimumBias_part10_v1'
    ),
    HIMinimumBias11 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part11_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part11_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part11_v1',
        'HLT_HIMinimumBias_part11_v1'
    ),
    HIMinimumBias12 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part12_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part12_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part12_v1',
        'HLT_HIMinimumBias_part12_v1'
    ),
    HIMinimumBias13 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part13_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part13_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part13_v1',
        'HLT_HIMinimumBias_part13_v1'
    ),
    HIMinimumBias14 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part14_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part14_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part14_v1',
        'HLT_HIMinimumBias_part14_v1'
    ),
    HIMinimumBias15 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part15_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part15_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part15_v1',
        'HLT_HIMinimumBias_part15_v1'
    ),
    HIMinimumBias16 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part16_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part16_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part16_v1',
        'HLT_HIMinimumBias_part16_v1'
    ),
    HIMinimumBias17 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part17_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part17_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part17_v1',
        'HLT_HIMinimumBias_part17_v1'
    ),
    HIMinimumBias18 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part18_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part18_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part18_v1',
        'HLT_HIMinimumBias_part18_v1'
    ),
    HIMinimumBias19 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part19_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part19_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part19_v1',
        'HLT_HIMinimumBias_part19_v1'
    ),
    HIMinimumBias2 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part2_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part2_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part2_v1',
        'HLT_HIMinimumBias_part2_v1'
    ),
    HIMinimumBias3 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part3_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part3_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part3_v1',
        'HLT_HIMinimumBias_part3_v1'
    ),
    HIMinimumBias4 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part4_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part4_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part4_v1',
        'HLT_HIMinimumBias_part4_v1'
    ),
    HIMinimumBias5 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part5_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part5_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part5_v1',
        'HLT_HIMinimumBias_part5_v1'
    ),
    HIMinimumBias6 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part6_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part6_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part6_v1',
        'HLT_HIMinimumBias_part6_v1'
    ),
    HIMinimumBias7 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part7_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part7_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part7_v1',
        'HLT_HIMinimumBias_part7_v1'
    ),
    HIMinimumBias8 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part8_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part8_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part8_v1',
        'HLT_HIMinimumBias_part8_v1'
    ),
    HIMinimumBias9 = cms.vstring(
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part9_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part9_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part9_v1',
        'HLT_HIMinimumBias_part9_v1'
    ),
    HIMinimumBiasReducedFormat0 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part0_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part1_v1',
        'HLT_HIMinimumBiasRF_part0_v1',
        'HLT_HIMinimumBiasRF_part1_v1'
    ),
    HIMinimumBiasReducedFormat1 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part2_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part3_v1',
        'HLT_HIMinimumBiasRF_part2_v1',
        'HLT_HIMinimumBiasRF_part3_v1'
    ),
    HIMinimumBiasReducedFormat10 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part20_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part21_v1',
        'HLT_HIMinimumBiasRF_part20_v1',
        'HLT_HIMinimumBiasRF_part21_v1'
    ),
    HIMinimumBiasReducedFormat11 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part22_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part23_v1',
        'HLT_HIMinimumBiasRF_part22_v1',
        'HLT_HIMinimumBiasRF_part23_v1'
    ),
    HIMinimumBiasReducedFormat2 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part4_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part5_v1',
        'HLT_HIMinimumBiasRF_part4_v1',
        'HLT_HIMinimumBiasRF_part5_v1'
    ),
    HIMinimumBiasReducedFormat3 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part6_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part7_v1',
        'HLT_HIMinimumBiasRF_part6_v1',
        'HLT_HIMinimumBiasRF_part7_v1'
    ),
    HIMinimumBiasReducedFormat4 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part8_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part9_v1',
        'HLT_HIMinimumBiasRF_part8_v1',
        'HLT_HIMinimumBiasRF_part9_v1'
    ),
    HIMinimumBiasReducedFormat5 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part10_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part11_v1',
        'HLT_HIMinimumBiasRF_part10_v1',
        'HLT_HIMinimumBiasRF_part11_v1'
    ),
    HIMinimumBiasReducedFormat6 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part12_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part13_v1',
        'HLT_HIMinimumBiasRF_part12_v1',
        'HLT_HIMinimumBiasRF_part13_v1'
    ),
    HIMinimumBiasReducedFormat7 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part14_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part15_v1',
        'HLT_HIMinimumBiasRF_part14_v1',
        'HLT_HIMinimumBiasRF_part15_v1'
    ),
    HIMinimumBiasReducedFormat8 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part16_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part17_v1',
        'HLT_HIMinimumBiasRF_part16_v1',
        'HLT_HIMinimumBiasRF_part17_v1'
    ),
    HIMinimumBiasReducedFormat9 = cms.vstring(
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part18_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part19_v1',
        'HLT_HIMinimumBiasRF_part18_v1',
        'HLT_HIMinimumBiasRF_part19_v1'
    ),
    HINCaloJets = cms.vstring(
        'HLT_AK4CaloJet100_v10',
        'HLT_AK4CaloJet120_v9',
        'HLT_AK4CaloJet30_v11',
        'HLT_AK4CaloJet40_v10',
        'HLT_AK4CaloJet50_v10',
        'HLT_AK4CaloJet80_v10'
    ),
    HINPFJets = cms.vstring(
        'HLT_AK4PFJet100_v19',
        'HLT_AK4PFJet120_v18',
        'HLT_AK4PFJet30_v19',
        'HLT_AK4PFJet50_v19',
        'HLT_AK4PFJet80_v19'
    ),
    HIOnlineMonitor = cms.vstring(
        'HLT_HICentralityVeto_v1',
        'HLT_HICsAK4PFJet60Eta1p5_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt20_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt20_v1',
        'HLT_HIEle15Gsf_v1',
        'HLT_HIGEDPhoton10_v1',
        'HLT_HIHcalNZS_v1',
        'HLT_HIHcalPhiSym_v1',
        'HLT_HIIslandPhoton10_Eta2p4_v1',
        'HLT_HIL1DoubleMu10_v1',
        'HLT_HIL2_L1DoubleMu10_v1',
        'HLT_HIL3DoubleMuOpen_JpsiPsi_v1',
        'HLT_HIL3_L1DoubleMu10_v1',
        'HLT_HILcPPTrackingGlobal_Dpt20_v1',
        'HLT_HIPhysics_v1',
        'HLT_HIPuAK4CaloJet40Eta5p1_v1',
        'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p75_v1',
        'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p4_v1',
        'HLT_HIRandom_v1',
        'HLT_HIUPC_NotMBHF2OR_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_NotMBHF2OR_BptxAND_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2AND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_ZeroBias_SinglePixelTrack_v1'
    ),
    HISingleMuon = cms.vstring(
        'HLT_HIL1MuOpen_Centrality_70_100_v1',
        'HLT_HIL1MuOpen_Centrality_80_100_v1',
        'HLT_HIL2Mu3_NHitQ15_v1',
        'HLT_HIL2Mu5_NHitQ15_v1',
        'HLT_HIL2Mu7_NHitQ15_v1',
        'HLT_HIL3Mu12_v1',
        'HLT_HIL3Mu15_v1',
        'HLT_HIL3Mu20_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIL3Mu3_NHitQ10_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIL3Mu5_NHitQ10_v1',
        'HLT_HIL3Mu7_NHitQ10_v1'
    ),
    HITrackerNZS = cms.vstring('HLT_HIPhysicsForZS_v1'),
    HIZeroBias1 = cms.vstring('HLT_HIZeroBias_part0_v6'),
    HIZeroBias10 = cms.vstring('HLT_HIZeroBias_part9_v6'),
    HIZeroBias11 = cms.vstring('HLT_HIZeroBias_part10_v6'),
    HIZeroBias12 = cms.vstring('HLT_HIZeroBias_part11_v6'),
    HIZeroBias2 = cms.vstring('HLT_HIZeroBias_part1_v6'),
    HIZeroBias3 = cms.vstring('HLT_HIZeroBias_part2_v6'),
    HIZeroBias4 = cms.vstring('HLT_HIZeroBias_part3_v6'),
    HIZeroBias5 = cms.vstring('HLT_HIZeroBias_part4_v6'),
    HIZeroBias6 = cms.vstring('HLT_HIZeroBias_part5_v6'),
    HIZeroBias7 = cms.vstring('HLT_HIZeroBias_part6_v6'),
    HIZeroBias8 = cms.vstring('HLT_HIZeroBias_part7_v6'),
    HIZeroBias9 = cms.vstring('HLT_HIZeroBias_part8_v6'),
    HLTMonitor = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Ele32_WPTight_Gsf_v15',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT550_DisplacedDijet60_Inclusive_v13',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v1',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v8',
        'HLT_PFHT510_v17',
        'HLT_PFJet260_v20',
        'HLT_PFJet320_v20',
        'HLT_PFMET130_PFMHT130_IDTight_v20',
        'HLT_PFMET140_PFMHT140_IDTight_v20'
    ),
    HLTPhysics = cms.vstring(
        'HLT_L1FatEvents_v2',
        'HLT_Physics_v7'
    ),
    HcalNZS = cms.vstring(
        'HLT_HcalNZS_v13',
        'HLT_HcalPhiSym_v15'
    ),
    HeavyFlavor = cms.vstring(
        'HLT_DmesonPPTrackingGlobal_Dpt15ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt20ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt30ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt40ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt50ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt60ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt8ForPPRef_v11'
    ),
    HighEGJet = cms.vstring(),
    HighMultiplicity = cms.vstring(
        'HLT_PixelTracks_Multiplicity110ForPPRef_v5',
        'HLT_PixelTracks_Multiplicity135ForPPRef_v5',
        'HLT_PixelTracks_Multiplicity160ForPPRef_v5',
        'HLT_PixelTracks_Multiplicity60ForPPRef_v5',
        'HLT_PixelTracks_Multiplicity85ForPPRef_v5'
    ),
    HighMultiplicityEOF = cms.vstring(),
    HighPtJet80 = cms.vstring(
        'HLT_AK4CaloJet100_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet100_Jet35_Eta0p7ForPPRef_v9',
        'HLT_AK4CaloJet100_Jet35_Eta1p1ForPPRef_v9',
        'HLT_AK4CaloJet110_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet120_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet150ForPPRef_v9',
        'HLT_AK4CaloJet80_45_45_Eta2p1ForPPRef_v9',
        'HLT_AK4CaloJet80_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet80_Jet35_Eta0p7ForPPRef_v9',
        'HLT_AK4CaloJet80_Jet35_Eta1p1ForPPRef_v9',
        'HLT_AK4PFJet100_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet110_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet120_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet80_Eta5p1ForPPRef_v16'
    ),
    HighPtLowerJets = cms.vstring(
        'HLT_AK4CaloJet40_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet60_Eta5p1ForPPRef_v9',
        'HLT_AK4PFJet40_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet60_Eta5p1ForPPRef_v16'
    ),
    HighPtLowerPhotons = cms.vstring(
        'HLT_SinglePhoton10_Eta3p1ForPPRef_v8',
        'HLT_SinglePhoton15_Eta3p1ForPPRef_v9',
        'HLT_SinglePhoton20_Eta3p1ForPPRef_v9'
    ),
    HighPtPhoton30AndZ = cms.vstring(
        'HLT_SinglePhoton30_Eta3p1ForPPRef_v9',
        'HLT_SinglePhoton40_Eta3p1ForPPRef_v8',
        'HLT_SinglePhoton50_Eta3p1ForPPRef_v8',
        'HLT_SinglePhoton60_Eta3p1ForPPRef_v8'
    ),
    IsolatedBunch = cms.vstring('HLT_HcalIsolatedbunch_v5'),
    JetHT = cms.vstring(
        'HLT_AK4PFBJetBCSV60_Eta2p1ForPPRef_v16',
        'HLT_AK4PFBJetBCSV80_Eta2p1ForPPRef_v16',
        'HLT_AK4PFBJetBSSV60_Eta2p1ForPPRef_v16',
        'HLT_AK4PFBJetBSSV80_Eta2p1ForPPRef_v16',
        'HLT_AK4PFDJet60_Eta2p1ForPPRef_v16',
        'HLT_AK4PFDJet80_Eta2p1ForPPRef_v16',
        'HLT_AK8PFHT750_TrimMass50_v12',
        'HLT_AK8PFHT800_TrimMass50_v12',
        'HLT_AK8PFHT850_TrimMass50_v11',
        'HLT_AK8PFHT900_TrimMass50_v11',
        'HLT_AK8PFJet140_v15',
        'HLT_AK8PFJet15_v3',
        'HLT_AK8PFJet200_v15',
        'HLT_AK8PFJet25_v3',
        'HLT_AK8PFJet260_v16',
        'HLT_AK8PFJet320_v16',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p1_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_p02_v3',
        'HLT_AK8PFJet360_TrimMass30_v18',
        'HLT_AK8PFJet380_TrimMass30_v11',
        'HLT_AK8PFJet400_TrimMass30_v12',
        'HLT_AK8PFJet400_v16',
        'HLT_AK8PFJet40_v16',
        'HLT_AK8PFJet420_TrimMass30_v11',
        'HLT_AK8PFJet450_v16',
        'HLT_AK8PFJet500_v16',
        'HLT_AK8PFJet550_v11',
        'HLT_AK8PFJet60_v15',
        'HLT_AK8PFJet80_v15',
        'HLT_AK8PFJetFwd140_v14',
        'HLT_AK8PFJetFwd15_v3',
        'HLT_AK8PFJetFwd200_v14',
        'HLT_AK8PFJetFwd25_v3',
        'HLT_AK8PFJetFwd260_v15',
        'HLT_AK8PFJetFwd320_v15',
        'HLT_AK8PFJetFwd400_v15',
        'HLT_AK8PFJetFwd40_v15',
        'HLT_AK8PFJetFwd450_v15',
        'HLT_AK8PFJetFwd500_v15',
        'HLT_AK8PFJetFwd60_v14',
        'HLT_AK8PFJetFwd80_v14',
        'HLT_CaloJet500_NoJetID_v12',
        'HLT_CaloJet550_NoJetID_v7',
        'HLT_DiPFJetAve100_HFJEC_v16',
        'HLT_DiPFJetAve140_v13',
        'HLT_DiPFJetAve160_HFJEC_v16',
        'HLT_DiPFJetAve200_v13',
        'HLT_DiPFJetAve220_HFJEC_v16',
        'HLT_DiPFJetAve260_v14',
        'HLT_DiPFJetAve300_HFJEC_v16',
        'HLT_DiPFJetAve320_v14',
        'HLT_DiPFJetAve400_v14',
        'HLT_DiPFJetAve40_v14',
        'HLT_DiPFJetAve500_v14',
        'HLT_DiPFJetAve60_HFJEC_v15',
        'HLT_DiPFJetAve60_v14',
        'HLT_DiPFJetAve80_HFJEC_v16',
        'HLT_DiPFJetAve80_v13',
        'HLT_DoublePFJets100_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets200_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets350_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets40_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets62MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_PFHT1050_v18',
        'HLT_PFHT180_v17',
        'HLT_PFHT250_v17',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v9',
        'HLT_PFHT350MinPFJet15_v9',
        'HLT_PFHT350_v19',
        'HLT_PFHT370_v17',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v8',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v8',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v8',
        'HLT_PFHT400_SixPFJet32_v8',
        'HLT_PFHT430_v17',
        'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v7',
        'HLT_PFHT450_SixPFJet36_v7',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v12',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v12',
        'HLT_PFHT510_v17',
        'HLT_PFHT590_v17',
        'HLT_PFHT680_v17',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v12',
        'HLT_PFHT700_PFMET95_PFMHT95_IDTight_v12',
        'HLT_PFHT780_v17',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v12',
        'HLT_PFHT800_PFMET85_PFMHT85_IDTight_v12',
        'HLT_PFHT890_v17',
        'HLT_PFJet140_v19',
        'HLT_PFJet15_v3',
        'HLT_PFJet200_v19',
        'HLT_PFJet25_v3',
        'HLT_PFJet260_v20',
        'HLT_PFJet320_v20',
        'HLT_PFJet400_v20',
        'HLT_PFJet40_v21',
        'HLT_PFJet450_v21',
        'HLT_PFJet500_v21',
        'HLT_PFJet550_v11',
        'HLT_PFJet60_v21',
        'HLT_PFJet80_v20',
        'HLT_PFJetFwd140_v18',
        'HLT_PFJetFwd15_v3',
        'HLT_PFJetFwd200_v18',
        'HLT_PFJetFwd25_v3',
        'HLT_PFJetFwd260_v19',
        'HLT_PFJetFwd320_v19',
        'HLT_PFJetFwd400_v19',
        'HLT_PFJetFwd40_v19',
        'HLT_PFJetFwd450_v19',
        'HLT_PFJetFwd500_v19',
        'HLT_PFJetFwd60_v19',
        'HLT_PFJetFwd80_v18',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v5',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v5',
        'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet98_83_71_15_v5',
        'HLT_Rsq0p35_v15',
        'HLT_Rsq0p40_v15',
        'HLT_RsqMR300_Rsq0p09_MR200_4jet_v15',
        'HLT_RsqMR300_Rsq0p09_MR200_v15',
        'HLT_RsqMR320_Rsq0p09_MR200_4jet_v15',
        'HLT_RsqMR320_Rsq0p09_MR200_v15',
        'HLT_SingleJet30_Mu12_SinglePFJet40_v11'
    ),
    JetsTOTEM = cms.vstring(
        'HLT_L1DoubleJetANDTotem_v1',
        'HLT_L1DoubleJet_gap_v1',
        'HLT_L1DoubleJet_v1'
    ),
    L1Accept = cms.vstring(
        'DST_Physics_v7',
        'DST_ZeroBias_v2'
    ),
    L1MinimumBias = cms.vstring(
        'HLT_L1MinimumBiasHF1AND_v4',
        'HLT_L1MinimumBiasHF1OR_v4',
        'HLT_L1MinimumBiasHF2AND_v4',
        'HLT_L1MinimumBiasHF2ORNoBptxGating_v5',
        'HLT_L1MinimumBiasHF2OR_v4',
        'HLT_L1MinimumBiasHF_OR_v3'
    ),
    LowEGJet = cms.vstring(),
    MET = cms.vstring(
        'HLT_CaloMET100_NotCleaned_v4',
        'HLT_CaloMET110_NotCleaned_v4',
        'HLT_CaloMET250_NotCleaned_v4',
        'HLT_CaloMET300_NotCleaned_v4',
        'HLT_CaloMET350_NotCleaned_v4',
        'HLT_CaloMET80_NotCleaned_v4',
        'HLT_CaloMET90_NotCleaned_v4',
        'HLT_CaloMHT90_v4',
        'HLT_DiJet110_35_Mjj650_PFMET110_v9',
        'HLT_DiJet110_35_Mjj650_PFMET120_v9',
        'HLT_DiJet110_35_Mjj650_PFMET130_v9',
        'HLT_L1ETMHadSeeds_v2',
        'HLT_MET105_IsoTrk50_v9',
        'HLT_MET120_IsoTrk50_v9',
        'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v20',
        'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v20',
        'HLT_MonoCentralPFJet80_PFMETNoMu130_PFMHTNoMu130_IDTight_v19',
        'HLT_MonoCentralPFJet80_PFMETNoMu140_PFMHTNoMu140_IDTight_v19',
        'HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET100_PFMHT100_IDTight_PFHT60_v9',
        'HLT_PFMET110_PFMHT110_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET110_PFMHT110_IDTight_v20',
        'HLT_PFMET120_PFMHT120_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v9',
        'HLT_PFMET120_PFMHT120_IDTight_v20',
        'HLT_PFMET130_PFMHT130_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET130_PFMHT130_IDTight_v20',
        'HLT_PFMET140_PFMHT140_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET140_PFMHT140_IDTight_v20',
        'HLT_PFMET200_BeamHaloCleaned_v9',
        'HLT_PFMET200_NotCleaned_v9',
        'HLT_PFMET250_NotCleaned_v9',
        'HLT_PFMET300_NotCleaned_v9',
        'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_PFHT60_v9',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v20',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v9',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v20',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v19',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v19',
        'HLT_PFMETTypeOne100_PFMHT100_IDTight_PFHT60_v9',
        'HLT_PFMETTypeOne110_PFMHT110_IDTight_v12',
        'HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v9',
        'HLT_PFMETTypeOne120_PFMHT120_IDTight_v12',
        'HLT_PFMETTypeOne130_PFMHT130_IDTight_v12',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v11',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v9'
    ),
    MinBiasTOTEM = cms.vstring('HLT_L1TOTEM1_MinBias_v4'),
    MinimumBias = cms.vstring(
        'HLT_CaloJet10_NoJetID_v3',
        'HLT_CaloJet20_NoJetID_v3',
        'HLT_CaloJet50_NoJetID_v3',
        'HLT_L1DoubleJetC50_v2',
        'HLT_L1EXT_HCAL_LaserMon1_v1',
        'HLT_L1EXT_HCAL_LaserMon4_v1',
        'HLT_L1SingleEG10_v2',
        'HLT_L1SingleEG15_v2',
        'HLT_L1SingleEG18_v1',
        'HLT_L1SingleJet10erHE_v1',
        'HLT_L1SingleJet12erHE_v1',
        'HLT_L1SingleJet16_v1',
        'HLT_L1SingleJet200_v1',
        'HLT_L1SingleJet20_v1',
        'HLT_L1SingleJet35_v1',
        'HLT_L1SingleJet8erHE_v1'
    ),
    MinimumBias0 = cms.vstring('HLT_L1MinimumBiasHF_OR_part0_v1'),
    MinimumBias1 = cms.vstring('HLT_L1MinimumBiasHF_OR_part1_v1'),
    MinimumBias2 = cms.vstring('HLT_L1MinimumBiasHF_OR_part2_v1'),
    MinimumBias3 = cms.vstring('HLT_L1MinimumBiasHF_OR_part3_v1'),
    MinimumBias4 = cms.vstring('HLT_L1MinimumBiasHF_OR_part4_v1'),
    MinimumBias5 = cms.vstring('HLT_L1MinimumBiasHF_OR_part5_v1'),
    MinimumBias6 = cms.vstring('HLT_L1MinimumBiasHF_OR_part6_v1'),
    MinimumBias7 = cms.vstring('HLT_L1MinimumBiasHF_OR_part7_v1'),
    MinimumBias8 = cms.vstring('HLT_L1MinimumBiasHF_OR_part8_v1'),
    MinimumBias9 = cms.vstring('HLT_L1MinimumBiasHF_OR_part9_v1'),
    MonteCarlo = cms.vstring(
        'MC_AK4CaloJetsFromPV_v8',
        'MC_AK4CaloJets_v9',
        'MC_AK4PFJets_v17',
        'MC_AK8CaloHT_v8',
        'MC_AK8PFHT_v16',
        'MC_AK8PFJets_v17',
        'MC_AK8TrimPFJets_v17',
        'MC_CaloBTagDeepCSV_v8',
        'MC_CaloHT_v8',
        'MC_CaloMET_JetIdCleaned_v9',
        'MC_CaloMET_v8',
        'MC_CaloMHT_v8',
        'MC_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_v13',
        'MC_DoubleEle5_CaloIdL_MW_v15',
        'MC_DoubleGlbTrkMu_TrkIsoVVL_DZ_v12',
        'MC_DoubleMuNoFiltersNoVtx_v7',
        'MC_DoubleMu_TrkIsoVVL_DZ_v11',
        'MC_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'MC_Ele5_WPTight_Gsf_v8',
        'MC_IsoMu_v15',
        'MC_IsoTkMu15_v12',
        'MC_PFBTagDeepCSV_v10',
        'MC_PFHT_v16',
        'MC_PFMET_v17',
        'MC_PFMHT_v16',
        'MC_ReducedIterativeTracking_v12'
    ),
    MuOnia = cms.vstring(
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v8',
        'HLT_Dimuon0_Upsilon_L1_4p5_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v7',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v9',
        'HLT_Dimuon0_Upsilon_L1_5M_v8',
        'HLT_Dimuon0_Upsilon_L1_5_v9',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v6',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v6',
        'HLT_Dimuon0_Upsilon_NoVertexing_v7',
        'HLT_Dimuon12_Upsilon_y1p4_v2',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v7',
        'HLT_Dimuon24_Phi_noCorrL1_v6',
        'HLT_Dimuon24_Upsilon_noCorrL1_v6',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v4',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v4',
        'HLT_Mu20_TkMu0_Phi_v8',
        'HLT_Mu25_TkMu0_Onia_v8',
        'HLT_Mu25_TkMu0_Phi_v8',
        'HLT_Mu30_TkMu0_Upsilon_v1',
        'HLT_Mu7p5_L2Mu2_Upsilon_v10',
        'HLT_Mu7p5_Track2_Upsilon_v11',
        'HLT_Mu7p5_Track3p5_Upsilon_v11',
        'HLT_Mu7p5_Track7_Upsilon_v11',
        'HLT_Trimuon2_Upsilon5_Muon_NoL1Mass_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v5',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v3'
    ),
    MuPlusX = cms.vstring(
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1ForPPRef_v11',
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1ForPPRef_v11',
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1ForPPRef_v11',
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1ForPPRef_v11'
    ),
    MuonEG = cms.vstring(
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v17',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v17',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v17',
        'HLT_DoubleMu20_7_Mass0to30_L1_DM4EG_v8',
        'HLT_DoubleMu20_7_Mass0to30_L1_DM4_v7',
        'HLT_DoubleMu20_7_Mass0to30_Photon23_v8',
        'HLT_Mu12_DoublePhoton20_v5',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v7',
        'HLT_Mu17_Photon30_IsoCaloId_v6',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v7',
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v10',
        'HLT_Mu27_Ele37_CaloIdL_MW_v5',
        'HLT_Mu37_Ele27_CaloIdL_MW_v5',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v1',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v1',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v5',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v5',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v18',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v18',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v19',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v19',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v13',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v11'
    ),
    MuonEGammaTOTEM = cms.vstring(
        'HLT_L1DoubleMu_v1',
        'HLT_L1SingleMu_v1'
    ),
    NoBPTX = cms.vstring(
        'HLT_CDC_L2cosmic_10_er1p0_v1',
        'HLT_CDC_L2cosmic_5p5_er1p0_v1',
        'HLT_L1BptxXOR_v1',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v5',
        'HLT_L2Mu10_NoVertex_NoBPTX_v6',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v5',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v4',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v6',
        'HLT_UncorrectedJetE30_NoBPTX_v6',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v6',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v6'
    ),
    OnlineMonitor = cms.vstring( (
        'HLT_AK4CaloJet100_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet100_Jet35_Eta0p7ForPPRef_v9',
        'HLT_AK4CaloJet100_Jet35_Eta1p1ForPPRef_v9',
        'HLT_AK4CaloJet100_v10',
        'HLT_AK4CaloJet110_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet120_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet120_v9',
        'HLT_AK4CaloJet150ForPPRef_v9',
        'HLT_AK4CaloJet30_v11',
        'HLT_AK4CaloJet40_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet40_v10',
        'HLT_AK4CaloJet50_v10',
        'HLT_AK4CaloJet60_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet80_45_45_Eta2p1ForPPRef_v9',
        'HLT_AK4CaloJet80_Eta5p1ForPPRef_v9',
        'HLT_AK4CaloJet80_Jet35_Eta0p7ForPPRef_v9',
        'HLT_AK4CaloJet80_Jet35_Eta1p1ForPPRef_v9',
        'HLT_AK4CaloJet80_v10',
        'HLT_AK4PFBJetBCSV60_Eta2p1ForPPRef_v16',
        'HLT_AK4PFBJetBCSV80_Eta2p1ForPPRef_v16',
        'HLT_AK4PFBJetBSSV60_Eta2p1ForPPRef_v16',
        'HLT_AK4PFBJetBSSV80_Eta2p1ForPPRef_v16',
        'HLT_AK4PFDJet60_Eta2p1ForPPRef_v16',
        'HLT_AK4PFDJet80_Eta2p1ForPPRef_v16',
        'HLT_AK4PFJet100_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet100_v19',
        'HLT_AK4PFJet110_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet120_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet120_v18',
        'HLT_AK4PFJet30_v19',
        'HLT_AK4PFJet40_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet50_v19',
        'HLT_AK4PFJet60_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet80_Eta5p1ForPPRef_v16',
        'HLT_AK4PFJet80_v19',
        'HLT_AK8PFHT750_TrimMass50_v12',
        'HLT_AK8PFHT800_TrimMass50_v12',
        'HLT_AK8PFHT850_TrimMass50_v11',
        'HLT_AK8PFHT900_TrimMass50_v11',
        'HLT_AK8PFJet140_v15',
        'HLT_AK8PFJet15_v3',
        'HLT_AK8PFJet200_v15',
        'HLT_AK8PFJet25_v3',
        'HLT_AK8PFJet260_v16',
        'HLT_AK8PFJet320_v16',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p1_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_p02_v3',
        'HLT_AK8PFJet360_TrimMass30_v18',
        'HLT_AK8PFJet380_TrimMass30_v11',
        'HLT_AK8PFJet400_TrimMass30_v12',
        'HLT_AK8PFJet400_v16',
        'HLT_AK8PFJet40_v16',
        'HLT_AK8PFJet420_TrimMass30_v11',
        'HLT_AK8PFJet450_v16',
        'HLT_AK8PFJet500_v16',
        'HLT_AK8PFJet550_v11',
        'HLT_AK8PFJet60_v15',
        'HLT_AK8PFJet80_v15',
        'HLT_AK8PFJetFwd140_v14',
        'HLT_AK8PFJetFwd15_v3',
        'HLT_AK8PFJetFwd200_v14',
        'HLT_AK8PFJetFwd25_v3',
        'HLT_AK8PFJetFwd260_v15',
        'HLT_AK8PFJetFwd320_v15',
        'HLT_AK8PFJetFwd400_v15',
        'HLT_AK8PFJetFwd40_v15',
        'HLT_AK8PFJetFwd450_v15',
        'HLT_AK8PFJetFwd500_v15',
        'HLT_AK8PFJetFwd60_v14',
        'HLT_AK8PFJetFwd80_v14',
        'HLT_BTagMu_AK4DiJet110_Mu5_v13',
        'HLT_BTagMu_AK4DiJet170_Mu5_v12',
        'HLT_BTagMu_AK4DiJet20_Mu5_v13',
        'HLT_BTagMu_AK4DiJet40_Mu5_v13',
        'HLT_BTagMu_AK4DiJet70_Mu5_v13',
        'HLT_BTagMu_AK4Jet300_Mu5_v12',
        'HLT_BTagMu_AK8DiJet170_Mu5_v9',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v2',
        'HLT_BTagMu_AK8Jet300_Mu5_v12',
        'HLT_CDC_L2cosmic_10_er1p0_v1',
        'HLT_CDC_L2cosmic_5p5_er1p0_v1',
        'HLT_CaloJet10_NoJetID_v3',
        'HLT_CaloJet20_NoJetID_v3',
        'HLT_CaloJet500_NoJetID_v12',
        'HLT_CaloJet50_NoJetID_v3',
        'HLT_CaloJet550_NoJetID_v7',
        'HLT_CaloMET100_NotCleaned_v4',
        'HLT_CaloMET110_NotCleaned_v4',
        'HLT_CaloMET250_NotCleaned_v4',
        'HLT_CaloMET300_NotCleaned_v4',
        'HLT_CaloMET350_NotCleaned_v4',
        'HLT_CaloMET80_NotCleaned_v4',
        'HLT_CaloMET90_NotCleaned_v4',
        'HLT_CaloMHT90_v4',
        'HLT_DQMPixels_SingleMuOpen_v1',
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v4',
        'HLT_DiJet110_35_Mjj650_PFMET110_v9',
        'HLT_DiJet110_35_Mjj650_PFMET120_v9',
        'HLT_DiJet110_35_Mjj650_PFMET130_v9',
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v17',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v17',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v17',
        'HLT_DiPFJet15_FBEta3_NoCaloMatched_v17',
        'HLT_DiPFJet15_NoCaloMatched_v16',
        'HLT_DiPFJet25_FBEta3_NoCaloMatched_v17',
        'HLT_DiPFJet25_NoCaloMatched_v16',
        'HLT_DiPFJetAve100_HFJEC_v16',
        'HLT_DiPFJetAve140_v13',
        'HLT_DiPFJetAve15_HFJEC_v17',
        'HLT_DiPFJetAve160_HFJEC_v16',
        'HLT_DiPFJetAve200_v13',
        'HLT_DiPFJetAve220_HFJEC_v16',
        'HLT_DiPFJetAve25_HFJEC_v17',
        'HLT_DiPFJetAve260_v14',
        'HLT_DiPFJetAve300_HFJEC_v16',
        'HLT_DiPFJetAve320_v14',
        'HLT_DiPFJetAve35_HFJEC_v17',
        'HLT_DiPFJetAve400_v14',
        'HLT_DiPFJetAve40_v14',
        'HLT_DiPFJetAve500_v14',
        'HLT_DiPFJetAve60_HFJEC_v15',
        'HLT_DiPFJetAve60_v14',
        'HLT_DiPFJetAve80_HFJEC_v16',
        'HLT_DiPFJetAve80_v13',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v13',
        'HLT_Dimuon0_Jpsi3p5_Muon2_v5',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v7',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_v8',
        'HLT_Dimuon0_Jpsi_v8',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v7',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v8',
        'HLT_Dimuon0_LowMass_L1_4R_v7',
        'HLT_Dimuon0_LowMass_L1_4_v8',
        'HLT_Dimuon0_LowMass_L1_TM530_v6',
        'HLT_Dimuon0_LowMass_v8',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v8',
        'HLT_Dimuon0_Upsilon_L1_4p5_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v7',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v9',
        'HLT_Dimuon0_Upsilon_L1_5M_v8',
        'HLT_Dimuon0_Upsilon_L1_5_v9',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v6',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v6',
        'HLT_Dimuon0_Upsilon_NoVertexing_v7',
        'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v7',
        'HLT_Dimuon12_Upsilon_y1p4_v2',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v7',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v6',
        'HLT_Dimuon18_PsiPrime_v14',
        'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v7',
        'HLT_Dimuon24_Phi_noCorrL1_v6',
        'HLT_Dimuon24_Upsilon_noCorrL1_v6',
        'HLT_Dimuon25_Jpsi_noCorrL1_v6',
        'HLT_Dimuon25_Jpsi_v14',
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_NoPixelVeto_Mass55_v13',
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_PixelVeto_Mass55_v15',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto_Mass55_v2',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto_v2',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v13',
        'HLT_DmesonPPTrackingGlobal_Dpt15ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt20ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt30ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt40ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt50ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt60ForPPRef_v11',
        'HLT_DmesonPPTrackingGlobal_Dpt8ForPPRef_v11',
        'HLT_DoubleEle25_CaloIdL_MW_v4',
        'HLT_DoubleEle27_CaloIdL_MW_v4',
        'HLT_DoubleEle33_CaloIdL_MW_v17',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v20',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v20',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_NoL2Matched_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_NoL2Matched_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_NoL2Matched_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_NoL2Matched_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v2',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v2',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v2',
        'HLT_DoubleL2Mu50_v2',
        'HLT_DoubleMu20_7_Mass0to30_L1_DM4EG_v8',
        'HLT_DoubleMu20_7_Mass0to30_L1_DM4_v7',
        'HLT_DoubleMu20_7_Mass0to30_Photon23_v8',
        'HLT_DoubleMu2_Jpsi_DoubleTkMu0_Phi_v5',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v6',
        'HLT_DoubleMu33NoFiltersNoVtxDisplaced_v1',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v10',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v10',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v10',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v4',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v4',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_v12',
        'HLT_DoubleMu40NoFiltersNoVtxDisplaced_v1',
        'HLT_DoubleMu43NoFiltersNoVtx_v4',
        'HLT_DoubleMu48NoFiltersNoVtx_v4',
        'HLT_DoubleMu4_3_Bs_v14',
        'HLT_DoubleMu4_3_Jpsi_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v7',
        'HLT_DoubleMu4_JpsiTrk_Displaced_v15',
        'HLT_DoubleMu4_Jpsi_Displaced_v7',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v7',
        'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v15',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v8',
        'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v15',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v4',
        'HLT_DoublePFJets100_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets200_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets350_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets40_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePhoton33_CaloIdL_v6',
        'HLT_DoublePhoton70_v6',
        'HLT_DoublePhoton85_v14',
        'HLT_ECALHT800_v10',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v14',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v7',
        'HLT_Ele145_CaloIdVT_GsfTrkIdT_v8',
        'HLT_Ele15_CaloIdL_TrackIdL_IsoVL_PFJet30_v3',
        'HLT_Ele15_Ele8_CaloIdL_TrackIdL_IsoVL_v3',
        'HLT_Ele15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v8',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v16',
        'HLT_Ele15_IsoVVVL_PFHT450_v16',
        'HLT_Ele15_IsoVVVL_PFHT600_v20',
        'HLT_Ele15_WPLoose_Gsf_v3',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v9',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v16',
        'HLT_Ele17_WPLoose_Gsf_v3',
        'HLT_Ele200_CaloIdVT_GsfTrkIdT_v8',
        'HLT_Ele20_WPLoose_Gsf_v6',
        'HLT_Ele20_WPTight_Gsf_v6',
        'HLT_Ele20_eta2p1_WPLoose_Gsf_v6',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v19',
        'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele250_CaloIdVT_GsfTrkIdT_v13',
        'HLT_Ele27_Ele37_CaloIdL_MW_v4',
        'HLT_Ele27_WPTight_Gsf_v16',
        'HLT_Ele28_HighEta_SC20_Mass55_v13',
        'HLT_Ele28_WPTight_Gsf_v1',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v13',
        'HLT_Ele300_CaloIdVT_GsfTrkIdT_v13',
        'HLT_Ele30_WPTight_Gsf_v1',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v9',
        'HLT_Ele32_WPTight_Gsf_v15',
        'HLT_Ele35_WPTight_Gsf_L1EGMT_v5',
        'HLT_Ele35_WPTight_Gsf_v9',
        'HLT_Ele38_WPTight_Gsf_v9',
        'HLT_Ele40_WPTight_Gsf_v9',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v18',
        'HLT_Ele50_IsoVVVL_PFHT450_v16',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v16',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_FullTrack18ForPPRef_v11',
        'HLT_FullTrack24ForPPRef_v11',
        'HLT_FullTrack34ForPPRef_v11',
        'HLT_FullTrack45ForPPRef_v11',
        'HLT_FullTrack53ForPPRef_v11',
        'HLT_HIL1CastorMediumJetForPPRef_v4',
        'HLT_HIL1DoubleMu0ForPPRef_v4',
        'HLT_HIL1DoubleMu10ForPPRef_v4',
        'HLT_HIL1NotBptxORForPPRef_v2',
        'HLT_HIL1UnpairedBunchBptxMinusForPPRef_v2',
        'HLT_HIL1UnpairedBunchBptxPlusForPPRef_v2',
        'HLT_HIL2DoubleMu0_NHitQForPPRef_v5',
        'HLT_HIL2Mu15ForPPRef_v6',
        'HLT_HIL2Mu20ForPPRef_v6',
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1ForPPRef_v11',
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1ForPPRef_v11',
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1ForPPRef_v11',
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1ForPPRef_v11',
        'HLT_HIL2Mu3_NHitQ10ForPPRef_v6',
        'HLT_HIL2Mu5_NHitQ10ForPPRef_v6',
        'HLT_HIL2Mu7_NHitQ10ForPPRef_v6',
        'HLT_HIL3DoubleMu0_OS_m2p5to4p5ForPPRef_v6',
        'HLT_HIL3DoubleMu0_OS_m7to14ForPPRef_v6',
        'HLT_HIL3Mu15ForPPRef_v6',
        'HLT_HIL3Mu20ForPPRef_v6',
        'HLT_HIL3Mu3_NHitQ15ForPPRef_v6',
        'HLT_HIL3Mu5_NHitQ15ForPPRef_v6',
        'HLT_HIL3Mu7_NHitQ15ForPPRef_v6',
        'HLT_HIZeroBias_part0_v6',
        'HLT_HIZeroBias_part10_v6',
        'HLT_HIZeroBias_part11_v6',
        'HLT_HIZeroBias_part1_v6',
        'HLT_HIZeroBias_part2_v6',
        'HLT_HIZeroBias_part3_v6',
        'HLT_HIZeroBias_part4_v6',
        'HLT_HIZeroBias_part5_v6',
        'HLT_HIZeroBias_part6_v6',
        'HLT_HIZeroBias_part7_v6',
        'HLT_HIZeroBias_part8_v6',
        'HLT_HIZeroBias_part9_v6',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT425_v9',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT430_DisplacedDijet60_DisplacedTrack_v13',
        'HLT_HT500_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT550_DisplacedDijet60_Inclusive_v13',
        'HLT_HT650_DisplacedDijet60_Inclusive_v13',
        'HLT_HcalIsolatedbunch_v5',
        'HLT_HcalNZS_v13',
        'HLT_HcalPhiSym_v15',
        'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v1',
        'HLT_IsoMu20_v15',
        'HLT_IsoMu24_TwoProngs35_v1',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v1',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS50_eta2p1_v1',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v1',
        'HLT_IsoMu24_eta2p1_v15',
        'HLT_IsoMu24_v13',
        'HLT_IsoMu27_v16',
        'HLT_IsoMu30_v4',
        'HLT_IsoTrackHB_v4',
        'HLT_IsoTrackHE_v4',
        'HLT_L1BptxXOR_v1',
        'HLT_L1DoubleJetANDTotem_v1',
        'HLT_L1DoubleJetC50_v2',
        'HLT_L1DoubleJet_gap_v1',
        'HLT_L1DoubleJet_v1',
        'HLT_L1DoubleMu0_v1',
        'HLT_L1DoubleMu_v1',
        'HLT_L1ETMHadSeeds_v2',
        'HLT_L1EXT_HCAL_LaserMon1_v1',
        'HLT_L1EXT_HCAL_LaserMon4_v1',
        'HLT_L1FatEvents_v2',
        'HLT_L1HFveto_v1',
        'HLT_L1MinimumBiasHF0OR_v4',
        'HLT_L1MinimumBiasHF1AND_v4',
        'HLT_L1MinimumBiasHF1OR_v4',
        'HLT_L1MinimumBiasHF2AND_v4',
        'HLT_L1MinimumBiasHF2ORNoBptxGating_v5',
        'HLT_L1MinimumBiasHF2OR_v4',
        'HLT_L1MinimumBiasHF_OR_part0_v1',
        'HLT_L1MinimumBiasHF_OR_part1_v1',
        'HLT_L1MinimumBiasHF_OR_part2_v1',
        'HLT_L1MinimumBiasHF_OR_part3_v1',
        'HLT_L1MinimumBiasHF_OR_part4_v1',
        'HLT_L1MinimumBiasHF_OR_part5_v1',
        'HLT_L1MinimumBiasHF_OR_part6_v1',
        'HLT_L1MinimumBiasHF_OR_part7_v1',
        'HLT_L1MinimumBiasHF_OR_part8_v1',
        'HLT_L1MinimumBiasHF_OR_part9_v1',
        'HLT_L1MinimumBiasHF_OR_v3',
        'HLT_L1NotBptxOR_v3',
        'HLT_L1RomanPot_part0_v1',
        'HLT_L1RomanPot_part1_v1',
        'HLT_L1RomanPot_part2_v1',
        'HLT_L1RomanPot_part3_v1',
        'HLT_L1SingleEG10_v2',
        'HLT_L1SingleEG15_v2',
        'HLT_L1SingleEG18_v1',
        'HLT_L1SingleJet10erHE_v1',
        'HLT_L1SingleJet12erHE_v1',
        'HLT_L1SingleJet16_v1',
        'HLT_L1SingleJet200_v1',
        'HLT_L1SingleJet20_v1',
        'HLT_L1SingleJet35_v1',
        'HLT_L1SingleJet8erHE_v1',
        'HLT_L1SingleMu18_v3',
        'HLT_L1SingleMu25_v2',
        'HLT_L1SingleMu3_v1',
        'HLT_L1SingleMu5_v1',
        'HLT_L1SingleMu7_v1',
        'HLT_L1SingleMuCosmics_v1',
        'HLT_L1SingleMuOpen_DT_v2',
        'HLT_L1SingleMuOpen_v2',
        'HLT_L1SingleMu_v1',
        'HLT_L1TOTEM1_MinBias_v4',
        'HLT_L1TOTEM2_ZeroBias_v4',
        'HLT_L1TOTEM_3_v1',
        'HLT_L1UnpairedBunchBptxMinus_v2',
        'HLT_L1UnpairedBunchBptxPlus_v2',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v2',
        'HLT_L1_DoubleJet30_Mass_Min400_Mu10_v1',
        'HLT_L2DoubleMu23_NoVertex_v2',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v5',
        'HLT_L2Mu10_NoVertex_NoBPTX_v6',
        'HLT_L2Mu10_v7',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v5',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v4',
        'HLT_L2Mu50_v2',
        'HLT_MET105_IsoTrk50_v9',
        'HLT_MET120_IsoTrk50_v9',
        'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau200HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau220HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET100_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET110_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET120_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v12',
        'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v20',
        'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v20',
        'HLT_MonoCentralPFJet80_PFMETNoMu130_PFMHTNoMu130_IDTight_v19',
        'HLT_MonoCentralPFJet80_PFMETNoMu140_PFMHTNoMu140_IDTight_v19',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v15',
        'HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets62MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePhoton20_v5',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v7',
        'HLT_Mu12_v3',
        'HLT_Mu15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v8',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v15',
        'HLT_Mu15_IsoVVVL_PFHT450_v15',
        'HLT_Mu15_IsoVVVL_PFHT600_v19',
        'HLT_Mu15_v3',
        'HLT_Mu17_Photon30_IsoCaloId_v6',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v14',
        'HLT_Mu17_TrkIsoVVL_v13',
        'HLT_Mu17_v13',
        'HLT_Mu18_Mu9_DZ_v4',
        'HLT_Mu18_Mu9_SameSign_DZ_v4',
        'HLT_Mu18_Mu9_SameSign_v4',
        'HLT_Mu18_Mu9_v4',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v3',
        'HLT_Mu19_TrkIsoVVL_v4',
        'HLT_Mu19_v4',
        'HLT_Mu20_Mu10_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_v4',
        'HLT_Mu20_Mu10_v4',
        'HLT_Mu20_TkMu0_Phi_v8',
        'HLT_Mu20_v12',
        'HLT_Mu23_Mu12_DZ_v4',
        'HLT_Mu23_Mu12_SameSign_DZ_v4',
        'HLT_Mu23_Mu12_SameSign_v4',
        'HLT_Mu23_Mu12_v4',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v7',
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v10',
        'HLT_Mu25_TkMu0_Onia_v8',
        'HLT_Mu25_TkMu0_Phi_v8',
        'HLT_Mu27_Ele37_CaloIdL_MW_v5',
        'HLT_Mu27_v13',
        'HLT_Mu30_TkMu0_Psi_v1',
        'HLT_Mu30_TkMu0_Upsilon_v1',
        'HLT_Mu37_Ele27_CaloIdL_MW_v5',
        'HLT_Mu37_TkMu27_v5',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v1',
        'HLT_Mu3_PFJet40_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET70_PFMHT70_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu70_PFMHTNoMu70_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v2',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v1',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v5',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v5',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v15',
        'HLT_Mu50_IsoVVVL_PFHT450_v15',
        'HLT_Mu50_v13',
        'HLT_Mu55_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v10',
        'HLT_Mu7p5_L2Mu2_Upsilon_v10',
        'HLT_Mu7p5_Track2_Jpsi_v11',
        'HLT_Mu7p5_Track2_Upsilon_v11',
        'HLT_Mu7p5_Track3p5_Jpsi_v11',
        'HLT_Mu7p5_Track3p5_Upsilon_v11',
        'HLT_Mu7p5_Track7_Jpsi_v11',
        'HLT_Mu7p5_Track7_Upsilon_v11',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v18',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v18',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v19',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v19',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v16',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v13',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v11',
        'HLT_Mu8_TrkIsoVVL_v12',
        'HLT_Mu8_v12',
        'HLT_OldMu100_v3',
        'HLT_PFHT1050_v18',
        'HLT_PFHT180_v17',
        'HLT_PFHT250_v17',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v9',
        'HLT_PFHT350MinPFJet15_v9',
        'HLT_PFHT350_v19',
        'HLT_PFHT370_v17',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v8',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v8',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v8',
        'HLT_PFHT400_SixPFJet32_v8',
        'HLT_PFHT430_v17',
        'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v7',
        'HLT_PFHT450_SixPFJet36_v7',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v12',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v12',
        'HLT_PFHT510_v17',
        'HLT_PFHT590_v17',
        'HLT_PFHT680_v17',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v12',
        'HLT_PFHT700_PFMET95_PFMHT95_IDTight_v12',
        'HLT_PFHT780_v17',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v12',
        'HLT_PFHT800_PFMET85_PFMHT85_IDTight_v12',
        'HLT_PFHT890_v17',
        'HLT_PFJet140_v19',
        'HLT_PFJet15_v3',
        'HLT_PFJet200_v19',
        'HLT_PFJet25_v3',
        'HLT_PFJet260_v20',
        'HLT_PFJet320_v20',
        'HLT_PFJet400_v20',
        'HLT_PFJet40_v21',
        'HLT_PFJet450_v21',
        'HLT_PFJet500_v21',
        'HLT_PFJet550_v11',
        'HLT_PFJet60_v21',
        'HLT_PFJet80_v20',
        'HLT_PFJetFwd140_v18',
        'HLT_PFJetFwd15_v3',
        'HLT_PFJetFwd200_v18',
        'HLT_PFJetFwd25_v3',
        'HLT_PFJetFwd260_v19',
        'HLT_PFJetFwd320_v19',
        'HLT_PFJetFwd400_v19',
        'HLT_PFJetFwd40_v19',
        'HLT_PFJetFwd450_v19',
        'HLT_PFJetFwd500_v19',
        'HLT_PFJetFwd60_v19',
        'HLT_PFJetFwd80_v18',
        'HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET100_PFMHT100_IDTight_PFHT60_v9',
        'HLT_PFMET110_PFMHT110_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET110_PFMHT110_IDTight_v20',
        'HLT_PFMET120_PFMHT120_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v9',
        'HLT_PFMET120_PFMHT120_IDTight_v20',
        'HLT_PFMET130_PFMHT130_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET130_PFMHT130_IDTight_v20',
        'HLT_PFMET140_PFMHT140_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET140_PFMHT140_IDTight_v20',
        'HLT_PFMET200_BeamHaloCleaned_v9',
        'HLT_PFMET200_NotCleaned_v9',
        'HLT_PFMET250_NotCleaned_v9',
        'HLT_PFMET300_NotCleaned_v9',
        'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_PFHT60_v9',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v20',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v9',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v20',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v19',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v19',
        'HLT_PFMETTypeOne100_PFMHT100_IDTight_PFHT60_v9',
        'HLT_PFMETTypeOne110_PFMHT110_IDTight_v12',
        'HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v9',
        'HLT_PFMETTypeOne120_PFMHT120_IDTight_v12',
        'HLT_PFMETTypeOne130_PFMHT130_IDTight_v12',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v11',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v9',
        'HLT_Photon100EBHE10_v2',
        'HLT_Photon100EB_TightID_TightIso_v2',
        'HLT_Photon100EEHE10_v2',
        'HLT_Photon100EE_TightID_TightIso_v2',
        'HLT_Photon110EB_TightID_TightIso_v2',
        'HLT_Photon120EB_TightID_TightIso_v2',
        'HLT_Photon120_R9Id90_HE10_IsoM_v14',
        'HLT_Photon120_v13',
        'HLT_Photon150_v6',
        'HLT_Photon165_R9Id90_HE10_IsoM_v15',
        'HLT_Photon175_v14',
        'HLT_Photon200_v13',
        'HLT_Photon20_HoverELoose_v10',
        'HLT_Photon20_v2',
        'HLT_Photon22_v2',
        'HLT_Photon25_v4',
        'HLT_Photon300_NoHE_v12',
        'HLT_Photon30_HoverELoose_v10',
        'HLT_Photon33_v5',
        'HLT_Photon35_TwoProngs35_v1',
        'HLT_Photon40_HoverELoose_v10',
        'HLT_Photon50_HoverELoose_v10',
        'HLT_Photon50_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_PFMET50_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_v14',
        'HLT_Photon50_v13',
        'HLT_Photon60_HoverELoose_v10',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350MinPFJet15_v11',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_v5',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_CaloMJJ300_PFJetsMJJ400DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_CaloMJJ400_PFJetsMJJ600DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ600DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_v14',
        'HLT_Photon75_v13',
        'HLT_Photon90_CaloIdL_PFHT700_v16',
        'HLT_Photon90_R9Id90_HE10_IsoM_v14',
        'HLT_Photon90_v13',
        'HLT_Physics_v7',
        'HLT_PixelTracks_Multiplicity110ForPPRef_v5',
        'HLT_PixelTracks_Multiplicity135ForPPRef_v5',
        'HLT_PixelTracks_Multiplicity160ForPPRef_v5',
        'HLT_PixelTracks_Multiplicity60ForPPRef_v5',
        'HLT_PixelTracks_Multiplicity85ForPPRef_v5',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v5',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v5',
        'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet98_83_71_15_v5',
        'HLT_Random_TOTEM_part0_v1',
        'HLT_Random_TOTEM_part1_v1',
        'HLT_Random_TOTEM_part2_v1',
        'HLT_Random_TOTEM_part3_v1',
        'HLT_Random_v3',
        'HLT_Rsq0p35_v15',
        'HLT_Rsq0p40_v15',
        'HLT_RsqMR300_Rsq0p09_MR200_4jet_v15',
        'HLT_RsqMR300_Rsq0p09_MR200_v15',
        'HLT_RsqMR320_Rsq0p09_MR200_4jet_v15',
        'HLT_RsqMR320_Rsq0p09_MR200_v15',
        'HLT_SingleJet30_Mu12_SinglePFJet40_v11',
        'HLT_SinglePhoton10_Eta3p1ForPPRef_v8',
        'HLT_SinglePhoton15_Eta3p1ForPPRef_v9',
        'HLT_SinglePhoton20_Eta3p1ForPPRef_v9',
        'HLT_SinglePhoton30_Eta3p1ForPPRef_v9',
        'HLT_SinglePhoton40_Eta3p1ForPPRef_v8',
        'HLT_SinglePhoton50_Eta3p1ForPPRef_v8',
        'HLT_SinglePhoton60_Eta3p1ForPPRef_v8',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part3_v1',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v4',
        'HLT_TkMu100_v2',
        'HLT_Trimuon2_Upsilon5_Muon_NoL1Mass_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v5',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v3',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v9',
        'HLT_TripleMu_10_5_5_DZ_v10',
        'HLT_TripleMu_12_10_5_v10',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v3',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v8',
        'HLT_TriplePhoton_20_20_20_CaloIdLV2_R9IdVL_v3',
        'HLT_TriplePhoton_20_20_20_CaloIdLV2_v3',
        'HLT_TriplePhoton_30_30_10_CaloIdLV2_R9IdVL_v4',
        'HLT_TriplePhoton_30_30_10_CaloIdLV2_v4',
        'HLT_TriplePhoton_35_35_5_CaloIdLV2_R9IdVL_v4',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v6',
        'HLT_TrkMu16_DoubleTrkMu6NoFiltersNoVtx_v12',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v13',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v6',
        'HLT_UncorrectedJetE30_NoBPTX_v6',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v6',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v6',
        'HLT_VBF_DoubleLooseChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_VBF_DoubleMediumChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_VBF_DoubleTightChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_ZeroBias_Alignment_v1',
        'HLT_ZeroBias_FirstBXAfterTrain_v3',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v5',
        'HLT_ZeroBias_FirstCollisionInTrain_v4',
        'HLT_ZeroBias_IsolatedBunches_v5',
        'HLT_ZeroBias_LastCollisionInTrain_v3',
        'HLT_ZeroBias_TOTEM_part0_v1',
        'HLT_ZeroBias_TOTEM_part1_v1',
        'HLT_ZeroBias_TOTEM_part2_v1',
        'HLT_ZeroBias_TOTEM_part3_v1',
        'HLT_ZeroBias_v6'
     ) ),
    ParkingBPH1 = cms.vstring(
        'HLT_Mu12_IP6_part0_v2',
        'HLT_Mu7_IP4_part0_v2',
        'HLT_Mu8_IP3_part0_v3',
        'HLT_Mu8_IP5_part0_v2',
        'HLT_Mu8_IP6_part0_v2',
        'HLT_Mu9_IP0_part0_v2',
        'HLT_Mu9_IP3_part0_v2',
        'HLT_Mu9_IP4_part0_v2',
        'HLT_Mu9_IP5_part0_v2',
        'HLT_Mu9_IP6_part0_v3'
    ),
    ParkingBPH2 = cms.vstring(
        'HLT_Mu12_IP6_part1_v2',
        'HLT_Mu7_IP4_part1_v2',
        'HLT_Mu8_IP3_part1_v3',
        'HLT_Mu8_IP5_part1_v2',
        'HLT_Mu8_IP6_part1_v2',
        'HLT_Mu9_IP4_part1_v2',
        'HLT_Mu9_IP5_part1_v2',
        'HLT_Mu9_IP6_part1_v3'
    ),
    ParkingBPH3 = cms.vstring(
        'HLT_Mu12_IP6_part2_v2',
        'HLT_Mu7_IP4_part2_v2',
        'HLT_Mu8_IP3_part2_v3',
        'HLT_Mu8_IP5_part2_v2',
        'HLT_Mu8_IP6_part2_v2',
        'HLT_Mu9_IP4_part2_v2',
        'HLT_Mu9_IP5_part2_v2',
        'HLT_Mu9_IP6_part2_v3'
    ),
    ParkingBPH4 = cms.vstring(
        'HLT_Mu12_IP6_part3_v2',
        'HLT_Mu7_IP4_part3_v2',
        'HLT_Mu8_IP3_part3_v3',
        'HLT_Mu8_IP5_part3_v2',
        'HLT_Mu8_IP6_part3_v2',
        'HLT_Mu9_IP4_part3_v2',
        'HLT_Mu9_IP5_part3_v2',
        'HLT_Mu9_IP6_part3_v3'
    ),
    ParkingBPH5 = cms.vstring(
        'HLT_Mu12_IP6_part4_v2',
        'HLT_Mu7_IP4_part4_v2',
        'HLT_Mu8_IP3_part4_v3',
        'HLT_Mu8_IP5_part4_v2',
        'HLT_Mu8_IP6_part4_v2',
        'HLT_Mu9_IP4_part4_v2',
        'HLT_Mu9_IP5_part4_v2',
        'HLT_Mu9_IP6_part4_v3'
    ),
    ParkingBPHPromptCSCS = cms.vstring(
        'HLT_Mu12_IP6_ToCSCS_v1',
        'HLT_Mu7_IP4_ToCSCS_v1',
        'HLT_Mu8_IP3_ToCSCS_v1',
        'HLT_Mu8_IP5_ToCSCS_v1',
        'HLT_Mu8_IP6_ToCSCS_v1',
        'HLT_Mu9_IP4_ToCSCS_v1',
        'HLT_Mu9_IP5_ToCSCS_v1',
        'HLT_Mu9_IP6_ToCSCS_v1'
    ),
    RPCMonitor = cms.vstring(
        'AlCa_HIRPCMuonNormalisation_v1',
        'AlCa_RPCMuonNormalisationForHI_v1',
        'AlCa_RPCMuonNormalisation_v13'
    ),
    RandomTOTEM1 = cms.vstring('HLT_Random_TOTEM_part0_v1'),
    RandomTOTEM2 = cms.vstring('HLT_Random_TOTEM_part1_v1'),
    RandomTOTEM3 = cms.vstring('HLT_Random_TOTEM_part2_v1'),
    RandomTOTEM4 = cms.vstring('HLT_Random_TOTEM_part3_v1'),
    ScoutingCaloCommissioning = cms.vstring(
        'DST_CaloJet40_CaloBTagScouting_v14',
        'DST_L1HTT_CaloBTagScouting_v14',
        'DST_ZeroBias_CaloScouting_PFScouting_v14'
    ),
    ScoutingCaloHT = cms.vstring(
        'DST_HT250_CaloBTagScouting_v10',
        'DST_HT250_CaloScouting_v10'
    ),
    ScoutingCaloMuon = cms.vstring(
        'DST_DoubleMu1_noVtx_CaloScouting_v2',
        'DST_DoubleMu3_noVtx_CaloScouting_Monitoring_v6',
        'DST_DoubleMu3_noVtx_CaloScouting_v6'
    ),
    ScoutingMonitor = cms.vstring(
        'DST_CaloJet40_BTagScouting_v15',
        'DST_CaloJet40_CaloBTagScouting_v14',
        'DST_CaloJet40_CaloScouting_PFScouting_v15',
        'DST_DoubleMu1_noVtx_CaloScouting_v2',
        'DST_DoubleMu3_noVtx_CaloScouting_Monitoring_v6',
        'DST_DoubleMu3_noVtx_CaloScouting_v6',
        'DST_DoubleMu3_noVtx_Mass10_PFScouting_v3',
        'DST_HT250_CaloBTagScouting_v10',
        'DST_HT250_CaloScouting_v10',
        'DST_HT410_BTagScouting_v16',
        'DST_HT410_PFScouting_v16',
        'DST_L1DoubleMu_BTagScouting_v16',
        'DST_L1DoubleMu_CaloScouting_PFScouting_v15',
        'DST_L1HTT_BTagScouting_v15',
        'DST_L1HTT_CaloBTagScouting_v14',
        'DST_L1HTT_CaloScouting_PFScouting_v15',
        'DST_Run3_PFScoutingPixelTracking_v16',
        'DST_ZeroBias_BTagScouting_v15',
        'DST_ZeroBias_CaloScouting_PFScouting_v14',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v14',
        'HLT_Ele35_WPTight_Gsf_v9',
        'HLT_IsoMu27_v16',
        'HLT_Mu50_v13',
        'HLT_PFHT1050_v18',
        'HLT_Photon200_v13'
    ),
    ScoutingPFCommissioning = cms.vstring(
        'DST_CaloJet40_BTagScouting_v15',
        'DST_CaloJet40_CaloScouting_PFScouting_v15',
        'DST_L1DoubleMu_BTagScouting_v16',
        'DST_L1DoubleMu_CaloScouting_PFScouting_v15',
        'DST_L1HTT_BTagScouting_v15',
        'DST_L1HTT_CaloScouting_PFScouting_v15',
        'DST_ZeroBias_BTagScouting_v15',
        'DST_ZeroBias_CaloScouting_PFScouting_v14'
    ),
    ScoutingPFHT = cms.vstring(
        'DST_HT410_BTagScouting_v16',
        'DST_HT410_PFScouting_v16'
    ),
    ScoutingPFMuon = cms.vstring('DST_DoubleMu3_noVtx_Mass10_PFScouting_v3'),
    ScoutingPFRun3 = cms.vstring('DST_Run3_PFScoutingPixelTracking_v16'),
    SingleMuHighPt = cms.vstring(
        'HLT_HIL2Mu15ForPPRef_v6',
        'HLT_HIL2Mu20ForPPRef_v6',
        'HLT_HIL2Mu5_NHitQ10ForPPRef_v6',
        'HLT_HIL2Mu7_NHitQ10ForPPRef_v6',
        'HLT_HIL3Mu15ForPPRef_v6',
        'HLT_HIL3Mu20ForPPRef_v6',
        'HLT_HIL3Mu5_NHitQ15ForPPRef_v6',
        'HLT_HIL3Mu7_NHitQ15ForPPRef_v6'
    ),
    SingleMuLowPt = cms.vstring(
        'HLT_HIL2Mu3_NHitQ10ForPPRef_v6',
        'HLT_HIL3Mu3_NHitQ15ForPPRef_v6'
    ),
    SingleMuon = cms.vstring(
        'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v1',
        'HLT_IsoMu20_v15',
        'HLT_IsoMu24_TwoProngs35_v1',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v1',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS50_eta2p1_v1',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v1',
        'HLT_IsoMu24_eta2p1_v15',
        'HLT_IsoMu24_v13',
        'HLT_IsoMu27_v16',
        'HLT_IsoMu30_v4',
        'HLT_L1SingleMu18_v3',
        'HLT_L1SingleMu25_v2',
        'HLT_L1_DoubleJet30_Mass_Min400_Mu10_v1',
        'HLT_L2Mu10_v7',
        'HLT_L2Mu50_v2',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v15',
        'HLT_Mu12_v3',
        'HLT_Mu15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v8',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v15',
        'HLT_Mu15_IsoVVVL_PFHT450_v15',
        'HLT_Mu15_IsoVVVL_PFHT600_v19',
        'HLT_Mu15_v3',
        'HLT_Mu20_v12',
        'HLT_Mu27_v13',
        'HLT_Mu3_PFJet40_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET70_PFMHT70_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu70_PFMHTNoMu70_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v2',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v15',
        'HLT_Mu50_IsoVVVL_PFHT450_v15',
        'HLT_Mu50_v13',
        'HLT_Mu55_v3',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v16',
        'HLT_OldMu100_v3',
        'HLT_TkMu100_v2'
    ),
    SingleTrack = cms.vstring(),
    TOTEM1part0 = cms.vstring(
        'HLT_L1RomanPot_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part0_v1'
    ),
    TOTEM1part1 = cms.vstring(
        'HLT_L1RomanPot_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part1_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part1_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part1_v1'
    ),
    TOTEM1part2 = cms.vstring(
        'HLT_L1RomanPot_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part2_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part2_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part2_v1'
    ),
    TOTEM1part3 = cms.vstring(
        'HLT_L1RomanPot_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay3_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu5NLay4_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay3_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu6NLay4_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay3_part3_v1',
        'HLT_TOTEM_1_AND_PixelClusterCounting_BPixNClu7NLay4_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult1_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult2_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_BPixOnly_Mult3_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult1_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult2_part3_v1',
        'HLT_TOTEM_1_AND_PixelTrackCounting_Mult3_part3_v1'
    ),
    TOTEM2part0 = cms.vstring(
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part0_v1'
    ),
    TOTEM2part1 = cms.vstring(
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part1_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part1_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part1_v1'
    ),
    TOTEM2part2 = cms.vstring(
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part2_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part2_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part2_v1'
    ),
    TOTEM2part3 = cms.vstring(
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay3_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu5NLay4_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay3_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu6NLay4_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay3_part3_v1',
        'HLT_TOTEM_2_AND_PixelClusterCounting_BPixNClu7NLay4_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult1_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult2_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_BPixOnly_Mult3_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult1_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult2_part3_v1',
        'HLT_TOTEM_2_AND_PixelTrackCounting_Mult3_part3_v1'
    ),
    TOTEM3 = cms.vstring('HLT_L1TOTEM_3_v1'),
    TOTEM4part0 = cms.vstring(
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part0_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part0_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part0_v1'
    ),
    TOTEM4part1 = cms.vstring(
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part1_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part1_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part1_v1'
    ),
    TOTEM4part2 = cms.vstring(
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part2_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part2_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part2_v1'
    ),
    TOTEM4part3 = cms.vstring(
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay3_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu5NLay4_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay3_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu6NLay4_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay3_part3_v1',
        'HLT_TOTEM_4_AND_PixelClusterCounting_BPixNClu7NLay4_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult1_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult2_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_BPixOnly_Mult3_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult1_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult2_part3_v1',
        'HLT_TOTEM_4_AND_PixelTrackCounting_Mult3_part3_v1'
    ),
    Tau = cms.vstring(
        'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_v1',
        'HLT_DoubleMediumDeepTauIsoPFTauHPS35_L2NN_eta2p1_v1',
        'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_v1',
        'HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1_v1',
        'HLT_LooseDeepTauPFTauHPS50_eta2p1_MET100_v1',
        'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau200HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau220HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET100_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET110_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET120_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v12',
        'HLT_Photon35_TwoProngs35_v1',
        'HLT_VBF_DoubleLooseChargedIsoPFTau20_Trk1_eta2p1_v3',
        'HLT_VBF_DoubleLooseChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_VBF_DoubleMediumChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_VBF_DoubleTightChargedIsoPFTauHPS20_Trk1_eta2p1_v1'
    ),
    TestEnablesEcalHcal = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v5'
    ),
    TestEnablesEcalHcalDQM = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v5'
    ),
    ZeroBias = cms.vstring(
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v1',
        'HLT_ZeroBias_FirstBXAfterTrain_v3',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v5',
        'HLT_ZeroBias_FirstCollisionInTrain_v4',
        'HLT_ZeroBias_IsolatedBunches_v5',
        'HLT_ZeroBias_LastCollisionInTrain_v3',
        'HLT_ZeroBias_v6'
    ),
    ZeroBiasTOTEM = cms.vstring('HLT_L1TOTEM2_ZeroBias_v4'),
    ZeroBiasTOTEM1 = cms.vstring('HLT_ZeroBias_TOTEM_part0_v1'),
    ZeroBiasTOTEM2 = cms.vstring('HLT_ZeroBias_TOTEM_part1_v1'),
    ZeroBiasTOTEM3 = cms.vstring('HLT_ZeroBias_TOTEM_part2_v1'),
    ZeroBiasTOTEM4 = cms.vstring('HLT_ZeroBias_TOTEM_part3_v1'),
    ppForward = cms.vstring('HLT_HIL1CastorMediumJetForPPRef_v4')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.nanoDQMIO_perLSoutput = cms.PSet(
    MEsToSave = cms.untracked.vstring(
        'DT/02-Segments/03-MeanT0/T0MeanAllWheels',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'Muons/MuonRecoAnalyzer/',
        'Muons/MuonIdDQM/GlobalMuons/',
        'PixelPhase1/Phase1_MechanicalView/',
        'PixelPhase1/Tracks/',
        'SiStrip/MechanicalView/',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/',
        'Tracking/TrackParameters/generalTracks/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/LSanalysis/',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/GeneralProperties/',
        'Tracking/TrackParameters/generalTracks/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/',
        'Tracking/TrackParameters/generalTracks/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/Pixel/',
        'Tracking/TrackParameters/generalTracks/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/Strip/'
    )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(4),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.streams = cms.PSet(
    ALCALumiPixelCountsExpress = cms.vstring('AlCaLumiPixelCountsExpress'),
    ALCALumiPixelCountsPrompt = cms.vstring('AlCaLumiPixelCountsPrompt'),
    ALCAP0 = cms.vstring('AlCaP0'),
    ALCAPHISYM = cms.vstring('AlCaPhiSym'),
    ALCAPPS = cms.vstring('AlCaPPS'),
    Calibration = cms.vstring('TestEnablesEcalHcal'),
    DQM = cms.vstring('OnlineMonitor'),
    DQMCalibration = cms.vstring('TestEnablesEcalHcalDQM'),
    DQMEventDisplay = cms.vstring('EventDisplay'),
    DQMOnlineBeamspot = cms.vstring('DQMOnlineBeamspot'),
    EcalCalibration = cms.vstring('EcalLaser'),
    Express = cms.vstring('ExpressPhysics'),
    ExpressAlignment = cms.vstring('ExpressAlignment'),
    ExpressCosmics = cms.vstring('ExpressCosmics'),
    HIDQM = cms.vstring('HIOnlineMonitor'),
    HIDQMEventDisplay = cms.vstring(),
    HIDQMOnlineBeamspot = cms.vstring('HIDQMOnlineBeamspot'),
    HIExpress = cms.vstring('HIExpressPhysics'),
    HIExpressAlignment = cms.vstring('HIExpressAlignment'),
    HIHLTMonitor = cms.vstring(),
    HIPhysicsCommissioning = cms.vstring(
        'HIEmptyBX',
        'HIHLTPhysics',
        'HIHcalNZS'
    ),
    HIPhysicsDoubleMuon = cms.vstring(
        'HIDoubleMuon',
        'HIDoubleMuonPsiPeri'
    ),
    HIPhysicsForward = cms.vstring(
        'HICastor',
        'HIForward'
    ),
    HIPhysicsHardProbes = cms.vstring('HIHardProbes'),
    HIPhysicsHardProbesLower = cms.vstring('HIHardProbesLower'),
    HIPhysicsHardProbesPeripheral = cms.vstring('HIHardProbesPeripheral'),
    HIPhysicsHeavyFlavor = cms.vstring('HIHeavyFlavor'),
    HIPhysicsHighMultiplicty = cms.vstring('HIHighMultiplicityETTAsym'),
    HIPhysicsLowMultiplicity = cms.vstring('HILowMultiplicity'),
    HIPhysicsLowMultiplicityReducedFormat = cms.vstring('HILowMultiplicityReducedFormat'),
    HIPhysicsMinimumBias0 = cms.vstring('HIMinimumBias0'),
    HIPhysicsMinimumBias1 = cms.vstring('HIMinimumBias1'),
    HIPhysicsMinimumBias2 = cms.vstring('HIMinimumBias2'),
    HIPhysicsMinimumBias3 = cms.vstring('HIMinimumBias3'),
    HIPhysicsMinimumBias4 = cms.vstring('HIMinimumBias4'),
    HIPhysicsMinimumBias5 = cms.vstring('HIMinimumBias5'),
    HIPhysicsMinimumBias6 = cms.vstring('HIMinimumBias6'),
    HIPhysicsMinimumBias7 = cms.vstring('HIMinimumBias7'),
    HIPhysicsMinimumBias8 = cms.vstring('HIMinimumBias8'),
    HIPhysicsMinimumBias9 = cms.vstring('HIMinimumBias9'),
    HIPhysicsSingleMuon = cms.vstring('HISingleMuon'),
    HITrackerNZS = cms.vstring('HITrackerNZS'),
    HLTMonitor = cms.vstring('HLTMonitor'),
    NanoDST = cms.vstring('L1Accept'),
    ParkingBPH1 = cms.vstring(
        'ParkingBPH1',
        'ParkingBPHPromptCSCS'
    ),
    ParkingBPH2 = cms.vstring('ParkingBPH2'),
    ParkingBPH3 = cms.vstring('ParkingBPH3'),
    ParkingBPH4 = cms.vstring('ParkingBPH4'),
    ParkingBPH5 = cms.vstring('ParkingBPH5'),
    Physics = cms.vstring(),
    PhysicsCommissioning = cms.vstring(
        'Commissioning',
        'Cosmics',
        'HFvetoTOTEM',
        'HLTPhysics',
        'HcalNZS',
        'HighEGJet',
        'HighPtLowerPhotons',
        'HighPtPhoton30AndZ',
        'IsolatedBunch',
        'LowEGJet',
        'MinBiasTOTEM',
        'MinimumBias',
        'MonteCarlo',
        'NoBPTX',
        'ZeroBias',
        'ZeroBiasTOTEM'
    ),
    PhysicsEGamma = cms.vstring('EGamma'),
    PhysicsEndOfFill = cms.vstring(
        'EmptyBX',
        'FSQJet1',
        'FSQJet2',
        'HINCaloJets',
        'HINPFJets',
        'HighMultiplicityEOF',
        'L1MinimumBias'
    ),
    PhysicsForward = cms.vstring('ppForward'),
    PhysicsHIMinimumBias10 = cms.vstring('HIMinimumBias10'),
    PhysicsHIMinimumBias11 = cms.vstring('HIMinimumBias11'),
    PhysicsHIMinimumBias12 = cms.vstring('HIMinimumBias12'),
    PhysicsHIMinimumBias13 = cms.vstring('HIMinimumBias13'),
    PhysicsHIMinimumBias14 = cms.vstring('HIMinimumBias14'),
    PhysicsHIMinimumBias15 = cms.vstring('HIMinimumBias15'),
    PhysicsHIMinimumBias16 = cms.vstring('HIMinimumBias16'),
    PhysicsHIMinimumBias17 = cms.vstring('HIMinimumBias17'),
    PhysicsHIMinimumBias18 = cms.vstring('HIMinimumBias18'),
    PhysicsHIMinimumBias19 = cms.vstring('HIMinimumBias19'),
    PhysicsHIMinimumBiasReducedFormat0 = cms.vstring('HIMinimumBiasReducedFormat0'),
    PhysicsHIMinimumBiasReducedFormat1 = cms.vstring('HIMinimumBiasReducedFormat1'),
    PhysicsHIMinimumBiasReducedFormat10 = cms.vstring('HIMinimumBiasReducedFormat10'),
    PhysicsHIMinimumBiasReducedFormat11 = cms.vstring('HIMinimumBiasReducedFormat11'),
    PhysicsHIMinimumBiasReducedFormat2 = cms.vstring('HIMinimumBiasReducedFormat2'),
    PhysicsHIMinimumBiasReducedFormat3 = cms.vstring('HIMinimumBiasReducedFormat3'),
    PhysicsHIMinimumBiasReducedFormat4 = cms.vstring('HIMinimumBiasReducedFormat4'),
    PhysicsHIMinimumBiasReducedFormat5 = cms.vstring('HIMinimumBiasReducedFormat5'),
    PhysicsHIMinimumBiasReducedFormat6 = cms.vstring('HIMinimumBiasReducedFormat6'),
    PhysicsHIMinimumBiasReducedFormat7 = cms.vstring('HIMinimumBiasReducedFormat7'),
    PhysicsHIMinimumBiasReducedFormat8 = cms.vstring('HIMinimumBiasReducedFormat8'),
    PhysicsHIMinimumBiasReducedFormat9 = cms.vstring('HIMinimumBiasReducedFormat9'),
    PhysicsHIZeroBias1 = cms.vstring(
        'HIZeroBias1',
        'HIZeroBias2'
    ),
    PhysicsHIZeroBias2 = cms.vstring(
        'HIZeroBias3',
        'HIZeroBias4'
    ),
    PhysicsHIZeroBias3 = cms.vstring(
        'HIZeroBias5',
        'HIZeroBias6'
    ),
    PhysicsHIZeroBias4 = cms.vstring(
        'HIZeroBias7',
        'HIZeroBias8'
    ),
    PhysicsHIZeroBias5 = cms.vstring(
        'HIZeroBias10',
        'HIZeroBias9'
    ),
    PhysicsHIZeroBias6 = cms.vstring(
        'HIZeroBias11',
        'HIZeroBias12'
    ),
    PhysicsHLTPhysics1 = cms.vstring(
        'EphemeralHLTPhysics1',
        'EphemeralHLTPhysics2'
    ),
    PhysicsHLTPhysics2 = cms.vstring(
        'EphemeralHLTPhysics3',
        'EphemeralHLTPhysics4'
    ),
    PhysicsHLTPhysics3 = cms.vstring(
        'EphemeralHLTPhysics5',
        'EphemeralHLTPhysics6'
    ),
    PhysicsHLTPhysics4 = cms.vstring(
        'EphemeralHLTPhysics7',
        'EphemeralHLTPhysics8'
    ),
    PhysicsHadronsTaus = cms.vstring(
        'BTagMu',
        'DisplacedJet',
        'HeavyFlavor',
        'HighPtJet80',
        'HighPtLowerJets',
        'JetHT',
        'JetsTOTEM',
        'MET',
        'Tau'
    ),
    PhysicsMinimumBias0 = cms.vstring('MinimumBias0'),
    PhysicsMinimumBias1 = cms.vstring('MinimumBias1'),
    PhysicsMinimumBias2 = cms.vstring('MinimumBias2'),
    PhysicsMinimumBias3 = cms.vstring('MinimumBias3'),
    PhysicsMinimumBias4 = cms.vstring('MinimumBias4'),
    PhysicsMinimumBias5 = cms.vstring('MinimumBias5'),
    PhysicsMinimumBias6 = cms.vstring('MinimumBias6'),
    PhysicsMinimumBias7 = cms.vstring('MinimumBias7'),
    PhysicsMinimumBias8 = cms.vstring('MinimumBias8'),
    PhysicsMinimumBias9 = cms.vstring('MinimumBias9'),
    PhysicsMuons = cms.vstring(
        'Charmonium',
        'DoubleMuon',
        'DoubleMuonLowMass',
        'MuOnia',
        'MuPlusX',
        'MuonEG',
        'MuonEGammaTOTEM',
        'SingleMuHighPt',
        'SingleMuLowPt',
        'SingleMuon'
    ),
    PhysicsRandomTOTEM1 = cms.vstring('RandomTOTEM1'),
    PhysicsRandomTOTEM2 = cms.vstring('RandomTOTEM2'),
    PhysicsRandomTOTEM3 = cms.vstring('RandomTOTEM3'),
    PhysicsRandomTOTEM4 = cms.vstring('RandomTOTEM4'),
    PhysicsScoutingMonitor = cms.vstring('ScoutingMonitor'),
    PhysicsTOTEM1part0 = cms.vstring('TOTEM1part0'),
    PhysicsTOTEM1part1 = cms.vstring('TOTEM1part1'),
    PhysicsTOTEM1part2 = cms.vstring('TOTEM1part2'),
    PhysicsTOTEM1part3 = cms.vstring('TOTEM1part3'),
    PhysicsTOTEM2part0 = cms.vstring('TOTEM2part0'),
    PhysicsTOTEM2part1 = cms.vstring('TOTEM2part1'),
    PhysicsTOTEM2part2 = cms.vstring('TOTEM2part2'),
    PhysicsTOTEM2part3 = cms.vstring('TOTEM2part3'),
    PhysicsTOTEM3 = cms.vstring('TOTEM3'),
    PhysicsTOTEM4part0 = cms.vstring('TOTEM4part0'),
    PhysicsTOTEM4part1 = cms.vstring('TOTEM4part1'),
    PhysicsTOTEM4part2 = cms.vstring('TOTEM4part2'),
    PhysicsTOTEM4part3 = cms.vstring('TOTEM4part3'),
    PhysicsTracks = cms.vstring(
        'FullTrack',
        'HighMultiplicity',
        'SingleTrack'
    ),
    PhysicsZeroBias1 = cms.vstring(
        'EphemeralZeroBias1',
        'EphemeralZeroBias2'
    ),
    PhysicsZeroBias2 = cms.vstring(
        'EphemeralZeroBias3',
        'EphemeralZeroBias4'
    ),
    PhysicsZeroBias3 = cms.vstring(
        'EphemeralZeroBias5',
        'EphemeralZeroBias6'
    ),
    PhysicsZeroBias4 = cms.vstring(
        'EphemeralZeroBias7',
        'EphemeralZeroBias8'
    ),
    PhysicsZeroBiasTOTEM1 = cms.vstring('ZeroBiasTOTEM1'),
    PhysicsZeroBiasTOTEM2 = cms.vstring('ZeroBiasTOTEM2'),
    PhysicsZeroBiasTOTEM3 = cms.vstring('ZeroBiasTOTEM3'),
    PhysicsZeroBiasTOTEM4 = cms.vstring('ZeroBiasTOTEM4'),
    RPCMON = cms.vstring('RPCMonitor'),
    ReleaseValidation = cms.vstring(),
    ScoutingCaloMuon = cms.vstring(
        'ScoutingCaloCommissioning',
        'ScoutingCaloHT',
        'ScoutingCaloMuon'
    ),
    ScoutingPF = cms.vstring(
        'ScoutingPFCommissioning',
        'ScoutingPFHT',
        'ScoutingPFMuon',
        'ScoutingPFRun3'
    )
)

process.transferSystem = cms.PSet(
    default = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        streamLookArea = cms.PSet(

        ),
        test = cms.vstring('Lustre')
    ),
    destinations = cms.vstring(
        'Tier0',
        'DQM',
        'ECAL',
        'EventDisplay',
        'Lustre',
        'None'
    ),
    streamA = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        test = cms.vstring('Lustre')
    ),
    streamCalibration = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamDQM = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamDQMCalibration = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamEcalCalibration = cms.PSet(
        default = cms.vstring('ECAL'),
        emulator = cms.vstring('None'),
        test = cms.vstring('ECAL')
    ),
    streamEventDisplay = cms.PSet(
        default = cms.vstring(
            'EventDisplay',
            'Tier0'
        ),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'EventDisplay',
            'Lustre'
        )
    ),
    streamExpressCosmics = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        test = cms.vstring('Lustre')
    ),
    streamLookArea = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamNanoDST = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamRPCMON = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamTrackerCalibration = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    transferModes = cms.vstring(
        'default',
        'test',
        'emulator'
    )
)

process.hltCSCrechitClusters = cms.EDProducer("CSCrechitClusterProducer",
    nRechitMin = cms.int32(50),
    nStationThres = cms.int32(10),
    rParam = cms.double(0.4),
    recHitLabel = cms.InputTag("hltCsc2DRecHits")
)


process.hltCsc2DRecHits = cms.EDProducer("CSCRecHitDProducer",
    CSCDebug = cms.untracked.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripxtalksOffset = cms.double(0.03),
    CSCUseCalibrations = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(False),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCUseStaticPedestals = cms.bool(False),
    CSCUseTimingCorrections = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCstripWireDeltaTime = cms.int32(8),
    ConstSyst_ME12 = cms.double(0.0),
    ConstSyst_ME13 = cms.double(0.0),
    ConstSyst_ME1a = cms.double(0.022),
    ConstSyst_ME1b = cms.double(0.007),
    ConstSyst_ME21 = cms.double(0.0),
    ConstSyst_ME22 = cms.double(0.0),
    ConstSyst_ME31 = cms.double(0.0),
    ConstSyst_ME32 = cms.double(0.0),
    ConstSyst_ME41 = cms.double(0.0),
    NoiseLevel_ME12 = cms.double(9.0),
    NoiseLevel_ME13 = cms.double(8.0),
    NoiseLevel_ME1a = cms.double(7.0),
    NoiseLevel_ME1b = cms.double(8.0),
    NoiseLevel_ME21 = cms.double(9.0),
    NoiseLevel_ME22 = cms.double(9.0),
    NoiseLevel_ME31 = cms.double(9.0),
    NoiseLevel_ME32 = cms.double(9.0),
    NoiseLevel_ME41 = cms.double(9.0),
    UseAverageTime = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    UseParabolaFit = cms.bool(False),
    XTasymmetry_ME12 = cms.double(0.0),
    XTasymmetry_ME13 = cms.double(0.0),
    XTasymmetry_ME1a = cms.double(0.0),
    XTasymmetry_ME1b = cms.double(0.0),
    XTasymmetry_ME21 = cms.double(0.0),
    XTasymmetry_ME22 = cms.double(0.0),
    XTasymmetry_ME31 = cms.double(0.0),
    XTasymmetry_ME32 = cms.double(0.0),
    XTasymmetry_ME41 = cms.double(0.0),
    readBadChambers = cms.bool(True),
    readBadChannels = cms.bool(False),
    stripDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCWireDigi")
)


process.hltCscSegments = cms.EDProducer("CSCSegmentProducer",
    algo_psets = cms.VPSet(cms.PSet(
        algo_name = cms.string('CSCSegAlgoRU'),
        algo_psets = cms.VPSet(
            cms.PSet(
                chi2Max = cms.double(100.0),
                chi2Norm_2D_ = cms.double(35.0),
                chi2_str = cms.double(50.0),
                dPhiIntMax = cms.double(0.005),
                dPhiMax = cms.double(0.006),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(100.0),
                chi2Norm_2D_ = cms.double(35.0),
                chi2_str = cms.double(50.0),
                dPhiIntMax = cms.double(0.004),
                dPhiMax = cms.double(0.005),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(100.0),
                chi2Norm_2D_ = cms.double(35.0),
                chi2_str = cms.double(50.0),
                dPhiIntMax = cms.double(0.003),
                dPhiMax = cms.double(0.004),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(60.0),
                chi2Norm_2D_ = cms.double(20.0),
                chi2_str = cms.double(30.0),
                dPhiIntMax = cms.double(0.002),
                dPhiMax = cms.double(0.003),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(180.0),
                chi2Norm_2D_ = cms.double(60.0),
                chi2_str = cms.double(80.0),
                dPhiIntMax = cms.double(0.005),
                dPhiMax = cms.double(0.007),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(100.0),
                chi2Norm_2D_ = cms.double(35.0),
                chi2_str = cms.double(50.0),
                dPhiIntMax = cms.double(0.004),
                dPhiMax = cms.double(0.006),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            )
        ),
        chamber_types = cms.vstring(
            'ME1/a',
            'ME1/b',
            'ME1/2',
            'ME1/3',
            'ME2/1',
            'ME2/2',
            'ME3/1',
            'ME3/2',
            'ME4/1',
            'ME4/2'
        ),
        parameters_per_chamber_type = cms.vint32(
            1, 2, 3, 4, 5,
            6, 5, 6, 5, 6
        )
    )),
    algo_type = cms.int32(1),
    inputObjects = cms.InputTag("hltCsc2DRecHits")
)


process.hltDTrechitClusters = cms.EDProducer("DTrechitClusterProducer",
    nRechitMin = cms.int32(50),
    nStationThres = cms.int32(10),
    rParam = cms.double(0.4),
    recHitLabel = cms.InputTag("hltDt1DRecHits")
)


process.hltDt1DRecHits = cms.EDProducer("DTRecHitProducer",
    debug = cms.untracked.bool(False),
    dtDigiLabel = cms.InputTag("hltMuonDTDigis"),
    recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
    recAlgoConfig = cms.PSet(
        debug = cms.untracked.bool(False),
        doVdriftCorr = cms.bool(True),
        maxTime = cms.double(420.0),
        minTime = cms.double(-3.0),
        readLegacyTTrigDB = cms.bool(True),
        readLegacyVDriftDB = cms.bool(True),
        stepTwoFromDigi = cms.bool(False),
        tTrigMode = cms.string('DTTTrigSyncFromDB'),
        tTrigModeConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doT0Correction = cms.bool(True),
            doTOFCorrection = cms.bool(True),
            doWirePropCorrection = cms.bool(True),
            t0Label = cms.string(''),
            tTrigLabel = cms.string(''),
            tofCorrType = cms.int32(0),
            vPropWire = cms.double(24.4),
            wirePropCorrType = cms.int32(0)
        ),
        useUncertDB = cms.bool(True)
    )
)


process.hltDt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    Reco4DAlgoConfig = cms.PSet(
        AllDTRecHits = cms.bool(True),
        Reco2DAlgoConfig = cms.PSet(
            AlphaMaxPhi = cms.double(1.0),
            AlphaMaxTheta = cms.double(0.9),
            MaxAllowedHits = cms.uint32(50),
            debug = cms.untracked.bool(False),
            hit_afterT0_resolution = cms.double(0.03),
            nSharedHitsMax = cms.int32(2),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False),
            performT0_vdriftSegCorrection = cms.bool(False),
            perform_delta_rejecting = cms.bool(False),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doVdriftCorr = cms.bool(True),
                maxTime = cms.double(420.0),
                minTime = cms.double(-3.0),
                readLegacyTTrigDB = cms.bool(True),
                readLegacyVDriftDB = cms.bool(True),
                stepTwoFromDigi = cms.bool(False),
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                tTrigModeConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doT0Correction = cms.bool(True),
                    doTOFCorrection = cms.bool(True),
                    doWirePropCorrection = cms.bool(True),
                    t0Label = cms.string(''),
                    tTrigLabel = cms.string(''),
                    tofCorrType = cms.int32(0),
                    vPropWire = cms.double(24.4),
                    wirePropCorrType = cms.int32(0)
                ),
                useUncertDB = cms.bool(True)
            ),
            segmCleanerMode = cms.int32(2)
        ),
        Reco2DAlgoName = cms.string('DTCombinatorialPatternReco'),
        debug = cms.untracked.bool(False),
        hit_afterT0_resolution = cms.double(0.03),
        nSharedHitsMax = cms.int32(2),
        nUnSharedHitsMin = cms.int32(2),
        performT0SegCorrection = cms.bool(False),
        performT0_vdriftSegCorrection = cms.bool(False),
        perform_delta_rejecting = cms.bool(False),
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doVdriftCorr = cms.bool(True),
            maxTime = cms.double(420.0),
            minTime = cms.double(-3.0),
            readLegacyTTrigDB = cms.bool(True),
            readLegacyVDriftDB = cms.bool(True),
            stepTwoFromDigi = cms.bool(False),
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            tTrigModeConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doT0Correction = cms.bool(True),
                doTOFCorrection = cms.bool(True),
                doWirePropCorrection = cms.bool(True),
                t0Label = cms.string(''),
                tTrigLabel = cms.string(''),
                tofCorrType = cms.int32(0),
                vPropWire = cms.double(24.4),
                wirePropCorrType = cms.int32(0)
            ),
            useUncertDB = cms.bool(True)
        ),
        segmCleanerMode = cms.int32(2)
    ),
    Reco4DAlgoName = cms.string('DTCombinatorialPatternReco4D'),
    debug = cms.untracked.bool(False),
    recHits1DLabel = cms.InputTag("hltDt1DRecHits"),
    recHits2DLabel = cms.InputTag("dt2DSegments")
)


process.hltFEDSelector = cms.EDProducer("EvFFEDSelector",
    fedList = cms.vuint32(1023, 1024),
    inputTag = cms.InputTag("rawDataCollector")
)


process.hltGemRecHits = cms.EDProducer("GEMRecHitProducer",
    applyMasking = cms.bool(False),
    gemDigiLabel = cms.InputTag("hltMuonGEMDigis"),
    recAlgo = cms.string('GEMRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    )
)


process.hltGemSegments = cms.EDProducer("GEMSegmentProducer",
    algo_name = cms.string('GEMSegmentAlgorithm'),
    algo_pset = cms.PSet(
        clusterOnlySameBXRecHits = cms.bool(True),
        dEtaChainBoxMax = cms.double(0.05),
        dPhiChainBoxMax = cms.double(0.02),
        dXclusBoxMax = cms.double(1.0),
        dYclusBoxMax = cms.double(5.0),
        maxRecHitsInCluster = cms.int32(4),
        minHitsPerSegment = cms.uint32(2),
        preClustering = cms.bool(True),
        preClusteringUseChaining = cms.bool(True)
    ),
    ge0_name = cms.string('GE0SegAlgoRU'),
    ge0_pset = cms.PSet(
        allowWideSegments = cms.bool(True),
        doCollisions = cms.bool(True),
        maxChi2Additional = cms.double(100.0),
        maxChi2GoodSeg = cms.double(50.0),
        maxChi2Prune = cms.double(50.0),
        maxETASeeds = cms.double(0.1),
        maxNumberOfHits = cms.uint32(300),
        maxNumberOfHitsPerLayer = cms.uint32(100),
        maxPhiAdditional = cms.double(0.001096605744),
        maxPhiSeeds = cms.double(0.001096605744),
        maxTOFDiff = cms.double(25.0),
        minNumberOfHits = cms.uint32(4),
        requireCentralBX = cms.bool(True)
    ),
    gemRecHitLabel = cms.InputTag("hltGemRecHits")
)


process.hltGtStage2Digis = cms.EDProducer("L1TRawToDigi",
    CTP7 = cms.untracked.bool(False),
    DmxFWId = cms.uint32(0),
    FWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("rawDataCollector"),
    MTF7 = cms.untracked.bool(False),
    MinFeds = cms.uint32(0),
    Setup = cms.string('stage2::GTSetup'),
    TMTCheck = cms.bool(True),
    debug = cms.untracked.bool(False),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.hltGtStage2ObjectMap = cms.EDProducer("L1TGlobalProducer",
    AlgoBlkInputTag = cms.InputTag("hltGtStage2Digis"),
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    BstLengthBytes = cms.int32(-1),
    EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    EmulateBxInEvent = cms.int32(1),
    EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    ExtInputTag = cms.InputTag("hltGtStage2Digis"),
    GetPrescaleColumnFromData = cms.bool(False),
    JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1DataBxInEvent = cms.int32(5),
    MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    MuonShowerInputTag = cms.InputTag(""),
    PrescaleCSVFile = cms.string('prescale_L1TGlobal.csv'),
    PrescaleSet = cms.uint32(1),
    PrintL1Menu = cms.untracked.bool(False),
    ProduceL1GtDaqRecord = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    RequireMenuToMatchAlgoBlkInput = cms.bool(True),
    TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    TriggerMenuLuminosity = cms.string('startup'),
    Verbosity = cms.untracked.int32(0),
    useMuonShowers = cms.bool(False)
)


process.hltMuonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    B904Setup = cms.untracked.bool(False),
    Debug = cms.untracked.bool(False),
    DisableMappingCheck = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535558134),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    runDQM = cms.untracked.bool(False),
    useCSCShowers = cms.bool(False),
    useGEMs = cms.bool(False),
    useRPCs = cms.bool(False)
)


process.hltMuonDTDigis = cms.EDProducer("DTuROSRawToDigi",
    debug = cms.untracked.bool(False),
    inputLabel = cms.InputTag("rawDataCollector")
)


process.hltMuonGEMDigis = cms.EDProducer("GEMRawToDigiModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    fedIdEnd = cms.uint32(1478),
    fedIdStart = cms.uint32(1467),
    keepDAQStatus = cms.bool(False),
    readMultiBX = cms.bool(False),
    useDBEMap = cms.bool(False)
)


process.hltMuonRPCDigis = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(False)
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    beamMode = cms.untracked.uint32(11),
    changeToCMSCoordinates = cms.bool(False),
    gtEvmLabel = cms.InputTag(""),
    maxRadius = cms.double(2.0),
    maxZ = cms.double(40.0),
    setSigmaZ = cms.double(0.0),
    src = cms.InputTag("hltScalersRawToDigi"),
    useTransientRecord = cms.bool(False)
)


process.hltOnlineMetaDataDigis = cms.EDProducer("OnlineMetaDataRawToDigi",
    onlineMetaDataInputLabel = cms.InputTag("rawDataCollector")
)


process.hltPSetMap = cms.EDProducer("ParameterSetBlobProducer")


process.hltRpcRecHits = cms.EDProducer("RPCRecHitProducer",
    deadSource = cms.string('File'),
    deadvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat'),
    maskSource = cms.string('File'),
    maskvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat'),
    recAlgo = cms.string('RPCRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    ),
    rpcDigiLabel = cms.InputTag("hltMuonRPCDigis")
)


process.hltScalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
    moduleLabelPatternsToMatch = cms.vstring('hlt*'),
    moduleLabelPatternsToSkip = cms.vstring(),
    processName = cms.string('@'),
    throw = cms.bool(False)
)


process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
    processName = cms.string('@')
)


process.packCaloStage2 = cms.EDProducer("L1TDigiToRaw",
    FWId = cms.uint32(1),
    FedId = cms.int32(1366),
    InputLabel = cms.InputTag("simCaloStage2Digis"),
    Setup = cms.string('stage2::CaloSetup'),
    TowerInputLabel = cms.InputTag("simCaloStage2Layer1Digis"),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.packGmtStage2 = cms.EDProducer("L1TDigiToRaw",
    BMTFInputLabel = cms.InputTag("simKBmtfDigis","BMTF"),
    EMTFInputLabel = cms.InputTag("simEmtfDigis","EMTF"),
    EMTFShowerInputLabel = cms.InputTag("simEmtfShowers","EMTF"),
    FWId = cms.uint32(117440512),
    FedId = cms.int32(1402),
    ImdInputLabelBMTF = cms.InputTag("simGmtStage2Digis","imdMuonsBMTF"),
    ImdInputLabelEMTFNeg = cms.InputTag("simGmtStage2Digis","imdMuonsEMTFNeg"),
    ImdInputLabelEMTFPos = cms.InputTag("simGmtStage2Digis","imdMuonsEMTFPos"),
    ImdInputLabelOMTFNeg = cms.InputTag("simGmtStage2Digis","imdMuonsOMTFNeg"),
    ImdInputLabelOMTFPos = cms.InputTag("simGmtStage2Digis","imdMuonsOMTFPos"),
    InputLabel = cms.InputTag("simGmtStage2Digis"),
    OMTFInputLabel = cms.InputTag("simOmtfDigis","OMTF"),
    Setup = cms.string('stage2::GMTSetup'),
    ShowerInputLabel = cms.InputTag("simGmtShowerDigis"),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.packGtStage2 = cms.EDProducer("L1TDigiToRaw",
    EGammaInputTag = cms.InputTag("simCaloStage2Digis"),
    EtSumInputTag = cms.InputTag("simCaloStage2Digis"),
    ExtInputTag = cms.InputTag("simGtExtFakeStage2Digis"),
    FWId = cms.uint32(69377),
    FedId = cms.int32(1404),
    GtInputTag = cms.InputTag("simGtStage2Digis"),
    JetInputTag = cms.InputTag("simCaloStage2Digis"),
    MuonInputTag = cms.InputTag("simGmtStage2Digis"),
    Setup = cms.string('stage2::GTSetup'),
    ShowerInputLabel = cms.InputTag("simGmtShowerDigis"),
    TauInputTag = cms.InputTag("simCaloStage2Digis"),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.rawDataCollector = cms.EDProducer("RawDataCollectorByLabel",
    RawCollectionList = cms.VInputTag("packCaloStage2", "packGmtStage2", "packGtStage2", cms.InputTag("rawDataCollector","","@skipCurrentProcess")),
    verbose = cms.untracked.int32(0)
)


process.simBmtfDigis = cms.EDProducer("L1TMuonBarrelTrackProducer",
    DTDigi_Source = cms.InputTag("simTwinMuxDigis"),
    DTDigi_Theta_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    Debug = cms.untracked.int32(0)
)


process.simCaloStage2Digis = cms.EDProducer("L1TStage2Layer2Producer",
    firmware = cms.int32(1),
    towerToken = cms.InputTag("simCaloStage2Layer1Digis"),
    useStaticConfig = cms.bool(False)
)


process.simCaloStage2Layer1Digis = cms.EDProducer("L1TCaloLayer1",
    ecalToken = cms.InputTag("unpackEcal","EcalTriggerPrimitives"),
    firmwareVersion = cms.int32(3),
    hcalToken = cms.InputTag("simHcalTriggerPrimitiveDigis"),
    unpackEcalMask = cms.bool(False),
    unpackHcalMask = cms.bool(False),
    useCalib = cms.bool(True),
    useECALLUT = cms.bool(True),
    useHCALLUT = cms.bool(True),
    useHFLUT = cms.bool(True),
    useLSB = cms.bool(True),
    verbose = cms.bool(False)
)


process.simCscTriggerPrimitiveDigis = cms.EDProducer("CSCTriggerPrimitivesProducer",
    CSCComparatorDigiProducer = cms.InputTag("unpackCSC","MuonCSCComparatorDigi"),
    CSCWireDigiProducer = cms.InputTag("unpackCSC","MuonCSCWireDigi"),
    GEMPadDigiClusterProducer = cms.InputTag("simMuonGEMPadDigiClusters"),
    MaxBX = cms.int32(11),
    MinBX = cms.int32(5),
    alctPhase1 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(4),
        alctGhostCancellationSideQuality = cms.bool(False),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(False),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(4),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    alctPhase2 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    alctPhase2GEM = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    checkBadChambers = cms.bool(False),
    clctPhase1 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(10),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctStartBxShift = cms.int32(0),
        useDeadTimeZoning = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    clctPhase2 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        useDeadTimeZoning = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    clctPhase2GEM = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(3),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        useDeadTimeZoning = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    commonParam = cms.PSet(
        disableME1a = cms.bool(False),
        disableME42 = cms.bool(False),
        enableAlctPhase2 = cms.bool(False),
        gangedME1a = cms.bool(False),
        runCCLUT_OTMB = cms.bool(False),
        runCCLUT_TMB = cms.bool(False),
        runME11ILT = cms.bool(True),
        runME11Up = cms.bool(True),
        runME21ILT = cms.bool(False),
        runME21Up = cms.bool(True),
        runME31Up = cms.bool(True),
        runME41Up = cms.bool(True),
        runPhase2 = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    copadParamGE11 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(4),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    copadParamGE21 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(4),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    debugParameters = cms.bool(True),
    keepALCTPreTriggers = cms.bool(False),
    keepCLCTPreTriggers = cms.bool(True),
    keepShowers = cms.bool(True),
    mpcParam = cms.PSet(
        dropInvalidStubs = cms.bool(False),
        dropLowQualityStubs = cms.bool(False),
        maxStubs = cms.uint32(18),
        sortStubs = cms.bool(False)
    ),
    showerParam = cms.PSet(
        anodeShower = cms.PSet(
            minLayersCentralTBin = cms.uint32(5),
            showerMaxInTBin = cms.uint32(8),
            showerMaxOutTBin = cms.uint32(7),
            showerMinInTBin = cms.uint32(8),
            showerMinOutTBin = cms.uint32(4),
            showerThresholds = cms.vuint32(
                140, 140, 140, 20, 41,
                45, 8, 12, 16, 28,
                56, 58, 9, 18, 22,
                26, 55, 57, 8, 16,
                20, 31, 62, 64, 13,
                27, 31
            )
        ),
        cathodeShower = cms.PSet(
            minLayersCentralTBin = cms.uint32(5),
            showerMaxInTBin = cms.uint32(8),
            showerMaxOutTBin = cms.uint32(5),
            showerMinInTBin = cms.uint32(6),
            showerMinOutTBin = cms.uint32(2),
            showerThresholds = cms.vuint32(
                100, 100, 100, 19, 38,
                42, 8, 11, 15, 17,
                33, 35, 10, 20, 24,
                15, 31, 33, 9, 18,
                22, 17, 34, 36, 11,
                22, 26
            )
        ),
        source = cms.uint32(3)
    ),
    tmbPhase1 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        tmbDropUsedClcts = cms.bool(True),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(5),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(5),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2GE11 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        assignGEMCSCBending = cms.bool(False),
        buildLCTfromALCTCLCTand1GEM = cms.bool(True),
        buildLCTfromALCTCLCTand2GEM = cms.bool(True),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromALCTandGEM_ME1a = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM_ME1a = cms.bool(True),
        clctTrigEnable = cms.uint32(0),
        dropLowQualityALCTsNoGEMs = cms.bool(False),
        dropLowQualityCLCTsNoGEMs = cms.bool(True),
        dropLowQualityCLCTsNoGEMs_ME1a = cms.bool(True),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchEarliestGemsOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(5),
        matchWithHS = cms.bool(True),
        maxDeltaBXALCTGEM = cms.uint32(1),
        maxDeltaBXCLCTGEM = cms.uint32(2),
        maxDeltaHsEven = cms.uint32(7),
        maxDeltaHsEvenME1a = cms.uint32(5),
        maxDeltaHsOdd = cms.uint32(16),
        maxDeltaHsOddME1a = cms.uint32(12),
        mitigateSlopeByCosi = cms.bool(True),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        tmbDropUsedClcts = cms.bool(False),
        tmbDropUsedGems = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(5),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2GE21 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        assignGEMCSCBending = cms.bool(False),
        buildLCTfromALCTCLCTand1GEM = cms.bool(True),
        buildLCTfromALCTCLCTand2GEM = cms.bool(True),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(True),
        clctTrigEnable = cms.uint32(0),
        dropLowQualityALCTsNoGEMs = cms.bool(True),
        dropLowQualityCLCTsNoGEMs = cms.bool(True),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchEarliestGemsOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(5),
        matchWithHS = cms.bool(True),
        maxDeltaBXALCTGEM = cms.uint32(1),
        maxDeltaBXCLCTGEM = cms.uint32(2),
        maxDeltaHsEven = cms.uint32(3),
        maxDeltaHsOdd = cms.uint32(5),
        mitigateSlopeByCosi = cms.bool(True),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        tmbDropUsedClcts = cms.bool(False),
        tmbDropUsedGems = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(5),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    )
)


process.simCscTriggerPrimitiveDigisRun3 = cms.EDProducer("CSCTriggerPrimitivesProducer",
    CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi"),
    CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi"),
    GEMPadDigiClusterProducer = cms.InputTag("simMuonGEMPadDigiClusters"),
    MaxBX = cms.int32(11),
    MinBX = cms.int32(5),
    alctPhase1 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(4),
        alctGhostCancellationSideQuality = cms.bool(False),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(False),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(4),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    alctPhase2 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    alctPhase2GEM = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    checkBadChambers = cms.bool(False),
    clctPhase1 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(10),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctStartBxShift = cms.int32(0),
        useDeadTimeZoning = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    clctPhase2 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        useDeadTimeZoning = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    clctPhase2GEM = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(3),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        useDeadTimeZoning = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    commonParam = cms.PSet(
        disableME1a = cms.bool(False),
        disableME42 = cms.bool(False),
        enableAlctPhase2 = cms.bool(False),
        gangedME1a = cms.bool(False),
        runCCLUT_OTMB = cms.bool(True),
        runCCLUT_TMB = cms.bool(False),
        runME11ILT = cms.bool(True),
        runME11Up = cms.bool(True),
        runME21ILT = cms.bool(False),
        runME21Up = cms.bool(True),
        runME31Up = cms.bool(True),
        runME41Up = cms.bool(True),
        runPhase2 = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    copadParamGE11 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(4),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    copadParamGE21 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(4),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    debugParameters = cms.bool(True),
    keepALCTPreTriggers = cms.bool(False),
    keepCLCTPreTriggers = cms.bool(True),
    keepShowers = cms.bool(True),
    mpcParam = cms.PSet(
        dropInvalidStubs = cms.bool(False),
        dropLowQualityStubs = cms.bool(False),
        maxStubs = cms.uint32(18),
        sortStubs = cms.bool(False)
    ),
    showerParam = cms.PSet(
        anodeShower = cms.PSet(
            minLayersCentralTBin = cms.uint32(5),
            showerMaxInTBin = cms.uint32(8),
            showerMaxOutTBin = cms.uint32(7),
            showerMinInTBin = cms.uint32(8),
            showerMinOutTBin = cms.uint32(4),
            showerThresholds = cms.vuint32(
                140, 140, 140, 20, 41,
                45, 8, 12, 16, 28,
                56, 58, 9, 18, 22,
                26, 55, 57, 8, 16,
                20, 31, 62, 64, 13,
                27, 31
            )
        ),
        cathodeShower = cms.PSet(
            minLayersCentralTBin = cms.uint32(5),
            showerMaxInTBin = cms.uint32(8),
            showerMaxOutTBin = cms.uint32(5),
            showerMinInTBin = cms.uint32(6),
            showerMinOutTBin = cms.uint32(2),
            showerThresholds = cms.vuint32(
                100, 100, 100, 19, 38,
                42, 8, 11, 15, 17,
                33, 35, 10, 20, 24,
                15, 31, 33, 9, 18,
                22, 17, 34, 36, 11,
                22, 26
            )
        ),
        source = cms.uint32(3)
    ),
    tmbPhase1 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        tmbDropUsedClcts = cms.bool(True),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(5),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(5),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2GE11 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        assignGEMCSCBending = cms.bool(False),
        buildLCTfromALCTCLCTand1GEM = cms.bool(True),
        buildLCTfromALCTCLCTand2GEM = cms.bool(True),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromALCTandGEM_ME1a = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM_ME1a = cms.bool(True),
        clctTrigEnable = cms.uint32(0),
        dropLowQualityALCTsNoGEMs = cms.bool(False),
        dropLowQualityCLCTsNoGEMs = cms.bool(True),
        dropLowQualityCLCTsNoGEMs_ME1a = cms.bool(True),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchEarliestGemsOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(5),
        matchWithHS = cms.bool(True),
        maxDeltaBXALCTGEM = cms.uint32(1),
        maxDeltaBXCLCTGEM = cms.uint32(2),
        maxDeltaHsEven = cms.uint32(7),
        maxDeltaHsEvenME1a = cms.uint32(5),
        maxDeltaHsOdd = cms.uint32(16),
        maxDeltaHsOddME1a = cms.uint32(12),
        mitigateSlopeByCosi = cms.bool(True),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        tmbDropUsedClcts = cms.bool(False),
        tmbDropUsedGems = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(5),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2GE21 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        assignGEMCSCBending = cms.bool(False),
        buildLCTfromALCTCLCTand1GEM = cms.bool(True),
        buildLCTfromALCTCLCTand2GEM = cms.bool(True),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(True),
        clctTrigEnable = cms.uint32(0),
        dropLowQualityALCTsNoGEMs = cms.bool(True),
        dropLowQualityCLCTsNoGEMs = cms.bool(True),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchEarliestGemsOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(5),
        matchWithHS = cms.bool(True),
        maxDeltaBXALCTGEM = cms.uint32(1),
        maxDeltaBXCLCTGEM = cms.uint32(2),
        maxDeltaHsEven = cms.uint32(3),
        maxDeltaHsOdd = cms.uint32(5),
        mitigateSlopeByCosi = cms.bool(True),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        tmbDropUsedClcts = cms.bool(False),
        tmbDropUsedGems = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(5),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    )
)


process.simDtTriggerPrimitiveDigis = cms.EDProducer("DTTrigProd",
    DTTFSectorNumbering = cms.bool(True),
    debug = cms.untracked.bool(False),
    digiTag = cms.InputTag("unpackDT"),
    lutBtic = cms.untracked.int32(31),
    lutDumpFlag = cms.untracked.bool(False)
)


process.simEmtfDigis = cms.EDProducer("L1TMuonEndCapTrackProducer",
    BXWindow = cms.int32(2),
    CPPFEnable = cms.bool(False),
    CPPFInput = cms.InputTag("simCPPFDigis"),
    CSCComparatorInput = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi"),
    CSCEnable = cms.bool(True),
    CSCInput = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED"),
    CSCInputBXShift = cms.int32(-8),
    DTEnable = cms.bool(False),
    DTPhiInput = cms.InputTag("simTwinMuxDigis"),
    DTThetaInput = cms.InputTag("simDtTriggerPrimitiveDigis"),
    Era = cms.string('Run3_2021'),
    FWConfig = cms.bool(True),
    GEMEnable = cms.bool(False),
    GEMInput = cms.InputTag("simMuonGEMPadDigiClusters"),
    GEMInputBXShift = cms.int32(0),
    IRPCEnable = cms.bool(False),
    ME0Enable = cms.bool(False),
    ME0Input = cms.InputTag("me0TriggerConvertedPseudoDigis"),
    ME0InputBXShift = cms.int32(-8),
    MaxBX = cms.int32(3),
    MinBX = cms.int32(-3),
    RPCEnable = cms.bool(True),
    RPCInput = cms.InputTag("unpackRPC"),
    RPCInputBXShift = cms.int32(0),
    UseRun3CCLUT_OTMB = cms.bool(False),
    UseRun3CCLUT_TMB = cms.bool(False),
    spGCParams16 = cms.PSet(
        BugSameSectorPt0 = cms.bool(False),
        MaxRoadsPerZone = cms.int32(3),
        MaxTracks = cms.int32(3),
        UseSecondEarliest = cms.bool(True)
    ),
    spPAParams16 = cms.PSet(
        Bug9BitDPhi = cms.bool(False),
        BugGMTPhi = cms.bool(False),
        BugMode7CLCT = cms.bool(False),
        BugNegPt = cms.bool(False),
        FixMode15HighPt = cms.bool(True),
        ModeQualVer = cms.int32(2),
        PromoteMode7 = cms.bool(False),
        ProtobufFileName = cms.string('model_graph.displ.5.pb'),
        ReadPtLUTFile = cms.bool(False)
    ),
    spPCParams16 = cms.PSet(
        DuplicateTheta = cms.bool(True),
        FixME11Edges = cms.bool(True),
        FixZonePhi = cms.bool(True),
        IncludeNeighbor = cms.bool(True),
        UseNewZones = cms.bool(False),
        ZoneBoundaries = cms.vint32(0, 41, 49, 87, 127),
        ZoneOverlap = cms.int32(2)
    ),
    spPRParams16 = cms.PSet(
        PatternDefinitions = cms.vstring(
            '4,15:15,7:7,7:7,7:7',
            '3,16:16,7:7,7:6,7:6',
            '3,14:14,7:7,8:7,8:7',
            '2,18:17,7:7,7:5,7:5',
            '2,13:12,7:7,10:7,10:7',
            '1,22:19,7:7,7:0,7:0',
            '1,11:8,7:7,14:7,14:7',
            '0,30:23,7:7,7:0,7:0',
            '0,7:0,7:7,14:7,14:7'
        ),
        SymPatternDefinitions = cms.vstring(
            '4,15:15:15:15,7:7:7:7,7:7:7:7,7:7:7:7',
            '3,16:16:14:14,7:7:7:7,8:7:7:6,8:7:7:6',
            '2,18:17:13:12,7:7:7:7,10:7:7:4,10:7:7:4',
            '1,22:19:11:8,7:7:7:7,14:7:7:0,14:7:7:0',
            '0,30:23:7:0,7:7:7:7,14:7:7:0,14:7:7:0'
        ),
        UseSymmetricalPatterns = cms.bool(True)
    ),
    spTBParams16 = cms.PSet(
        BugAmbigThetaWin = cms.bool(False),
        BugME11Dupes = cms.bool(False),
        BugSt2PhDiff = cms.bool(False),
        ThetaWindow = cms.int32(8),
        ThetaWindowZone0 = cms.int32(4),
        TwoStationSameBX = cms.bool(True),
        UseSingleHits = cms.bool(False)
    ),
    verbosity = cms.untracked.int32(0)
)


process.simEmtfShowers = cms.EDProducer("L1TMuonEndCapShowerProducer",
    CSCShowerInput = cms.InputTag("simCscTriggerPrimitiveDigis"),
    enableOneNominalShowers = cms.bool(True),
    enableOneTightShowers = cms.bool(True),
    enableTwoLooseShowers = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    nLooseShowers = cms.uint32(2),
    nNominalShowers = cms.uint32(1),
    nTightShowers = cms.uint32(1)
)


process.simGmtCaloSumDigis = cms.EDProducer("L1TMuonCaloSumProducer",
    caloStage2Layer2Label = cms.InputTag("simCaloStage2Layer1Digis")
)


process.simGmtShowerDigis = cms.EDProducer("L1TMuonShowerProducer",
    bxMax = cms.int32(0),
    bxMin = cms.int32(0),
    mightGet = cms.optional.untracked.vstring,
    showerInput = cms.InputTag("simEmtfShowers","EMTF")
)


process.simGmtStage2Digis = cms.EDProducer("L1TMuonProducer",
    autoBxRange = cms.bool(True),
    autoCancelMode = cms.bool(False),
    barrelTFInput = cms.InputTag("simKBmtfDigis","BMTF"),
    bmtfCancelMode = cms.string('kftracks'),
    bxMax = cms.int32(2),
    bxMin = cms.int32(-2),
    emtfCancelMode = cms.string('coordinate'),
    forwardTFInput = cms.InputTag("simEmtfDigis","EMTF"),
    overlapTFInput = cms.InputTag("simOmtfDigis","OMTF"),
    triggerTowerInput = cms.InputTag("simGmtCaloSumDigis","TriggerTowerSums")
)


process.simGtExtFakeStage2Digis = cms.EDProducer("L1TExtCondProducer",
    bxFirst = cms.int32(-2),
    bxLast = cms.int32(2),
    setBptxAND = cms.bool(True),
    setBptxMinus = cms.bool(True),
    setBptxOR = cms.bool(True),
    setBptxPlus = cms.bool(True),
    tcdsRecordLabel = cms.InputTag("")
)


process.simGtStage2Digis = cms.EDProducer("L1TGlobalProducer",
    AlgoBlkInputTag = cms.InputTag("gtStage2Digis"),
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    EGammaInputTag = cms.InputTag("simCaloStage2Digis"),
    EtSumInputTag = cms.InputTag("simCaloStage2Digis"),
    ExtInputTag = cms.InputTag("simGtExtFakeStage2Digis"),
    GetPrescaleColumnFromData = cms.bool(False),
    JetInputTag = cms.InputTag("simCaloStage2Digis"),
    MuonInputTag = cms.InputTag("simGmtStage2Digis"),
    MuonShowerInputTag = cms.InputTag("simGmtShowerDigis"),
    RequireMenuToMatchAlgoBlkInput = cms.bool(False),
    TauInputTag = cms.InputTag("simCaloStage2Digis"),
    useMuonShowers = cms.bool(True)
)


process.simHcalTriggerPrimitiveDigis = cms.EDProducer("HcalTrigPrimDigiProducer",
    FG_HF_thresholds = cms.vuint32(17, 255),
    FG_threshold = cms.uint32(12),
    FrontEndFormatError = cms.bool(False),
    InputTagFEDRaw = cms.InputTag("rawDataCollector"),
    LSConfig = cms.untracked.PSet(
        HcalFeatureHFEMBit = cms.bool(False),
        Long_Short_Offset = cms.double(10.1),
        Long_vrs_Short_Slope = cms.double(100.2),
        Min_Long_Energy = cms.double(10),
        Min_Short_Energy = cms.double(10)
    ),
    MinSignalThreshold = cms.uint32(0),
    PMTNoiseThreshold = cms.uint32(0),
    PeakFinderAlgorithm = cms.int32(2),
    RunZS = cms.bool(False),
    ZS_threshold = cms.uint32(1),
    applySaturationFix = cms.bool(True),
    inputLabel = cms.VInputTag("unpackHcal", "unpackHcal"),
    inputUpgradeLabel = cms.VInputTag("unpackHcal", "unpackHcal"),
    latency = cms.int32(1),
    numberOfFilterPresamplesHBQIE11 = cms.int32(0),
    numberOfFilterPresamplesHEQIE11 = cms.int32(0),
    numberOfPresamples = cms.int32(2),
    numberOfPresamplesHF = cms.int32(1),
    numberOfSamples = cms.int32(4),
    numberOfSamplesHF = cms.int32(2),
    overrideDBweightsAndFilterHB = cms.bool(False),
    overrideDBweightsAndFilterHE = cms.bool(False),
    peakFilter = cms.bool(True),
    tpScales = cms.PSet(
        HBHE = cms.PSet(
            LSBQIE11 = cms.double(0.0625),
            LSBQIE11Overlap = cms.double(0.0625),
            LSBQIE8 = cms.double(0.125)
        ),
        HF = cms.PSet(
            NCTShift = cms.int32(2),
            RCTShift = cms.int32(3)
        )
    ),
    upgradeHB = cms.bool(True),
    upgradeHE = cms.bool(True),
    upgradeHF = cms.bool(True),
    useTDCInMinBiasBits = cms.bool(False),
    weights = cms.vdouble(1.0, 1.0),
    weightsQIE11 = cms.PSet(
        ieta1 = cms.vdouble(1.0, 1.0),
        ieta10 = cms.vdouble(1.0, 1.0),
        ieta11 = cms.vdouble(1.0, 1.0),
        ieta12 = cms.vdouble(1.0, 1.0),
        ieta13 = cms.vdouble(1.0, 1.0),
        ieta14 = cms.vdouble(1.0, 1.0),
        ieta15 = cms.vdouble(1.0, 1.0),
        ieta16 = cms.vdouble(1.0, 1.0),
        ieta17 = cms.vdouble(1.0, 1.0),
        ieta18 = cms.vdouble(1.0, 1.0),
        ieta19 = cms.vdouble(1.0, 1.0),
        ieta2 = cms.vdouble(1.0, 1.0),
        ieta20 = cms.vdouble(1.0, 1.0),
        ieta21 = cms.vdouble(1.0, 1.0),
        ieta22 = cms.vdouble(1.0, 1.0),
        ieta23 = cms.vdouble(1.0, 1.0),
        ieta24 = cms.vdouble(1.0, 1.0),
        ieta25 = cms.vdouble(1.0, 1.0),
        ieta26 = cms.vdouble(1.0, 1.0),
        ieta27 = cms.vdouble(1.0, 1.0),
        ieta28 = cms.vdouble(1.0, 1.0),
        ieta3 = cms.vdouble(1.0, 1.0),
        ieta4 = cms.vdouble(1.0, 1.0),
        ieta5 = cms.vdouble(1.0, 1.0),
        ieta6 = cms.vdouble(1.0, 1.0),
        ieta7 = cms.vdouble(1.0, 1.0),
        ieta8 = cms.vdouble(1.0, 1.0),
        ieta9 = cms.vdouble(1.0, 1.0)
    )
)


process.simKBmtfDigis = cms.EDProducer("L1TMuonBarrelKalmanTrackProducer",
    algoSettings = cms.PSet(
        aPhi = cms.vdouble(1.942, 0.01511, 0.01476, 0.009799),
        aPhiB = cms.vdouble(-1.508, -0.1237, -0.1496, -0.1333),
        aPhiBNLO = cms.vdouble(0.000331, 0, 0, 0),
        bPhi = cms.vdouble(-1, 0.18245, 0.20898, 0.17286),
        bPhiB = cms.vdouble(-1, 1.18245, 1.20898, 1.17286),
        chiSquare = cms.vdouble(0.0, 0.109375, 0.234375, 0.359375),
        chiSquareCut = cms.vint32(126, 126, 126, 126, 126),
        chiSquareCutCurvMax = cms.vint32(2500, 2500, 2500, 2500, 2500),
        chiSquareCutPattern = cms.vint32(7, 11, 13, 14, 15),
        chiSquareCutTight = cms.vint32(
            40, 126, 60, 126, 126,
            126
        ),
        combos1 = cms.vint32(),
        combos2 = cms.vint32(3),
        combos3 = cms.vint32(5, 6, 7),
        combos4 = cms.vint32(
            9, 10, 11, 12, 13,
            14, 15
        ),
        eLoss = cms.vdouble(0.000765, 0, 0, 0),
        etaLUT0 = cms.vdouble(8.946, 7.508, 6.279, 6.399),
        etaLUT1 = cms.vdouble(0.159, 0.116, 0.088, 0.128),
        initialK = cms.vdouble(-1.196, -1.581, -2.133, -2.263),
        initialK2 = cms.vdouble(-0.000326, -0.0007165, 0.002305, -0.00563),
        lutFile = cms.string('L1Trigger/L1TMuon/data/bmtf_luts/kalmanLUTs_v302.root'),
        mScatteringPhi = cms.vdouble(0.00249, 5.47e-05, 3.49e-05, 1.37e-05),
        mScatteringPhiB = cms.vdouble(0.00722, 0.003461, 0.004447, 0.00412),
        phiAt2 = cms.double(0.15918),
        pointResolutionPhi = cms.double(1.0),
        pointResolutionPhiB = cms.double(500.0),
        pointResolutionPhiBH = cms.vdouble(151.0, 173.0, 155.0, 153.0),
        pointResolutionPhiBL = cms.vdouble(17866.0, 19306.0, 23984.0, 23746.0),
        pointResolutionVertex = cms.double(1.0),
        trackComp = cms.vdouble(1.75, 1.25, 0.625, 0.25),
        trackCompCut = cms.vint32(
            15, 15, 15, 15, 15,
            15
        ),
        trackCompCutCurvMax = cms.vint32(
            34, 34, 34, 34, 34,
            34
        ),
        trackCompCutPattern = cms.vint32(
            3, 5, 6, 9, 10,
            12
        ),
        trackCompErr1 = cms.vdouble(2.0, 2.0, 2.0, 2.0),
        trackCompErr2 = cms.vdouble(0.21875, 0.21875, 0.21875, 0.3125),
        useOfflineAlgo = cms.bool(False),
        verbose = cms.bool(False)
    ),
    bx = cms.vint32(-2, -1, 0, 1, 2),
    src = cms.InputTag("simKBmtfStubs"),
    trackFinderSettings = cms.PSet(
        sectorSettings = cms.PSet(
            regionSettings = cms.PSet(
                verbose = cms.int32(0)
            ),
            verbose = cms.int32(0),
            wheelsToProcess = cms.vint32(-2, -1, 0, 1, 2)
        ),
        sectorsToProcess = cms.vint32(
            0, 1, 2, 3, 4,
            5, 6, 7, 8, 9,
            10, 11
        ),
        verbose = cms.int32(0)
    )
)


process.simKBmtfStubs = cms.EDProducer("L1TMuonBarrelKalmanStubProducer",
    cotTheta_1 = cms.vint32(
        105, 101, 97, 93, 88,
        84, 79, 69, 64, 58,
        52, 46, 40, 34, 21,
        14, 7, 0, -7, -14,
        -21, -34, -40, -46, -52,
        -58, -64, -69, -79, -84,
        -88, -93, -97, -101, -105
    ),
    cotTheta_2 = cms.vint32(
        93, 89, 85, 81, 77,
        73, 68, 60, 55, 50,
        45, 40, 34, 29, 17,
        12, 6, 0, -6, -12,
        -17, -29, -34, -40, -45,
        -50, -55, -60, -68, -73,
        -77, -81, -85, -89, -93
    ),
    cotTheta_3 = cms.vint32(
        81, 77, 74, 70, 66,
        62, 58, 51, 46, 42,
        38, 33, 29, 24, 15,
        10, 5, 0, -5, -10,
        -15, -24, -29, -33, -38,
        -42, -46, -51, -58, -62,
        -66, -70, -74, -77, -81
    ),
    disableMasks = cms.bool(False),
    maxBX = cms.int32(2),
    minBX = cms.int32(-2),
    minPhiQuality = cms.int32(0),
    minThetaQuality = cms.int32(0),
    srcPhi = cms.InputTag("simTwinMuxDigis"),
    srcTheta = cms.InputTag("simDtTriggerPrimitiveDigis"),
    verbose = cms.int32(0)
)


process.simMuonGEMPadDigiClusters = cms.EDProducer("GEMPadDigiClusterProducer",
    InputCollection = cms.InputTag("simMuonGEMPadDigis"),
    maxClusterSize = cms.uint32(8),
    maxClustersOHGE11 = cms.uint32(4),
    maxClustersOHGE21 = cms.uint32(5),
    mightGet = cms.optional.untracked.vstring,
    nOHGE11 = cms.uint32(2),
    nOHGE21 = cms.uint32(4),
    sendOverflowClusters = cms.bool(False)
)


process.simMuonGEMPadDigis = cms.EDProducer("GEMPadDigiProducer",
    InputCollection = cms.InputTag("simMuonGEMDigis"),
    mightGet = cms.optional.untracked.vstring
)


process.simOmtfDigis = cms.EDProducer("L1TMuonOverlapPhase1TrackProducer",
    XMLDumpFileName = cms.string('TestEvents.xml'),
    bxMax = cms.int32(0),
    bxMin = cms.int32(0),
    dropCSCPrimitives = cms.bool(False),
    dropDTPrimitives = cms.bool(False),
    dropRPCPrimitives = cms.bool(False),
    dumpDetailedResultToXML = cms.bool(False),
    dumpGPToXML = cms.bool(False),
    dumpResultToXML = cms.bool(False),
    eventsXMLFiles = cms.vstring('TestEvents.xml'),
    processorType = cms.string('OMTFProcessor'),
    readEventsFromXML = cms.bool(False),
    srcCSC = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED"),
    srcDTPh = cms.InputTag("simDtTriggerPrimitiveDigis"),
    srcDTTh = cms.InputTag("simDtTriggerPrimitiveDigis"),
    srcRPC = cms.InputTag("unpackRPC")
)


process.simTwinMuxDigis = cms.EDProducer("L1TTwinMuxProducer",
    DTDigi_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    DTThetaDigi_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    RPC_Source = cms.InputTag("unpackRPC")
)


process.unpackCSC = cms.EDProducer("CSCDCCUnpacker",
    B904Setup = cms.untracked.bool(False),
    Debug = cms.untracked.bool(False),
    DisableMappingCheck = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535558134),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    runDQM = cms.untracked.bool(False),
    useCSCShowers = cms.bool(True),
    useGEMs = cms.bool(False),
    useRPCs = cms.bool(False)
)


process.unpackDT = cms.EDProducer("DTuROSRawToDigi",
    debug = cms.untracked.bool(False),
    inputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess")
)


process.unpackEcal = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30,
        31, 32, 33, 34, 35,
        36, 37, 38, 39, 40,
        41, 42, 43, 44, 45,
        46, 47, 48, 49, 50,
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.unpackHcal = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(True),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    mightGet = cms.optional.untracked.vstring,
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)


process.unpackRPC = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    doSynchro = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltBoolFalse = cms.EDFilter("HLTBool",
    result = cms.bool(False)
)


process.hltCscClusterLoose = cms.EDFilter("HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag("hltCSCrechitClusters"),
    MaxEta = cms.double(-1.0),
    MaxSizeRegionCutEtas = cms.vdouble(1.9, 1.9, -1.0, -1.0),
    MaxSizeRegionCutNstations = cms.vint32(1, -1, 1, -1),
    MaxTime = cms.double(999.0),
    MaxTimeSpread = cms.double(-1.0),
    Max_nMB1 = cms.int32(-1),
    Max_nMB2 = cms.int32(-1),
    Max_nME11 = cms.int32(-1),
    Max_nME12 = cms.int32(-1),
    Max_nME41 = cms.int32(-1),
    Max_nME42 = cms.int32(-1),
    MinAvgStation = cms.double(0.0),
    MinEta = cms.double(-1.0),
    MinN = cms.int32(1),
    MinNstation = cms.int32(0),
    MinSize = cms.int32(-1),
    MinSizeMinusMB1 = cms.int32(-1),
    MinSizeRegionCutClusterSize = cms.vint32(200, 100, 500, 500),
    MinSizeRegionCutEtas = cms.vdouble(-1.0, -1.0, 1.9, 1.9),
    MinSizeRegionCutNstations = cms.vint32(-1, 1, -1, 1),
    MinTime = cms.double(-999.0)
)


process.hltCscClusterMedium = cms.EDFilter("HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag("hltCSCrechitClusters"),
    MaxEta = cms.double(-1.0),
    MaxSizeRegionCutEtas = cms.vdouble(1.9, 1.9, -1.0, -1.0),
    MaxSizeRegionCutNstations = cms.vint32(1, -1, 1, -1),
    MaxTime = cms.double(999.0),
    MaxTimeSpread = cms.double(-1.0),
    Max_nMB1 = cms.int32(-1),
    Max_nMB2 = cms.int32(-1),
    Max_nME11 = cms.int32(-1),
    Max_nME12 = cms.int32(-1),
    Max_nME41 = cms.int32(-1),
    Max_nME42 = cms.int32(-1),
    MinAvgStation = cms.double(0.0),
    MinEta = cms.double(-1.0),
    MinN = cms.int32(1),
    MinNstation = cms.int32(0),
    MinSize = cms.int32(-1),
    MinSizeMinusMB1 = cms.int32(-1),
    MinSizeRegionCutClusterSize = cms.vint32(300, 100, 800, 500),
    MinSizeRegionCutEtas = cms.vdouble(-1.0, -1.0, 1.9, 1.9),
    MinSizeRegionCutNstations = cms.vint32(-1, 1, -1, 1),
    MinTime = cms.double(-999.0)
)


process.hltCscClusterTight = cms.EDFilter("HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag("hltCSCrechitClusters"),
    MaxEta = cms.double(-1.0),
    MaxSizeRegionCutEtas = cms.vdouble(1.9, 1.9, -1.0, -1.0),
    MaxSizeRegionCutNstations = cms.vint32(1, -1, 1, -1),
    MaxTime = cms.double(999.0),
    MaxTimeSpread = cms.double(-1.0),
    Max_nMB1 = cms.int32(-1),
    Max_nMB2 = cms.int32(-1),
    Max_nME11 = cms.int32(-1),
    Max_nME12 = cms.int32(-1),
    Max_nME41 = cms.int32(-1),
    Max_nME42 = cms.int32(-1),
    MinAvgStation = cms.double(0.0),
    MinEta = cms.double(-1.0),
    MinN = cms.int32(1),
    MinNstation = cms.int32(0),
    MinSize = cms.int32(-1),
    MinSizeMinusMB1 = cms.int32(-1),
    MinSizeRegionCutClusterSize = cms.vint32(500, 100, 800, 500),
    MinSizeRegionCutEtas = cms.vdouble(-1.0, -1.0, 1.9, 1.9),
    MinSizeRegionCutNstations = cms.vint32(-1, 1, -1, 1),
    MinTime = cms.double(-999.0)
)


process.hltDTCluster50NoMB1 = cms.EDFilter("HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag("hltDTrechitClusters"),
    MaxEta = cms.double(-1.0),
    MaxSizeRegionCutEtas = cms.vdouble(1.9, 1.9, -1.0, -1.0),
    MaxSizeRegionCutNstations = cms.vint32(1, -1, 1, -1),
    MaxTime = cms.double(999.0),
    MaxTimeSpread = cms.double(-1.0),
    Max_nMB1 = cms.int32(0),
    Max_nMB2 = cms.int32(-1),
    Max_nME11 = cms.int32(-1),
    Max_nME12 = cms.int32(-1),
    Max_nME41 = cms.int32(-1),
    Max_nME42 = cms.int32(-1),
    MinAvgStation = cms.double(0.0),
    MinEta = cms.double(-1.0),
    MinN = cms.int32(1),
    MinNstation = cms.int32(0),
    MinSize = cms.int32(50),
    MinSizeMinusMB1 = cms.int32(-1),
    MinSizeRegionCutClusterSize = cms.vint32(-1, -1, -1, -1),
    MinSizeRegionCutEtas = cms.vdouble(-1.0, -1.0, 1.9, 1.9),
    MinSizeRegionCutNstations = cms.vint32(-1, 1, -1, 1),
    MinTime = cms.double(-999.0)
)


process.hltDTCluster75NoMB1 = cms.EDFilter("HLTMuonRecHitClusterFilter",
    ClusterTag = cms.InputTag("hltDTrechitClusters"),
    MaxEta = cms.double(-1.0),
    MaxSizeRegionCutEtas = cms.vdouble(1.9, 1.9, -1.0, -1.0),
    MaxSizeRegionCutNstations = cms.vint32(1, -1, 1, -1),
    MaxTime = cms.double(999.0),
    MaxTimeSpread = cms.double(-1.0),
    Max_nMB1 = cms.int32(0),
    Max_nMB2 = cms.int32(-1),
    Max_nME11 = cms.int32(-1),
    Max_nME12 = cms.int32(-1),
    Max_nME41 = cms.int32(-1),
    Max_nME42 = cms.int32(-1),
    MinAvgStation = cms.double(0.0),
    MinEta = cms.double(-1.0),
    MinN = cms.int32(1),
    MinNstation = cms.int32(0),
    MinSize = cms.int32(75),
    MinSizeMinusMB1 = cms.int32(-1),
    MinSizeRegionCutClusterSize = cms.vint32(-1, -1, -1, -1),
    MinSizeRegionCutEtas = cms.vdouble(-1.0, -1.0, 1.9, 1.9),
    MinSizeRegionCutNstations = cms.vint32(-1, 1, -1, 1),
    MinTime = cms.double(-999.0)
)


process.hltL1sMuShowerOneNominal = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_MuShower_OneNominal OR L1_MuShower_OneTight'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltPreCscClusterLoose = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("L1_MuShower_OneNominal OR L1_MuShower_OneTight"),
    offset = cms.uint32(0)
)


process.hltPreCscClusterMedium = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreCscClusterTight = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreL1CSCShowerDTCluster50 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreL1CSCShowerDTCluster75 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


process.hltGetConditions = cms.EDAnalyzer("EventSetupRecordDataGetter",
    toGet = cms.VPSet(),
    verbose = cms.untracked.bool(False)
)


process.hltGetRaw = cms.EDAnalyzer("HLTGetRaw",
    RawDataCollection = cms.InputTag("rawDataCollector")
)


process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string('DQMIO.root')
)


process.CUDAService = cms.Service("CUDAService",
    allocator = cms.untracked.PSet(
        devicePreallocate = cms.untracked.vuint32(),
        hostPreallocate = cms.untracked.vuint32()
    ),
    enabled = cms.untracked.bool(True),
    limits = cms.untracked.PSet(
        cudaLimitDevRuntimePendingLaunchCount = cms.untracked.int32(-1),
        cudaLimitDevRuntimeSyncDepth = cms.untracked.int32(-1),
        cudaLimitMallocHeapSize = cms.untracked.int32(-1),
        cudaLimitPrintfFifoSize = cms.untracked.int32(-1),
        cudaLimitStackSize = cms.untracked.int32(-1)
    ),
    verbose = cms.untracked.bool(False)
)


process.DQMStore = cms.Service("DQMStore",
    MEsToSave = cms.untracked.vstring(
        'DT/02-Segments/03-MeanT0/T0MeanAllWheels',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'Muons/MuonRecoAnalyzer/',
        'Muons/MuonIdDQM/GlobalMuons/',
        'PixelPhase1/Phase1_MechanicalView/',
        'PixelPhase1/Tracks/',
        'SiStrip/MechanicalView/',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/',
        'Tracking/TrackParameters/generalTracks/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/LSanalysis/',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/GeneralProperties/',
        'Tracking/TrackParameters/generalTracks/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/',
        'Tracking/TrackParameters/generalTracks/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/Pixel/',
        'Tracking/TrackParameters/generalTracks/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/Strip/'
    ),
    assertLegacySafe = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    saveByLumi = cms.untracked.bool(False),
    trackME = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)


process.FastTimerService = cms.Service("FastTimerService",
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    dqmMemoryRange = cms.untracked.double(1000000.0),
    dqmMemoryResolution = cms.untracked.double(5000.0),
    dqmModuleMemoryRange = cms.untracked.double(100000.0),
    dqmModuleMemoryResolution = cms.untracked.double(500.0),
    dqmModuleTimeRange = cms.untracked.double(40.0),
    dqmModuleTimeResolution = cms.untracked.double(0.2),
    dqmPath = cms.untracked.string('HLT/TimerService'),
    dqmPathMemoryRange = cms.untracked.double(1000000.0),
    dqmPathMemoryResolution = cms.untracked.double(5000.0),
    dqmPathTimeRange = cms.untracked.double(100.0),
    dqmPathTimeResolution = cms.untracked.double(0.5),
    dqmTimeRange = cms.untracked.double(2000.0),
    dqmTimeResolution = cms.untracked.double(5.0),
    enableDQM = cms.untracked.bool(True),
    enableDQMTransitions = cms.untracked.bool(False),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    enableDQMbyModule = cms.untracked.bool(False),
    enableDQMbyPath = cms.untracked.bool(False),
    enableDQMbyProcesses = cms.untracked.bool(True),
    jsonFileName = cms.untracked.string('resources.json'),
    printEventSummary = cms.untracked.bool(False),
    printJobSummary = cms.untracked.bool(True),
    printRunSummary = cms.untracked.bool(True),
    writeJSONSummary = cms.untracked.bool(False)
)


process.MessageLogger = cms.Service("MessageLogger",
    FastReport = cms.untracked.PSet(

    ),
    HLTrigReport = cms.untracked.PSet(

    ),
    L1GtTrigReport = cms.untracked.PSet(

    ),
    L1TGlobalSummary = cms.untracked.PSet(

    ),
    ThroughputService = cms.untracked.PSet(

    ),
    TriggerSummaryProducerAOD = cms.untracked.PSet(

    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        threshold = cms.untracked.string('INFO')
    ),
    debugModules = cms.untracked.vstring(),
    suppressDebug = cms.untracked.vstring(),
    suppressError = cms.untracked.vstring(
        'hltOnlineBeamSpot',
        'hltL3MuonCandidates',
        'hltL3TkTracksFromL2OIState',
        'hltPFJetCtfWithMaterialTracks',
        'hltL3TkTracksFromL2IOHit',
        'hltL3TkTracksFromL2OIHit'
    ),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(
        'hltOnlineBeamSpot',
        'hltCtf3HitL1SeededWithMaterialTracks',
        'hltL3MuonsOIState',
        'hltPixelTracksForHighMult',
        'hltHITPixelTracksHE',
        'hltHITPixelTracksHB',
        'hltCtfL1SeededWithMaterialTracks',
        'hltRegionalTracksForL3MuonIsolation',
        'hltSiPixelClusters',
        'hltActivityStartUpElectronPixelSeeds',
        'hltLightPFTracks',
        'hltPixelVertices3DbbPhi',
        'hltL3MuonsIOHit',
        'hltPixelTracks',
        'hltSiPixelDigis',
        'hltL3MuonsOIHit',
        'hltL1SeededElectronGsfTracks',
        'hltL1SeededStartUpElectronPixelSeeds',
        'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
        'hltCtfActivityWithMaterialTracks'
    )
)


process.ThroughputService = cms.Service("ThroughputService",
    dqmPath = cms.untracked.string('HLT/Throughput'),
    dqmPathByProcesses = cms.untracked.bool(False),
    enableDQM = cms.untracked.bool(True),
    eventRange = cms.untracked.uint32(10000),
    eventResolution = cms.untracked.uint32(1),
    printEventSummary = cms.untracked.bool(False),
    timeRange = cms.untracked.double(60000.0),
    timeResolution = cms.untracked.double(5.828)
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CSCIndexerESProducer = cms.ESProducer("CSCIndexerESProducer",
    AlgoName = cms.string('CSCIndexerPostls1')
)


process.CSCObjectMapESProducer = cms.ESProducer("CSCObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTPGTranscoder = cms.ESProducer("CaloTPGTranscoderULUTs",
    LUTfactor = cms.vint32(1, 2, 5, 0),
    RCTLSB = cms.double(0.25),
    ZS = cms.vint32(4, 2, 1, 0),
    hcalLUT1 = cms.FileInPath('CalibCalorimetry/CaloTPG/data/outputLUTtranscoder_physics.dat'),
    hcalLUT2 = cms.FileInPath('CalibCalorimetry/CaloTPG/data/TPGcalcDecompress2.txt'),
    ietaLowerBound = cms.vint32(1, 18, 27, 29),
    ietaUpperBound = cms.vint32(17, 26, 28, 32),
    linearLUTs = cms.bool(True),
    nominal_gain = cms.double(0.177),
    read_Ascii_Compression_LUTs = cms.bool(False),
    read_Ascii_RCT_LUTs = cms.bool(False),
    tpScales = cms.PSet(
        HBHE = cms.PSet(
            LSBQIE11 = cms.double(0.0625),
            LSBQIE11Overlap = cms.double(0.0625),
            LSBQIE8 = cms.double(0.125)
        ),
        HF = cms.PSet(
            NCTShift = cms.int32(2),
            RCTShift = cms.int32(3)
        )
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapAuto = cms.untracked.bool(False),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    )
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.DTObjectMapESProducer = cms.ESProducer("DTObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    appendToDataLabel = cms.string(''),
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.GlobalParameters = cms.ESProducer("StableParametersTrivialProducer",
    IfCaloEtaNumberBits = cms.uint32(4),
    IfMuEtaNumberBits = cms.uint32(6),
    NumberChips = cms.uint32(1),
    NumberConditionChips = cms.uint32(1),
    NumberL1CenJet = cms.uint32(4),
    NumberL1EGamma = cms.uint32(12),
    NumberL1ForJet = cms.uint32(4),
    NumberL1IsoEG = cms.uint32(4),
    NumberL1Jet = cms.uint32(12),
    NumberL1JetCounts = cms.uint32(12),
    NumberL1Mu = cms.uint32(4),
    NumberL1Muon = cms.uint32(8),
    NumberL1NoIsoEG = cms.uint32(4),
    NumberL1Tau = cms.uint32(12),
    NumberL1TauJet = cms.uint32(4),
    NumberPhysTriggers = cms.uint32(512),
    NumberPhysTriggersExtended = cms.uint32(64),
    NumberPsbBoards = cms.int32(7),
    NumberTechnicalTriggers = cms.uint32(64),
    OrderConditionChip = cms.vint32(1),
    OrderOfChip = cms.vint32(1),
    PinsOnChip = cms.uint32(512),
    PinsOnConditionChip = cms.uint32(512),
    TotalBxInEvent = cms.int32(5),
    UnitLength = cms.int32(8),
    WordLength = cms.int32(64),
    appendToDataLabel = cms.string('')
)


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.HcalTPGCoderULUT = cms.ESProducer("HcalTPGCoderULUT",
    FGLUTs = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/HBHE_FG_LUT.dat'),
    FG_HF_thresholds = cms.vuint32(17, 255),
    LUTGenerationMode = cms.bool(True),
    MaskBit = cms.int32(32768),
    RCalibFile = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/RecHit-TPG-calib.dat'),
    applyFixPCC = cms.bool(True),
    contain1TSHB = cms.bool(False),
    contain1TSHE = cms.bool(False),
    containPhaseNSHB = cms.double(6.0),
    containPhaseNSHE = cms.double(6.0),
    inputLUTs = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/inputLUTcoder_physics.dat'),
    linearLUTs = cms.bool(True),
    overrideDBweightsAndFilterHB = cms.bool(False),
    overrideDBweightsAndFilterHE = cms.bool(False),
    read_Ascii_LUTs = cms.bool(False),
    read_FG_LUTs = cms.bool(False),
    read_XML_LUTs = cms.bool(False),
    tpScales = cms.PSet(
        HBHE = cms.PSet(
            LSBQIE11 = cms.double(0.0625),
            LSBQIE11Overlap = cms.double(0.0625),
            LSBQIE8 = cms.double(0.125)
        ),
        HF = cms.PSet(
            NCTShift = cms.int32(2),
            RCTShift = cms.int32(3)
        )
    )
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.HcalTrigTowerGeometryESProducer = cms.ESProducer("HcalTrigTowerGeometryESProducer")


process.L1DTConfigFromDB = cms.ESProducer("DTConfigDBProducer",
    DTTPGMap = cms.untracked.PSet(
    **dict(
        [
            ("wh0st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh0st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh0st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh0st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh0st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh0st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh0st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh0st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh1st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se4" , cms.untracked.vint32(50, 48, 50, 13) ),
            ("wh1st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se4" , cms.untracked.vint32(60, 48, 60, 15) ),
            ("wh1st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se4" , cms.untracked.vint32(72, 48, 72, 18) ),
            ("wh1st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh1st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh1st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh1st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh1st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh1st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh1st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh1st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh2st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh2st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh2st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh2st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh2st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh2st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh2st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh2st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm1st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se3" , cms.untracked.vint32(50, 48, 50, 13) ),
            ("whm1st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se3" , cms.untracked.vint32(60, 48, 60, 15) ),
            ("whm1st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se3" , cms.untracked.vint32(72, 48, 72, 18) ),
            ("whm1st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm1st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm1st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm1st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm1st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm1st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm1st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm1st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
        ] +
        [
            ("whm2st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm2st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm2st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm2st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm2st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm2st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm2st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm2st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ]
        )
    ),
    DTTPGParameters = cms.PSet(
        Debug = cms.untracked.bool(False),
        SectCollParameters = cms.PSet(
            Debug = cms.untracked.bool(False),
            SCCSP1 = cms.int32(0),
            SCCSP2 = cms.int32(0),
            SCCSP3 = cms.int32(0),
            SCCSP4 = cms.int32(0),
            SCCSP5 = cms.int32(0),
            SCECF1 = cms.bool(False),
            SCECF2 = cms.bool(False),
            SCECF3 = cms.bool(False),
            SCECF4 = cms.bool(False)
        ),
        TUParameters = cms.PSet(
            BtiParameters = cms.PSet(
                AC1 = cms.int32(0),
                AC2 = cms.int32(3),
                ACH = cms.int32(1),
                ACL = cms.int32(2),
                CH = cms.int32(41),
                CL = cms.int32(22),
                DEAD = cms.int32(31),
                Debug = cms.untracked.int32(0),
                KACCTHETA = cms.int32(1),
                KMAX = cms.int32(64),
                LH = cms.int32(21),
                LL = cms.int32(2),
                LTS = cms.int32(3),
                PTMS0 = cms.int32(0),
                PTMS1 = cms.int32(0),
                PTMS10 = cms.int32(1),
                PTMS11 = cms.int32(1),
                PTMS12 = cms.int32(1),
                PTMS13 = cms.int32(1),
                PTMS14 = cms.int32(1),
                PTMS15 = cms.int32(1),
                PTMS16 = cms.int32(1),
                PTMS17 = cms.int32(1),
                PTMS18 = cms.int32(1),
                PTMS19 = cms.int32(1),
                PTMS2 = cms.int32(0),
                PTMS20 = cms.int32(1),
                PTMS21 = cms.int32(1),
                PTMS22 = cms.int32(1),
                PTMS23 = cms.int32(1),
                PTMS24 = cms.int32(1),
                PTMS25 = cms.int32(1),
                PTMS26 = cms.int32(1),
                PTMS27 = cms.int32(1),
                PTMS28 = cms.int32(1),
                PTMS29 = cms.int32(1),
                PTMS3 = cms.int32(0),
                PTMS30 = cms.int32(0),
                PTMS31 = cms.int32(0),
                PTMS4 = cms.int32(1),
                PTMS5 = cms.int32(1),
                PTMS6 = cms.int32(1),
                PTMS7 = cms.int32(1),
                PTMS8 = cms.int32(1),
                PTMS9 = cms.int32(1),
                RE43 = cms.int32(2),
                RH = cms.int32(61),
                RL = cms.int32(42),
                RON = cms.bool(True),
                SET = cms.int32(7),
                ST43 = cms.int32(42),
                WEN0 = cms.int32(1),
                WEN1 = cms.int32(1),
                WEN2 = cms.int32(1),
                WEN3 = cms.int32(1),
                WEN4 = cms.int32(1),
                WEN5 = cms.int32(1),
                WEN6 = cms.int32(1),
                WEN7 = cms.int32(1),
                WEN8 = cms.int32(1),
                XON = cms.bool(False)
            ),
            Debug = cms.untracked.bool(False),
            LutParameters = cms.PSet(
                BTIC = cms.untracked.int32(0),
                D = cms.untracked.double(0),
                Debug = cms.untracked.bool(False),
                WHEEL = cms.untracked.int32(-1),
                XCN = cms.untracked.double(0)
            ),
            TSPhiParameters = cms.PSet(
                Debug = cms.untracked.bool(False),
                TSMCCE1 = cms.bool(True),
                TSMCCE2 = cms.bool(False),
                TSMCCEC = cms.bool(False),
                TSMCGS1 = cms.bool(True),
                TSMCGS2 = cms.bool(True),
                TSMGS1 = cms.int32(1),
                TSMGS2 = cms.int32(1),
                TSMHSP = cms.int32(1),
                TSMHTE1 = cms.bool(True),
                TSMHTE2 = cms.bool(False),
                TSMHTEC = cms.bool(False),
                TSMMSK1 = cms.int32(312),
                TSMMSK2 = cms.int32(312),
                TSMNOE1 = cms.bool(True),
                TSMNOE2 = cms.bool(False),
                TSMNOEC = cms.bool(False),
                TSMWORD = cms.int32(255),
                TSSCCE1 = cms.bool(True),
                TSSCCE2 = cms.bool(False),
                TSSCCEC = cms.bool(False),
                TSSCGS1 = cms.bool(True),
                TSSCGS2 = cms.bool(True),
                TSSGS1 = cms.int32(1),
                TSSGS2 = cms.int32(1),
                TSSHTE1 = cms.bool(True),
                TSSHTE2 = cms.bool(False),
                TSSHTEC = cms.bool(False),
                TSSMSK1 = cms.int32(312),
                TSSMSK2 = cms.int32(312),
                TSSNOE1 = cms.bool(True),
                TSSNOE2 = cms.bool(False),
                TSSNOEC = cms.bool(False),
                TSTREN0 = cms.bool(True),
                TSTREN1 = cms.bool(True),
                TSTREN10 = cms.bool(True),
                TSTREN11 = cms.bool(True),
                TSTREN12 = cms.bool(True),
                TSTREN13 = cms.bool(True),
                TSTREN14 = cms.bool(True),
                TSTREN15 = cms.bool(True),
                TSTREN16 = cms.bool(True),
                TSTREN17 = cms.bool(True),
                TSTREN18 = cms.bool(True),
                TSTREN19 = cms.bool(True),
                TSTREN2 = cms.bool(True),
                TSTREN20 = cms.bool(True),
                TSTREN21 = cms.bool(True),
                TSTREN22 = cms.bool(True),
                TSTREN23 = cms.bool(True),
                TSTREN3 = cms.bool(True),
                TSTREN4 = cms.bool(True),
                TSTREN5 = cms.bool(True),
                TSTREN6 = cms.bool(True),
                TSTREN7 = cms.bool(True),
                TSTREN8 = cms.bool(True),
                TSTREN9 = cms.bool(True)
            ),
            TSThetaParameters = cms.PSet(
                Debug = cms.untracked.bool(False)
            ),
            TracoParameters = cms.PSet(
                BTIC = cms.int32(32),
                DD = cms.int32(18),
                Debug = cms.untracked.int32(0),
                FHISM = cms.int32(0),
                FHTMSK = cms.int32(0),
                FHTPRF = cms.int32(1),
                FLTMSK = cms.int32(1),
                FPRGCOMP = cms.int32(2),
                FSLMSK = cms.int32(0),
                IBTIOFF = cms.int32(0),
                KPRGCOM = cms.int32(255),
                KRAD = cms.int32(0),
                LTF = cms.int32(0),
                LTS = cms.int32(0),
                LVALIDIFH = cms.int32(0),
                REUSEI = cms.int32(1),
                REUSEO = cms.int32(1),
                SHISM = cms.int32(0),
                SHTMSK = cms.int32(0),
                SHTPRF = cms.int32(1),
                SLTMSK = cms.int32(1),
                SPRGCOMP = cms.int32(2),
                SSLMSK = cms.int32(0),
                TRGENB0 = cms.int32(1),
                TRGENB1 = cms.int32(1),
                TRGENB10 = cms.int32(1),
                TRGENB11 = cms.int32(1),
                TRGENB12 = cms.int32(1),
                TRGENB13 = cms.int32(1),
                TRGENB14 = cms.int32(1),
                TRGENB15 = cms.int32(1),
                TRGENB2 = cms.int32(1),
                TRGENB3 = cms.int32(1),
                TRGENB4 = cms.int32(1),
                TRGENB5 = cms.int32(1),
                TRGENB6 = cms.int32(1),
                TRGENB7 = cms.int32(1),
                TRGENB8 = cms.int32(1),
                TRGENB9 = cms.int32(1)
            )
        )
    ),
    TracoLutsFromDB = cms.bool(True),
    UseBtiAcceptParam = cms.bool(True),
    UseT0 = cms.bool(False),
    bxOffset = cms.int32(19),
    cfgConfig = cms.bool(False),
    debug = cms.bool(False),
    debugBti = cms.int32(0),
    debugDB = cms.bool(False),
    debugLUTs = cms.bool(False),
    debugPed = cms.bool(False),
    debugSC = cms.bool(False),
    debugTSP = cms.bool(False),
    debugTST = cms.bool(False),
    debugTU = cms.bool(False),
    debugTraco = cms.int32(0),
    finePhase = cms.double(25.0)
)


process.L1TriggerMenu = cms.ESProducer("L1TUtmTriggerMenuESProducer",
    L1TriggerMenuFile = cms.string('L1Menu_Collisions2022_v0_1_2.xml')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOppositeForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PixelCPEFastESProducer = cms.ESProducer("PixelCPEFastESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEFast'),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    isPhase2 = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStep'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.RPCConeBuilder = cms.ESProducer("RPCConeBuilder",
    towerBeg = cms.int32(0),
    towerEnd = cms.int32(16)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiStripClusterizerConditionsESProducer = cms.ESProducer("SiStripClusterizerConditionsESProducer",
    Label = cms.string(''),
    QualityLabel = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SiStripRegionConnectivity = cms.ESProducer("SiStripRegionConnectivity",
    EtaDivisions = cms.untracked.uint32(20),
    EtaMax = cms.untracked.double(2.5),
    PhiDivisions = cms.untracked.uint32(20)
)


process.SimpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    minVertices = cms.uint32(1),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.TrackerAdditionalParametersPerDetESModule = cms.ESProducer("TrackerAdditionalParametersPerDetESModule",
    appendToDataLabel = cms.string('')
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloConfig = cms.ESProducer("L1TCaloConfigESProducer",
    fwVersionLayer2 = cms.uint32(3),
    l1Epoch = cms.string('Stage1')
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.ctppsGeometryESModule = cms.ESProducer("CTPPSGeometryESModule",
    appendToDataLabel = cms.string(''),
    buildMisalignedGeometry = cms.bool(False),
    compactViewTag = cms.string(''),
    dbTag = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromPreprocessedDB = cms.untracked.bool(True),
    isRun2 = cms.bool(False),
    verbosity = cms.untracked.uint32(1)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string('')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring(
            'kNonRespondingIsolated',
            'kDeadVFE',
            'kDeadFE',
            'kNoDataNoTP'
        ),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring(
            'kDAC',
            'kNoLaser',
            'kNoisy',
            'kNNoisy',
            'kNNNoisy',
            'kNNNNoisy',
            'kNNNNNoisy',
            'kFixedG6',
            'kFixedG1',
            'kFixedG0'
        ),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring(
            'kFaultyHardware',
            'kDead',
            'kKilled'
        ),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring(
            'kPoorReco',
            'kPoorCalib',
            'kNoisy',
            'kSaturated'
        ),
        kRecovered = cms.vstring(
            'kLeadingEdgeRecovered',
            'kTowerRecovered'
        ),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring(
            'kWeird',
            'kDiWeird'
        )
    ),
    timeThresh = cms.double(2.0)
)


process.fakeTwinMuxParams = cms.ESProducer("L1TTwinMuxParamsESProducer",
    CorrectDTBxwRPC = cms.bool(True),
    dphiWindowBxShift = cms.uint32(9999),
    fwVersion = cms.uint32(1),
    useLowQDT = cms.bool(False),
    useOnlyDT = cms.bool(False),
    useOnlyRPC = cms.bool(False),
    useRpcBxForDtBelowQuality = cms.uint32(4),
    verbose = cms.bool(False)
)


process.hcalChannelPropertiesESProd = cms.ESProducer("HcalChannelPropertiesEP")


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring(
        'HcalCellMask',
        'HcalCellOff',
        'HcalCellDead'
    ),
    RecoveredRecHitBits = cms.vstring(),
    SeverityLevels = cms.VPSet(
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(0),
            RecHitFlags = cms.vstring('TimingFromTDC')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring(
                'HBHEHpdHitMultiplicity',
                'HBHEIsolatedNoise',
                'HBHEFlatNoise',
                'HBHESpikeNoise',
                'HBHETS4TS5Noise',
                'HBHENegativeNoise',
                'HBHEPulseFitBit',
                'HBHEOOTPU'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring(
                'HFLongShort',
                'HFS8S1Ratio',
                'HFPET',
                'HFSignalAsymmetry'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(
                'HcalCellOff',
                'HcalCellDead'
            ),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring()
        )
    ),
    appendToDataLabel = cms.string(''),
    phase = cms.uint32(1)
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_v4.weights.xml.gz')
)


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertex',
        'CombinedSVPseudoVertex',
        'CombinedSVNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltCombinedSecondaryVertexV2 = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex',
        'CombinedSVIVFV2PseudoVertex',
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2ChargeLooseMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeLooseMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator2000 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    MaxChi2 = cms.double(2000.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutForHI')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2MeasurementEstimator100 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator100'),
    MaxChi2 = cms.double(40.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator30 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D'),
    MaxComponents = cms.int32(12)
)


process.hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.2),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.2),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerCorrection = cms.int32(2),
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    Mass = cms.double(0.000511),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator')
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPKFFittingSmootherForLoopers'),
    standardFitter = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK')
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPGsfTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    ErrorRescaling = cms.double(100.0),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2MeasurementEstimator36 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2MeasurementEstimator36'),
    MaxChi2 = cms.double(36.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherForLoopers'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPRKTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPRKTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPMixedStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPMixedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMixedTripletStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPMixedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder')
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    NoTemplateErrorsWhenNoTrkAngles = cms.bool(False),
    SmallPitch = cms.bool(False),
    TruncatePixelCharge = cms.bool(True),
    Upgrade = cms.bool(False),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(False),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPETemplateReco = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPETemplateReco'),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    appendToDataLabel = cms.string(''),
    barrelTemplateID = cms.int32(0),
    directoryWithTemplates = cms.int32(0),
    doLorentzFromAlignment = cms.bool(False),
    forwardTemplateID = cms.int32(0),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    speed = cms.int32(-2),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True)
)


process.hltESPPixelLessStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPPixelLessStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelLessStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPPixelPairStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPPixelPairStepChi2MeasurementEstimator25 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2MeasurementEstimator25'),
    MaxChi2 = cms.double(25.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPPixelPairTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelPairTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.hltESPRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPRKTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPRKTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    distance = cms.double(0.5)
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPStripCPEfromTrackAngle = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle')
)


process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPETemplateReco'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.hltESPTobTecStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPTobTecStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPTobTecStepFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmoother'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    standardFitter = cms.string('hltESPTobTecStepFitterSmoother')
)


process.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTobTecStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.09)
)


process.hltESPTrackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('hltESPTrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(),
    appendToDataLabel = cms.string('')
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    appendToDataLabel = cms.string(''),
    trackerGeometryLabel = cms.untracked.string(''),
    usePhase2Stacks = cms.bool(False)
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    ValidHitBonus = cms.double(100.0),
    allowSharedFirstHit = cms.bool(False),
    fractionShared = cms.double(0.5)
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltPixelTracksCleanerBySharedHits = cms.ESProducer("PixelTrackCleanerBySharedHitsESProducer",
    ComponentName = cms.string('hltPixelTracksCleanerBySharedHits'),
    appendToDataLabel = cms.string(''),
    useQuadrupletAlgo = cms.bool(False)
)


process.hltTrackCleaner = cms.ESProducer("TrackCleanerESProducer",
    ComponentName = cms.string('hltTrackCleaner'),
    appendToDataLabel = cms.string('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.muonSeededTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(1.0),
    ValidHitBonus = cms.double(1000.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.1)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    siPixelQualityLabel = cms.string('')
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CSCChannelMapperESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCChannelMapperRecord')
)


process.CSCINdexerESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCIndexerRecord')
)


process.CSCL1TPLookupTableEP = cms.ESSource("CSCL1TPLookupTableEP",
    esDiffToSlopeME1aFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME1a_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME1a_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME1a_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME1a_odd.txt'
    ),
    esDiffToSlopeME1bFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME1b_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME1b_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME1b_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME1b_odd.txt'
    ),
    esDiffToSlopeME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME21_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME21_odd.txt'
    ),
    gemCscSlopeCorrectionFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCSlopeCorr_ME11_even_GE11_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCSlopeCorr_ME11_even_GE11_layer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCSlopeCorr_ME11_odd_GE11_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCSlopeCorr_ME11_odd_GE11_layer2.txt'
    ),
    gemCscSlopeCosiCorrectionFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11_even_GE11_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11_even_GE11_layer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11_odd_GE11_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11_odd_GE11_layer2.txt'
    ),
    gemCscSlopeCosiFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11_even_GE11_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11_odd_GE11_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11_even_GE11_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11_odd_GE11_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11_even_GE11_layer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11_odd_GE11_layer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11_even_GE11_layer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11_odd_GE11_layer2.txt'
    ),
    padToEsME1aFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1a_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1a_odd.txt'
    ),
    padToEsME1bFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1b_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1b_odd.txt'
    ),
    padToEsME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME21_odd.txt'
    ),
    padToHsME1aFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME1a_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME1a_odd.txt'
    ),
    padToHsME1bFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME1b_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME1b_odd.txt'
    ),
    padToHsME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME21_odd.txt'
    ),
    positionLUTFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat0_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat1_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat2_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat3_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat4_v1.txt'
    ),
    rollToMaxWgME11Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME11_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME11_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME11_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME11_odd.txt'
    ),
    rollToMaxWgME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME21_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME21_odd.txt'
    ),
    rollToMinWgME11Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME11_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME11_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME11_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME11_odd.txt'
    ),
    rollToMinWgME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME21_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME21_odd.txt'
    ),
    slopeLUTFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat0_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat1_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat2_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat3_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat4_v1.txt'
    )
)


process.GlobalParametersRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TGlobalParametersRcd')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(0),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('123X_mcRun3_2021_realistic_v6'),
    pfnPostfix = cms.untracked.string('None'),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.bmbtfParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TMuonBarrelParamsRcd')
)


process.caloConfigSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TCaloConfigRcd')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.l1ugmtdb = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('L1TMuonGlobalParamsO2ORcd'),
        tag = cms.string('L1TMuonGlobalParamsPrototype_Stage2v0_hlt')
    ))
)


process.ppsPixelTopologyESSource = cms.ESSource("PPSPixelTopologyESSource",
    PitchSimX = cms.double(0.1),
    PitchSimY = cms.double(0.15),
    RunType = cms.string('Run3'),
    activeEdgeSigma = cms.double(0.02),
    appendToDataLabel = cms.string(''),
    deadEdgeWidth = cms.double(0.2),
    noOfPixelSimX = cms.int32(160),
    noOfPixelSimY = cms.int32(104),
    noOfPixels = cms.int32(16640),
    physActiveEdgeDist = cms.double(0.15),
    simXWidth = cms.double(16.6),
    simYWidth = cms.double(16.2),
    thickness = cms.double(0.23)
)


process.rpcconesrc = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1RPCConeBuilderRcd')
)


process.twinmuxParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TTwinMuxParamsRcd')
)


process.prefer("L1TriggerMenu")

process.SimL1TCalorimeterTask = cms.Task(process.simCaloStage2Digis, process.simCaloStage2Layer1Digis)


process.SimL1TGlobalTask = cms.Task(process.simGtStage2Digis)


process.SimL1TMuonCommonTask = cms.Task(process.simCscTriggerPrimitiveDigis, process.simDtTriggerPrimitiveDigis)


process.SimL1TechnicalTriggersTask = cms.Task(process.simGtExtFakeStage2Digis)


process.simMuonGEMPadTask = cms.Task(process.simMuonGEMPadDigiClusters, process.simMuonGEMPadDigis)


process.SimL1TMuonTask = cms.Task(process.SimL1TMuonCommonTask, process.simBmtfDigis, process.simCscTriggerPrimitiveDigisRun3, process.simEmtfDigis, process.simEmtfShowers, process.simGmtCaloSumDigis, process.simGmtShowerDigis, process.simGmtStage2Digis, process.simKBmtfDigis, process.simKBmtfStubs, process.simMuonGEMPadTask, process.simOmtfDigis, process.simTwinMuxDigis)


process.SimL1EmulatorCoreTask = cms.Task(process.SimL1TCalorimeterTask, process.SimL1TGlobalTask, process.SimL1TMuonTask, process.SimL1TechnicalTriggersTask)


process.SimL1EmulatorTask = cms.Task(process.SimL1EmulatorCoreTask, process.packCaloStage2, process.packGmtStage2, process.packGtStage2, process.rawDataCollector, process.simHcalTriggerPrimitiveDigis, process.unpackCSC, process.unpackDT, process.unpackEcal, process.unpackHcal, process.unpackRPC)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtStage2Digis+process.hltGtStage2ObjectMap)


process.HLTBeamSpot = cms.Sequence(process.hltScalersRawToDigi+process.hltOnlineMetaDataDigis+process.hltOnlineBeamSpot)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTMuonLocalRecoSequence = cms.Sequence(process.hltMuonDTDigis+process.hltDt1DRecHits+process.hltDt4DSegments+process.hltMuonCSCDigis+process.hltCsc2DRecHits+process.hltCscSegments+process.hltMuonRPCDigis+process.hltRpcRecHits+process.hltMuonGEMDigis+process.hltGemRecHits+process.hltGemSegments)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.SimL1Emulator = cms.Sequence(process.SimL1EmulatorTask)


process.HLTriggerFirstPath = cms.Path(process.SimL1Emulator+process.hltGetConditions+process.hltGetRaw+process.hltPSetMap+process.hltBoolFalse)


process.HLT_CscCluster_Loose_v0 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sMuShowerOneNominal+process.hltPreCscClusterLoose+process.HLTMuonLocalRecoSequence+process.hltCSCrechitClusters+process.hltCscClusterLoose+process.HLTEndSequence)


process.HLT_CscCluster_Medium_v0 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sMuShowerOneNominal+process.hltPreCscClusterMedium+process.HLTMuonLocalRecoSequence+process.hltCSCrechitClusters+process.hltCscClusterMedium+process.HLTEndSequence)


process.HLT_CscCluster_Tight_v0 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sMuShowerOneNominal+process.hltPreCscClusterTight+process.HLTMuonLocalRecoSequence+process.hltCSCrechitClusters+process.hltCscClusterTight+process.HLTEndSequence)


process.HLT_L1CSCShower_DTCluster50_v0 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sMuShowerOneNominal+process.hltPreL1CSCShowerDTCluster50+process.HLTMuonLocalRecoSequence+process.hltDTrechitClusters+process.hltDTCluster50NoMB1+process.HLTEndSequence)


process.HLT_L1CSCShower_DTCluster75_v0 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sMuShowerOneNominal+process.hltPreL1CSCShowerDTCluster75+process.HLTMuonLocalRecoSequence+process.hltDTrechitClusters+process.hltDTCluster75NoMB1+process.HLTEndSequence)


process.HLTriggerFinalPath = cms.Path(process.SimL1Emulator+process.hltGtStage2Digis+process.hltScalersRawToDigi+process.hltFEDSelector+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)


process.DQMOutput = cms.EndPath(process.dqmOutput)


process.schedule = cms.Schedule(*[ process.HLTriggerFirstPath, process.HLT_CscCluster_Loose_v0, process.HLT_CscCluster_Medium_v0, process.HLT_CscCluster_Tight_v0, process.HLT_L1CSCShower_DTCluster50_v0, process.HLT_L1CSCShower_DTCluster75_v0, process.HLTriggerFinalPath, process.DQMOutput ])

