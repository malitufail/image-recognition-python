from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import PIL 
import time
import functools as ft
from collections import Counter

def createExamples():
    numberArrayExamples = open('numArr.txt','a')
    numberWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for eachNum in numberWeHave:
        for eachVer in versionsWeHave:
            print(str(eachNum) + '.' +str(eachVer))
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' +str(eachVer) + '.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())
            lineToWrite = str(eachNum) + '::' + eiar1 + '\n'
            numberArrayExamples.write(lineToWrite)

createExamples()


def threshold(imageArray):
    balanceArray = []
    newArr = imageArray

    for row in imageArray:
        for pixel in row:
            print(pixel)
            avgNum = ft.reduce(lambda x, y: x+y, pixel[:3])/len(pixel[:3])
            balanceArray.append(avgNum)
    balance = ft.reduce(lambda x, y: x+y, balanceArray)/len(balanceArray)

    for row in newArr:
        for pixel in row:
            if ft.reduce(lambda x, y: x+y, pixel[:3])/len(pixel[:3]) > balance:
                pixel[0] = 255
                pixel[1] = 255
                pixel[2] = 255
                pixel[3] = 255
            else:
                pixel[0] = 0
                pixel[1] = 0
                pixel[2] = 0
                pixel[3] = 255
    return newArr    

#matching Images
def whatNumisThis(filePath):
    matchedArr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps= loadExamps.split('\n')

    i= Image.open(filePath)
    iar = np.array(i)
    iar1 = iar.tolist()
    inQuestion = str(iar1) 
    for eachExample in loadExamps: 
        if len(eachExample) > 3:
         
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentArr = splitEx[1] 
            eachPixEx = currentArr.split('],')
            eachPixInQ = inQuestion.split('],')

            x=0
            while x < len(eachPixEx): 
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedArr.append(int(currentNum)) 
                x+=1
    print("matchedArr")
    print(matchedArr)
    x=Counter(matchedArr)
    print(x)

    graphX = []
    graphY = []
    print("x",x)
    for eachThing in x:
        print(eachThing)
        graphX.append(eachThing)
        print(x[eachThing])
        graphY.append(eachThing)
        print(x[eachThing])

    fig=plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)
    print(iar)
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')

    #plt.ylim(1000)
    plt.show()

whatNumisThis('images/numbers/0.1.png')


# img = Image.open('images/numbers/0.1.png')
# iar = np.array(img)

# img2 = Image.open('images/numbers/y0.4.png')
# iar2 = np.array(img2)

# img3 = Image.open('images/numbers/y0.5.png')
# iar3 = np.array(img3)

# img4 = Image.open('images/sentdex.png')
# iar4 = np.array(img4)

#Creating Threshold
# threshold(iar3)
# threshold(iar2)
# threshold(iar4)

#Displaying Figures
# fig = plt.figure()
# ax1 = plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
# ax2 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
# ax3 = plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
# ax4 = plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)
# ax1.imshow(iar)
# ax2.imshow(iar2)
# ax3.imshow(iar3)
# ax4.imshow(iar4)

# plt.show()

#Converting Images to Matrices
# img = Image.open('images/numbers/0.5.png')
# imgArray = np.asarray(img)
# print(imgArray)
# plt.imshow(imgArray)
# plt.show()
