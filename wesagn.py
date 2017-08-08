from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.datasets import load_sample_image
import os,fnmatch

def createExamples():
    numberArrayExamples =open('zelanAr.txt','a')
    charswehave = range(1,381)
    # versionwehave = range(1,7)
    
    for eachnum in charswehave:
        imgFilepath = "/home/tesfay/Documents/Thesis/thesis_day to day/codes/washra fonts/gofferfiles/"+ str(eachnum) + '.jpg'
        ei =Image.open( imgFilepath)
        eiar = np.array(ei)
        eiar1 =str(eiar.tolist())
            
        linetowrite = str(eachnum)+'::' + eiar1 + '\n'
        numberArrayExamples.write(linetowrite)
        # print str(eachnum) 
            

            
