import os 
import sys 
import numpy
from ROOT import TMath
class weightCalculator:
    def __init__(self):
        self.puweight_= self.setpuweight()
        #self.EWKWZWeights_ = self.setEWKWZWeights()
        
    def setpuweight(self):
        puweight=[]
        #puweight.append(0.0)  ## this is not needed, because the npu starts from zero, however histo bin content starts from 1 hence this is needed when reading the histo 
        puweight.append(0.361415)
        puweight.append(0.934779)
        puweight.append(1.22111)
        puweight.append(1.00593)
        puweight.append(1.11733)
        puweight.append(1.12163)
        puweight.append(0.81101)
        puweight.append(0.474133)
        puweight.append(0.777016)
        puweight.append(0.865138)
        puweight.append(0.966505)
        puweight.append(1.06934)
        puweight.append(1.11888)
        puweight.append(1.17932)
        puweight.append(1.20627)
        puweight.append(1.20834)
        puweight.append(1.19857)
        puweight.append(1.17711)
        puweight.append(1.1442)
        puweight.append(1.09576)
        puweight.append(1.06293)
        puweight.append(1.05223)
        puweight.append(1.05222)
        puweight.append(1.05155)
        puweight.append(1.05288)
        puweight.append(1.0592)
        puweight.append(1.0722)
        puweight.append(1.08227)
        puweight.append(1.09488)
        puweight.append(1.11515)
        puweight.append(1.09142)
        puweight.append(1.0902)
        puweight.append(1.04263)
        puweight.append(0.984303)
        puweight.append(0.911068)
        puweight.append(0.824302)
        puweight.append(0.714571)
        puweight.append(0.61301)
        puweight.append(0.505156)
        puweight.append(0.401956)
        puweight.append(0.309801)
        puweight.append(0.227478)
        puweight.append(0.163045)
        puweight.append(0.113213)
        puweight.append(0.0772157)
        puweight.append(0.0507651)
        puweight.append(0.031776)
        puweight.append(0.0201048)
        puweight.append(0.012311)
        puweight.append(0.00729927)
        puweight.append(0.00442663)
        puweight.append(0.00263016)
        puweight.append(0.00151534)
        puweight.append(0.000976188)
        puweight.append(0.000701043)
        puweight.append(0.000680397)
        puweight.append(0.000756293)
        puweight.append(0.000988397)
        puweight.append(0.00135186)
        puweight.append(0.00161507)
        puweight.append(0.00293591)
        puweight.append(0.00349124)
        puweight.append(0.0045456)
        puweight.append(0.00478266)
        puweight.append(0.00644435)
        puweight.append(0.00533489)
        puweight.append(0.00480443)
        puweight.append(0.00366081)
        puweight.append(0.00390283)
        puweight.append(0.00298031)
        puweight.append(0.0030184)
        puweight.append(0.00274978)
        puweight.append(0.00276308)
        puweight.append(0.00214139)
        puweight.append(0.00178307)
        puweight.append(0)
        puweight.append(0)
        puweight.append(0)
        puweight.append(0)
        puweight.append(0)
        return puweight

    def GetPUWeights(self, pu_nTrueInt):
        weight_pu_ = 0.0
        ntrueint = (int) (pu_nTrueInt)
        if ntrueint < len(self.puweight_) :
            weight_pu_ = self.puweight_[ntrueint]
        return weight_pu_

        
    
    
    #def setEWKWZWeight(self):
        
        
        
    def GetEWKWZWeights(self, pt):
        
        return [1,2,3]
    
    ''' top pt reweighting for 13 TeV https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopPtReweighting'''
    def GetTopPtReWeighting(self, pt1, pt2):
        w1 = TMath.Exp(0.0615 - 0.0005 * pt1);
        w2 = TMath.Exp(0.0615 - 0.0005 * pt2);
        return TMath.Sqrt(w1*w2)


    ''' this is a test fucntion which will be used in other palces but will be deleted from here '''
    def getetabin(self,eta):
        etabins=[-2.5,-2.1, -1.5, -1.4, -0.8, 0.0, 0.8, 1.4, 1.5, 2.1, 2.5] 
        val_ = min(etabins, key=lambda x:abs(x-eta))
        idx_ = etabins.index(val_)
        if (etabins[idx_]-eta) >0: idx_=idx_-1
        if (etabins[idx_]-eta) <0: idx_=idx_ 
        if (etabins[idx_]-eta) ==0: idx_=idx_
        return idx_

    ''' this is a test fucntion which will be used in other palces but will be deleted from here '''
    def getptbin(self, pt):
        ptbins=[0., 10., .....] 
        val_ = min(ptbins, key=lambda x:abs(x-pt))
        idx_ = ptbins.index(val_)
        if (ptbins[idx_]-pt) >0: idx_=idx_-1
        if (ptbins[idx_]-pt) <0: idx_=idx_ 
        if (ptbins[idx_]-pt) ==0: idx_=idx_
        return idx_

        ''' 
        ele_trig: 
        eta_bin=[-2.5, -2.0, -1.566, -1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] 
        pt_bin = [10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 150.0, 200.0]
        
        ele_reco: 
        eta_bin = [-2.5, -2.45, -2.4, -2.3, -2.2, -2.0, -1.8, -1.63, -1.566, -1.444, -1.2, -1.0, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 1.0, 1.2, 1.444, 1.566, 1.63, 1.8, 2.0, 2.2, 2.3, 2.4, 2.45, 2.5]
        pt_bin= [25.0, 500.0]
        '''



    def GetEleTriggerWeights(self, pt, eta):
        return 
    
    def GetEleRecoWeights(self, pt, eta):
        return 

    def GetEleLooseIDWeights(self, pt, eta):
        return 

    def GetEleTightIDWeights(self, pt, eta):
        return
    
    def GetMuTriggerWeights(self, pt, eta):
        return 
    
    def GetMuIDWeights(self, pt, eta):
        return

    def GetMuIsoWeights(self, pt, eta):
        return 
        
    def GetMuTrackingWeight(self, pt, eta):
        return

    def GetJECWeight(self, pt, eta):
        return 

if __name__ == "__main__":
    weightObj = weightCalculator()
    weightObj.setpuweight
    print weightObj.getetabin(1.34)
    
