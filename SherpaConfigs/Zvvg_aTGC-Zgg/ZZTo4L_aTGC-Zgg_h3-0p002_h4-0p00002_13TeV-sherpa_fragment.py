import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
    SherpaProcess = cms.string('0p002I0p00002'),
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
            ' H3_GAMMA 0.002;', 
            ' H4_GAMMA 0.00002;', 
            ' UNITARIZATION_SCALE 100000;', 
            ' UNITARIZATION_N 2;', 
            ' UNITARIZATION_M 1;', 
            '}(run)', 
            '(processes){', 
            ' Process 93 93 -> 91 91 22;', 
            ' Order_EW 3; CKKW sqr(QCUT/E_CMS);', 
            '}(processes)', 
            '(selector){', 
            ' PT2 91 91 150. E_CMS;', 
            ' PT  22    150. E_CMS;', 
            ' IsolationCut 22 0.4 2 0.025;', 
            '}(selector)'),
        MPI_Cross_Sections = cms.vstring(' MPIs in Sherpa, Model = Amisic:', 
            ' semihard xsec = 73.929 mb,', 
            ' non-diffractive xsec = 18.1593 mb with nd factor = 0.335.')
    ),
    filterEfficiency = cms.untracked.double(1.0),
    FetchSherpack = cms.bool(True),
    SherpackChecksum = cms.string('2d62952ba7f8c651914f353734356dbc'),
    SherpaResultDir = cms.string('Result'),
    SherpaPath = cms.string('./'),
    crossSection = cms.untracked.double(-1),
    maxEventsToPrint = cms.int32(0),
    SherpaPathPiece = cms.string('./'),
    SherpackLocation = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/sherpa/V2.1.1/ZZTo4L_aTGC-f4'),
    SherpaDefaultWeight = cms.double(1.0)
)

ProductionFilterSequence = cms.Sequence(generator)
