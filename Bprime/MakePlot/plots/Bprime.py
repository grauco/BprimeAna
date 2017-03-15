
met_range = (0,2000, True)


# title,    scale,  rebin, usrrng
settings = {
#    'h_htcheck':('', 1,1, (0,2000)),
#    'h_htbprimemass':('', None, None, None),
#    'h_ht_presel'           : ('H_{T} (GeV)', 10, 5, (1200,2000)),
#    'h_nfatjet_opt'          : ("AK8 jets multiplicity", 10, 1, None),
#    'h_nGoodPV'               : ("Number of Primary Vertices", 1000, 1, (0, 30)),
#    'h_nGoodPVw'           : ("Number of Primary Vertices", 1000, 1, (0, 30)),
    #'h_AK4bphilead'    :("Leading bjet #phi", 100, 1, None ),
    'h_nPV'               : ("Number of Primary Vertices", 1000, 3, (0, 75)),
    'h_nPV_w'           : ("Number of Primary Vertices", 1000, 3, (0, 75)),
    'h_nHiggsCand_A'    : ("Higgs jet multiplicity", 100, 1, None),
    'h_nHiggsCand_B'    : ("Higgs jet multiplicity", 100, 1, None),
    'h_nHiggsCand_C'    : ("Higgs jet multiplicity", 100, 1, None),
    'h_nHiggsCand_D'    : ("Higgs jet multiplicity", 100, 1, None),
    'h_bCandpt_A'       : ("b-jet p_{T} (GeV)", 100, 4, None),
    'h_bCandeta_A'     : ("b-jet #eta", 100, 4, None),
    'h_bCandphi_A'     : ("b-jet #phi", 100, 4, None),
    'h_hCandpt_A'       : ("Higgs-jet p_{T} (GeV)", 100, 4, None),
    'h_hCandeta_A'     : ("Higgs-jet #eta", 100, 4, None),
    'h_hCandphi_A'     : ("Higgs-jet #phi", 100, 4, None),
    'h_bCandmult_A'     : ("b-jet multiplicity", 100, 1, None),
#        'h_bCandpt_CRB'       : ("b-jet p_{T} (GeV)", 100, 4, None),
#    'h_bCandeta_CRB'     : ("b-jet #eta", 100, 4, None),
#    'h_bCandphi_CRB'     : ("b-jet #phi", 100, 4, None),
#    'h_hCandpt_CRB'       : ("Higgs-jet p_{T} (GeV)", 100, 4, None),
#    'h_hCandeta_CRB'     : ("Higgs-jet #eta", 100, 4, None),
#    'h_hCandphi_CRB'     : ("Higgs-jet #phi", 100, 4, None),
#    'h_bCandmult_CRB'     : ("b-jet multiplicity", 100, 1, None),

#    'h_bCandpt_CRC'       : ("b-jet p_{T} (GeV)", 100, 4, None),
#    'h_bCandeta_CRC'     : ("b-jet #eta", 100, 4, None),
#    'h_bCandphi_CRC'     : ("b-jet #phi", 100, 4, None),
#    'h_hCandpt_CRC'       : ("Higgs-jet p_{T} (GeV)", 100, 4, None),
#    'h_hCandeta_CRC'     : ("Higgs-jet #eta", 100, 4, None),
#    'h_hCandphi_CRC'     : ("Higgs-jet #phi", 100, 4, None),
#    'h_bCandmult_CRC'     : ("b-jet multiplicity", 100, 1, None),

#    'h_bCandpt_CRD'       : ("b-jet p_{T} (GeV)", 100, 4, None),
#    'h_bCandeta_CRD'     : ("b-jet #eta", 100, 4, None),
#    'h_bCandphi_CRD'     : ("b-jet #phi", 100, 4, None),
#    'h_hCandpt_CRD'       : ("Higgs-jet p_{T} (GeV)", 100, 4, None),
#    'h_hCandeta_CRD'     : ("Higgs-jet #eta", 100, 4, None),
#    'h_hCandphi_CRD'     : ("Higgs-jet #phi", 100, 4, None),
#    'h_bCandmult_CRD'     : ("b-jet multiplicity", 100, 1, None),

    'h_bjetpt'     : ("b-jet p_{T} (GeV)", 100, 2, None),
    'h_bjeteta'     : ("b-jet #eta", 100, 2, None),
    'h_bjetphi'     : ("b-jet #phi", 100, 1, None),
    'h_bjetmult'     : ("b-jet multiplicity", 100, 1, None),
    #    'h_deltaRbH'        : ("#DeltaR(b,H)", 100, 10, None),
    'h_AK4fwjets'      : ("AK4 forward jet multiplicity", 100, 1, None),
    'h_AK4cjets'      : ("AK4 central jet multiplicity", 100, 1, None),
    'h_AK4bjets'      : ("AK4 b-tagged jet multiplicity", 100, 1, None),
    #'h_AK4bjetmultaft'      : ("AK4 b-tagged jet multiplicity", 100, 1, None),
    #    'h_AK4fwjets_SR'      : ("AK4 forward jet multiplicity", 1, 1, (0, 10)),
    'h_AK4mult'        : ("AK4 jet multiplicity", 100, 1, (0,10)),
    #'h_AK4mult aft'        : ("AK4 jet multiplicity", 100, 1, (0,10)),
    'h_AK4bmult'        : ("CSVM AK4 jet multiplicity", 100, 1, (0,5)),
    'h_AK8mult'        : ("AK8 jet multiplicity", 100, 1, (0,10)),
    #'h_AK8mult aft'        : ("AK8 jet multiplicity", 100, 1, (0,10)),
    'h_AK4pt'        : ("AK4 jet p_{T} (GeV)", 100, 4, (30,500)),
    'h_AK4eta'        : ("AK4 jet #eta (GeV)", 100, 1, None),
    'h_AK4phi'        : ("AK4 jet #phi (GeV)", 100, 4, (-3.5, 3.5)),
#   'h_AK4csv'        : ("AK4 jet CSVv2", 100, 2, None),
    'h_fwjetmult'    : ("AK4 forward jet multiplicity", 10, 1, None),
    'h_AK4bmultaft'  : ("AK4 b-tagged jet multiplicity", 10, 1, None),
    'h_AK4multaft'  : ("AK4 jet multiplicity", 10, 1, None),
    'h_AK4bmultaft_nH'  :("AK4 b-tagged jet multiplicity", 10, 1, None),
    'h_AK8pt'        : ("AK8 jet p_{T} (GeV)", 100, 4, (300,1000)),
    'h_AK8eta'        : ("AK8 jet #eta (GeV)", 100, 4, None),
    'h_AK8phi'        : ("AK8 jet #phi (GeV)", 100, 4, (-3.5, 3.5)),
    'h_AK4fwjetpt'   : ("forward jets p_{T}", 100, 1, (30, 700)),
    'h_AK4cjetpt'   : ("central jets p_{T}", 100, 1, (30, 500)),
    'h_AK4bjetpt'   : ("b-tagged jets p_{T}", 100, 1, (30, 700)),
    'h_AK4fwjeteta'   : ("forward jets #eta", 100, 1, None),
    'h_AK4cjeteta'   : ("central jets #eta", 100, 1, None),
    'h_AK4bjeteta'   : ("b-tagged jets #eta", 100, 1, None),
    'h_nsubj'        : ("Number of subjets", 100, 1, None),
    'h_tau2tau1'       : ("N-subjetiness",100, 2, None),
    'h_prunedmass'       : ("AK8 pruned mass (GeV)", 100, 2,(0,300)),
    'h_Ht'                  : ('H_{T} (GeV)', 1000, 20, (1000,2500)),#
    'h_Ht_bef'                  : ('H_{T} (GeV)', 1000, 20, (1000,2500)),#
    'h_Ht_SR'                  : ('H_{T} (GeV)', 1, 20, (200,2500)),# 
    'h_Ht_trigaft'                  : ('H_{T} (GeV)', 10, 10, (0,2500)),
#    'h_Ht_trigbef'                  : ('H_{T} (GeV)', 10, 10, (200,2500)),
    'h_Ht_CRD'                  : ('H_{T} (GeV)', 10, 20, (200,2500)),
    'h_Ht_CRC'                  : ('H_{T} (GeV)', 10, 20, (200,2500)),
    'h_Ht_CRB'                  : ('H_{T} (GeV)', 10, 20, (200,2500)),
#    'h_Ht_trigbef'                  : ('H_{T} (GeV)', 10, 20, (600,2500)),
    'h_AK4ptlead'          : ('leading AK4 jet p_{T} (GeV)', 100, 4, None),
    'h_AK4bptlead'       : ('leading AK4 CSVM jet p_{T} (GeV)', 100, 4, None),
    'h_AK4fwptlead'       : ('leading AK4 forward jet p_{T} (GeV)', 100, 2, None),
    'h_AK4ptsublead'       : ('subleading AK4 jet p_{T} (GeV)', 100, 4, None),
    'h_AK4bptsublead'       : ('subleading AK4 CSVM jet p_{T} (GeV)', 100, 4, None),
    'h_AK4fwptsublead'       : ('subleading AK4 forward jet p_{T} (GeV)', 100, 4, None),

    'h_AK4etalead'       : ('leading AK4 jet #eta ', 100, 4, None),
    'h_AK4betalead'       : ('leading AK4 CSVM jet #eta ', 100, 4, None),
    'h_AK4fwetalead'       : ('leading AK4 forward jet #eta ', 100, 4, None),
    'h_AK4etasublead'       : ('subleading AK4 jet #eta ', 100, 4, None),
    'h_AK4betasublead'       : ('subleading AK4 CSVM jet #eta ', 100, 4, None),
    'h_AK4fwetasublead'       : ('subleading AK4 forward jet #eta ', 100, 4, None),


    'h_AK4philead'       : ('leading AK4 jet #phi ', 100, 4, (-3.5,3.5)),
    'h_AK4bphilead'       : ('leading AK4 CSVM jet #phi ', 100, 4, (-3.5,3.5)),
    'h_AK4fwphilead'       : ('leading AK4 forward jet #phi ', 100, 4, (-3.5,3.5)),
    'h_AK4phisublead'       : ('subleading AK4 jet #phi ', 100, 4, (-3.5,3.5)),
    'h_AK4bphisublead'       : ('subleading AK4 CSVM jet #phi ', 100, 4, (-3.5,3.5)),
    'h_AK4fwphisublead'       : ('subleading AK4 forward jet #phi ', 100, 4, (-3.5,3.5)),

    'h_nsubj_SR'        : ("Number of subjets", 10, 1, None),
    'h_tau2tau1_SR'       : ("N-subjetiness",1, 2, None),
    'h_prunedmass_SR'       : ("AK8 pruned mass (GeV)", 10, 2,(0,300)),
    'h_AK8_selh_pt_SR'        : ("Higgs-tagged jet p_{T} (GeV)", 10, 4, None),
    'h_AK8_selh_eta_SR'        : ("Higgs-tagged jet #eta", 10, 4, None),
    'h_AK8_selh_phi_SR'        : ("Higgs-tagged jet #phi", 10, 4, (-3.5,3.5)),
    'h_AK4_selb_pt_SR'        : ("b-tagged jet p_{T} (GeV)", 10, 4, None),
    'h_AK4_selb_eta_SR'        : ("b-tagged jet #eta", 10, 4, None),
    'h_AK4_selb_phi_SR'        : ("b-tagged jet #phi", 10, 4, (-3.5,3.5)),######

    'h_AK8_selh_pt_CRB'        : ("Higgs-tagged jet p_{T} (GeV)", 10, 4, None),
    'h_AK8_selh_eta_CRB'        : ("Higgs-tagged jet #eta", 10, 4, None),
    'h_AK8_selh_phi_CRB'        : ("Higgs-tagged jet #phi", 10, 4, (-3.5,3.5)),
    'h_nsubj_CRB'        : ("Number of subjets", 10, 1, None),
    'h_tau2tau1_CRB'       : ("N-subjetiness",10, 2, None),
    'h_prunedmass_CRB'       : ("AK8 pruned mass (GeV)", 10, 2,(0,300)),
    'h_AK4_selb_pt_CRB'        : ("b-tagged jet p_{T} (GeV)", 10, 4, None),
    'h_AK4_selb_eta_CRB'        : ("b-tagged jet #eta", 10, 4, None),
    'h_AK4_selb_phi_CRB'        : ("b-tagged jet #phi", 10, 4, (-3.5,3.5)),####
    'h_AK8_selh_pt_CRC'        : ("Higgs-tagged jet p_{T} (GeV)", 10, 4, None),
    'h_AK8_selh_eta_CRC'        : ("Higgs-tagged jet #eta", 10, 4, None),
    'h_AK8_selh_phi_CRC'        : ("Higgs-tagged jet #phi", 10, 4, (-3.5,3.5)),
    'h_nsubj_CRC'        : ("Number of subjets", 10, 1, None),
    'h_tau2tau1_CRC'       : ("N-subjetiness",10, 2, None),
    'h_prunedmass_CRC'       : ("AK8 pruned mass (GeV)", 10, 2,(0,300)),
    'h_AK4_selb_pt_CRC'        : ("b-tagged jet p_{T} (GeV)", 10, 4, None),
    'h_AK4_selb_eta_CRC'        : ("b-tagged jet #eta", 10, 4, None),
    'h_AK4_selb_phi_CRC'        : ("b-tagged jet #phi", 10, 4, (-3.5,3.5)),##
    'h_AK8_selh_pt_CRD'        : ("Higgs-tagged jet p_{T} (GeV)", 10, 4, None),
    'h_AK8_selh_eta_CRD'        : ("Higgs-tagged jet #eta", 10, 4, None),
    'h_AK8_selh_phi_CRD'        : ("Higgs-tagged jet #phi", 10, 4, (-3.5,3.5)),
    'h_nsubj_CRD'        : ("Number of subjets", 10, 1, None),
    'h_tau2tau1_CRD'       : ("N-subjetiness",10, 2, None),
    'h_prunedmass_CRD'       : ("AK8 pruned mass (GeV)", 10, 2,(0,300)),
    'h_AK4_selb_pt_CRD'        : ("b-tagged jet p_{T} (GeV)", 10, 4, None),
    'h_AK4_selb_eta_CRD'        : ("b-tagged jet #eta", 10, 4, None),
    'h_AK4_selb_phi_CRD'        : ("b-tagged jet #phi", 10, 4, (-3.5,3.5)),##

    'h_bprimemass_SR'          : ("Reconstructed B' mass (GeV)", 10, 20, (500,2300)),
    #'h_bprimemass_SR_1'          : ("Reconstructed B' mass (GeV)", 10, 20, (400,2700)),
    #'h_bprimemass_SR_2'          : ("Reconstructed B' mass (GeV)", 10, 20, (400,2700)),
    #'h_bprimemass_SR_3'          : ("Reconstructed B' mass (GeV)", 10, 20, (400,2700)),
    #'h_bprimemass_SR_4'          : ("Reconstructed B' mass (GeV)", 10, 20, (400,2700)),
    #'h_bprimemass_SR_5'          : ("Reconstructed B' mass (GeV)", 10, 20, (400,2700)),
    'h_bprimemass_CRC'        : ("Reconstructed B' mass (GeV)", 10, 20, (500,2300)),
    'h_bprimemass_CRB'        : ("Reconstructed B' mass (GeV)", 10, 20, (500,2300)),
    'h_bprimemass_CRD'        : ("Reconstructed B' mass (GeV)", 10, 20, (500,2300)),##

    'h_bprimept_SR'          : ("Reconstructed B' p_{T} (GeV)", 10, 4, None),
    'h_bprimept_CRC'        : ("Reconstructed B' p_{T} (GeV)", 10, 4, None),
    'h_bprimept_CRB'        : ("Reconstructed B' p_{T} (GeV)", 10, 4, None),
    'h_bprimept_CRD'        : ("Reconstructed B' p_{T} (GeV)", 10, 4, None),###

    'h_bprimeeta_SR'          : ("Reconstructed B' #eta (GeV)", 10, 4, None),
    'h_bprimeeta_CRC'        : ("Reconstructed B' #eta (GeV)", 10, 4, None),
    'h_bprimeeta_CRB'        : ("Reconstructed B' #eta (GeV)", 10, 4, None),
    'h_bprimeeta_CRD'        : ("Reconstructed B' #eta (GeV)", 10, 4, None),###

    'h_bprimephi_SR'          : ("Reconstructed B' #phi (GeV)", 10, 4, (-3.5,3.5)),
    'h_bprimephi_CRC'        : ("Reconstructed B' #phi (GeV)", 10, 4, (-3.5,3.5)),
    'h_bprimephi_CRB'        : ("Reconstructed B' #phi (GeV)", 10, 4, (-3.5,3.5)),
    'h_bprimephi_CRD'        : ("Reconstructed B' #phi (GeV)", 10, 4, (-3.5,3.5)),


#    'h_bprimept_SR'        : ("Reconstructed B' p_{T} (GeV)", 100, 2, None),
#    'h_bprimept_CRB'        : ("Reconstructed B' p_{T} (GeV)", 100, 2, None),
#    'h_bprimept_CRC'        : ("Reconstructed B' p_{T} (GeV)", 100, 2, None),
#    'h_bprimept_CRD'        : ("Reconstructed B' p_{T} (GeV)", 100, 2, None),

 #   'h_bprimeeta_SR'        : ("Reconstructed B' #eta ", 1, 2, None),
 #   'h_bprimeeta_CRB'        : ("Reconstructed B' #eta ", 1, 2, None),
 #   'h_bprimeeta_CRC'        : ("Reconstructed B' #eta ", 1, 2, None),
  #  'h_bprimeeta_CRD'        : ("Reconstructed B' #eta ", 1, 2, None),



    #    'h_ht_b'                  : ('H_{T} (GeV)', 10, 5, (200,2000)),
#    'h_ht_c'                  : ('H_{T} (GeV)', 10, 5, (200,2000)),
#    'h_ht_d'                  : ('H_{T} (GeV)', 10, 5, (200,2000)),
#    'h_ht_antib'            : ('H_{T} (GeV)', 10, 5, (1200,2000)),
#    'h_ht_santib'           : ('H_{T} (GeV)', 10, 5, (1200,2000)),
#    'h_ht_sb'               : ('H_{T} (GeV)', 10, 5, (1200,2000)),

#    'h_bprimemass_b'        : ('Mass (GeV)', 10, 2, None),
#    'h_bprimemass_c'        : ('Mass (GeV)', 10, 2, None),
#    'h_bprimemass_d'        : ('Mass (GeV)', 10, 2, None),

#    'h_ht_closure'          : ('H_{T} (GeV)', 10, 10, None),
#    'h_ht_antib_closure'    : ('H_{T} (GeV)', 10, 10, None),
#    'h_ht_santib_closure'   : ('H_{T} (GeV)', 10, 10, None),
#    'h_ht_sb_closure'       : ('H_{T} (GeV)', 10, 10, None),

#    'h_bprimemassbbreg1'          : ('Mass (GeV)', 10, 2, None),
#    'h_bprimemassbbreg2'          : ('Mass (GeV)', 10, 2, None),

#    'h_bprimemassbbregm1'          : ('Mass (GeV)', 10, 2, None),
#    'h_bprimemassnobbreg1'          : ('Mass (GeV)', 10, 2, None),
#    'h_bprimemassnobbreg2'          : ('Mass (GeV)', 10, 2, None),
#    'h_bprimemassnobbregm1'          : ('Mass (GeV)', 10, 2, None),
    
#    'h_bprimemass_doubleb04'          : ('Mass (GeV)', 10, 4, None),
#    'h_bprimemass_doubleb06'          : ('Mass (GeV)', 10, 4, None),
#    'h_bprimemass_doubleb08'          : ('Mass (GeV)', 10, 4, None),

#    'h_bprimemass_a0'          : ('Mass (GeV)', 10, 4, None),
#    'h_bprimemass_a1'          : ('Mass (GeV)', 10, 4, None),
#    'h_bprimemass_a2'          : ('Mass (GeV)', 10, 4, None),
#    'h_bprimemass_a3'          : ('Mass (GeV)', 10, 4, None),
    
#    'h_bprimemass_a'          : ('Mass (GeV)', 1, 4, None),
#    'h_bprimemass_b'          : ('Mass (GeV)', 1, 4, None),
#    'h_bprimemass_c'          : ('Mass (GeV)', 1, 4, None),
#    'h_bprimemass_d'          : ('Mass (GeV)', 1, 4, None),

#    'h_bprimemass_a_closure'          : ('Mass (GeV)', 10, 4, None),
#    'h_bprimemass_b_closure'          : ('Mass (GeV)', 10, 4, None),
#    'h_bprimemass_c_closure'          : ('Mass (GeV)', 10, 4, None),
#    'h_bprimemass_d_closure'          : ('Mass (GeV)', 10, 4, None),

#    'h_genfwqpt'            : ('p_{T} (GeV)', 10, 4, None),
#    'h_genfwqeta'           : ('#eta', 10, 5, None),
#    'h_genfwqphi'            : ('#phi', 10, 7, None),

#    'h_jetpt'               : ('p_{T} (GeV)', 10, 4, None),
#    'h_jeteta'              : ('#eta', 10, 5, None),
#    'h_jetphi'              : ('#phi', 10, 7, None),
#    'h_njet'                : ('AK4 jets multiplicity', 10, None, None),
    
#    'h_bjetpt'              : ('p_{T} (GeV)', 10, 4, None),
#    'h_bjeteta'             : ('#eta', 10, 5, None),
#    'h_bjetphi'             : ('#phi', 10, 7, None),
#    'h_nbjet'               : ('CVSM AK4 jets multiplicity', 10, None, None),

#    'h_nqcjet'              : ('forward jets multiplicity', 10, None, None),
#    'h_qcjetpt'            : ('p_{T} (GeV)', 10, 4, None),
#    'h_qcjeteta'           : ('#eta', 10, 5, None),

#    'h_deltaRb1'            : ("#DeltaR(reco b, gen b)", 10, 10, None),
#    'h_deltaRb2'            : ("#DeltaR(reco b, gen b)", 10, 10, None),
#    'h_matching'            : ("", 10, None, None),
#    'h_higgsjet_pt_a'   : ('p_{T} (GeV)', 10, 10, None),
#    'h_nhiggsjet_mass_presel' : ('Mass (GeV)',10, 10, None),
    
#    'h_nhiggsjet_nsubj_presel' : ('number of subjets', 10, 1, None),
#    'h_nhiggsjet_nsubj_a' : ('number of subjets', 10, 1,None),
#    'h_nhiggsjet_nsubj_b' : ('number of subjets', 10, 1,None),
#    'h_nhiggsjet_nsubj_c' : ('number of subjets', 10, 1,None),
#    'h_nhiggsjet_nsubj_d' : ('number of subjets', 10, 1,None),

#    'h_nhiggsjet_doubleB_presel'       : ('Double b-tag', 10, 1, None),
#    'h_nhiggsjet_doubleB_a'       : ('Double b-tag', 10, 1, None),
#    'h_nhiggsjet_doubleB_b'       : ('Double b-tag', 10, 1, None),
#    'h_nhiggsjet_doubleB_c'       : ('Double b-tag', 10, 1, None),
#    'h_nhiggsjet_doubleB_d'       : ('Double b-tag', 10, 1, None),
#    'h_fatjetpt'            : ('p_{T} (GeV)', 10, 4, None),
#    'h_fatjeteta'           : ('#eta', 10, 5, None),
#    'h_fatjetphi'           : ('#phi', 10, 7, None),
#    'h_nfatjet'             : ('AK8 jets multiplicity', 10, None, None),
#    'h_fatjetncsvmsubjets'  : ('CSVM subjets multiplicity', 10, None, None),
#    'h_fatjetprunedmass'    : ('pruned mass (GeV)', 10, None, None),
#    'h_fatjetnsubjetiness'  : ('#tau_{2}/#tau_{1}', 10, None, None),
#    'h_fatjetleadpt'        : ('Leading AK8 jet p_{T} (GeV)', 10, 4, None),
#    'h_fatjetsubleadpt'     : ('Sub-leading AK8 jet p_{T} (GeV)', 10, 4, None),

#    'h_higgspt'             : ('p_{T} (GeV)', 10, 4, None),
#    'h_higgseta'            : ('#eta', 10, 5, None),
#    'h_higgsphi'            : ('#phi', 10, 7, None),
#    'h_nhiggsjet'           : ('Higgs-tagged jets multiplicity', 10, None, None),#
#    'h_duobleb'             : ('double b-tagging cut', 10, 1, None),
    'h_cutFlow'             : ('', 10, None, None),
}


