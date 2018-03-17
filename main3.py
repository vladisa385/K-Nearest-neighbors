# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10
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

    def setupUi(self):
        #MainWindow.setObjectName("MainWindow")
       ## MainWindow.setFixedSize
        self.setMinimumSize(QtCore.QSize(754, 603))
        self.setMaximumSize(QtCore.QSize(754, 603))

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 80, 741, 541))
        self.graphicsView.setObjectName("graphicsView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 740, 62))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.loadIrisButton = QtWidgets.QPushButton(self.widget)
        self.loadIrisButton.setObjectName("loadIrisButton")
        self.gridLayout.addWidget(self.loadIrisButton, 0, 0, 1, 2)
        self.checkDateButton = QtWidgets.QPushButton(self.widget)
        self.checkDateButton.setObjectName("checkDateButton")
        self.gridLayout.addWidget(self.checkDateButton, 0, 4, 1, 3)
        self.generateButton = QtWidgets.QPushButton(self.widget)
        self.generateButton.setObjectName("generateButton")
        self.gridLayout.addWidget(self.generateButton, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.spinBoxClasses = QtWidgets.QSpinBox(self.widget)
        self.spinBoxClasses.setMinimum(2)
        self.spinBoxClasses.setMaximum(8)
        self.spinBoxClasses.setObjectName("spinBoxClasses")
        self.gridLayout.addWidget(self.spinBoxClasses, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        self.spinBoxElements = QtWidgets.QSpinBox(self.widget)
        self.spinBoxElements.setMinimum(1)
        self.spinBoxElements.setProperty("value", 20)
        self.spinBoxElements.setObjectName("spinBoxElements")
        self.gridLayout.addWidget(self.spinBoxElements, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 5, 1, 1)
        self.spinBoxK = QtWidgets.QSpinBox(self.widget)
        self.spinBoxK.setMinimum(3)
        self.spinBoxK.setSingleStep(2)
        self.spinBoxK.setObjectName("spinBoxK")
        self.gridLayout.addWidget(self.spinBoxK, 1, 6, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.w1 = self.graphicsView.addPlot()
        self.w1.scene().sigMouseClicked.connect(self.onClick)
        self.generateButton.clicked.connect(self.generateDate)
        self.loadIrisButton.clicked.connect(self.loadIris)
        self.checkDateButton.clicked.connect(self.checkTest)
        self.setCentralWidget(self.centralwidget)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
       # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadIrisButton.setText(_translate("MainWindow", "Загрузить данные с рисом"))
        self.checkDateButton.setText(_translate("MainWindow", "Проверить тестовую выборку"))
        self.generateButton.setText(_translate("MainWindow", "Сгенерировать выборку"))
        self.label_3.setText(_translate("MainWindow", "Кол-во классов"))
        self.label_2.setText(_translate("MainWindow", "Кол-во элементов"))
        self.label.setText(_translate("MainWindow", "Кол-во соседей(K)"))

    def onClick(self, event):
        if len(self.traindata) == 0:
            return 1
        vb = self.w1.vb
        mousePoint = vb.mapSceneToView(event.scenePos())
        testdata = [[mousePoint.x(), mousePoint.y()]]
        testDataLabels = classifyKNN(self.traindata, testdata, self.spinBoxK.value(), self.numberofclasses)
        myS = pg.ScatterPlotItem(size=10, pen=pg.mkPen(colors[testDataLabels[0]]), brush=pg.mkBrush(255, 255, 255, 120))
        myspots = []
        myspots.append({'pos': np.asarray([mousePoint.x(), mousePoint.y()]), 'data': testDataLabels[0]})
        myS.addPoints(myspots)
        self.w1.addItem(myS)
        self.traindata.append([[mousePoint.x(), mousePoint.y()], testDataLabels[0]])
        print(self.traindata)
        print(mousePoint)

    def loadIris(self):

        with open ('train', 'rb') as fp:
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
        self.labeltestdata = classifyKNN(trainData, self.testData, self.spinBoxK.value(), self.numberofclasses)

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

    def checkTest(self):
        if len(self.traindata) == 0:
            return 1
        x = sum([int(self.labeltestdata[i] == self.trueTestDataLabels[i][1]) for i in range(len(self.trueTestDataLabels))]) / float(
                  len (self.trueTestDataLabels))
        self.labeltestdata = classifyKNN(self.traindata, self.testData, self.spinBoxK.value(), self.numberofclasses)

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
        self.labeltestdata = classifyKNN(trainData, self.testData, self.spinBoxK.value(), self.numberofclasses)

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()

    sys.exit(app.exec_())