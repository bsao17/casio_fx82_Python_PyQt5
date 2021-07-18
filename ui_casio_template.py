# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Casio_template.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import ressource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(660, 1000)
        MainWindow.setMaximumSize(QSize(660, 1000))
        MainWindow.setStyleSheet(u"background-image: url(:/image/casioBg.png);")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClosed = QAction(MainWindow)
        self.actionClosed.setObjectName(u"actionClosed")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, -50, 661, 1061))
        font = QFont()
        font.setPointSize(25)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-image: url(:/background/image/casioBg.png);")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 690, 71, 51))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Medium"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_2.setFlat(False)
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(310, 690, 71, 51))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_3.setFlat(False)
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(310, 760, 71, 51))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_4.setFlat(False)
        self.lcdNumber = QLCDNumber(self.widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setEnabled(True)
        self.lcdNumber.setGeometry(QRect(170, 320, 351, 91))
        self.lcdNumber.setStyleSheet(u"background-image: url(:/background/image/screenColor.png);\n"
"border-radius: 10px;")
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(220, 760, 71, 51))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_5.setFlat(False)
        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(130, 760, 71, 51))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_6.setFlat(False)
        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(220, 830, 71, 51))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_8.setFlat(False)
        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(310, 830, 71, 51))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(130, 890, 71, 51))
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_10.setFlat(False)
        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(220, 890, 71, 51))
        font2 = QFont()
        font2.setFamilies([u"French Script MT"])
        font2.setPointSize(35)
        font2.setBold(True)
        self.pushButton_11.setFont(font2)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_11.setFlat(False)
        self.pushButton_12 = QPushButton(self.widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(310, 890, 71, 51))
        font3 = QFont()
        font3.setFamilies([u"Franklin Gothic Medium"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.pushButton_12.setFont(font3)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_12.setFlat(False)
        self.pushButton_13 = QPushButton(self.widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(390, 690, 71, 51))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.pushButton_13.setFont(font4)
        self.pushButton_13.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(149, 69, 57);\n"
"color: #FFF;")
        self.pushButton_14 = QPushButton(self.widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(480, 690, 71, 51))
        self.pushButton_14.setFont(font4)
        self.pushButton_14.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(149, 69, 57);\n"
"color: #FFF;")
        self.pushButton_15 = QPushButton(self.widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(390, 760, 71, 51))
        font5 = QFont()
        font5.setFamilies([u"Franklin Gothic Medium Cond"])
        font5.setPointSize(20)
        font5.setBold(True)
        self.pushButton_15.setFont(font5)
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_15.setFlat(False)
        self.pushButton_16 = QPushButton(self.widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(390, 830, 71, 51))
        font6 = QFont()
        font6.setFamilies([u"Franklin Gothic Medium Cond"])
        font6.setPointSize(30)
        font6.setBold(True)
        self.pushButton_16.setFont(font6)
        self.pushButton_16.setAutoFillBackground(False)
        self.pushButton_16.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_16.setFlat(False)
        self.pushButton_17 = QPushButton(self.widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(480, 830, 71, 51))
        font7 = QFont()
        font7.setFamilies([u"Franklin Gothic Book"])
        font7.setPointSize(40)
        font7.setBold(True)
        self.pushButton_17.setFont(font7)
        self.pushButton_17.setAutoFillBackground(False)
        self.pushButton_17.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_17.setFlat(False)
        self.pushButton_18 = QPushButton(self.widget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(480, 760, 71, 51))
        font8 = QFont()
        font8.setFamilies([u"Franklin Gothic Book"])
        font8.setPointSize(30)
        font8.setBold(True)
        self.pushButton_18.setFont(font8)
        self.pushButton_18.setAutoFillBackground(False)
        self.pushButton_18.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_18.setFlat(False)
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(130, 830, 71, 51))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_7.setFlat(False)
        self.pushButton_19 = QPushButton(self.widget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(130, 690, 71, 51))
        self.pushButton_19.setFont(font1)
        self.pushButton_19.setAutoFillBackground(False)
        self.pushButton_19.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_19.setFlat(False)
        self.pushButton_20 = QPushButton(self.widget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(390, 890, 71, 51))
        self.pushButton_20.setFont(font6)
        self.pushButton_20.setAutoFillBackground(False)
        self.pushButton_20.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_20.setFlat(False)
        self.pushButton_21 = QPushButton(self.widget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(480, 890, 71, 51))
        self.pushButton_21.setFont(font3)
        self.pushButton_21.setAutoFillBackground(False)
        self.pushButton_21.setStyleSheet(u"color: white;\n"
"background-color: rgb(17, 17, 20);\n"
"border-radius: 5px;")
        self.pushButton_21.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 660, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClosed)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClosed.setText(QCoreApplication.translate("MainWindow", u"Closed", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"EXP", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"M+", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

