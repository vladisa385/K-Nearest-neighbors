# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

colors = [None, 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']

import pyqtgraph as pg
from Kneirboor import *
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,qApp
from PyQt5.QtCore import Qt,QEvent
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from pyqtgraph import GraphicsLayoutWidget


class Ui_MainWindow(QMainWindow):


    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.traindata = []
        self.numberofclasses = 0
        self.trueTestDataLabels= []
        self.labeltestdata= []
        self.testData = []

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget()
        self.setMinimumSize(QtCore.QSize(766, 430))
        self.setMaximumSize(QtCore.QSize(766, 430))
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 80, 751, 321))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButtonExplore = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExplore.setGeometry(QtCore.QRect(12, 402, 337, 27))
        self.pushButtonExplore.setObjectName("pushButtonExplore")
        self.graphicsView_2 = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 440, 751, 221))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 750, 62))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtotLoadIris = QtWidgets.QPushButton(self.widget)
        self.pushButtotLoadIris.setObjectName("pushButtotLoadIris")
        self.gridLayout.addWidget(self.pushButtotLoadIris, 0, 0, 1, 2)
        self.checkBoxSuspended = QtWidgets.QCheckBox(self.widget)
        self.checkBoxSuspended.setObjectName("checkBoxSuspended")
        self.gridLayout.addWidget(self.checkBoxSuspended, 0, 2, 1, 3)
        self.pushButtonCheckTest = QtWidgets.QPushButton(self.widget)
        self.pushButtonCheckTest.setObjectName("pushButtonCheckTest")
        self.gridLayout.addWidget(self.pushButtonCheckTest, 0, 5, 1, 3)
        self.pushButtonGenerate = QtWidgets.QPushButton(self.widget)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.gridLayout.addWidget(self.pushButtonGenerate, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 2)
        self.spinBoxClasses = QtWidgets.QSpinBox(self.widget)
        self.spinBoxClasses.setMinimum(1)
        self.spinBoxClasses.setMaximum(8)
        self.spinBoxClasses.setObjectName("spinBoxClasses")
        self.gridLayout.addWidget(self.spinBoxClasses, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 4, 1, 1)
        self.spinBoxElements = QtWidgets.QSpinBox(self.widget)
        self.spinBoxElements.setMinimum(1)
        self.spinBoxElements.setProperty("value", 20)
        self.spinBoxElements.setObjectName("spinBoxElements")
        self.gridLayout.addWidget(self.spinBoxElements, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 6, 1, 1)
        self.spinBoxK = QtWidgets.QSpinBox(self.widget)
        self.spinBoxK.setMinimum(3)
        self.spinBoxK.setSingleStep(2)
        self.spinBoxK.setObjectName("spinBoxK")
        self.gridLayout.addWidget(self.spinBoxK, 1, 7, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.w1 = self.graphicsView.addPlot()
        self.w2 = self.graphicsView_2.addPlot()
        self.legend= self.w2.addLegend()
        self.w1.scene().sigMouseClicked.connect(self.onClick)
        self.pushButtonGenerate.clicked.connect(self.generateDate)
        self.pushButtotLoadIris.clicked.connect(self.loadIris)
        self.pushButtonCheckTest.clicked.connect(self.checkTest)
        self.pushButtonExplore.clicked.connect(self.explore)
        self.setCentralWidget(self.centralwidget)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButtonExplore.setText(_translate("MainWindow", "Исследование влияния k для разных метрик"))
        self.pushButtotLoadIris.setText(_translate("MainWindow", "Загрузить данные с рисом"))
        self.checkBoxSuspended.setText(_translate("MainWindow", "Использовать взвешенный kNN"))
        self.pushButtonCheckTest.setText(_translate("MainWindow", "Проверить тестовую выборку"))
        self.pushButtonGenerate.setText(_translate("MainWindow", "Сгенерировать выборку"))
        self.label_3.setText(_translate("MainWindow", "Кол-во классов"))
        self.label_2.setText(_translate("MainWindow", "Кол-во элементов"))
        self.label.setText(_translate("MainWindow", "Кол-во соседей(K)"))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Delete:
            self.w1.clear()
            classes = []
            i = 0
            while i < 20:
                classes.append([])
                i += 1

            for i in self.traindata:
                classes[i[1]].append(np.asarray(i[0]))
            i = 0
            for j in classes:
                myS = pg.ScatterPlotItem(size=10, pen=pg.mkPen(colors[i]), brush=pg.mkBrush(255, 255, 255, 120))
                myspots = []
                if (len(j)):
                    for k in j:
                        myspots.append({'pos': k, 'data': i})
                    i += 1
                    myS.addPoints(myspots)
                    self.w1.addItem(myS)

    def onClick(self, event):
        if len(self.traindata) == 0:
            return 1
        vb = self.w1.vb
        mousePoint = vb.mapSceneToView(event.scenePos())
        testdata = [[mousePoint.x(), mousePoint.y()]]
        testDataLabels = classifyKNN(self.traindata, testdata, self.spinBoxK.value(), self.numberofclasses,self.checkBoxSuspended.isChecked(),0)
        myS = pg.ScatterPlotItem(size=10, pen=pg.mkPen(colors[testDataLabels[0]]), brush=pg.mkBrush(255, 255, 255, 120))
        myspots = []
        myspots.append({'pos': np.asarray([mousePoint.x(), mousePoint.y()]), 'data': testDataLabels[0]})
        myS.addPoints(myspots)
        self.w1.addItem(myS)
        self.traindata.append([[mousePoint.x(), mousePoint.y()], testDataLabels[0]])
        print(self.traindata)


    def loadIris(self):

        with open('train', 'rb') as fp:
            train = pickle.load(fp)
        with open('labels', 'rb') as fp:
            labels = pickle.load(fp)
        self.w1.clear()

        self.numberofclasses = 3
        self.traindata = []
        n = 0
        for i in train:
             self.traindata.append([])
             self.traindata[n].append(i.tolist())
             self.traindata[n].append(labels[n])
             n += 1

        # testDataLabels = classifyKNN(trainData, testData, 5, 2)

        trainData, self.trueTestDataLabels = splitTrainTest(self.traindata, 0.33)

        self.traindata = trainData
        self.testData = [self.trueTestDataLabels[i][0] for i in range(len(self.trueTestDataLabels))]
      #  self.labeltestdata = classifyKNN(trainData, self.testData, self.spinBoxK.value(), self.numberofclasses,self.checkBoxSuspended.isChecked())

        classes = []
        i = 0
        while i < 20:
            classes.append([])
            i += 1

        for i in self.traindata:
            classes[i[1]].append(np.asarray(i[0]))
        i = 0
        for j in classes:
            myS = pg.ScatterPlotItem(size=10, pen=pg.mkPen(colors[i]), brush=pg.mkBrush(255, 255, 255, 120))
            myspots = []
            if (len(j)):
                for k in j:
                    myspots.append({'pos': k, 'data': i})
                i += 1
                myS.addPoints(myspots)
                self.w1.addItem(myS)
        self.spinBoxClasses.setValue(3)
        self.spinBoxK.setValue(4)
        self.spinBoxK.setSingleStep(3)
        self.spinBoxElements.setValue(75)

    def checkTest(self):
        if len(self.traindata) == 0:
            return 1
        print(self.testData)
        self.labeltestdata = classifyKNN(self.traindata, self.testData, self.spinBoxK.value(), self.numberofclasses,self.checkBoxSuspended.isChecked(),0)
        x = sum([int(self.labeltestdata[i] == self.trueTestDataLabels[i][1]) for i in
                 range(len(self.trueTestDataLabels))]) / float(
            len(self.trueTestDataLabels))

        classes = []
        i = 0
        while i < 20:
            classes.append([])
            i += 1

        for i in self.trueTestDataLabels:
            classes[i[1]].append(np.asarray(i[0]))
        i = 0
        for j in classes:
            myS = pg.ScatterPlotItem(size=10, pen=pg.mkPen(colors[i]), brush=pg.mkBrush(255, 255, 255, 120))
            myspots = []
            if (len(j)):
                for k in j:
                    myspots.append({'pos': k, 'data': i})
                i += 1
                myS.addPoints(myspots)
                self.w1.addItem(myS)

        dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                       "Точность классификации ", str(x),
                                       buttons=QtWidgets.QMessageBox.Ok
                                       ,
                                       parent=None)
        result = dialog.exec_()

    def changeK(self, i):

        self.spinBoxK.setSingleStep(i)
        self.spinBoxK.setMinimum(i + 1)
        self.spinBoxK.setProperty("value", i + 1)

    def generateDate(self):
        self.w1.clear()
        data = generateData(self.spinBoxElements.value(), self.spinBoxClasses.value())
        self.numberofclasses = self.spinBoxClasses.value()
        trainData, self.trueTestDataLabels = splitTrainTest(data, 0.33)

        self.traindata = trainData
        self.testData = [self.trueTestDataLabels[i][0] for i in range(len(self.trueTestDataLabels))]
       # self.labeltestdata = classifyKNN(trainData, self.testData, self.spinBoxK.value(), self.numberofclasses,self.checkBoxSuspended.isChecked())

        classes = []
        i = 0
        while i < 20:
            classes.append([])
            i += 1

        for i in trainData:
            classes[i[1]].append(np.asarray(i[0]))
        i = 0
        for j in classes:
            myS = pg.ScatterPlotItem(size=10, pen=pg.mkPen(colors[i]), brush=pg.mkBrush(255, 255, 255, 120))
            myspots = []
            if (len(j)):
                for k in j:
                    myspots.append({'pos': k, 'data': i})
                i += 1
                myS.addPoints(myspots)
                self.w1.addItem(myS)

    def explore(self):
        if not(self.traindata):
            return
        self.w2.clear()
        self.legend.scene().removeItem(self.legend)
        self.legend = self.w2.addLegend((20,20),(420,20))
        myspots = []
        i = self.spinBoxK.value()
        while i < self.spinBoxElements.value():
            self.labeltestdata = classifyKNN(self.traindata,
                                             self.testData,
                                             i,
                                             self.numberofclasses,
                                             self.checkBoxSuspended.isChecked(),
                                             0)
            myspots.append([i, sum([int(self.labeltestdata[i] == self.trueTestDataLabels[i][1]) for i in
                                    range(len(self.trueTestDataLabels))]) / float(
                len(self.trueTestDataLabels))])
            i += self.spinBoxK.singleStep()
        self.w2.plot(x=[x[0] for x in myspots],
                     y=[y[1] for y in myspots],
                     symbol='o',
                     name = "Евклидово расстояние",
                     pen = (0, 0, 255),

                     )


        myspots = []
        i = self.spinBoxK.value()
        while i < self.spinBoxElements.value():
            self.labeltestdata = classifyKNN(self.traindata,
                                             self.testData,
                                             i,
                                             self.numberofclasses,
                                             self.checkBoxSuspended.isChecked(),
                                             1)
            myspots.append([i, sum([int(self.labeltestdata[i] == self.trueTestDataLabels[i][1]) for i in
                                    range(len(self.trueTestDataLabels))]) / float(
                len(self.trueTestDataLabels))])
            i += self.spinBoxK.singleStep()
        self.w2.plot(x=[x[0] for x in myspots],
                     y=[y[1] for y in myspots],
                     pen=(255, 0, 0),
                     symbolBrush=(255, 0, 0),
                     symbolPen='w',
                     name="Манхэттенское расстояние")
        myspots = []
        i = self.spinBoxK.value()
        while i < self.spinBoxElements.value():
            self.labeltestdata = classifyKNN(self.traindata,
                                             self.testData,
                                             i,
                                             self.numberofclasses,
                                             self.checkBoxSuspended.isChecked(),
                                             2)
            myspots.append([i, sum([int(self.labeltestdata[i] == self.trueTestDataLabels[i][1]) for i in
                                    range(len(self.trueTestDataLabels))]) / float(
                len(self.trueTestDataLabels))])
            i += self.spinBoxK.singleStep()
        self.w2.plot(x=[x[0] for x in myspots], y=[y[1] for y in myspots],
                     pen=(0, 255, 0),
                     symbolBrush=(0, 255, 0),
                     symbolPen='g',
                     name="Расстояние Чебышева")
        self.w2.setLabels(title='Сравнение метрик', left="Точность", bottom="K")

        self.setMinimumSize(QtCore.QSize(766, 717))
        self.setMaximumSize(QtCore.QSize(766, 717))

        #self.w2.plot(myspots, pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='w')

from pyqtgraph import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()

    sys.exit(app.exec_())

