# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(707, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.AlreadyUsedCardsGroupBox_3 = QGroupBox(self.frame_3)
        self.AlreadyUsedCardsGroupBox_3.setObjectName(u"AlreadyUsedCardsGroupBox_3")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AlreadyUsedCardsGroupBox_3.setFont(font)
        self.verticalLayout_11 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.AlreadyUsedCardsCombo_3 = QComboBox(self.AlreadyUsedCardsGroupBox_3)
        self.AlreadyUsedCardsCombo_3.setObjectName(u"AlreadyUsedCardsCombo_3")

        self.verticalLayout_11.addWidget(self.AlreadyUsedCardsCombo_3)


        self.verticalLayout_10.addWidget(self.AlreadyUsedCardsGroupBox_3)

        self.SearchCardGroupBox_3 = QGroupBox(self.frame_3)
        self.SearchCardGroupBox_3.setObjectName(u"SearchCardGroupBox_3")
        self.SearchCardGroupBox_3.setFont(font)
        self.verticalLayout_12 = QVBoxLayout(self.SearchCardGroupBox_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.SearchCardEdit_3 = QLineEdit(self.SearchCardGroupBox_3)
        self.SearchCardEdit_3.setObjectName(u"SearchCardEdit_3")

        self.verticalLayout_12.addWidget(self.SearchCardEdit_3)

        self.SearchCardCombo_3 = QComboBox(self.SearchCardGroupBox_3)
        self.SearchCardCombo_3.setObjectName(u"SearchCardCombo_3")

        self.verticalLayout_12.addWidget(self.SearchCardCombo_3)


        self.verticalLayout_10.addWidget(self.SearchCardGroupBox_3)

        self.CopyFromGroupBox_3 = QGroupBox(self.frame_3)
        self.CopyFromGroupBox_3.setObjectName(u"CopyFromGroupBox_3")
        self.CopyFromGroupBox_3.setFont(font)
        self.gridLayout_5 = QGridLayout(self.CopyFromGroupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CopyUpButton_3 = QToolButton(self.CopyFromGroupBox_3)
        self.CopyUpButton_3.setObjectName(u"CopyUpButton_3")

        self.gridLayout_5.addWidget(self.CopyUpButton_3, 0, 1, 1, 1)

        self.CopyLeftButton_3 = QToolButton(self.CopyFromGroupBox_3)
        self.CopyLeftButton_3.setObjectName(u"CopyLeftButton_3")
        self.CopyLeftButton_3.setEnabled(False)

        self.gridLayout_5.addWidget(self.CopyLeftButton_3, 1, 0, 1, 1)

        self.CopyDownButton_3 = QToolButton(self.CopyFromGroupBox_3)
        self.CopyDownButton_3.setObjectName(u"CopyDownButton_3")

        self.gridLayout_5.addWidget(self.CopyDownButton_3, 2, 1, 1, 1)

        self.CopyRightButton_3 = QToolButton(self.CopyFromGroupBox_3)
        self.CopyRightButton_3.setObjectName(u"CopyRightButton_3")

        self.gridLayout_5.addWidget(self.CopyRightButton_3, 1, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.CopyFromGroupBox_3)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_0 = QFrame(self.centralwidget)
        self.frame_0.setObjectName(u"frame_0")
        sizePolicy1.setHeightForWidth(self.frame_0.sizePolicy().hasHeightForWidth())
        self.frame_0.setSizePolicy(sizePolicy1)
        self.frame_0.setFrameShape(QFrame.StyledPanel)
        self.frame_0.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AlreadyUsedCardsGroupBox_0 = QGroupBox(self.frame_0)
        self.AlreadyUsedCardsGroupBox_0.setObjectName(u"AlreadyUsedCardsGroupBox_0")
        self.AlreadyUsedCardsGroupBox_0.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.AlreadyUsedCardsCombo_0 = QComboBox(self.AlreadyUsedCardsGroupBox_0)
        self.AlreadyUsedCardsCombo_0.setObjectName(u"AlreadyUsedCardsCombo_0")

        self.verticalLayout_3.addWidget(self.AlreadyUsedCardsCombo_0)


        self.verticalLayout.addWidget(self.AlreadyUsedCardsGroupBox_0)

        self.SearchCardGroupBox_0 = QGroupBox(self.frame_0)
        self.SearchCardGroupBox_0.setObjectName(u"SearchCardGroupBox_0")
        self.SearchCardGroupBox_0.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.SearchCardGroupBox_0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SearchCardEdit_0 = QLineEdit(self.SearchCardGroupBox_0)
        self.SearchCardEdit_0.setObjectName(u"SearchCardEdit_0")

        self.verticalLayout_2.addWidget(self.SearchCardEdit_0)

        self.SearchCardCombo_0 = QComboBox(self.SearchCardGroupBox_0)
        self.SearchCardCombo_0.setObjectName(u"SearchCardCombo_0")

        self.verticalLayout_2.addWidget(self.SearchCardCombo_0)


        self.verticalLayout.addWidget(self.SearchCardGroupBox_0)

        self.CopyFromGroupBox_0 = QGroupBox(self.frame_0)
        self.CopyFromGroupBox_0.setObjectName(u"CopyFromGroupBox_0")
        self.CopyFromGroupBox_0.setFont(font)
        self.gridLayout_2 = QGridLayout(self.CopyFromGroupBox_0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CopyUpButton_0 = QToolButton(self.CopyFromGroupBox_0)
        self.CopyUpButton_0.setObjectName(u"CopyUpButton_0")
        self.CopyUpButton_0.setEnabled(False)

        self.gridLayout_2.addWidget(self.CopyUpButton_0, 0, 1, 1, 1)

        self.CopyLeftButton_0 = QToolButton(self.CopyFromGroupBox_0)
        self.CopyLeftButton_0.setObjectName(u"CopyLeftButton_0")
        self.CopyLeftButton_0.setEnabled(False)

        self.gridLayout_2.addWidget(self.CopyLeftButton_0, 1, 0, 1, 1)

        self.CopyDownButton_0 = QToolButton(self.CopyFromGroupBox_0)
        self.CopyDownButton_0.setObjectName(u"CopyDownButton_0")

        self.gridLayout_2.addWidget(self.CopyDownButton_0, 2, 1, 1, 1)

        self.CopyRightButton_0 = QToolButton(self.CopyFromGroupBox_0)
        self.CopyRightButton_0.setObjectName(u"CopyRightButton_0")

        self.gridLayout_2.addWidget(self.CopyRightButton_0, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.CopyFromGroupBox_0)


        self.gridLayout.addWidget(self.frame_0, 0, 0, 1, 1)

        self.frame_1 = QFrame(self.centralwidget)
        self.frame_1.setObjectName(u"frame_1")
        sizePolicy1.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy1)
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.AlreadyUsedCardsGroupBox_1 = QGroupBox(self.frame_1)
        self.AlreadyUsedCardsGroupBox_1.setObjectName(u"AlreadyUsedCardsGroupBox_1")
        self.AlreadyUsedCardsGroupBox_1.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.AlreadyUsedCardsCombo_1 = QComboBox(self.AlreadyUsedCardsGroupBox_1)
        self.AlreadyUsedCardsCombo_1.setObjectName(u"AlreadyUsedCardsCombo_1")

        self.verticalLayout_5.addWidget(self.AlreadyUsedCardsCombo_1)


        self.verticalLayout_4.addWidget(self.AlreadyUsedCardsGroupBox_1)

        self.SearchCardGroupBox_1 = QGroupBox(self.frame_1)
        self.SearchCardGroupBox_1.setObjectName(u"SearchCardGroupBox_1")
        self.SearchCardGroupBox_1.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.SearchCardGroupBox_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SearchCardEdit_1 = QLineEdit(self.SearchCardGroupBox_1)
        self.SearchCardEdit_1.setObjectName(u"SearchCardEdit_1")

        self.verticalLayout_6.addWidget(self.SearchCardEdit_1)

        self.SearchCardCombo_1 = QComboBox(self.SearchCardGroupBox_1)
        self.SearchCardCombo_1.setObjectName(u"SearchCardCombo_1")

        self.verticalLayout_6.addWidget(self.SearchCardCombo_1)


        self.verticalLayout_4.addWidget(self.SearchCardGroupBox_1)

        self.CopyFromGroupBox_1 = QGroupBox(self.frame_1)
        self.CopyFromGroupBox_1.setObjectName(u"CopyFromGroupBox_1")
        self.CopyFromGroupBox_1.setFont(font)
        self.gridLayout_3 = QGridLayout(self.CopyFromGroupBox_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.CopyUpButton_1 = QToolButton(self.CopyFromGroupBox_1)
        self.CopyUpButton_1.setObjectName(u"CopyUpButton_1")
        self.CopyUpButton_1.setEnabled(False)

        self.gridLayout_3.addWidget(self.CopyUpButton_1, 0, 1, 1, 1)

        self.CopyLeftButton_1 = QToolButton(self.CopyFromGroupBox_1)
        self.CopyLeftButton_1.setObjectName(u"CopyLeftButton_1")

        self.gridLayout_3.addWidget(self.CopyLeftButton_1, 1, 0, 1, 1)

        self.CopyDownButton_1 = QToolButton(self.CopyFromGroupBox_1)
        self.CopyDownButton_1.setObjectName(u"CopyDownButton_1")

        self.gridLayout_3.addWidget(self.CopyDownButton_1, 2, 1, 1, 1)

        self.CopyRightButton_1 = QToolButton(self.CopyFromGroupBox_1)
        self.CopyRightButton_1.setObjectName(u"CopyRightButton_1")

        self.gridLayout_3.addWidget(self.CopyRightButton_1, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.CopyFromGroupBox_1)


        self.gridLayout.addWidget(self.frame_1, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.AlreadyUsedCardsGroupBox_4 = QGroupBox(self.frame_4)
        self.AlreadyUsedCardsGroupBox_4.setObjectName(u"AlreadyUsedCardsGroupBox_4")
        self.AlreadyUsedCardsGroupBox_4.setFont(font)
        self.verticalLayout_14 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.AlreadyUsedCardsCombo_4 = QComboBox(self.AlreadyUsedCardsGroupBox_4)
        self.AlreadyUsedCardsCombo_4.setObjectName(u"AlreadyUsedCardsCombo_4")

        self.verticalLayout_14.addWidget(self.AlreadyUsedCardsCombo_4)


        self.verticalLayout_13.addWidget(self.AlreadyUsedCardsGroupBox_4)

        self.SearchCardGroupBox_4 = QGroupBox(self.frame_4)
        self.SearchCardGroupBox_4.setObjectName(u"SearchCardGroupBox_4")
        self.SearchCardGroupBox_4.setFont(font)
        self.verticalLayout_15 = QVBoxLayout(self.SearchCardGroupBox_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.SearchCardEdit_4 = QLineEdit(self.SearchCardGroupBox_4)
        self.SearchCardEdit_4.setObjectName(u"SearchCardEdit_4")

        self.verticalLayout_15.addWidget(self.SearchCardEdit_4)

        self.SearchCardCombo_4 = QComboBox(self.SearchCardGroupBox_4)
        self.SearchCardCombo_4.setObjectName(u"SearchCardCombo_4")

        self.verticalLayout_15.addWidget(self.SearchCardCombo_4)


        self.verticalLayout_13.addWidget(self.SearchCardGroupBox_4)

        self.CopyFromGroupBox_4 = QGroupBox(self.frame_4)
        self.CopyFromGroupBox_4.setObjectName(u"CopyFromGroupBox_4")
        self.CopyFromGroupBox_4.setFont(font)
        self.gridLayout_6 = QGridLayout(self.CopyFromGroupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.CopyUpButton_4 = QToolButton(self.CopyFromGroupBox_4)
        self.CopyUpButton_4.setObjectName(u"CopyUpButton_4")

        self.gridLayout_6.addWidget(self.CopyUpButton_4, 0, 1, 1, 1)

        self.CopyLeftButton_4 = QToolButton(self.CopyFromGroupBox_4)
        self.CopyLeftButton_4.setObjectName(u"CopyLeftButton_4")

        self.gridLayout_6.addWidget(self.CopyLeftButton_4, 1, 0, 1, 1)

        self.CopyDownButton_4 = QToolButton(self.CopyFromGroupBox_4)
        self.CopyDownButton_4.setObjectName(u"CopyDownButton_4")

        self.gridLayout_6.addWidget(self.CopyDownButton_4, 2, 1, 1, 1)

        self.CopyRightButton_4 = QToolButton(self.CopyFromGroupBox_4)
        self.CopyRightButton_4.setObjectName(u"CopyRightButton_4")

        self.gridLayout_6.addWidget(self.CopyRightButton_4, 1, 2, 1, 1)


        self.verticalLayout_13.addWidget(self.CopyFromGroupBox_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.AlreadyUsedCardsGroupBox_2 = QGroupBox(self.frame_2)
        self.AlreadyUsedCardsGroupBox_2.setObjectName(u"AlreadyUsedCardsGroupBox_2")
        self.AlreadyUsedCardsGroupBox_2.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.AlreadyUsedCardsCombo_2 = QComboBox(self.AlreadyUsedCardsGroupBox_2)
        self.AlreadyUsedCardsCombo_2.setObjectName(u"AlreadyUsedCardsCombo_2")

        self.verticalLayout_8.addWidget(self.AlreadyUsedCardsCombo_2)


        self.verticalLayout_7.addWidget(self.AlreadyUsedCardsGroupBox_2)

        self.SearchCardGroupBox_2 = QGroupBox(self.frame_2)
        self.SearchCardGroupBox_2.setObjectName(u"SearchCardGroupBox_2")
        self.SearchCardGroupBox_2.setFont(font)
        self.verticalLayout_9 = QVBoxLayout(self.SearchCardGroupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.SearchCardEdit_2 = QLineEdit(self.SearchCardGroupBox_2)
        self.SearchCardEdit_2.setObjectName(u"SearchCardEdit_2")

        self.verticalLayout_9.addWidget(self.SearchCardEdit_2)

        self.SearchCardCombo_2 = QComboBox(self.SearchCardGroupBox_2)
        self.SearchCardCombo_2.setObjectName(u"SearchCardCombo_2")

        self.verticalLayout_9.addWidget(self.SearchCardCombo_2)


        self.verticalLayout_7.addWidget(self.SearchCardGroupBox_2)

        self.CopyFromGroupBox_2 = QGroupBox(self.frame_2)
        self.CopyFromGroupBox_2.setObjectName(u"CopyFromGroupBox_2")
        self.CopyFromGroupBox_2.setFont(font)
        self.gridLayout_4 = QGridLayout(self.CopyFromGroupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.CopyUpButton_2 = QToolButton(self.CopyFromGroupBox_2)
        self.CopyUpButton_2.setObjectName(u"CopyUpButton_2")
        self.CopyUpButton_2.setEnabled(False)

        self.gridLayout_4.addWidget(self.CopyUpButton_2, 0, 1, 1, 1)

        self.CopyLeftButton_2 = QToolButton(self.CopyFromGroupBox_2)
        self.CopyLeftButton_2.setObjectName(u"CopyLeftButton_2")

        self.gridLayout_4.addWidget(self.CopyLeftButton_2, 1, 0, 1, 1)

        self.CopyDownButton_2 = QToolButton(self.CopyFromGroupBox_2)
        self.CopyDownButton_2.setObjectName(u"CopyDownButton_2")

        self.gridLayout_4.addWidget(self.CopyDownButton_2, 2, 1, 1, 1)

        self.CopyRightButton_2 = QToolButton(self.CopyFromGroupBox_2)
        self.CopyRightButton_2.setObjectName(u"CopyRightButton_2")
        self.CopyRightButton_2.setEnabled(False)

        self.gridLayout_4.addWidget(self.CopyRightButton_2, 1, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.CopyFromGroupBox_2)


        self.gridLayout.addWidget(self.frame_2, 0, 3, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.AlreadyUsedCardsGroupBox_5 = QGroupBox(self.frame_5)
        self.AlreadyUsedCardsGroupBox_5.setObjectName(u"AlreadyUsedCardsGroupBox_5")
        self.AlreadyUsedCardsGroupBox_5.setFont(font)
        self.verticalLayout_17 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.AlreadyUsedCardsCombo_5 = QComboBox(self.AlreadyUsedCardsGroupBox_5)
        self.AlreadyUsedCardsCombo_5.setObjectName(u"AlreadyUsedCardsCombo_5")

        self.verticalLayout_17.addWidget(self.AlreadyUsedCardsCombo_5)


        self.verticalLayout_16.addWidget(self.AlreadyUsedCardsGroupBox_5)

        self.SearchCardGroupBox_5 = QGroupBox(self.frame_5)
        self.SearchCardGroupBox_5.setObjectName(u"SearchCardGroupBox_5")
        self.SearchCardGroupBox_5.setFont(font)
        self.verticalLayout_18 = QVBoxLayout(self.SearchCardGroupBox_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.SearchCardEdit_5 = QLineEdit(self.SearchCardGroupBox_5)
        self.SearchCardEdit_5.setObjectName(u"SearchCardEdit_5")

        self.verticalLayout_18.addWidget(self.SearchCardEdit_5)

        self.SearchCardCombo_5 = QComboBox(self.SearchCardGroupBox_5)
        self.SearchCardCombo_5.setObjectName(u"SearchCardCombo_5")

        self.verticalLayout_18.addWidget(self.SearchCardCombo_5)


        self.verticalLayout_16.addWidget(self.SearchCardGroupBox_5)

        self.CopyFromGroupBox_5 = QGroupBox(self.frame_5)
        self.CopyFromGroupBox_5.setObjectName(u"CopyFromGroupBox_5")
        self.CopyFromGroupBox_5.setFont(font)
        self.gridLayout_7 = QGridLayout(self.CopyFromGroupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.CopyUpButton_5 = QToolButton(self.CopyFromGroupBox_5)
        self.CopyUpButton_5.setObjectName(u"CopyUpButton_5")

        self.gridLayout_7.addWidget(self.CopyUpButton_5, 0, 1, 1, 1)

        self.CopyLeftButton_5 = QToolButton(self.CopyFromGroupBox_5)
        self.CopyLeftButton_5.setObjectName(u"CopyLeftButton_5")

        self.gridLayout_7.addWidget(self.CopyLeftButton_5, 1, 0, 1, 1)

        self.CopyDownButton_5 = QToolButton(self.CopyFromGroupBox_5)
        self.CopyDownButton_5.setObjectName(u"CopyDownButton_5")

        self.gridLayout_7.addWidget(self.CopyDownButton_5, 2, 1, 1, 1)

        self.CopyRightButton_5 = QToolButton(self.CopyFromGroupBox_5)
        self.CopyRightButton_5.setObjectName(u"CopyRightButton_5")
        self.CopyRightButton_5.setEnabled(False)

        self.gridLayout_7.addWidget(self.CopyRightButton_5, 1, 2, 1, 1)


        self.verticalLayout_16.addWidget(self.CopyFromGroupBox_5)


        self.gridLayout.addWidget(self.frame_5, 1, 3, 1, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.AlreadyUsedCardsGroupBox_6 = QGroupBox(self.frame_6)
        self.AlreadyUsedCardsGroupBox_6.setObjectName(u"AlreadyUsedCardsGroupBox_6")
        self.AlreadyUsedCardsGroupBox_6.setFont(font)
        self.verticalLayout_20 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.AlreadyUsedCardsCombo_6 = QComboBox(self.AlreadyUsedCardsGroupBox_6)
        self.AlreadyUsedCardsCombo_6.setObjectName(u"AlreadyUsedCardsCombo_6")

        self.verticalLayout_20.addWidget(self.AlreadyUsedCardsCombo_6)


        self.verticalLayout_19.addWidget(self.AlreadyUsedCardsGroupBox_6)

        self.SearchCardGroupBox_6 = QGroupBox(self.frame_6)
        self.SearchCardGroupBox_6.setObjectName(u"SearchCardGroupBox_6")
        self.SearchCardGroupBox_6.setFont(font)
        self.verticalLayout_21 = QVBoxLayout(self.SearchCardGroupBox_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.SearchCardEdit_6 = QLineEdit(self.SearchCardGroupBox_6)
        self.SearchCardEdit_6.setObjectName(u"SearchCardEdit_6")

        self.verticalLayout_21.addWidget(self.SearchCardEdit_6)

        self.SearchCardCombo_6 = QComboBox(self.SearchCardGroupBox_6)
        self.SearchCardCombo_6.setObjectName(u"SearchCardCombo_6")

        self.verticalLayout_21.addWidget(self.SearchCardCombo_6)


        self.verticalLayout_19.addWidget(self.SearchCardGroupBox_6)

        self.CopyFromGroupBox_6 = QGroupBox(self.frame_6)
        self.CopyFromGroupBox_6.setObjectName(u"CopyFromGroupBox_6")
        self.CopyFromGroupBox_6.setFont(font)
        self.gridLayout_8 = QGridLayout(self.CopyFromGroupBox_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.CopyUpButton_6 = QToolButton(self.CopyFromGroupBox_6)
        self.CopyUpButton_6.setObjectName(u"CopyUpButton_6")

        self.gridLayout_8.addWidget(self.CopyUpButton_6, 0, 1, 1, 1)

        self.CopyLeftButton_6 = QToolButton(self.CopyFromGroupBox_6)
        self.CopyLeftButton_6.setObjectName(u"CopyLeftButton_6")
        self.CopyLeftButton_6.setEnabled(False)

        self.gridLayout_8.addWidget(self.CopyLeftButton_6, 1, 0, 1, 1)

        self.CopyDownButton_6 = QToolButton(self.CopyFromGroupBox_6)
        self.CopyDownButton_6.setObjectName(u"CopyDownButton_6")
        self.CopyDownButton_6.setEnabled(False)

        self.gridLayout_8.addWidget(self.CopyDownButton_6, 2, 1, 1, 1)

        self.CopyRightButton_6 = QToolButton(self.CopyFromGroupBox_6)
        self.CopyRightButton_6.setObjectName(u"CopyRightButton_6")

        self.gridLayout_8.addWidget(self.CopyRightButton_6, 1, 2, 1, 1)


        self.verticalLayout_19.addWidget(self.CopyFromGroupBox_6)


        self.gridLayout.addWidget(self.frame_6, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.AlreadyUsedCardsGroupBox_7 = QGroupBox(self.frame_7)
        self.AlreadyUsedCardsGroupBox_7.setObjectName(u"AlreadyUsedCardsGroupBox_7")
        self.AlreadyUsedCardsGroupBox_7.setFont(font)
        self.verticalLayout_23 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.AlreadyUsedCardsCombo_7 = QComboBox(self.AlreadyUsedCardsGroupBox_7)
        self.AlreadyUsedCardsCombo_7.setObjectName(u"AlreadyUsedCardsCombo_7")

        self.verticalLayout_23.addWidget(self.AlreadyUsedCardsCombo_7)


        self.verticalLayout_22.addWidget(self.AlreadyUsedCardsGroupBox_7)

        self.SearchCardGroupBox_7 = QGroupBox(self.frame_7)
        self.SearchCardGroupBox_7.setObjectName(u"SearchCardGroupBox_7")
        self.SearchCardGroupBox_7.setFont(font)
        self.verticalLayout_24 = QVBoxLayout(self.SearchCardGroupBox_7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.SearchCardEdit_7 = QLineEdit(self.SearchCardGroupBox_7)
        self.SearchCardEdit_7.setObjectName(u"SearchCardEdit_7")

        self.verticalLayout_24.addWidget(self.SearchCardEdit_7)

        self.SearchCardCombo_7 = QComboBox(self.SearchCardGroupBox_7)
        self.SearchCardCombo_7.setObjectName(u"SearchCardCombo_7")

        self.verticalLayout_24.addWidget(self.SearchCardCombo_7)


        self.verticalLayout_22.addWidget(self.SearchCardGroupBox_7)

        self.CopyFromGroupBox_7 = QGroupBox(self.frame_7)
        self.CopyFromGroupBox_7.setObjectName(u"CopyFromGroupBox_7")
        self.CopyFromGroupBox_7.setFont(font)
        self.gridLayout_9 = QGridLayout(self.CopyFromGroupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.CopyUpButton_7 = QToolButton(self.CopyFromGroupBox_7)
        self.CopyUpButton_7.setObjectName(u"CopyUpButton_7")

        self.gridLayout_9.addWidget(self.CopyUpButton_7, 0, 1, 1, 1)

        self.CopyLeftButton_7 = QToolButton(self.CopyFromGroupBox_7)
        self.CopyLeftButton_7.setObjectName(u"CopyLeftButton_7")

        self.gridLayout_9.addWidget(self.CopyLeftButton_7, 1, 0, 1, 1)

        self.CopyDownButton_7 = QToolButton(self.CopyFromGroupBox_7)
        self.CopyDownButton_7.setObjectName(u"CopyDownButton_7")
        self.CopyDownButton_7.setEnabled(False)

        self.gridLayout_9.addWidget(self.CopyDownButton_7, 2, 1, 1, 1)

        self.CopyRightButton_7 = QToolButton(self.CopyFromGroupBox_7)
        self.CopyRightButton_7.setObjectName(u"CopyRightButton_7")

        self.gridLayout_9.addWidget(self.CopyRightButton_7, 1, 2, 1, 1)


        self.verticalLayout_22.addWidget(self.CopyFromGroupBox_7)


        self.gridLayout.addWidget(self.frame_7, 2, 1, 1, 1)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.AlreadyUsedCardsGroupBox_8 = QGroupBox(self.frame_8)
        self.AlreadyUsedCardsGroupBox_8.setObjectName(u"AlreadyUsedCardsGroupBox_8")
        self.AlreadyUsedCardsGroupBox_8.setFont(font)
        self.verticalLayout_26 = QVBoxLayout(self.AlreadyUsedCardsGroupBox_8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.AlreadyUsedCardsCombo_8 = QComboBox(self.AlreadyUsedCardsGroupBox_8)
        self.AlreadyUsedCardsCombo_8.setObjectName(u"AlreadyUsedCardsCombo_8")

        self.verticalLayout_26.addWidget(self.AlreadyUsedCardsCombo_8)


        self.verticalLayout_25.addWidget(self.AlreadyUsedCardsGroupBox_8)

        self.SearchCardGroupBox_8 = QGroupBox(self.frame_8)
        self.SearchCardGroupBox_8.setObjectName(u"SearchCardGroupBox_8")
        self.SearchCardGroupBox_8.setFont(font)
        self.verticalLayout_27 = QVBoxLayout(self.SearchCardGroupBox_8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.SearchCardEdit_8 = QLineEdit(self.SearchCardGroupBox_8)
        self.SearchCardEdit_8.setObjectName(u"SearchCardEdit_8")

        self.verticalLayout_27.addWidget(self.SearchCardEdit_8)

        self.SearchCardCombo_8 = QComboBox(self.SearchCardGroupBox_8)
        self.SearchCardCombo_8.setObjectName(u"SearchCardCombo_8")

        self.verticalLayout_27.addWidget(self.SearchCardCombo_8)


        self.verticalLayout_25.addWidget(self.SearchCardGroupBox_8)

        self.CopyFromGroupBox_8 = QGroupBox(self.frame_8)
        self.CopyFromGroupBox_8.setObjectName(u"CopyFromGroupBox_8")
        self.CopyFromGroupBox_8.setFont(font)
        self.gridLayout_10 = QGridLayout(self.CopyFromGroupBox_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.CopyUpButton_8 = QToolButton(self.CopyFromGroupBox_8)
        self.CopyUpButton_8.setObjectName(u"CopyUpButton_8")

        self.gridLayout_10.addWidget(self.CopyUpButton_8, 0, 1, 1, 1)

        self.CopyLeftButton_8 = QToolButton(self.CopyFromGroupBox_8)
        self.CopyLeftButton_8.setObjectName(u"CopyLeftButton_8")

        self.gridLayout_10.addWidget(self.CopyLeftButton_8, 1, 0, 1, 1)

        self.CopyDownButton_8 = QToolButton(self.CopyFromGroupBox_8)
        self.CopyDownButton_8.setObjectName(u"CopyDownButton_8")
        self.CopyDownButton_8.setEnabled(False)

        self.gridLayout_10.addWidget(self.CopyDownButton_8, 2, 1, 1, 1)

        self.CopyRightButton_8 = QToolButton(self.CopyFromGroupBox_8)
        self.CopyRightButton_8.setObjectName(u"CopyRightButton_8")
        self.CopyRightButton_8.setEnabled(False)

        self.gridLayout_10.addWidget(self.CopyRightButton_8, 1, 2, 1, 1)


        self.verticalLayout_25.addWidget(self.CopyFromGroupBox_8)


        self.gridLayout.addWidget(self.frame_8, 2, 3, 1, 1)

        self.ExportPDFButton = QPushButton(self.centralwidget)
        self.ExportPDFButton.setObjectName(u"ExportPDFButton")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.ExportPDFButton.setFont(font1)
        self.ExportPDFButton.setStyleSheet(u"color: rgba(10, 150, 10, 255);")

        self.gridLayout.addWidget(self.ExportPDFButton, 3, 3, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 3, 1, 1, 1)

        self.GetImagesButton = QPushButton(self.centralwidget)
        self.GetImagesButton.setObjectName(u"GetImagesButton")
        self.GetImagesButton.setFont(font1)

        self.gridLayout.addWidget(self.GetImagesButton, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YGOProxyPrinter", None))
        self.AlreadyUsedCardsGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.AlreadyUsedCardsGroupBox_0.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_0.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_0.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_0.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_0.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_0.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_0.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.AlreadyUsedCardsGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_1.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_1.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_1.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_1.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.AlreadyUsedCardsGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.AlreadyUsedCardsGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.AlreadyUsedCardsGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.AlreadyUsedCardsGroupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.AlreadyUsedCardsGroupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.AlreadyUsedCardsGroupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Already-used cards", None))
        self.SearchCardGroupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card name...", None))
        self.CopyFromGroupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Copy from...", None))
        self.CopyUpButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.ExportPDFButton.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.GetImagesButton.setText(QCoreApplication.translate("MainWindow", u"Get images", None))
    # retranslateUi

