import random
import math
import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap


def generateData(numberOfClassEl, numberOfClasses):
    data = []
    for classNum in range(numberOfClasses):

        centerX, centerY = random.random() * 5.0, random.random() * 5.0

        for rowNum in range(numberOfClassEl):
            data.append([[random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)], classNum])
    return data


def showData(nClasses, nItemsInClass):
    trainData = generateData(nItemsInClass, nClasses)
    classColormap = ListedColormap(['#FF0000', '#00FF00', '#FFFFFF'])
    pl.scatter([trainData[i][0][0] for i in range(len(trainData))],
               [trainData[i][0][1] for i in range(len(trainData))],
               c=[trainData[i][1] for i in range(len(trainData))],
               cmap=classColormap)
    pl.show()


# showData (3, 40)



def splitTrainTest(data, testPercent):
    trainData = []
    testData = []
    for row in data:
        if random.random() < testPercent:
            testData.append(row)
        else:
            trainData.append(row)
    return trainData, testData


def classifyKNN(trainData, testData, k, numberOfClasses, isSuspended,metrick):

    def dist(a, b,metrick):
        if metrick==0:
         n=0
         temp = 0
         while n<len(a):
             temp+=((a[n] - b[n]) ** 2)
             n+=1
         return math.sqrt(temp)
        if metrick==1:
         n=0
         temp =0

         while n<len(a):

           temp = temp +  math.fabs(a[n] - b[n])
           n+=1

         return temp/n
        if metrick==2:
         n=0
         temp=[]
         while n < len(a):
             temp.append(math.fabs((a[n] - b[n])))
             n+=1

         return max(temp)

    testLabels = []
    for testPoint in testData:

        testDist = [[dist(testPoint, trainData[i][0],metrick), trainData[i][1]] for i in range(len(trainData))]

        stat = [0 for i in range(numberOfClasses)]
        for d in sorted(testDist)[0:k]:
            stat[d[1]] += 1
        if isSuspended:
         suspendedtestdist = sorted(testDist, key=lambda x: (x[1], x[0]))
         for i in stat:
             n = next(obj for obj in suspendedtestdist if obj[1] == stat.index(i))[0]
             if n==0:
                n=0.00001
             stat[stat.index(i)] = i/ (n * k)


        testLabels.append(sorted(zip(stat, range(numberOfClasses)), reverse=True)[0][1])
    return testLabels


def calculateAccuracy(nClasses, nItemsInClass, k, testPercent):
    data = generateData(nItemsInClass, nClasses)
    trainData, testDataWithLabels = splitTrainTest(data, testPercent)
    testData = [testDataWithLabels[i][0] for i in range(len(testDataWithLabels))]
    testDataLabels = classifyKNN(trainData, testData, k, nClasses)

    print("Accuracy: ",
          sum([int(testDataLabels[i] == testDataWithLabels[i][1]) for i in range(len(testDataWithLabels))]) / float(
              len(testDataWithLabels)))

def calculateRecall(nClasses, nItemsInClass, k, testPercent):
    data = generateData(nItemsInClass, nClasses)
    trainData, testDataWithLabels = splitTrainTest(data, testPercent)
    testData = [testDataWithLabels[i][0] for i in range(len(testDataWithLabels))]
    testDataLabels = classifyKNN(trainData, testData, k, nClasses)
    print(testDataLabels)
    print("Accuracy: ",
          sum([int(testDataLabels[i] == testDataWithLabels[i][1]) for i in range(len(testDataWithLabels))]) / float(
              len(testDataWithLabels)))



def showDataOnMesh(nClasses, nItemsInClass, k):

    def generateTestMesh(trainData):
        x_min = min([trainData[i][0][0] for i in range(len(trainData))]) - 1.0
        x_max = max([trainData[i][0][0] for i in range(len(trainData))]) + 1.0
        y_min = min([trainData[i][0][1] for i in range(len(trainData))]) - 1.0
        y_max = max([trainData[i][0][1] for i in range(len(trainData))]) + 1.0
        h = 0.05
        testX, testY = np.meshgrid(np.arange(x_min, x_max, h),
                                   np.arange(y_min, y_max, h))
        return [testX, testY]

    trainData = generateData(nItemsInClass, nClasses)
    testMesh = generateTestMesh(trainData)
    testMeshLabels = classifyKNN(trainData, zip(testMesh[0].ravel(), testMesh[1].ravel()), k, nClasses)
    classColormap = ListedColormap(['#FF0000', '#00FF00', '#FFFFFF'])
    testColormap = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAAA'])
    pl.pcolormesh(testMesh[0],
                  testMesh[1],
                  np.asarray(testMeshLabels).reshape(testMesh[0].shape),
                  cmap=testColormap)
    pl.scatter([trainData[i][0][0] for i in range(len(trainData))],
               [trainData[i][0][1] for i in range(len(trainData))],
               c=[trainData[i][1] for i in range(len(trainData))],
               cmap=classColormap)
    pl.show()

# calculateAccuracy(2,40,9,90)
#calculateAccuracy(2,40,9,0.1)
#showDataOnMesh(3,40,5)
