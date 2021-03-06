import ROOT
import tdrstyle, CMS_lumi
#from services_sign import Histo, Stack, Legend, deltaPhi, Histo1

ROOT.gROOT.Reset();
ROOT.gROOT.SetStyle('Plain')
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()        # don't pop up canvases                                                                         
ROOT.TH1.SetDefaultSumw2()
ROOT.TH1.AddDirectory(False)

tdrstyle.setTDRStyle();

file_mc = ROOT.TFile("puMC.root", "RECREATE")

npu2015_25ns = [
    1.78653e-05,
    2.56602e-05,
    5.27857e-05,
    8.88954e-05,
    0.000109362,
    0.000140973,
    0.000240998,
    0.00071209,
    0.00130121,
    0.00245255,
    0.00502589,
    0.00919534,
    0.0146697,
    0.0204126,
    0.0267586,
    0.0337697,
    0.0401478,
    0.0450159,
    0.0490577,
    0.0524855,
    0.0548159,
    0.0559937,
    0.0554468,
    0.0537687,
    0.0512055,
    0.0476713,
    0.0435312,
    0.0393107,
    0.0349812,
    0.0307413,
    0.0272425,
    0.0237115,
    0.0208329,
    0.0182459,
    0.0160712,
    0.0142498,
    0.012804,
    0.011571,
    0.010547,
    0.00959489,
    0.00891718,
    0.00829292,
    0.0076195,
    0.0069806,
    0.0062025,
    0.00546581,
    0.00484127,
    0.00407168,
    0.00337681,
    0.00269893,
    0.00212473,
    0.00160208,
    0.00117884,
    0.000859662,
    0.000569085,
    0.000365431,
    0.000243565,
    0.00015688,
    9.88128e-05,
    6.53783e-05,
    3.73924e-05,
    2.61382e-05,
    2.0307e-05,
    1.73032e-05,
    1.435e-05,
    1.36486e-05,
    1.35555e-05,
    1.37491e-05,
    1.34255e-05,
    1.33987e-05,
    1.34061e-05,
    1.34211e-05,
    1.34177e-05,
    1.32959e-05,
    1.33287e-05]

MC_pu = ROOT.TH1F("MC_pu","MC_pu",75,0,75)

for i in range(0,75):
    #print " pu ", i, "  ", npu2015_25ns[i]
    MC_pu.Fill(i, npu2015_25ns[i])
    #if(i==52): print "i ", i, " value ", npu2015_25ns[i-1]

MC_pu.Write()
file_mc.Close()


#infile = ROOT.TFile.Open("MyDataPileupHistogram.root")
infile = ROOT.TFile.Open("ttJets.meta.pu.root")   
htmp = infile.Get("pu_distribution")

#infile2 = ROOT.TFile.Open("MyDataPileupHistogramDOWN.root")
infile2 = ROOT.TFile.Open("QCD_Mu_20to30.meta.pu.root")
htmp2 = infile2.Get("pu_distribution")

infile3 = ROOT.TFile.Open("MyDataPileupHistogramUP.root")
htmp3 = infile3.Get("pileup")

htmp.Scale(1/htmp.Integral())
htmp.SetLineColor(ROOT.kGreen)
htmp2.Scale(1/htmp2.Integral())
htmp2.SetLineColor(ROOT.kBlue)
htmp2.SetLineStyle(2)
htmp3.Scale(1/htmp3.Integral())
htmp3.SetLineColor(ROOT.kRed)
htmp3.SetLineStyle(3)

MC_pu.SetLineColor(ROOT.kRed)
MC_pu.SetLineStyle(3)

htmp.GetXaxis().SetRangeUser(0,75)
htmp2.GetXaxis().SetRangeUser(0,75)
htmp3.GetXaxis().SetRangeUser(0,75)
MC_pu.GetXaxis().SetRangeUser(0,75)

htmp.SetLineWidth(3)
htmp2.SetLineWidth(3)
htmp3.SetLineWidth(3)
MC_pu.SetLineWidth(3)

H=600
W=700

H_ref = 600
W_ref = 700

T = 0.08*H_ref
B = 0.12*H_ref
L = 0.12*W_ref
R = 0.08*W_ref

tdrstyle.setTDRStyle();

c1 = ROOT.TCanvas("c1","c1",50,50,W,H)
c1.SetFillColor(0);
c1.SetBorderMode(0);
c1.SetFrameFillStyle(0);
c1.SetFrameBorderMode(0);
c1.SetLeftMargin( 0.15 );#L/W                                                                                                                                     
c1.SetRightMargin( R/W );
c1.SetTopMargin( T/H );
c1.SetBottomMargin(0.14);
c1.SetTickx(0);
c1.SetTicky(0);
c1.Draw()

leg_sign = ROOT.TLegend(.68, .58, 0.91, .89)
#leg_sign.SetNColumns(2)
leg_sign.SetFillColor(0)
leg_sign.SetTextSize(0.032)
leg_sign.SetTextFont(42)

#leg_sign.AddEntry(htmp, "#splitline{2016 data}{#sigma = 69.200 mb}", "l")
leg_sign.AddEntry(htmp, "2016 TT MC", "l")
leg_sign.AddEntry(htmp2, "2016 QCD MC", "l")
#leg_sign.AddEntry(htmp2, "#splitline{2016 data}{#sigma =  66.017 mb}", "l")
#leg_sign.AddEntry(htmp3, "#splitline{2016 data}{#sigma = 72.383 mb}", "l")
leg_sign.AddEntry(MC_pu, "2016 mix_2016_25ns_Moriond17MC_PoissonOOTPU MC ", "l")

maximum = max([htmp.GetMaximum(),htmp2.GetMaximum(), htmp3.GetMaximum()])
minimum = min([htmp.GetMinimum(), htmp2.GetMinimum(), htmp3.GetMinimum()])

htmp.SetMaximum(maximum*1.3)
if(minimum > 0):htmp.SetMinimum(0.01*minimum)
else: htmp.SetMinimum(0.01)

htmp.GetXaxis().SetLabelFont(42);
htmp.GetYaxis().SetLabelFont(42);
htmp.GetXaxis().SetTitleFont(42);
htmp.GetYaxis().SetTitleFont(42);
htmp.GetXaxis().SetTitleOffset(0.9);
htmp.GetYaxis().SetTitleOffset(1.2);
htmp.SetTitleFont(42);
htmp.SetTitle("");

htmp.GetXaxis().SetLabelSize(0.05);
htmp.GetYaxis().SetLabelSize(0.05);
htmp.GetXaxis().SetTitleSize(0.055);
htmp.GetYaxis().SetTitleSize(0.06);

htmp.SetLineWidth(2)
htmp.GetXaxis().SetTitle("Number of pile up interactions")
htmp.GetYaxis().SetTitle("Normalized events/ bin")

htmp.Draw("hist")
htmp2.Draw("histsame")
#htmp3.Draw("histsame")
MC_pu.Draw("histsame")
leg_sign.Draw("same")
    
CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = " (13 TeV)"

iPeriod = 0
iPos = 11

CMS_lumi.CMS_lumi(c1, iPeriod, iPos)

c1.cd()
c1.Update();
c1.RedrawAxis();
#c1.GetFrame().Draw();

c1.Print("Plots/puMC_comp.pdf")
c1.Print("Plots/puMC_comp.png")
c1.Print("Plots/puMC_comp.root")
    
