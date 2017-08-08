from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import time

'''
i =Image.open('Zelanfiles/1.jpg')
iar = np.asarray(i)
plt.imshow(iar)
plt.show()
# print iar
'''
def threshold(imageArray):
    balanceAr =[]
    newAr =imageArray
    
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum =reduce(lambda x, y: x +y , eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)            
    balance = reduce(lambda x, y: x +y , balanceAr[:3])/len(balanceAr)         
   
    for eachRow in newAr:
            for eachPix in eachRow:
                if reduce(lambda x, y: x +y , eachPix[:3])/len(eachPix[:3]) > balance:
                    eachPix[0] =255
                    eachPix[1] =255
                    eachPix[2] =255
                else:
                    eachPix[0] =0
                    eachPix[1] =0
                    eachPix[2] =0
                   
    return newAr   
                
            
i = Image.open('Zelanfiles/1.jpg')   
iar =np.array(i)

i2 = Image.open('Zelanfiles/2.jpg')   
iar2 =np.array(i2)

i3= Image.open('Zelanfiles/3.jpg')   
iar3 =np.array(i3)

i4 = Image.open('Zelanfiles/4.jpg')   
iar4 =np.array(iar4)


threshold(iar)
threshold(iar2)
threshold(iar3)
threshold(iar4)



fig =plt.figure()
ax1 =plt.subplot2grid((8,6),(0,0) ,rowspan =4  ,colspan =3)
ax2 =plt.subplot2grid((8,6),(4,0) ,rowspan =4  ,colspan =3)
ax3 =plt.subplot2grid((8,6),(0,3) ,rowspan =4  ,colspan =3)
ax4=plt.subplot2grid((8,6),(4,3) ,rowspan =4  ,colspan =3)
ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)
plt.show()





