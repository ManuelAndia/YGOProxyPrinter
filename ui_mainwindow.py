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
        MainWindow.resize(647, 980)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(647, 980))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 4, 1, 1, 1)

        self.ExportPDFButton = QPushButton(self.centralwidget)
        self.ExportPDFButton.setObjectName(u"ExportPDFButton")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ExportPDFButton.setFont(font)
        self.ExportPDFButton.setStyleSheet(u"color: rgba(10, 150, 10, 255);")

        self.gridLayout.addWidget(self.ExportPDFButton, 4, 3, 1, 1)

        self.GetImagesButton = QPushButton(self.centralwidget)
        self.GetImagesButton.setObjectName(u"GetImagesButton")
        self.GetImagesButton.setFont(font)

        self.gridLayout.addWidget(self.GetImagesButton, 4, 0, 1, 1)

        self.frame_0 = QFrame(self.centralwidget)
        self.frame_0.setObjectName(u"frame_0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_0.sizePolicy().hasHeightForWidth())
        self.frame_0.setSizePolicy(sizePolicy1)
        self.frame_0.setFrameShape(QFrame.StyledPanel)
        self.frame_0.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SearchCardGroupBox_0 = QGroupBox(self.frame_0)
        self.SearchCardGroupBox_0.setObjectName(u"SearchCardGroupBox_0")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.SearchCardGroupBox_0.setFont(font1)
        self.gridLayout_12 = QGridLayout(self.SearchCardGroupBox_0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.SearchCardEdit_0 = QLineEdit(self.SearchCardGroupBox_0)
        self.SearchCardEdit_0.setObjectName(u"SearchCardEdit_0")
        self.SearchCardEdit_0.setClearButtonEnabled(True)

        self.gridLayout_12.addWidget(self.SearchCardEdit_0, 0, 0, 1, 1)

        self.RunSearchToolButton_0 = QToolButton(self.SearchCardGroupBox_0)
        self.RunSearchToolButton_0.setObjectName(u"RunSearchToolButton_0")
        self.RunSearchToolButton_0.setArrowType(Qt.NoArrow)

        self.gridLayout_12.addWidget(self.RunSearchToolButton_0, 0, 1, 1, 1)

        self.SearchCardCombo_0 = QComboBox(self.SearchCardGroupBox_0)
        self.SearchCardCombo_0.setObjectName(u"SearchCardCombo_0")

        self.gridLayout_12.addWidget(self.SearchCardCombo_0, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.SearchCardGroupBox_0)

        self.CopyToGroupBox_0 = QGroupBox(self.frame_0)
        self.CopyToGroupBox_0.setObjectName(u"CopyToGroupBox_0")
        self.CopyToGroupBox_0.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.CopyToGroupBox_0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CopyUpButton_0 = QToolButton(self.CopyToGroupBox_0)
        self.CopyUpButton_0.setObjectName(u"CopyUpButton_0")
        self.CopyUpButton_0.setEnabled(False)
        self.CopyUpButton_0.setMinimumSize(QSize(30, 25))

        self.gridLayout_2.addWidget(self.CopyUpButton_0, 0, 1, 1, 1)

        self.CopyLeftButton_0 = QToolButton(self.CopyToGroupBox_0)
        self.CopyLeftButton_0.setObjectName(u"CopyLeftButton_0")
        self.CopyLeftButton_0.setEnabled(False)
        self.CopyLeftButton_0.setMinimumSize(QSize(30, 25))

        self.gridLayout_2.addWidget(self.CopyLeftButton_0, 1, 0, 1, 1)

        self.CopyDownButton_0 = QToolButton(self.CopyToGroupBox_0)
        self.CopyDownButton_0.setObjectName(u"CopyDownButton_0")
        self.CopyDownButton_0.setMinimumSize(QSize(30, 25))

        self.gridLayout_2.addWidget(self.CopyDownButton_0, 2, 1, 1, 1)

        self.CopyRightButton_0 = QToolButton(self.CopyToGroupBox_0)
        self.CopyRightButton_0.setObjectName(u"CopyRightButton_0")
        self.CopyRightButton_0.setMinimumSize(QSize(30, 25))

        self.gridLayout_2.addWidget(self.CopyRightButton_0, 1, 2, 1, 1)

        self.DeleteButton_0 = QToolButton(self.CopyToGroupBox_0)
        self.DeleteButton_0.setObjectName(u"DeleteButton_0")
        self.DeleteButton_0.setMinimumSize(QSize(30, 25))

        self.gridLayout_2.addWidget(self.DeleteButton_0, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.CopyToGroupBox_0)


        self.gridLayout.addWidget(self.frame_0, 1, 0, 1, 1)

        self.frame_1 = QFrame(self.centralwidget)
        self.frame_1.setObjectName(u"frame_1")
        sizePolicy1.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy1)
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SearchCardGroupBox_1 = QGroupBox(self.frame_1)
        self.SearchCardGroupBox_1.setObjectName(u"SearchCardGroupBox_1")
        self.SearchCardGroupBox_1.setFont(font1)
        self.gridLayout_13 = QGridLayout(self.SearchCardGroupBox_1)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.SearchCardEdit_1 = QLineEdit(self.SearchCardGroupBox_1)
        self.SearchCardEdit_1.setObjectName(u"SearchCardEdit_1")
        self.SearchCardEdit_1.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.SearchCardEdit_1, 0, 0, 1, 1)

        self.RunSearchToolButton_1 = QToolButton(self.SearchCardGroupBox_1)
        self.RunSearchToolButton_1.setObjectName(u"RunSearchToolButton_1")

        self.gridLayout_13.addWidget(self.RunSearchToolButton_1, 0, 1, 1, 1)

        self.SearchCardCombo_1 = QComboBox(self.SearchCardGroupBox_1)
        self.SearchCardCombo_1.setObjectName(u"SearchCardCombo_1")

        self.gridLayout_13.addWidget(self.SearchCardCombo_1, 2, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.SearchCardGroupBox_1)

        self.CopyToGroupBox_1 = QGroupBox(self.frame_1)
        self.CopyToGroupBox_1.setObjectName(u"CopyToGroupBox_1")
        self.CopyToGroupBox_1.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.CopyToGroupBox_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.CopyUpButton_1 = QToolButton(self.CopyToGroupBox_1)
        self.CopyUpButton_1.setObjectName(u"CopyUpButton_1")
        self.CopyUpButton_1.setEnabled(False)
        self.CopyUpButton_1.setMinimumSize(QSize(30, 25))

        self.gridLayout_3.addWidget(self.CopyUpButton_1, 0, 1, 1, 1)

        self.CopyLeftButton_1 = QToolButton(self.CopyToGroupBox_1)
        self.CopyLeftButton_1.setObjectName(u"CopyLeftButton_1")
        self.CopyLeftButton_1.setMinimumSize(QSize(30, 25))

        self.gridLayout_3.addWidget(self.CopyLeftButton_1, 1, 0, 1, 1)

        self.CopyDownButton_1 = QToolButton(self.CopyToGroupBox_1)
        self.CopyDownButton_1.setObjectName(u"CopyDownButton_1")
        self.CopyDownButton_1.setMinimumSize(QSize(30, 25))

        self.gridLayout_3.addWidget(self.CopyDownButton_1, 2, 1, 1, 1)

        self.CopyRightButton_1 = QToolButton(self.CopyToGroupBox_1)
        self.CopyRightButton_1.setObjectName(u"CopyRightButton_1")
        self.CopyRightButton_1.setMinimumSize(QSize(30, 25))

        self.gridLayout_3.addWidget(self.CopyRightButton_1, 1, 2, 1, 1)

        self.DeleteButton_1 = QToolButton(self.CopyToGroupBox_1)
        self.DeleteButton_1.setObjectName(u"DeleteButton_1")
        self.DeleteButton_1.setMinimumSize(QSize(30, 25))

        self.gridLayout_3.addWidget(self.DeleteButton_1, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.CopyToGroupBox_1)


        self.gridLayout.addWidget(self.frame_1, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SearchCardGroupBox_3 = QGroupBox(self.frame_3)
        self.SearchCardGroupBox_3.setObjectName(u"SearchCardGroupBox_3")
        self.SearchCardGroupBox_3.setFont(font1)
        self.gridLayout_15 = QGridLayout(self.SearchCardGroupBox_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.SearchCardEdit_3 = QLineEdit(self.SearchCardGroupBox_3)
        self.SearchCardEdit_3.setObjectName(u"SearchCardEdit_3")
        self.SearchCardEdit_3.setClearButtonEnabled(True)

        self.gridLayout_15.addWidget(self.SearchCardEdit_3, 0, 0, 1, 1)

        self.RunSearchToolButton_3 = QToolButton(self.SearchCardGroupBox_3)
        self.RunSearchToolButton_3.setObjectName(u"RunSearchToolButton_3")

        self.gridLayout_15.addWidget(self.RunSearchToolButton_3, 0, 1, 1, 1)

        self.SearchCardCombo_3 = QComboBox(self.SearchCardGroupBox_3)
        self.SearchCardCombo_3.setObjectName(u"SearchCardCombo_3")

        self.gridLayout_15.addWidget(self.SearchCardCombo_3, 2, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.SearchCardGroupBox_3)

        self.CopyToGroupBox_3 = QGroupBox(self.frame_3)
        self.CopyToGroupBox_3.setObjectName(u"CopyToGroupBox_3")
        self.CopyToGroupBox_3.setFont(font1)
        self.gridLayout_5 = QGridLayout(self.CopyToGroupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CopyUpButton_3 = QToolButton(self.CopyToGroupBox_3)
        self.CopyUpButton_3.setObjectName(u"CopyUpButton_3")
        self.CopyUpButton_3.setMinimumSize(QSize(30, 25))

        self.gridLayout_5.addWidget(self.CopyUpButton_3, 0, 1, 1, 1)

        self.CopyLeftButton_3 = QToolButton(self.CopyToGroupBox_3)
        self.CopyLeftButton_3.setObjectName(u"CopyLeftButton_3")
        self.CopyLeftButton_3.setEnabled(False)
        self.CopyLeftButton_3.setMinimumSize(QSize(30, 25))

        self.gridLayout_5.addWidget(self.CopyLeftButton_3, 1, 0, 1, 1)

        self.CopyDownButton_3 = QToolButton(self.CopyToGroupBox_3)
        self.CopyDownButton_3.setObjectName(u"CopyDownButton_3")
        self.CopyDownButton_3.setMinimumSize(QSize(30, 25))

        self.gridLayout_5.addWidget(self.CopyDownButton_3, 2, 1, 1, 1)

        self.CopyRightButton_3 = QToolButton(self.CopyToGroupBox_3)
        self.CopyRightButton_3.setObjectName(u"CopyRightButton_3")
        self.CopyRightButton_3.setMinimumSize(QSize(30, 25))

        self.gridLayout_5.addWidget(self.CopyRightButton_3, 1, 2, 1, 1)

        self.DeleteButton_3 = QToolButton(self.CopyToGroupBox_3)
        self.DeleteButton_3.setObjectName(u"DeleteButton_3")
        self.DeleteButton_3.setMinimumSize(QSize(30, 25))

        self.gridLayout_5.addWidget(self.DeleteButton_3, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.CopyToGroupBox_3)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.SearchCardGroupBox_8 = QGroupBox(self.frame_8)
        self.SearchCardGroupBox_8.setObjectName(u"SearchCardGroupBox_8")
        self.SearchCardGroupBox_8.setFont(font1)
        self.gridLayout_20 = QGridLayout(self.SearchCardGroupBox_8)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.SearchCardEdit_8 = QLineEdit(self.SearchCardGroupBox_8)
        self.SearchCardEdit_8.setObjectName(u"SearchCardEdit_8")
        self.SearchCardEdit_8.setClearButtonEnabled(True)

        self.gridLayout_20.addWidget(self.SearchCardEdit_8, 0, 0, 1, 1)

        self.RunSearchToolButton_8 = QToolButton(self.SearchCardGroupBox_8)
        self.RunSearchToolButton_8.setObjectName(u"RunSearchToolButton_8")

        self.gridLayout_20.addWidget(self.RunSearchToolButton_8, 0, 1, 1, 1)

        self.SearchCardCombo_8 = QComboBox(self.SearchCardGroupBox_8)
        self.SearchCardCombo_8.setObjectName(u"SearchCardCombo_8")

        self.gridLayout_20.addWidget(self.SearchCardCombo_8, 2, 0, 1, 2)


        self.verticalLayout_9.addWidget(self.SearchCardGroupBox_8)

        self.CopyToGroupBox_8 = QGroupBox(self.frame_8)
        self.CopyToGroupBox_8.setObjectName(u"CopyToGroupBox_8")
        self.CopyToGroupBox_8.setFont(font1)
        self.gridLayout_10 = QGridLayout(self.CopyToGroupBox_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.CopyUpButton_8 = QToolButton(self.CopyToGroupBox_8)
        self.CopyUpButton_8.setObjectName(u"CopyUpButton_8")
        self.CopyUpButton_8.setMinimumSize(QSize(30, 25))

        self.gridLayout_10.addWidget(self.CopyUpButton_8, 0, 1, 1, 1)

        self.CopyLeftButton_8 = QToolButton(self.CopyToGroupBox_8)
        self.CopyLeftButton_8.setObjectName(u"CopyLeftButton_8")
        self.CopyLeftButton_8.setMinimumSize(QSize(30, 25))

        self.gridLayout_10.addWidget(self.CopyLeftButton_8, 1, 0, 1, 1)

        self.CopyDownButton_8 = QToolButton(self.CopyToGroupBox_8)
        self.CopyDownButton_8.setObjectName(u"CopyDownButton_8")
        self.CopyDownButton_8.setEnabled(False)
        self.CopyDownButton_8.setMinimumSize(QSize(30, 25))

        self.gridLayout_10.addWidget(self.CopyDownButton_8, 2, 1, 1, 1)

        self.CopyRightButton_8 = QToolButton(self.CopyToGroupBox_8)
        self.CopyRightButton_8.setObjectName(u"CopyRightButton_8")
        self.CopyRightButton_8.setEnabled(False)
        self.CopyRightButton_8.setMinimumSize(QSize(30, 25))

        self.gridLayout_10.addWidget(self.CopyRightButton_8, 1, 2, 1, 1)

        self.DeleteButton_8 = QToolButton(self.CopyToGroupBox_8)
        self.DeleteButton_8.setObjectName(u"DeleteButton_8")
        self.DeleteButton_8.setMinimumSize(QSize(30, 25))

        self.gridLayout_10.addWidget(self.DeleteButton_8, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.CopyToGroupBox_8)


        self.gridLayout.addWidget(self.frame_8, 3, 3, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SearchCardGroupBox_4 = QGroupBox(self.frame_4)
        self.SearchCardGroupBox_4.setObjectName(u"SearchCardGroupBox_4")
        self.SearchCardGroupBox_4.setFont(font1)
        self.gridLayout_16 = QGridLayout(self.SearchCardGroupBox_4)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.SearchCardEdit_4 = QLineEdit(self.SearchCardGroupBox_4)
        self.SearchCardEdit_4.setObjectName(u"SearchCardEdit_4")
        self.SearchCardEdit_4.setClearButtonEnabled(True)

        self.gridLayout_16.addWidget(self.SearchCardEdit_4, 0, 0, 1, 1)

        self.RunSearchToolButton_4 = QToolButton(self.SearchCardGroupBox_4)
        self.RunSearchToolButton_4.setObjectName(u"RunSearchToolButton_4")

        self.gridLayout_16.addWidget(self.RunSearchToolButton_4, 0, 1, 1, 1)

        self.SearchCardCombo_4 = QComboBox(self.SearchCardGroupBox_4)
        self.SearchCardCombo_4.setObjectName(u"SearchCardCombo_4")

        self.gridLayout_16.addWidget(self.SearchCardCombo_4, 2, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.SearchCardGroupBox_4)

        self.CopyToGroupBox_4 = QGroupBox(self.frame_4)
        self.CopyToGroupBox_4.setObjectName(u"CopyToGroupBox_4")
        self.CopyToGroupBox_4.setFont(font1)
        self.gridLayout_6 = QGridLayout(self.CopyToGroupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.CopyUpButton_4 = QToolButton(self.CopyToGroupBox_4)
        self.CopyUpButton_4.setObjectName(u"CopyUpButton_4")
        self.CopyUpButton_4.setMinimumSize(QSize(30, 25))

        self.gridLayout_6.addWidget(self.CopyUpButton_4, 0, 1, 1, 1)

        self.CopyLeftButton_4 = QToolButton(self.CopyToGroupBox_4)
        self.CopyLeftButton_4.setObjectName(u"CopyLeftButton_4")
        self.CopyLeftButton_4.setMinimumSize(QSize(30, 25))

        self.gridLayout_6.addWidget(self.CopyLeftButton_4, 1, 0, 1, 1)

        self.CopyDownButton_4 = QToolButton(self.CopyToGroupBox_4)
        self.CopyDownButton_4.setObjectName(u"CopyDownButton_4")
        self.CopyDownButton_4.setMinimumSize(QSize(30, 25))

        self.gridLayout_6.addWidget(self.CopyDownButton_4, 2, 1, 1, 1)

        self.CopyRightButton_4 = QToolButton(self.CopyToGroupBox_4)
        self.CopyRightButton_4.setObjectName(u"CopyRightButton_4")
        self.CopyRightButton_4.setMinimumSize(QSize(30, 25))

        self.gridLayout_6.addWidget(self.CopyRightButton_4, 1, 2, 1, 1)

        self.DeleteButton_4 = QToolButton(self.CopyToGroupBox_4)
        self.DeleteButton_4.setObjectName(u"DeleteButton_4")
        self.DeleteButton_4.setMinimumSize(QSize(30, 25))

        self.gridLayout_6.addWidget(self.DeleteButton_4, 1, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.CopyToGroupBox_4)


        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SearchCardGroupBox_2 = QGroupBox(self.frame_2)
        self.SearchCardGroupBox_2.setObjectName(u"SearchCardGroupBox_2")
        self.SearchCardGroupBox_2.setFont(font1)
        self.gridLayout_14 = QGridLayout(self.SearchCardGroupBox_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.SearchCardEdit_2 = QLineEdit(self.SearchCardGroupBox_2)
        self.SearchCardEdit_2.setObjectName(u"SearchCardEdit_2")
        self.SearchCardEdit_2.setClearButtonEnabled(True)

        self.gridLayout_14.addWidget(self.SearchCardEdit_2, 0, 0, 1, 1)

        self.RunSearchToolButton_2 = QToolButton(self.SearchCardGroupBox_2)
        self.RunSearchToolButton_2.setObjectName(u"RunSearchToolButton_2")

        self.gridLayout_14.addWidget(self.RunSearchToolButton_2, 0, 1, 1, 1)

        self.SearchCardCombo_2 = QComboBox(self.SearchCardGroupBox_2)
        self.SearchCardCombo_2.setObjectName(u"SearchCardCombo_2")

        self.gridLayout_14.addWidget(self.SearchCardCombo_2, 2, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.SearchCardGroupBox_2)

        self.CopyToGroupBox_2 = QGroupBox(self.frame_2)
        self.CopyToGroupBox_2.setObjectName(u"CopyToGroupBox_2")
        self.CopyToGroupBox_2.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.CopyToGroupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.CopyUpButton_2 = QToolButton(self.CopyToGroupBox_2)
        self.CopyUpButton_2.setObjectName(u"CopyUpButton_2")
        self.CopyUpButton_2.setEnabled(False)
        self.CopyUpButton_2.setMinimumSize(QSize(30, 25))

        self.gridLayout_4.addWidget(self.CopyUpButton_2, 0, 1, 1, 1)

        self.CopyLeftButton_2 = QToolButton(self.CopyToGroupBox_2)
        self.CopyLeftButton_2.setObjectName(u"CopyLeftButton_2")
        self.CopyLeftButton_2.setMinimumSize(QSize(30, 25))

        self.gridLayout_4.addWidget(self.CopyLeftButton_2, 1, 0, 1, 1)

        self.CopyDownButton_2 = QToolButton(self.CopyToGroupBox_2)
        self.CopyDownButton_2.setObjectName(u"CopyDownButton_2")
        self.CopyDownButton_2.setMinimumSize(QSize(30, 25))

        self.gridLayout_4.addWidget(self.CopyDownButton_2, 2, 1, 1, 1)

        self.CopyRightButton_2 = QToolButton(self.CopyToGroupBox_2)
        self.CopyRightButton_2.setObjectName(u"CopyRightButton_2")
        self.CopyRightButton_2.setEnabled(False)
        self.CopyRightButton_2.setMinimumSize(QSize(30, 25))

        self.gridLayout_4.addWidget(self.CopyRightButton_2, 1, 2, 1, 1)

        self.DeleteButton_2 = QToolButton(self.CopyToGroupBox_2)
        self.DeleteButton_2.setObjectName(u"DeleteButton_2")
        self.DeleteButton_2.setMinimumSize(QSize(30, 25))

        self.gridLayout_4.addWidget(self.DeleteButton_2, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.CopyToGroupBox_2)


        self.gridLayout.addWidget(self.frame_2, 1, 3, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SearchCardGroupBox_5 = QGroupBox(self.frame_5)
        self.SearchCardGroupBox_5.setObjectName(u"SearchCardGroupBox_5")
        self.SearchCardGroupBox_5.setFont(font1)
        self.gridLayout_17 = QGridLayout(self.SearchCardGroupBox_5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.SearchCardEdit_5 = QLineEdit(self.SearchCardGroupBox_5)
        self.SearchCardEdit_5.setObjectName(u"SearchCardEdit_5")
        self.SearchCardEdit_5.setClearButtonEnabled(True)

        self.gridLayout_17.addWidget(self.SearchCardEdit_5, 0, 0, 1, 1)

        self.RunSearchToolButton_5 = QToolButton(self.SearchCardGroupBox_5)
        self.RunSearchToolButton_5.setObjectName(u"RunSearchToolButton_5")

        self.gridLayout_17.addWidget(self.RunSearchToolButton_5, 0, 1, 1, 1)

        self.SearchCardCombo_5 = QComboBox(self.SearchCardGroupBox_5)
        self.SearchCardCombo_5.setObjectName(u"SearchCardCombo_5")

        self.gridLayout_17.addWidget(self.SearchCardCombo_5, 2, 0, 1, 2)


        self.verticalLayout_6.addWidget(self.SearchCardGroupBox_5)

        self.CopyToGroupBox_5 = QGroupBox(self.frame_5)
        self.CopyToGroupBox_5.setObjectName(u"CopyToGroupBox_5")
        self.CopyToGroupBox_5.setFont(font1)
        self.gridLayout_7 = QGridLayout(self.CopyToGroupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.CopyUpButton_5 = QToolButton(self.CopyToGroupBox_5)
        self.CopyUpButton_5.setObjectName(u"CopyUpButton_5")
        self.CopyUpButton_5.setMinimumSize(QSize(30, 25))

        self.gridLayout_7.addWidget(self.CopyUpButton_5, 0, 1, 1, 1)

        self.CopyLeftButton_5 = QToolButton(self.CopyToGroupBox_5)
        self.CopyLeftButton_5.setObjectName(u"CopyLeftButton_5")
        self.CopyLeftButton_5.setMinimumSize(QSize(30, 25))

        self.gridLayout_7.addWidget(self.CopyLeftButton_5, 1, 0, 1, 1)

        self.CopyDownButton_5 = QToolButton(self.CopyToGroupBox_5)
        self.CopyDownButton_5.setObjectName(u"CopyDownButton_5")
        self.CopyDownButton_5.setMinimumSize(QSize(30, 25))

        self.gridLayout_7.addWidget(self.CopyDownButton_5, 2, 1, 1, 1)

        self.CopyRightButton_5 = QToolButton(self.CopyToGroupBox_5)
        self.CopyRightButton_5.setObjectName(u"CopyRightButton_5")
        self.CopyRightButton_5.setEnabled(False)
        self.CopyRightButton_5.setMinimumSize(QSize(30, 25))

        self.gridLayout_7.addWidget(self.CopyRightButton_5, 1, 2, 1, 1)

        self.DeleteButton_5 = QToolButton(self.CopyToGroupBox_5)
        self.DeleteButton_5.setObjectName(u"DeleteButton_5")
        self.DeleteButton_5.setMinimumSize(QSize(30, 25))

        self.gridLayout_7.addWidget(self.DeleteButton_5, 1, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.CopyToGroupBox_5)


        self.gridLayout.addWidget(self.frame_5, 2, 3, 1, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.SearchCardGroupBox_6 = QGroupBox(self.frame_6)
        self.SearchCardGroupBox_6.setObjectName(u"SearchCardGroupBox_6")
        self.SearchCardGroupBox_6.setFont(font1)
        self.gridLayout_18 = QGridLayout(self.SearchCardGroupBox_6)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.SearchCardEdit_6 = QLineEdit(self.SearchCardGroupBox_6)
        self.SearchCardEdit_6.setObjectName(u"SearchCardEdit_6")
        self.SearchCardEdit_6.setClearButtonEnabled(True)

        self.gridLayout_18.addWidget(self.SearchCardEdit_6, 0, 0, 1, 1)

        self.RunSearchToolButton_6 = QToolButton(self.SearchCardGroupBox_6)
        self.RunSearchToolButton_6.setObjectName(u"RunSearchToolButton_6")

        self.gridLayout_18.addWidget(self.RunSearchToolButton_6, 0, 1, 1, 1)

        self.SearchCardCombo_6 = QComboBox(self.SearchCardGroupBox_6)
        self.SearchCardCombo_6.setObjectName(u"SearchCardCombo_6")

        self.gridLayout_18.addWidget(self.SearchCardCombo_6, 2, 0, 1, 2)


        self.verticalLayout_7.addWidget(self.SearchCardGroupBox_6)

        self.CopyToGroupBox_6 = QGroupBox(self.frame_6)
        self.CopyToGroupBox_6.setObjectName(u"CopyToGroupBox_6")
        self.CopyToGroupBox_6.setFont(font1)
        self.gridLayout_8 = QGridLayout(self.CopyToGroupBox_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.CopyUpButton_6 = QToolButton(self.CopyToGroupBox_6)
        self.CopyUpButton_6.setObjectName(u"CopyUpButton_6")
        self.CopyUpButton_6.setMinimumSize(QSize(30, 25))

        self.gridLayout_8.addWidget(self.CopyUpButton_6, 0, 1, 1, 1)

        self.CopyLeftButton_6 = QToolButton(self.CopyToGroupBox_6)
        self.CopyLeftButton_6.setObjectName(u"CopyLeftButton_6")
        self.CopyLeftButton_6.setEnabled(False)
        self.CopyLeftButton_6.setMinimumSize(QSize(30, 25))

        self.gridLayout_8.addWidget(self.CopyLeftButton_6, 1, 0, 1, 1)

        self.CopyDownButton_6 = QToolButton(self.CopyToGroupBox_6)
        self.CopyDownButton_6.setObjectName(u"CopyDownButton_6")
        self.CopyDownButton_6.setEnabled(False)
        self.CopyDownButton_6.setMinimumSize(QSize(30, 25))

        self.gridLayout_8.addWidget(self.CopyDownButton_6, 2, 1, 1, 1)

        self.CopyRightButton_6 = QToolButton(self.CopyToGroupBox_6)
        self.CopyRightButton_6.setObjectName(u"CopyRightButton_6")
        self.CopyRightButton_6.setMinimumSize(QSize(30, 25))

        self.gridLayout_8.addWidget(self.CopyRightButton_6, 1, 2, 1, 1)

        self.DeleteButton_6 = QToolButton(self.CopyToGroupBox_6)
        self.DeleteButton_6.setObjectName(u"DeleteButton_6")
        self.DeleteButton_6.setMinimumSize(QSize(30, 25))

        self.gridLayout_8.addWidget(self.DeleteButton_6, 1, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.CopyToGroupBox_6)


        self.gridLayout.addWidget(self.frame_6, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.SearchCardGroupBox_7 = QGroupBox(self.frame_7)
        self.SearchCardGroupBox_7.setObjectName(u"SearchCardGroupBox_7")
        self.SearchCardGroupBox_7.setFont(font1)
        self.gridLayout_19 = QGridLayout(self.SearchCardGroupBox_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.SearchCardEdit_7 = QLineEdit(self.SearchCardGroupBox_7)
        self.SearchCardEdit_7.setObjectName(u"SearchCardEdit_7")
        self.SearchCardEdit_7.setClearButtonEnabled(True)

        self.gridLayout_19.addWidget(self.SearchCardEdit_7, 0, 0, 1, 1)

        self.RunSearchToolButton_7 = QToolButton(self.SearchCardGroupBox_7)
        self.RunSearchToolButton_7.setObjectName(u"RunSearchToolButton_7")

        self.gridLayout_19.addWidget(self.RunSearchToolButton_7, 0, 1, 1, 1)

        self.SearchCardCombo_7 = QComboBox(self.SearchCardGroupBox_7)
        self.SearchCardCombo_7.setObjectName(u"SearchCardCombo_7")

        self.gridLayout_19.addWidget(self.SearchCardCombo_7, 2, 0, 1, 2)


        self.verticalLayout_8.addWidget(self.SearchCardGroupBox_7)

        self.CopyToGroupBox_7 = QGroupBox(self.frame_7)
        self.CopyToGroupBox_7.setObjectName(u"CopyToGroupBox_7")
        self.CopyToGroupBox_7.setFont(font1)
        self.gridLayout_9 = QGridLayout(self.CopyToGroupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.CopyUpButton_7 = QToolButton(self.CopyToGroupBox_7)
        self.CopyUpButton_7.setObjectName(u"CopyUpButton_7")
        self.CopyUpButton_7.setMinimumSize(QSize(30, 25))

        self.gridLayout_9.addWidget(self.CopyUpButton_7, 0, 1, 1, 1)

        self.CopyLeftButton_7 = QToolButton(self.CopyToGroupBox_7)
        self.CopyLeftButton_7.setObjectName(u"CopyLeftButton_7")
        self.CopyLeftButton_7.setMinimumSize(QSize(30, 25))

        self.gridLayout_9.addWidget(self.CopyLeftButton_7, 1, 0, 1, 1)

        self.CopyDownButton_7 = QToolButton(self.CopyToGroupBox_7)
        self.CopyDownButton_7.setObjectName(u"CopyDownButton_7")
        self.CopyDownButton_7.setEnabled(False)
        self.CopyDownButton_7.setMinimumSize(QSize(30, 25))

        self.gridLayout_9.addWidget(self.CopyDownButton_7, 2, 1, 1, 1)

        self.CopyRightButton_7 = QToolButton(self.CopyToGroupBox_7)
        self.CopyRightButton_7.setObjectName(u"CopyRightButton_7")
        self.CopyRightButton_7.setMinimumSize(QSize(30, 25))

        self.gridLayout_9.addWidget(self.CopyRightButton_7, 1, 2, 1, 1)

        self.DeleteButton_7 = QToolButton(self.CopyToGroupBox_7)
        self.DeleteButton_7.setObjectName(u"DeleteButton_7")
        self.DeleteButton_7.setMinimumSize(QSize(30, 25))

        self.gridLayout_9.addWidget(self.DeleteButton_7, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.CopyToGroupBox_7)


        self.gridLayout.addWidget(self.frame_7, 3, 1, 1, 1)

        self.LanguageGroupBox = QGroupBox(self.centralwidget)
        self.LanguageGroupBox.setObjectName(u"LanguageGroupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LanguageGroupBox.sizePolicy().hasHeightForWidth())
        self.LanguageGroupBox.setSizePolicy(sizePolicy2)
        self.LanguageGroupBox.setFont(font1)
        self.LanguageGroupBox.setStyleSheet(u"background-color: rgba(0, 0, 0, 0)")
        self.gridLayout_11 = QGridLayout(self.LanguageGroupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.GermanRadioButton = QRadioButton(self.LanguageGroupBox)
        self.GermanRadioButton.setObjectName(u"GermanRadioButton")

        self.gridLayout_11.addWidget(self.GermanRadioButton, 0, 2, 1, 1)

        self.FrenchRadioButton = QRadioButton(self.LanguageGroupBox)
        self.FrenchRadioButton.setObjectName(u"FrenchRadioButton")

        self.gridLayout_11.addWidget(self.FrenchRadioButton, 0, 1, 1, 1)

        self.EnglishRadioButton = QRadioButton(self.LanguageGroupBox)
        self.EnglishRadioButton.setObjectName(u"EnglishRadioButton")
        self.EnglishRadioButton.setChecked(True)

        self.gridLayout_11.addWidget(self.EnglishRadioButton, 0, 0, 1, 1)

        self.ItalianRadioButton = QRadioButton(self.LanguageGroupBox)
        self.ItalianRadioButton.setObjectName(u"ItalianRadioButton")

        self.gridLayout_11.addWidget(self.ItalianRadioButton, 0, 3, 1, 1)

        self.PortugueseRadioButton = QRadioButton(self.LanguageGroupBox)
        self.PortugueseRadioButton.setObjectName(u"PortugueseRadioButton")

        self.gridLayout_11.addWidget(self.PortugueseRadioButton, 0, 4, 1, 1)


        self.gridLayout.addWidget(self.LanguageGroupBox, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.SearchCardEdit_0, self.SearchCardCombo_0)
        QWidget.setTabOrder(self.SearchCardCombo_0, self.GetImagesButton)
        QWidget.setTabOrder(self.GetImagesButton, self.ExportPDFButton)
        QWidget.setTabOrder(self.ExportPDFButton, self.CopyUpButton_0)
        QWidget.setTabOrder(self.CopyUpButton_0, self.CopyLeftButton_0)
        QWidget.setTabOrder(self.CopyLeftButton_0, self.DeleteButton_0)
        QWidget.setTabOrder(self.DeleteButton_0, self.CopyRightButton_0)
        QWidget.setTabOrder(self.CopyRightButton_0, self.CopyDownButton_0)
        QWidget.setTabOrder(self.CopyDownButton_0, self.CopyUpButton_1)
        QWidget.setTabOrder(self.CopyUpButton_1, self.CopyLeftButton_1)
        QWidget.setTabOrder(self.CopyLeftButton_1, self.DeleteButton_1)
        QWidget.setTabOrder(self.DeleteButton_1, self.CopyRightButton_1)
        QWidget.setTabOrder(self.CopyRightButton_1, self.CopyDownButton_1)
        QWidget.setTabOrder(self.CopyDownButton_1, self.CopyUpButton_2)
        QWidget.setTabOrder(self.CopyUpButton_2, self.CopyLeftButton_2)
        QWidget.setTabOrder(self.CopyLeftButton_2, self.DeleteButton_2)
        QWidget.setTabOrder(self.DeleteButton_2, self.CopyRightButton_2)
        QWidget.setTabOrder(self.CopyRightButton_2, self.CopyDownButton_2)
        QWidget.setTabOrder(self.CopyDownButton_2, self.CopyUpButton_3)
        QWidget.setTabOrder(self.CopyUpButton_3, self.CopyLeftButton_3)
        QWidget.setTabOrder(self.CopyLeftButton_3, self.DeleteButton_3)
        QWidget.setTabOrder(self.DeleteButton_3, self.CopyRightButton_3)
        QWidget.setTabOrder(self.CopyRightButton_3, self.CopyDownButton_3)
        QWidget.setTabOrder(self.CopyDownButton_3, self.CopyUpButton_4)
        QWidget.setTabOrder(self.CopyUpButton_4, self.CopyLeftButton_4)
        QWidget.setTabOrder(self.CopyLeftButton_4, self.DeleteButton_4)
        QWidget.setTabOrder(self.DeleteButton_4, self.CopyRightButton_4)
        QWidget.setTabOrder(self.CopyRightButton_4, self.CopyDownButton_4)
        QWidget.setTabOrder(self.CopyDownButton_4, self.CopyUpButton_5)
        QWidget.setTabOrder(self.CopyUpButton_5, self.CopyLeftButton_5)
        QWidget.setTabOrder(self.CopyLeftButton_5, self.DeleteButton_5)
        QWidget.setTabOrder(self.DeleteButton_5, self.CopyRightButton_5)
        QWidget.setTabOrder(self.CopyRightButton_5, self.CopyDownButton_5)
        QWidget.setTabOrder(self.CopyDownButton_5, self.CopyUpButton_6)
        QWidget.setTabOrder(self.CopyUpButton_6, self.CopyLeftButton_6)
        QWidget.setTabOrder(self.CopyLeftButton_6, self.DeleteButton_6)
        QWidget.setTabOrder(self.DeleteButton_6, self.CopyRightButton_6)
        QWidget.setTabOrder(self.CopyRightButton_6, self.CopyDownButton_6)
        QWidget.setTabOrder(self.CopyDownButton_6, self.CopyUpButton_7)
        QWidget.setTabOrder(self.CopyUpButton_7, self.CopyLeftButton_7)
        QWidget.setTabOrder(self.CopyLeftButton_7, self.DeleteButton_7)
        QWidget.setTabOrder(self.DeleteButton_7, self.CopyRightButton_7)
        QWidget.setTabOrder(self.CopyRightButton_7, self.CopyDownButton_7)
        QWidget.setTabOrder(self.CopyDownButton_7, self.CopyUpButton_8)
        QWidget.setTabOrder(self.CopyUpButton_8, self.CopyLeftButton_8)
        QWidget.setTabOrder(self.CopyLeftButton_8, self.DeleteButton_8)
        QWidget.setTabOrder(self.DeleteButton_8, self.CopyRightButton_8)
        QWidget.setTabOrder(self.CopyRightButton_8, self.CopyDownButton_8)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YGOProxyPrinter", None))
        self.ExportPDFButton.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.GetImagesButton.setText(QCoreApplication.translate("MainWindow", u"Get images", None))
#if QT_CONFIG(tooltip)
        self.frame_0.setToolTip(QCoreApplication.translate("MainWindow", u"Card #1", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_0.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_0.setText("")
        self.CopyToGroupBox_0.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
#if QT_CONFIG(tooltip)
        self.CopyUpButton_0.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.CopyUpButton_0.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_0.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
#if QT_CONFIG(tooltip)
        self.CopyDownButton_0.setToolTip(QCoreApplication.translate("MainWindow", u"Copy down", None))
#endif // QT_CONFIG(tooltip)
        self.CopyDownButton_0.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
#if QT_CONFIG(tooltip)
        self.CopyRightButton_0.setToolTip(QCoreApplication.translate("MainWindow", u"Copy right", None))
#endif // QT_CONFIG(tooltip)
        self.CopyRightButton_0.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_0.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_0.setText("")
#if QT_CONFIG(tooltip)
        self.frame_1.setToolTip(QCoreApplication.translate("MainWindow", u"Card #2", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_1.setText("")
        self.CopyToGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
        self.CopyUpButton_1.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
#if QT_CONFIG(tooltip)
        self.CopyLeftButton_1.setToolTip(QCoreApplication.translate("MainWindow", u"Copy left", None))
#endif // QT_CONFIG(tooltip)
        self.CopyLeftButton_1.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
#if QT_CONFIG(tooltip)
        self.CopyDownButton_1.setToolTip(QCoreApplication.translate("MainWindow", u"Copy down", None))
#endif // QT_CONFIG(tooltip)
        self.CopyDownButton_1.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
#if QT_CONFIG(tooltip)
        self.CopyRightButton_1.setToolTip(QCoreApplication.translate("MainWindow", u"Copy right", None))
#endif // QT_CONFIG(tooltip)
        self.CopyRightButton_1.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_1.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_1.setText("")
#if QT_CONFIG(tooltip)
        self.frame_3.setToolTip(QCoreApplication.translate("MainWindow", u"Card #4", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_3.setText("")
        self.CopyToGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
#if QT_CONFIG(tooltip)
        self.CopyUpButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"Copy up", None))
#endif // QT_CONFIG(tooltip)
        self.CopyUpButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
#if QT_CONFIG(tooltip)
        self.CopyDownButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"Copy down", None))
#endif // QT_CONFIG(tooltip)
        self.CopyDownButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
#if QT_CONFIG(tooltip)
        self.CopyRightButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"Copy right", None))
#endif // QT_CONFIG(tooltip)
        self.CopyRightButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.frame_8.setToolTip(QCoreApplication.translate("MainWindow", u"Card #9", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_8.setText("")
        self.CopyToGroupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
#if QT_CONFIG(tooltip)
        self.CopyUpButton_8.setToolTip(QCoreApplication.translate("MainWindow", u"Copy up", None))
#endif // QT_CONFIG(tooltip)
        self.CopyUpButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
#if QT_CONFIG(tooltip)
        self.CopyLeftButton_8.setToolTip(QCoreApplication.translate("MainWindow", u"Copy left", None))
#endif // QT_CONFIG(tooltip)
        self.CopyLeftButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_8.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.frame_4.setToolTip(QCoreApplication.translate("MainWindow", u"Card #5", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_4.setText("")
        self.CopyToGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
#if QT_CONFIG(tooltip)
        self.CopyUpButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Copy up", None))
#endif // QT_CONFIG(tooltip)
        self.CopyUpButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
#if QT_CONFIG(tooltip)
        self.CopyLeftButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Copy left", None))
#endif // QT_CONFIG(tooltip)
        self.CopyLeftButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
#if QT_CONFIG(tooltip)
        self.CopyDownButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Copy down", None))
#endif // QT_CONFIG(tooltip)
        self.CopyDownButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
#if QT_CONFIG(tooltip)
        self.CopyRightButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Copy right", None))
#endif // QT_CONFIG(tooltip)
        self.CopyRightButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_4.setText("")
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip(QCoreApplication.translate("MainWindow", u"Card #3", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_2.setText("")
        self.CopyToGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
        self.CopyUpButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
#if QT_CONFIG(tooltip)
        self.CopyLeftButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Copy left", None))
#endif // QT_CONFIG(tooltip)
        self.CopyLeftButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
#if QT_CONFIG(tooltip)
        self.CopyDownButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Copy down", None))
#endif // QT_CONFIG(tooltip)
        self.CopyDownButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.frame_5.setToolTip(QCoreApplication.translate("MainWindow", u"Card #6", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_5.setText("")
        self.CopyToGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
#if QT_CONFIG(tooltip)
        self.CopyUpButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Copy up", None))
#endif // QT_CONFIG(tooltip)
        self.CopyUpButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
#if QT_CONFIG(tooltip)
        self.CopyLeftButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Copy left", None))
#endif // QT_CONFIG(tooltip)
        self.CopyLeftButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
#if QT_CONFIG(tooltip)
        self.CopyDownButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Copy down", None))
#endif // QT_CONFIG(tooltip)
        self.CopyDownButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.CopyRightButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.frame_6.setToolTip(QCoreApplication.translate("MainWindow", u"Card #7", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_6.setText("")
        self.CopyToGroupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
#if QT_CONFIG(tooltip)
        self.CopyUpButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Copy up", None))
#endif // QT_CONFIG(tooltip)
        self.CopyUpButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.CopyLeftButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
#if QT_CONFIG(tooltip)
        self.CopyRightButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Copy right", None))
#endif // QT_CONFIG(tooltip)
        self.CopyRightButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_6.setText("")
#if QT_CONFIG(tooltip)
        self.frame_7.setToolTip(QCoreApplication.translate("MainWindow", u"Card #8", None))
#endif // QT_CONFIG(tooltip)
        self.SearchCardGroupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Search by card name", None))
        self.SearchCardEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card...", None))
        self.RunSearchToolButton_7.setText("")
        self.CopyToGroupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Copy to / delete", None))
#if QT_CONFIG(tooltip)
        self.CopyUpButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Copy up", None))
#endif // QT_CONFIG(tooltip)
        self.CopyUpButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
#if QT_CONFIG(tooltip)
        self.CopyLeftButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Copy left", None))
#endif // QT_CONFIG(tooltip)
        self.CopyLeftButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.CopyDownButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
#if QT_CONFIG(tooltip)
        self.CopyRightButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Copy right", None))
#endif // QT_CONFIG(tooltip)
        self.CopyRightButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
#if QT_CONFIG(tooltip)
        self.DeleteButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteButton_7.setText("")
#if QT_CONFIG(tooltip)
        self.LanguageGroupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Choose which language to use for card name search", None))
#endif // QT_CONFIG(tooltip)
        self.LanguageGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Card name language", None))
#if QT_CONFIG(tooltip)
        self.GermanRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Deutsch", None))
#endif // QT_CONFIG(tooltip)
        self.GermanRadioButton.setText(QCoreApplication.translate("MainWindow", u"de", None))
#if QT_CONFIG(tooltip)
        self.FrenchRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))
#endif // QT_CONFIG(tooltip)
        self.FrenchRadioButton.setText(QCoreApplication.translate("MainWindow", u"fr", None))
#if QT_CONFIG(tooltip)
        self.EnglishRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"English", None))
#endif // QT_CONFIG(tooltip)
        self.EnglishRadioButton.setText(QCoreApplication.translate("MainWindow", u"en", None))
#if QT_CONFIG(tooltip)
        self.ItalianRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Italiano", None))
#endif // QT_CONFIG(tooltip)
        self.ItalianRadioButton.setText(QCoreApplication.translate("MainWindow", u"it", None))
#if QT_CONFIG(tooltip)
        self.PortugueseRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Portugu\u00eas", None))
#endif // QT_CONFIG(tooltip)
        self.PortugueseRadioButton.setText(QCoreApplication.translate("MainWindow", u"pt", None))
    # retranslateUi