store = [
    'h_AK4fwjetpt',
    'h_AK4bmultaft_nH',
#    'h_htcheck',
 #   'h_htbprimemass',
    'h_cutFlow',
#    'h_duobleb',
    'h_Ht',
    'h_Ht_trigbef',
#    'h_HiggsmassVSnsubj_presel',
    'h_bprimemass_SR',
       'h_bprimemass_SR_1',

       'h_bprimemass_SR_2',

       'h_bprimemass_SR_3',

       'h_bprimemass_SR_4',

       'h_bprimemass_SR_5',

    'h_bprimemass_CRB',
     'h_bprimemass_CRD',
     'h_bprimemass_CRC',
        'h_Ht_SR',
     'h_Ht_CRB',
     'h_Ht_CRD',
     'h_Ht_CRC',
    #    'h_bprimemass_doubleb06', 
#    'h_bprimemass_doubleb08',
#    'h_nhiggsjet_doubleB_presel',
#    'h_nhiggsjet_mass_presel',
#    'h_nhiggsjet_nsubj_presel',
#    'h_njet_opt',
##    'h_nfatjet_opt',
#    'h_ht_a',
#    'h_ht_b',
#    'h_ht_c',
#    'h_ht_d',
    #   'h_ht_antib',
 #   'h_ht_santib',
 #   'h_ht_sb',
 #   'h_ht_closure',
 #   'h_ht_antib_closure',
 #   'h_ht_santib_closure',
 #   'h_ht_sb_closure',
#    'h_bprimemass_a_closure',
#    'h_bprimemass_b_closure',
#    'h_bprimemass_c_closure',
#    'h_bprimemass_d_closure',
#    'h_bprimemass_a',
#    'h_bprimemass_a0',
#    'h_bprimemass_a1',
#    'h_bprimemass_a2',
#    'h_bprimemass_a3',
#    'h_bprimemass_b',
#    'h_bprimemass_c',
#    'h_bprimemass_d',
#    'met_preS',
#    'metFinal',
#    'metFinal_tag',
#    'metFinal_untag',
#    "metFinal_Angular",
#    "metFinal_Angular_tag",
#    "metFinal_Angular_untag",
]
