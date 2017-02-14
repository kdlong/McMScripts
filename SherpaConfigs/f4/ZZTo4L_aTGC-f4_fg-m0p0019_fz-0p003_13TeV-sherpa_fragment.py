import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
    SherpaProcess = cms.string('m0p0019I0p003'),
    SherpaParameters = cms.PSet(
        parameterSets = cms.vstring('MPI_Cross_Sections', 
            'Run'),
        Run = cms.vstring('(run){', 
            ' EVENTS 1M; ERROR 0.1;', 
            ' MASSIVE_PS 4 5;', 
            ' FSF:=1.; RSF:=1.; QSF:=1.;', 
            ' SCALES STRICT_METS{FSF*MU_F2}{RSF*MU_R2}{QSF*MU_Q2};', 
            ' NJET:=2; LJET:=3,4; QCUT:=20.;', 
            ' ME_SIGNAL_GENERATOR Amegic;', 
            ' EVENT_GENERATION_MODE Unweighted;', 
            ' MASSIVE[15] 1;', 
            ' BEAM_1 2212; BEAM_ENERGY_1 6500.;', 
            ' BEAM_2 2212; BEAM_ENERGY_2 6500.;', 
            ' MODEL SM+AGC;', 
            ' F4_Z     0.003', 
            ' F4_GAMMA -0.0019', 
            ' UNITARIZATION_SCALE 1000000;', 
            ' UNITARIZATION_N 2;', 
            ' UNITARIZATION_M 1;', 
            '}(run)', 
            '(processes){', 
            ' Process 93 93 -> 90 90 90 90;', 
            '}(processes)', 
            '(selector){', 
            ' Mass 11 -11 4. 1000000.;', 
            ' Mass 13 -13 4. 1000000.;', 
            '}(selector)'),
        MPI_Cross_Sections = cms.vstring(' MPIs in Sherpa, Model = Amisic:', 
            ' semihard xsec = 74.5722 mb,', 
            ' non-diffractive xsec = 18.1593 mb with nd factor = 0.335.')
    ),
    filterEfficiency = cms.untracked.double(1.0),
    FetchSherpack = cms.bool(True),
    SherpackChecksum = cms.string('c1bd3a3f209037c4ae8d6052f22e95bc'),
    SherpaResultDir = cms.string('Result'),
    SherpaPath = cms.string('./'),
    crossSection = cms.untracked.double(-1),
    maxEventsToPrint = cms.int32(0),
    SherpaPathPiece = cms.string('./'),
    SherpackLocation = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/sherpa/V2.1.1/ZZTo4L_aTGC-f4'),
    SherpaDefaultWeight = cms.double(1.0)
)

ProductionFilterSequence = cms.Sequence(generator)