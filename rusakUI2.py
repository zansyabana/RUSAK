# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rusakUI2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(440, 1074)
        MainWindow.setMinimumSize(QSize(440, 0))
        self.verticalLayout_12 = QVBoxLayout(MainWindow)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(393, 0))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tab_ctrl = QWidget()
        self.tab_ctrl.setObjectName(u"tab_ctrl")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.tab_ctrl.setFont(font1)
        self.tab_ctrl.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.tab_ctrl)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.scrollArea = QScrollArea(self.tab_ctrl)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 373, 992))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(172, 172, 172);\n"
"font: 75 10pt \"Rubik\";\n"
"color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.asCrv = QRadioButton(self.scrollAreaWidgetContents)
        self.ctrlAs_bGrp = QButtonGroup(MainWindow)
        self.ctrlAs_bGrp.setObjectName(u"ctrlAs_bGrp")
        self.ctrlAs_bGrp.addButton(self.asCrv)
        self.asCrv.setObjectName(u"asCrv")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asCrv.sizePolicy().hasHeightForWidth())
        self.asCrv.setSizePolicy(sizePolicy)
        self.asCrv.setChecked(True)

        self.horizontalLayout.addWidget(self.asCrv)

        self.asJnt = QRadioButton(self.scrollAreaWidgetContents)
        self.ctrlAs_bGrp.addButton(self.asJnt)
        self.asJnt.setObjectName(u"asJnt")
        sizePolicy.setHeightForWidth(self.asJnt.sizePolicy().hasHeightForWidth())
        self.asJnt.setSizePolicy(sizePolicy)
        self.asJnt.setChecked(False)

        self.horizontalLayout.addWidget(self.asJnt)

        self.asReplace = QRadioButton(self.scrollAreaWidgetContents)
        self.ctrlAs_bGrp.addButton(self.asReplace)
        self.asReplace.setObjectName(u"asReplace")

        self.horizontalLayout.addWidget(self.asReplace)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout.addWidget(self.label_14)

        self.spawnAtPivot_rBtn = QRadioButton(self.scrollAreaWidgetContents)
        self.spawnAt_bGrp = QButtonGroup(MainWindow)
        self.spawnAt_bGrp.setObjectName(u"spawnAt_bGrp")
        self.spawnAt_bGrp.addButton(self.spawnAtPivot_rBtn)
        self.spawnAtPivot_rBtn.setObjectName(u"spawnAtPivot_rBtn")
        self.spawnAtPivot_rBtn.setChecked(True)

        self.horizontalLayout.addWidget(self.spawnAtPivot_rBtn)

        self.spawnAtCenter_rBtn = QRadioButton(self.scrollAreaWidgetContents)
        self.spawnAt_bGrp.addButton(self.spawnAtCenter_rBtn)
        self.spawnAtCenter_rBtn.setObjectName(u"spawnAtCenter_rBtn")

        self.horizontalLayout.addWidget(self.spawnAtCenter_rBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.spawnMult_spBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.spawnMult_spBox.setObjectName(u"spawnMult_spBox")
        self.spawnMult_spBox.setDecimals(1)
        self.spawnMult_spBox.setMinimum(0.100000000000000)
        self.spawnMult_spBox.setValue(1.000000000000000)

        self.horizontalLayout_11.addWidget(self.spawnMult_spBox)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)


        self.horizontalLayout_27.addLayout(self.horizontalLayout_11)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_27.addWidget(self.label_2)

        self.createCtlSfx_lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.createCtlSfx_lineEdit.setObjectName(u"createCtlSfx_lineEdit")

        self.horizontalLayout_27.addWidget(self.createCtlSfx_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_27)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.shp_CrossArrow = QPushButton(self.groupBox)
        self.shp_CrossArrow.setObjectName(u"shp_CrossArrow")
        self.shp_CrossArrow.setFocusPolicy(Qt.NoFocus)
        self.shp_CrossArrow.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_CrossArrow.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icon/crossArrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_CrossArrow.setIcon(icon)
        self.shp_CrossArrow.setIconSize(QSize(20, 20))
        self.shp_CrossArrow.setCheckable(False)
        self.shp_CrossArrow.setChecked(False)
        self.shp_CrossArrow.setFlat(True)

        self.gridLayout.addWidget(self.shp_CrossArrow, 1, 1, 1, 1)

        self.shp_Arrow = QPushButton(self.groupBox)
        self.shp_Arrow.setObjectName(u"shp_Arrow")
        self.shp_Arrow.setFocusPolicy(Qt.NoFocus)
        self.shp_Arrow.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_Arrow.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/icon/arrowDouble.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_Arrow.setIcon(icon1)
        self.shp_Arrow.setIconSize(QSize(20, 20))
        self.shp_Arrow.setCheckable(False)
        self.shp_Arrow.setChecked(False)
        self.shp_Arrow.setFlat(True)

        self.gridLayout.addWidget(self.shp_Arrow, 1, 0, 1, 1)

        self.shp_Needle = QPushButton(self.groupBox)
        self.shp_Needle.setObjectName(u"shp_Needle")
        self.shp_Needle.setFocusPolicy(Qt.NoFocus)
        self.shp_Needle.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_Needle.setAutoFillBackground(False)
        self.shp_Needle.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        icon2 = QIcon()
        icon2.addFile(u":/icon/needle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_Needle.setIcon(icon2)
        self.shp_Needle.setIconSize(QSize(20, 20))
        self.shp_Needle.setCheckable(False)
        self.shp_Needle.setChecked(False)
        self.shp_Needle.setFlat(True)

        self.gridLayout.addWidget(self.shp_Needle, 1, 4, 1, 1)

        self.shp_ArrowBent = QPushButton(self.groupBox)
        self.shp_ArrowBent.setObjectName(u"shp_ArrowBent")
        self.shp_ArrowBent.setFocusPolicy(Qt.NoFocus)
        self.shp_ArrowBent.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_ArrowBent.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/icon/arrowBent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_ArrowBent.setIcon(icon3)
        self.shp_ArrowBent.setIconSize(QSize(20, 20))
        self.shp_ArrowBent.setCheckable(False)
        self.shp_ArrowBent.setChecked(False)
        self.shp_ArrowBent.setFlat(True)

        self.gridLayout.addWidget(self.shp_ArrowBent, 1, 2, 1, 1)

        self.shp_CrossArrowBent = QPushButton(self.groupBox)
        self.shp_CrossArrowBent.setObjectName(u"shp_CrossArrowBent")
        self.shp_CrossArrowBent.setFocusPolicy(Qt.NoFocus)
        self.shp_CrossArrowBent.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_CrossArrowBent.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/icon/crossArrowBent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_CrossArrowBent.setIcon(icon4)
        self.shp_CrossArrowBent.setIconSize(QSize(20, 20))
        self.shp_CrossArrowBent.setCheckable(False)
        self.shp_CrossArrowBent.setChecked(False)
        self.shp_CrossArrowBent.setFlat(True)

        self.gridLayout.addWidget(self.shp_CrossArrowBent, 1, 3, 1, 1)

        self.shp_Circle = QPushButton(self.groupBox)
        self.shp_Circle.setObjectName(u"shp_Circle")
        self.shp_Circle.setFocusPolicy(Qt.NoFocus)
        self.shp_Circle.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_Circle.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/icon/circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_Circle.setIcon(icon5)
        self.shp_Circle.setIconSize(QSize(20, 20))
        self.shp_Circle.setCheckable(False)
        self.shp_Circle.setChecked(False)
        self.shp_Circle.setFlat(True)

        self.gridLayout.addWidget(self.shp_Circle, 0, 0, 1, 1)

        self.shp_Square = QPushButton(self.groupBox)
        self.shp_Square.setObjectName(u"shp_Square")
        self.shp_Square.setFocusPolicy(Qt.NoFocus)
        self.shp_Square.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_Square.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/icon/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_Square.setIcon(icon6)
        self.shp_Square.setIconSize(QSize(20, 20))
        self.shp_Square.setCheckable(False)
        self.shp_Square.setChecked(False)
        self.shp_Square.setFlat(True)

        self.gridLayout.addWidget(self.shp_Square, 0, 1, 1, 1)

        self.shp_Cross = QPushButton(self.groupBox)
        self.shp_Cross.setObjectName(u"shp_Cross")
        self.shp_Cross.setFocusPolicy(Qt.NoFocus)
        self.shp_Cross.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_Cross.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/icon/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_Cross.setIcon(icon7)
        self.shp_Cross.setIconSize(QSize(20, 20))
        self.shp_Cross.setCheckable(False)
        self.shp_Cross.setChecked(False)
        self.shp_Cross.setFlat(True)

        self.gridLayout.addWidget(self.shp_Cross, 0, 4, 1, 1)

        self.shp_Sphere = QPushButton(self.groupBox)
        self.shp_Sphere.setObjectName(u"shp_Sphere")
        self.shp_Sphere.setMinimumSize(QSize(51, 28))
        self.shp_Sphere.setFocusPolicy(Qt.NoFocus)
        self.shp_Sphere.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_Sphere.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/icon/sphere.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_Sphere.setIcon(icon8)
        self.shp_Sphere.setIconSize(QSize(20, 20))
        self.shp_Sphere.setCheckable(False)
        self.shp_Sphere.setChecked(False)
        self.shp_Sphere.setFlat(True)

        self.gridLayout.addWidget(self.shp_Sphere, 0, 2, 1, 1)

        self.shp_Box = QPushButton(self.groupBox)
        self.shp_Box.setObjectName(u"shp_Box")
        self.shp_Box.setFocusPolicy(Qt.NoFocus)
        self.shp_Box.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shp_Box.setAutoFillBackground(False)
        icon9 = QIcon()
        icon9.addFile(u":/icon/box.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shp_Box.setIcon(icon9)
        self.shp_Box.setIconSize(QSize(20, 20))
        self.shp_Box.setCheckable(False)
        self.shp_Box.setChecked(False)
        self.shp_Box.setFlat(True)

        self.gridLayout.addWidget(self.shp_Box, 0, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.btn_createCtl = QPushButton(self.scrollAreaWidgetContents)
        self.btn_createCtl.setObjectName(u"btn_createCtl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_createCtl.sizePolicy().hasHeightForWidth())
        self.btn_createCtl.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.btn_createCtl)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.toolBox = QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy1.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 355, 660))
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.colorGrp = QWidget(self.page)
        self.colorGrp.setObjectName(u"colorGrp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(11)
        sizePolicy4.setHeightForWidth(self.colorGrp.sizePolicy().hasHeightForWidth())
        self.colorGrp.setSizePolicy(sizePolicy4)
        self.colorGrp.setMinimumSize(QSize(303, 82))
        self.gridLayout_2 = QGridLayout(self.colorGrp)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.col_22 = QPushButton(self.colorGrp)
        self.col_22.setObjectName(u"col_22")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(10)
        sizePolicy5.setHeightForWidth(self.col_22.sizePolicy().hasHeightForWidth())
        self.col_22.setSizePolicy(sizePolicy5)
        self.col_22.setMinimumSize(QSize(0, 15))
        self.col_22.setStyleSheet(u"background-color: rgb(255, 255, 99);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_22, 2, 3, 1, 1)

        self.col_18 = QPushButton(self.colorGrp)
        self.col_18.setObjectName(u"col_18")
        sizePolicy5.setHeightForWidth(self.col_18.sizePolicy().hasHeightForWidth())
        self.col_18.setSizePolicy(sizePolicy5)
        self.col_18.setMinimumSize(QSize(0, 15))
        self.col_18.setFocusPolicy(Qt.NoFocus)
        self.col_18.setAutoFillBackground(False)
        self.col_18.setStyleSheet(u"background-color:rgb(100, 220, 255);\n"
"border: 0px;")
        self.col_18.setFlat(False)

        self.gridLayout_2.addWidget(self.col_18, 1, 11, 1, 1)

        self.col_16 = QPushButton(self.colorGrp)
        self.col_16.setObjectName(u"col_16")
        sizePolicy5.setHeightForWidth(self.col_16.sizePolicy().hasHeightForWidth())
        self.col_16.setSizePolicy(sizePolicy5)
        self.col_16.setMinimumSize(QSize(0, 15))
        self.col_16.setFocusPolicy(Qt.NoFocus)
        self.col_16.setAutoFillBackground(False)
        self.col_16.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border: 0px;")
        self.col_16.setFlat(False)

        self.gridLayout_2.addWidget(self.col_16, 1, 8, 1, 1)

        self.col_20 = QPushButton(self.colorGrp)
        self.col_20.setObjectName(u"col_20")
        sizePolicy5.setHeightForWidth(self.col_20.sizePolicy().hasHeightForWidth())
        self.col_20.setSizePolicy(sizePolicy5)
        self.col_20.setMinimumSize(QSize(0, 15))
        self.col_20.setFocusPolicy(Qt.NoFocus)
        self.col_20.setAutoFillBackground(False)
        self.col_20.setStyleSheet(u"background-color:rgb(255, 176, 176);\n"
"border: 0px;")
        self.col_20.setFlat(False)

        self.gridLayout_2.addWidget(self.col_20, 2, 1, 1, 1)

        self.col_14 = QPushButton(self.colorGrp)
        self.col_14.setObjectName(u"col_14")
        sizePolicy5.setHeightForWidth(self.col_14.sizePolicy().hasHeightForWidth())
        self.col_14.setSizePolicy(sizePolicy5)
        self.col_14.setMinimumSize(QSize(0, 15))
        self.col_14.setFocusPolicy(Qt.NoFocus)
        self.col_14.setAutoFillBackground(False)
        self.col_14.setStyleSheet(u"background-color:rgb(0, 255, 0);\n"
"border: 0px;")
        self.col_14.setFlat(False)

        self.gridLayout_2.addWidget(self.col_14, 1, 4, 1, 1)

        self.col_12 = QPushButton(self.colorGrp)
        self.col_12.setObjectName(u"col_12")
        sizePolicy5.setHeightForWidth(self.col_12.sizePolicy().hasHeightForWidth())
        self.col_12.setSizePolicy(sizePolicy5)
        self.col_12.setMinimumSize(QSize(0, 15))
        self.col_12.setFocusPolicy(Qt.NoFocus)
        self.col_12.setAutoFillBackground(False)
        self.col_12.setStyleSheet(u"background-color:rgb(153, 38, 0);\n"
"border: 0px;")
        self.col_12.setFlat(False)

        self.gridLayout_2.addWidget(self.col_12, 1, 2, 1, 1)

        self.col_10 = QPushButton(self.colorGrp)
        self.col_10.setObjectName(u"col_10")
        sizePolicy5.setHeightForWidth(self.col_10.sizePolicy().hasHeightForWidth())
        self.col_10.setSizePolicy(sizePolicy5)
        self.col_10.setMinimumSize(QSize(0, 15))
        self.col_10.setFocusPolicy(Qt.NoFocus)
        self.col_10.setAutoFillBackground(False)
        self.col_10.setStyleSheet(u"background-color:rgb(138, 72, 51);\n"
"border: 0px;")
        self.col_10.setFlat(False)

        self.gridLayout_2.addWidget(self.col_10, 1, 0, 1, 1)

        self.col_17 = QPushButton(self.colorGrp)
        self.col_17.setObjectName(u"col_17")
        sizePolicy5.setHeightForWidth(self.col_17.sizePolicy().hasHeightForWidth())
        self.col_17.setSizePolicy(sizePolicy5)
        self.col_17.setMinimumSize(QSize(0, 15))
        self.col_17.setFocusPolicy(Qt.NoFocus)
        self.col_17.setAutoFillBackground(False)
        self.col_17.setStyleSheet(u"background-color:rgb(255, 255, 0);\n"
"border: 0px;")
        self.col_17.setFlat(False)

        self.gridLayout_2.addWidget(self.col_17, 1, 10, 1, 1)

        self.col_23 = QPushButton(self.colorGrp)
        self.col_23.setObjectName(u"col_23")
        sizePolicy5.setHeightForWidth(self.col_23.sizePolicy().hasHeightForWidth())
        self.col_23.setSizePolicy(sizePolicy5)
        self.col_23.setMinimumSize(QSize(0, 15))
        self.col_23.setFocusPolicy(Qt.NoFocus)
        self.col_23.setStyleSheet(u"background-color:rgb(0, 153, 84);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_23, 2, 4, 1, 1)

        self.col_11 = QPushButton(self.colorGrp)
        self.col_11.setObjectName(u"col_11")
        sizePolicy5.setHeightForWidth(self.col_11.sizePolicy().hasHeightForWidth())
        self.col_11.setSizePolicy(sizePolicy5)
        self.col_11.setMinimumSize(QSize(0, 15))
        self.col_11.setFocusPolicy(Qt.NoFocus)
        self.col_11.setAutoFillBackground(False)
        self.col_11.setStyleSheet(u"background-color:rgb(63, 35, 31);\n"
"border: 0px;")
        self.col_11.setFlat(False)

        self.gridLayout_2.addWidget(self.col_11, 1, 1, 1, 1)

        self.col_15 = QPushButton(self.colorGrp)
        self.col_15.setObjectName(u"col_15")
        sizePolicy5.setHeightForWidth(self.col_15.sizePolicy().hasHeightForWidth())
        self.col_15.setSizePolicy(sizePolicy5)
        self.col_15.setMinimumSize(QSize(0, 15))
        self.col_15.setFocusPolicy(Qt.NoFocus)
        self.col_15.setAutoFillBackground(False)
        self.col_15.setStyleSheet(u"background-color:rgb(0, 65, 153);\n"
"border: 0px;")
        self.col_15.setFlat(False)

        self.gridLayout_2.addWidget(self.col_15, 1, 6, 1, 1)

        self.col_19 = QPushButton(self.colorGrp)
        self.col_19.setObjectName(u"col_19")
        sizePolicy5.setHeightForWidth(self.col_19.sizePolicy().hasHeightForWidth())
        self.col_19.setSizePolicy(sizePolicy5)
        self.col_19.setMinimumSize(QSize(0, 15))
        self.col_19.setFocusPolicy(Qt.NoFocus)
        self.col_19.setAutoFillBackground(False)
        self.col_19.setStyleSheet(u"background-color:rgb(67, 255, 163);\n"
"border: 0px;")
        self.col_19.setFlat(False)

        self.gridLayout_2.addWidget(self.col_19, 2, 0, 1, 1)

        self.col_21 = QPushButton(self.colorGrp)
        self.col_21.setObjectName(u"col_21")
        sizePolicy5.setHeightForWidth(self.col_21.sizePolicy().hasHeightForWidth())
        self.col_21.setSizePolicy(sizePolicy5)
        self.col_21.setMinimumSize(QSize(0, 15))
        self.col_21.setFocusPolicy(Qt.NoFocus)
        self.col_21.setAutoFillBackground(False)
        self.col_21.setStyleSheet(u"background-color:rgb(228, 172, 121);\n"
"border: 0px;")
        self.col_21.setFlat(False)

        self.gridLayout_2.addWidget(self.col_21, 2, 2, 1, 1)

        self.col_13 = QPushButton(self.colorGrp)
        self.col_13.setObjectName(u"col_13")
        sizePolicy5.setHeightForWidth(self.col_13.sizePolicy().hasHeightForWidth())
        self.col_13.setSizePolicy(sizePolicy5)
        self.col_13.setMinimumSize(QSize(0, 15))
        self.col_13.setFocusPolicy(Qt.NoFocus)
        self.col_13.setAutoFillBackground(False)
        self.col_13.setStyleSheet(u"background-color:rgb(255, 0, 0);\n"
"border: 0px;")
        self.col_13.setFlat(False)

        self.gridLayout_2.addWidget(self.col_13, 1, 3, 1, 1)

        self.col_1 = QPushButton(self.colorGrp)
        self.col_1.setObjectName(u"col_1")
        sizePolicy5.setHeightForWidth(self.col_1.sizePolicy().hasHeightForWidth())
        self.col_1.setSizePolicy(sizePolicy5)
        self.col_1.setMinimumSize(QSize(0, 15))
        self.col_1.setFocusPolicy(Qt.NoFocus)
        self.col_1.setAutoFillBackground(False)
        self.col_1.setStyleSheet(u"background-color:black;\n"
"border: 0px;")
        self.col_1.setFlat(False)

        self.gridLayout_2.addWidget(self.col_1, 0, 0, 1, 1)

        self.col_2 = QPushButton(self.colorGrp)
        self.col_2.setObjectName(u"col_2")
        sizePolicy5.setHeightForWidth(self.col_2.sizePolicy().hasHeightForWidth())
        self.col_2.setSizePolicy(sizePolicy5)
        self.col_2.setMinimumSize(QSize(0, 15))
        self.col_2.setFocusPolicy(Qt.NoFocus)
        self.col_2.setAutoFillBackground(False)
        self.col_2.setStyleSheet(u"background-color:rgb(83, 83, 83);\n"
"border: 0px;")
        self.col_2.setFlat(False)

        self.gridLayout_2.addWidget(self.col_2, 0, 1, 1, 1)

        self.col_3 = QPushButton(self.colorGrp)
        self.col_3.setObjectName(u"col_3")
        sizePolicy5.setHeightForWidth(self.col_3.sizePolicy().hasHeightForWidth())
        self.col_3.setSizePolicy(sizePolicy5)
        self.col_3.setMinimumSize(QSize(0, 15))
        self.col_3.setFocusPolicy(Qt.NoFocus)
        self.col_3.setAutoFillBackground(False)
        self.col_3.setStyleSheet(u"background-color:rgb(213, 213, 213);\n"
"border: 0px;")
        self.col_3.setFlat(False)

        self.gridLayout_2.addWidget(self.col_3, 0, 2, 1, 1)

        self.col_4 = QPushButton(self.colorGrp)
        self.col_4.setObjectName(u"col_4")
        sizePolicy5.setHeightForWidth(self.col_4.sizePolicy().hasHeightForWidth())
        self.col_4.setSizePolicy(sizePolicy5)
        self.col_4.setMinimumSize(QSize(0, 15))
        self.col_4.setFocusPolicy(Qt.NoFocus)
        self.col_4.setAutoFillBackground(False)
        self.col_4.setStyleSheet(u"background-color:rgb(170, 0, 0);\n"
"border: 0px;")
        self.col_4.setFlat(False)

        self.gridLayout_2.addWidget(self.col_4, 0, 3, 1, 1)

        self.col_5 = QPushButton(self.colorGrp)
        self.col_5.setObjectName(u"col_5")
        sizePolicy5.setHeightForWidth(self.col_5.sizePolicy().hasHeightForWidth())
        self.col_5.setSizePolicy(sizePolicy5)
        self.col_5.setMinimumSize(QSize(0, 15))
        self.col_5.setFocusPolicy(Qt.NoFocus)
        self.col_5.setAutoFillBackground(False)
        self.col_5.setStyleSheet(u"background-color:rgb(0, 4, 96);\n"
"border: 0px;")
        self.col_5.setFlat(False)

        self.gridLayout_2.addWidget(self.col_5, 0, 4, 1, 1)

        self.col_6 = QPushButton(self.colorGrp)
        self.col_6.setObjectName(u"col_6")
        sizePolicy5.setHeightForWidth(self.col_6.sizePolicy().hasHeightForWidth())
        self.col_6.setSizePolicy(sizePolicy5)
        self.col_6.setMinimumSize(QSize(0, 15))
        self.col_6.setFocusPolicy(Qt.NoFocus)
        self.col_6.setAutoFillBackground(False)
        self.col_6.setStyleSheet(u"background-color:rgb(0, 0, 255);\n"
"border: 0px;")
        self.col_6.setFlat(False)

        self.gridLayout_2.addWidget(self.col_6, 0, 6, 1, 1)

        self.col_7 = QPushButton(self.colorGrp)
        self.col_7.setObjectName(u"col_7")
        sizePolicy5.setHeightForWidth(self.col_7.sizePolicy().hasHeightForWidth())
        self.col_7.setSizePolicy(sizePolicy5)
        self.col_7.setMinimumSize(QSize(0, 15))
        self.col_7.setFocusPolicy(Qt.NoFocus)
        self.col_7.setAutoFillBackground(False)
        self.col_7.setStyleSheet(u"background-color:rgb(0, 70, 25);\n"
"border: 0px;")
        self.col_7.setFlat(False)

        self.gridLayout_2.addWidget(self.col_7, 0, 8, 1, 1)

        self.col_8 = QPushButton(self.colorGrp)
        self.col_8.setObjectName(u"col_8")
        sizePolicy5.setHeightForWidth(self.col_8.sizePolicy().hasHeightForWidth())
        self.col_8.setSizePolicy(sizePolicy5)
        self.col_8.setMinimumSize(QSize(0, 15))
        self.col_8.setFocusPolicy(Qt.NoFocus)
        self.col_8.setAutoFillBackground(False)
        self.col_8.setStyleSheet(u"background-color:rgb(38, 0, 67);\n"
"border: 0px;")
        self.col_8.setFlat(False)

        self.gridLayout_2.addWidget(self.col_8, 0, 10, 1, 1)

        self.col_9 = QPushButton(self.colorGrp)
        self.col_9.setObjectName(u"col_9")
        sizePolicy5.setHeightForWidth(self.col_9.sizePolicy().hasHeightForWidth())
        self.col_9.setSizePolicy(sizePolicy5)
        self.col_9.setMinimumSize(QSize(0, 15))
        self.col_9.setFocusPolicy(Qt.NoFocus)
        self.col_9.setAutoFillBackground(False)
        self.col_9.setStyleSheet(u"background-color:rgb(200, 0, 200);\n"
"border: 0px;")
        self.col_9.setFlat(False)

        self.gridLayout_2.addWidget(self.col_9, 0, 11, 1, 1)

        self.col_24 = QPushButton(self.colorGrp)
        self.col_24.setObjectName(u"col_24")
        sizePolicy5.setHeightForWidth(self.col_24.sizePolicy().hasHeightForWidth())
        self.col_24.setSizePolicy(sizePolicy5)
        self.col_24.setMinimumSize(QSize(0, 15))
        self.col_24.setFocusPolicy(Qt.NoFocus)
        self.col_24.setStyleSheet(u"background-color: rgb(220, 147, 0);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_24, 2, 6, 1, 1)

        self.col_25 = QPushButton(self.colorGrp)
        self.col_25.setObjectName(u"col_25")
        sizePolicy5.setHeightForWidth(self.col_25.sizePolicy().hasHeightForWidth())
        self.col_25.setSizePolicy(sizePolicy5)
        self.col_25.setMinimumSize(QSize(0, 15))
        self.col_25.setStyleSheet(u"background-color:rgb(221, 221, 110);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_25, 2, 8, 1, 1)

        self.col_26 = QPushButton(self.colorGrp)
        self.col_26.setObjectName(u"col_26")
        sizePolicy5.setHeightForWidth(self.col_26.sizePolicy().hasHeightForWidth())
        self.col_26.setSizePolicy(sizePolicy5)
        self.col_26.setMinimumSize(QSize(0, 15))
        self.col_26.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_26, 2, 10, 1, 1)

        self.col_27 = QPushButton(self.colorGrp)
        self.col_27.setObjectName(u"col_27")
        sizePolicy5.setHeightForWidth(self.col_27.sizePolicy().hasHeightForWidth())
        self.col_27.setSizePolicy(sizePolicy5)
        self.col_27.setMinimumSize(QSize(0, 15))
        self.col_27.setFocusPolicy(Qt.NoFocus)
        self.col_27.setStyleSheet(u"background-color:rgb(48, 161, 93);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_27, 2, 11, 1, 1)

        self.col_28 = QPushButton(self.colorGrp)
        self.col_28.setObjectName(u"col_28")
        sizePolicy5.setHeightForWidth(self.col_28.sizePolicy().hasHeightForWidth())
        self.col_28.setSizePolicy(sizePolicy5)
        self.col_28.setMinimumSize(QSize(0, 15))
        self.col_28.setStyleSheet(u"background-color:rgb(48, 161, 161);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_28, 4, 0, 1, 1)

        self.col_29 = QPushButton(self.colorGrp)
        self.col_29.setObjectName(u"col_29")
        sizePolicy5.setHeightForWidth(self.col_29.sizePolicy().hasHeightForWidth())
        self.col_29.setSizePolicy(sizePolicy5)
        self.col_29.setMinimumSize(QSize(0, 15))
        self.col_29.setStyleSheet(u"background-color:rgb(48, 103, 161);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_29, 4, 1, 1, 1)

        self.col_30 = QPushButton(self.colorGrp)
        self.col_30.setObjectName(u"col_30")
        sizePolicy5.setHeightForWidth(self.col_30.sizePolicy().hasHeightForWidth())
        self.col_30.setSizePolicy(sizePolicy5)
        self.col_30.setMinimumSize(QSize(0, 15))
        self.col_30.setFocusPolicy(Qt.NoFocus)
        self.col_30.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_30, 4, 2, 1, 1)

        self.col_31 = QPushButton(self.colorGrp)
        self.col_31.setObjectName(u"col_31")
        sizePolicy5.setHeightForWidth(self.col_31.sizePolicy().hasHeightForWidth())
        self.col_31.setSizePolicy(sizePolicy5)
        self.col_31.setMinimumSize(QSize(0, 15))
        self.col_31.setFocusPolicy(Qt.NoFocus)
        self.col_31.setStyleSheet(u"background-color:rgb(255, 83, 201);\n"
"border: 0px;")

        self.gridLayout_2.addWidget(self.col_31, 4, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.colorGrp)

        self.colorRandom_btn = QPushButton(self.page)
        self.colorRandom_btn.setObjectName(u"colorRandom_btn")

        self.verticalLayout_3.addWidget(self.colorRandom_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.page, u"Color Picker")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 355, 660))
        self.verticalLayout_18 = QVBoxLayout(self.page_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.groupBox_5 = QGroupBox(self.page_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.spObject = QRadioButton(self.groupBox_5)
        self.spObject.setObjectName(u"spObject")
        self.spObject.setChecked(True)

        self.horizontalLayout_13.addWidget(self.spObject)

        self.spTransform = QRadioButton(self.groupBox_5)
        self.spTransform.setObjectName(u"spTransform")
        self.spTransform.setChecked(False)

        self.horizontalLayout_13.addWidget(self.spTransform)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)


        self.verticalLayout_18.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.transX_chkBox = QCheckBox(self.groupBox_4)
        self.transX_chkBox.setObjectName(u"transX_chkBox")
        self.transX_chkBox.setChecked(True)

        self.horizontalLayout_8.addWidget(self.transX_chkBox)

        self.transY_chkBox = QCheckBox(self.groupBox_4)
        self.transY_chkBox.setObjectName(u"transY_chkBox")
        self.transY_chkBox.setChecked(True)

        self.horizontalLayout_8.addWidget(self.transY_chkBox)

        self.transZ_chkBox = QCheckBox(self.groupBox_4)
        self.transZ_chkBox.setObjectName(u"transZ_chkBox")
        self.transZ_chkBox.setChecked(True)

        self.horizontalLayout_8.addWidget(self.transZ_chkBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_resizeStep_2 = QLabel(self.groupBox_4)
        self.label_resizeStep_2.setObjectName(u"label_resizeStep_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_resizeStep_2.sizePolicy().hasHeightForWidth())
        self.label_resizeStep_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_10.addWidget(self.label_resizeStep_2)

        self.sizeStepSpinBox_2 = QDoubleSpinBox(self.groupBox_4)
        self.sizeStepSpinBox_2.setObjectName(u"sizeStepSpinBox_2")
        self.sizeStepSpinBox_2.setDecimals(1)
        self.sizeStepSpinBox_2.setSingleStep(0.200000000000000)
        self.sizeStepSpinBox_2.setValue(1.200000000000000)

        self.horizontalLayout_10.addWidget(self.sizeStepSpinBox_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.resizeSlider_2 = QSlider(self.groupBox_4)
        self.resizeSlider_2.setObjectName(u"resizeSlider_2")
        self.resizeSlider_2.setFocusPolicy(Qt.ClickFocus)
        self.resizeSlider_2.setMinimum(-10)
        self.resizeSlider_2.setMaximum(10)
        self.resizeSlider_2.setTracking(True)
        self.resizeSlider_2.setOrientation(Qt.Horizontal)
        self.resizeSlider_2.setInvertedAppearance(False)
        self.resizeSlider_2.setInvertedControls(False)
        self.resizeSlider_2.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_10.addWidget(self.resizeSlider_2)


        self.verticalLayout_18.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 110))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.rotateGrp = QWidget(self.groupBox_2)
        self.rotateGrp.setObjectName(u"rotateGrp")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.rotateGrp.sizePolicy().hasHeightForWidth())
        self.rotateGrp.setSizePolicy(sizePolicy7)
        self.rotateGrp.setMinimumSize(QSize(0, 80))
        self.verticalLayout_7 = QVBoxLayout(self.rotateGrp)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_angle = QLabel(self.rotateGrp)
        self.label_angle.setObjectName(u"label_angle")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_angle.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_angle)

        self.angle_box = QSpinBox(self.rotateGrp)
        self.angle_box.setObjectName(u"angle_box")
        self.angle_box.setMaximum(360)
        self.angle_box.setSingleStep(45)
        self.angle_box.setValue(90)

        self.horizontalLayout_9.addWidget(self.angle_box)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMaximumSize)
        self.btn_rotateX = QPushButton(self.rotateGrp)
        self.btn_rotateX.setObjectName(u"btn_rotateX")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.btn_rotateX.sizePolicy().hasHeightForWidth())
        self.btn_rotateX.setSizePolicy(sizePolicy8)
        self.btn_rotateX.setMinimumSize(QSize(0, 26))
        self.btn_rotateX.setStyleSheet(u"background-color: rgb(255, 70, 70);\n"
"color: white;\n"
"border: 0px;")

        self.horizontalLayout_7.addWidget(self.btn_rotateX)

        self.btn_rotateY = QPushButton(self.rotateGrp)
        self.btn_rotateY.setObjectName(u"btn_rotateY")
        sizePolicy8.setHeightForWidth(self.btn_rotateY.sizePolicy().hasHeightForWidth())
        self.btn_rotateY.setSizePolicy(sizePolicy8)
        self.btn_rotateY.setMinimumSize(QSize(0, 26))
        self.btn_rotateY.setStyleSheet(u"background-color: rgb(72, 216, 0);\n"
"color: white;\n"
"border: 0px;")

        self.horizontalLayout_7.addWidget(self.btn_rotateY)

        self.btn_rotateZ = QPushButton(self.rotateGrp)
        self.btn_rotateZ.setObjectName(u"btn_rotateZ")
        sizePolicy8.setHeightForWidth(self.btn_rotateZ.sizePolicy().hasHeightForWidth())
        self.btn_rotateZ.setSizePolicy(sizePolicy8)
        self.btn_rotateZ.setMinimumSize(QSize(0, 26))
        self.btn_rotateZ.setStyleSheet(u"background-color: blue;\n"
"color: white;\n"
"border: 0px;")

        self.horizontalLayout_7.addWidget(self.btn_rotateZ)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addWidget(self.rotateGrp)


        self.verticalLayout_18.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sizeX = QCheckBox(self.groupBox_3)
        self.sizeX.setObjectName(u"sizeX")
        self.sizeX.setChecked(True)

        self.horizontalLayout_4.addWidget(self.sizeX)

        self.sizeY = QCheckBox(self.groupBox_3)
        self.sizeY.setObjectName(u"sizeY")
        self.sizeY.setChecked(True)

        self.horizontalLayout_4.addWidget(self.sizeY)

        self.sizeZ = QCheckBox(self.groupBox_3)
        self.sizeZ.setObjectName(u"sizeZ")
        self.sizeZ.setChecked(True)

        self.horizontalLayout_4.addWidget(self.sizeZ)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_resizeStep = QLabel(self.groupBox_3)
        self.label_resizeStep.setObjectName(u"label_resizeStep")
        sizePolicy6.setHeightForWidth(self.label_resizeStep.sizePolicy().hasHeightForWidth())
        self.label_resizeStep.setSizePolicy(sizePolicy6)

        self.horizontalLayout_5.addWidget(self.label_resizeStep)

        self.sizeStepSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.sizeStepSpinBox.setObjectName(u"sizeStepSpinBox")
        self.sizeStepSpinBox.setDecimals(1)
        self.sizeStepSpinBox.setSingleStep(0.200000000000000)
        self.sizeStepSpinBox.setValue(1.200000000000000)

        self.horizontalLayout_5.addWidget(self.sizeStepSpinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.resizeSlider = QSlider(self.groupBox_3)
        self.resizeSlider.setObjectName(u"resizeSlider")
        self.resizeSlider.setMinimum(-10)
        self.resizeSlider.setMaximum(10)
        self.resizeSlider.setTracking(True)
        self.resizeSlider.setOrientation(Qt.Horizontal)
        self.resizeSlider.setInvertedAppearance(False)
        self.resizeSlider.setInvertedControls(False)
        self.resizeSlider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_6.addWidget(self.resizeSlider)


        self.verticalLayout_18.addWidget(self.groupBox_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_2, u"Shape Transforms")

        self.verticalLayout.addWidget(self.toolBox)

        self.copyShp_Btn = QPushButton(self.scrollAreaWidgetContents)
        self.copyShp_Btn.setObjectName(u"copyShp_Btn")

        self.verticalLayout.addWidget(self.copyShp_Btn)

        self.saveShp_btn = QPushButton(self.scrollAreaWidgetContents)
        self.saveShp_btn.setObjectName(u"saveShp_btn")

        self.verticalLayout.addWidget(self.saveShp_btn)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_17.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_ctrl, icon5, "")
        self.tab_attr = QWidget()
        self.tab_attr.setObjectName(u"tab_attr")
        self.verticalLayout_27 = QVBoxLayout(self.tab_attr)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.groupBox_11 = QGroupBox(self.tab_attr)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(0, 230))
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.attrTranslate_chkBox = QCheckBox(self.groupBox_11)
        self.attrTranslate_chkBox.setObjectName(u"attrTranslate_chkBox")
        self.attrTranslate_chkBox.setChecked(True)

        self.horizontalLayout_28.addWidget(self.attrTranslate_chkBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(25, -1, -1, -1)
        self.attrTransY_chkBox = QCheckBox(self.groupBox_11)
        self.attrTransY_chkBox.setObjectName(u"attrTransY_chkBox")
        self.attrTransY_chkBox.setChecked(True)

        self.horizontalLayout_44.addWidget(self.attrTransY_chkBox)

        self.attrTransX_chkBox = QCheckBox(self.groupBox_11)
        self.attrTransX_chkBox.setObjectName(u"attrTransX_chkBox")
        self.attrTransX_chkBox.setChecked(True)

        self.horizontalLayout_44.addWidget(self.attrTransX_chkBox)

        self.attrTransZ_chkBox = QCheckBox(self.groupBox_11)
        self.attrTransZ_chkBox.setObjectName(u"attrTransZ_chkBox")
        self.attrTransZ_chkBox.setChecked(True)

        self.horizontalLayout_44.addWidget(self.attrTransZ_chkBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_44)


        self.verticalLayout_31.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.groupBox_11)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_2)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.attrRotate_chkBox = QCheckBox(self.groupBox_11)
        self.attrRotate_chkBox.setObjectName(u"attrRotate_chkBox")
        self.attrRotate_chkBox.setChecked(True)

        self.horizontalLayout_29.addWidget(self.attrRotate_chkBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_5)


        self.verticalLayout_23.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(25, -1, -1, -1)
        self.attrRotateX_chkBox = QCheckBox(self.groupBox_11)
        self.attrRotateX_chkBox.setObjectName(u"attrRotateX_chkBox")
        self.attrRotateX_chkBox.setChecked(True)

        self.horizontalLayout_45.addWidget(self.attrRotateX_chkBox)

        self.attrRotateY_chkBox = QCheckBox(self.groupBox_11)
        self.attrRotateY_chkBox.setObjectName(u"attrRotateY_chkBox")
        self.attrRotateY_chkBox.setChecked(True)

        self.horizontalLayout_45.addWidget(self.attrRotateY_chkBox)

        self.attrRotateZ_chkBox = QCheckBox(self.groupBox_11)
        self.attrRotateZ_chkBox.setObjectName(u"attrRotateZ_chkBox")
        self.attrRotateZ_chkBox.setChecked(True)

        self.horizontalLayout_45.addWidget(self.attrRotateZ_chkBox)


        self.verticalLayout_23.addLayout(self.horizontalLayout_45)


        self.verticalLayout_31.addLayout(self.verticalLayout_23)

        self.line_3 = QFrame(self.groupBox_11)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_3)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.attrScale_chkBox = QCheckBox(self.groupBox_11)
        self.attrScale_chkBox.setObjectName(u"attrScale_chkBox")
        self.attrScale_chkBox.setChecked(True)

        self.horizontalLayout_46.addWidget(self.attrScale_chkBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_6)


        self.verticalLayout_30.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(25, -1, -1, -1)
        self.attrScaleX_chkBox = QCheckBox(self.groupBox_11)
        self.attrScaleX_chkBox.setObjectName(u"attrScaleX_chkBox")
        self.attrScaleX_chkBox.setChecked(True)

        self.horizontalLayout_47.addWidget(self.attrScaleX_chkBox)

        self.attrScaleY_chkBox = QCheckBox(self.groupBox_11)
        self.attrScaleY_chkBox.setObjectName(u"attrScaleY_chkBox")
        self.attrScaleY_chkBox.setChecked(True)

        self.horizontalLayout_47.addWidget(self.attrScaleY_chkBox)

        self.attrScaleZ_chkBox = QCheckBox(self.groupBox_11)
        self.attrScaleZ_chkBox.setObjectName(u"attrScaleZ_chkBox")
        self.attrScaleZ_chkBox.setChecked(True)

        self.horizontalLayout_47.addWidget(self.attrScaleZ_chkBox)


        self.verticalLayout_30.addLayout(self.horizontalLayout_47)


        self.verticalLayout_31.addLayout(self.verticalLayout_30)

        self.line_4 = QFrame(self.groupBox_11)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_4)

        self.attrVisibility_chkBox = QCheckBox(self.groupBox_11)
        self.attrVisibility_chkBox.setObjectName(u"attrVisibility_chkBox")
        self.attrVisibility_chkBox.setChecked(True)

        self.verticalLayout_31.addWidget(self.attrVisibility_chkBox)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_3)

        self.attrAuto_chkBox = QCheckBox(self.groupBox_11)
        self.attrAuto_chkBox.setObjectName(u"attrAuto_chkBox")
        self.attrAuto_chkBox.setChecked(True)

        self.horizontalLayout_31.addWidget(self.attrAuto_chkBox)

        self.attrSet_Btn = QPushButton(self.groupBox_11)
        self.attrSet_Btn.setObjectName(u"attrSet_Btn")
        self.attrSet_Btn.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_31.addWidget(self.attrSet_Btn)


        self.verticalLayout_31.addLayout(self.horizontalLayout_31)


        self.verticalLayout_27.addWidget(self.groupBox_11)

        self.groupBox_15 = QGroupBox(self.tab_attr)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.customAttrCreate_rBtn = QRadioButton(self.groupBox_15)
        self.customAttrCreateEdit_bGrp = QButtonGroup(MainWindow)
        self.customAttrCreateEdit_bGrp.setObjectName(u"customAttrCreateEdit_bGrp")
        self.customAttrCreateEdit_bGrp.addButton(self.customAttrCreate_rBtn)
        self.customAttrCreate_rBtn.setObjectName(u"customAttrCreate_rBtn")
        self.customAttrCreate_rBtn.setChecked(True)

        self.horizontalLayout_39.addWidget(self.customAttrCreate_rBtn)

        self.customAttrEdit_rBtn = QRadioButton(self.groupBox_15)
        self.customAttrCreateEdit_bGrp.addButton(self.customAttrEdit_rBtn)
        self.customAttrEdit_rBtn.setObjectName(u"customAttrEdit_rBtn")

        self.horizontalLayout_39.addWidget(self.customAttrEdit_rBtn)

        self.customAttrList_cBox = QComboBox(self.groupBox_15)
        self.customAttrList_cBox.addItem("")
        self.customAttrList_cBox.addItem("")
        self.customAttrList_cBox.addItem("")
        self.customAttrList_cBox.addItem("")
        self.customAttrList_cBox.addItem("")
        self.customAttrList_cBox.addItem("")
        self.customAttrList_cBox.addItem("")
        self.customAttrList_cBox.addItem("")
        self.customAttrList_cBox.setObjectName(u"customAttrList_cBox")
        self.customAttrList_cBox.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.customAttrList_cBox.sizePolicy().hasHeightForWidth())
        self.customAttrList_cBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_39.addWidget(self.customAttrList_cBox)

        self.customAttrLoad_Btn = QPushButton(self.groupBox_15)
        self.customAttrLoad_Btn.setObjectName(u"customAttrLoad_Btn")

        self.horizontalLayout_39.addWidget(self.customAttrLoad_Btn)


        self.verticalLayout_25.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_11 = QLabel(self.groupBox_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_37.addWidget(self.label_11)

        self.customAttrName_lineEdit = QLineEdit(self.groupBox_15)
        self.customAttrName_lineEdit.setObjectName(u"customAttrName_lineEdit")

        self.horizontalLayout_37.addWidget(self.customAttrName_lineEdit)


        self.verticalLayout_25.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_12 = QLabel(self.groupBox_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_38.addWidget(self.label_12)

        self.customAttrNiceName_lineEdit = QLineEdit(self.groupBox_15)
        self.customAttrNiceName_lineEdit.setObjectName(u"customAttrNiceName_lineEdit")

        self.horizontalLayout_38.addWidget(self.customAttrNiceName_lineEdit)


        self.verticalLayout_25.addLayout(self.horizontalLayout_38)

        self.keyable_grpBox = QGroupBox(self.groupBox_15)
        self.keyable_grpBox.setObjectName(u"keyable_grpBox")
        self.horizontalLayout_40 = QHBoxLayout(self.keyable_grpBox)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.customAttrKeyable_rBtn = QRadioButton(self.keyable_grpBox)
        self.customAttrKeyable_rBtn.setObjectName(u"customAttrKeyable_rBtn")
        self.customAttrKeyable_rBtn.setChecked(True)

        self.horizontalLayout_40.addWidget(self.customAttrKeyable_rBtn)

        self.customAttrNonKeyable_rBtn = QRadioButton(self.keyable_grpBox)
        self.customAttrNonKeyable_rBtn.setObjectName(u"customAttrNonKeyable_rBtn")

        self.horizontalLayout_40.addWidget(self.customAttrNonKeyable_rBtn)

        self.customAttrHidden_rBtn = QRadioButton(self.keyable_grpBox)
        self.customAttrHidden_rBtn.setObjectName(u"customAttrHidden_rBtn")

        self.horizontalLayout_40.addWidget(self.customAttrHidden_rBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_4)


        self.verticalLayout_25.addWidget(self.keyable_grpBox)

        self.customAttrType_grpBox = QGroupBox(self.groupBox_15)
        self.customAttrType_grpBox.setObjectName(u"customAttrType_grpBox")
        self.horizontalLayout_41 = QHBoxLayout(self.customAttrType_grpBox)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.customAttrFloat_rBtn = QRadioButton(self.customAttrType_grpBox)
        self.customAttrType_bGrp = QButtonGroup(MainWindow)
        self.customAttrType_bGrp.setObjectName(u"customAttrType_bGrp")
        self.customAttrType_bGrp.addButton(self.customAttrFloat_rBtn)
        self.customAttrFloat_rBtn.setObjectName(u"customAttrFloat_rBtn")
        self.customAttrFloat_rBtn.setChecked(True)

        self.horizontalLayout_32.addWidget(self.customAttrFloat_rBtn)

        self.customAttrInt_rBtn = QRadioButton(self.customAttrType_grpBox)
        self.customAttrType_bGrp.addButton(self.customAttrInt_rBtn)
        self.customAttrInt_rBtn.setObjectName(u"customAttrInt_rBtn")

        self.horizontalLayout_32.addWidget(self.customAttrInt_rBtn)

        self.customAttrBool_rBtn = QRadioButton(self.customAttrType_grpBox)
        self.customAttrType_bGrp.addButton(self.customAttrBool_rBtn)
        self.customAttrBool_rBtn.setObjectName(u"customAttrBool_rBtn")

        self.horizontalLayout_32.addWidget(self.customAttrBool_rBtn)

        self.customAttrEnum_rBtn = QRadioButton(self.customAttrType_grpBox)
        self.customAttrType_bGrp.addButton(self.customAttrEnum_rBtn)
        self.customAttrEnum_rBtn.setObjectName(u"customAttrEnum_rBtn")

        self.horizontalLayout_32.addWidget(self.customAttrEnum_rBtn)

        self.customAttrVector_rBtn = QRadioButton(self.customAttrType_grpBox)
        self.customAttrType_bGrp.addButton(self.customAttrVector_rBtn)
        self.customAttrVector_rBtn.setObjectName(u"customAttrVector_rBtn")

        self.horizontalLayout_32.addWidget(self.customAttrVector_rBtn)

        self.customAttrString_rBtn = QRadioButton(self.customAttrType_grpBox)
        self.customAttrType_bGrp.addButton(self.customAttrString_rBtn)
        self.customAttrString_rBtn.setObjectName(u"customAttrString_rBtn")

        self.horizontalLayout_32.addWidget(self.customAttrString_rBtn)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_32)


        self.verticalLayout_25.addWidget(self.customAttrType_grpBox)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_10 = QLabel(self.groupBox_15)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_35.addWidget(self.label_10)

        self.customAttrValue_lineEdit = QLineEdit(self.groupBox_15)
        self.customAttrValue_lineEdit.setObjectName(u"customAttrValue_lineEdit")

        self.horizontalLayout_35.addWidget(self.customAttrValue_lineEdit)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.customAttrMin_chkBox = QCheckBox(self.groupBox_15)
        self.customAttrMin_chkBox.setObjectName(u"customAttrMin_chkBox")

        self.horizontalLayout_33.addWidget(self.customAttrMin_chkBox)

        self.customAttrMinVal_spinBox = QDoubleSpinBox(self.groupBox_15)
        self.customAttrMinVal_spinBox.setObjectName(u"customAttrMinVal_spinBox")
        self.customAttrMinVal_spinBox.setEnabled(False)
        self.customAttrMinVal_spinBox.setMaximum(9999.000000000000000)

        self.horizontalLayout_33.addWidget(self.customAttrMinVal_spinBox)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.customAttrMax_chkBox = QCheckBox(self.groupBox_15)
        self.customAttrMax_chkBox.setObjectName(u"customAttrMax_chkBox")

        self.horizontalLayout_34.addWidget(self.customAttrMax_chkBox)

        self.customAttrMaxVal_spinBox = QDoubleSpinBox(self.groupBox_15)
        self.customAttrMaxVal_spinBox.setObjectName(u"customAttrMaxVal_spinBox")
        self.customAttrMaxVal_spinBox.setEnabled(False)
        self.customAttrMaxVal_spinBox.setMaximum(9999.000000000000000)
        self.customAttrMaxVal_spinBox.setValue(1.000000000000000)

        self.horizontalLayout_34.addWidget(self.customAttrMaxVal_spinBox)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_34)


        self.verticalLayout_25.addLayout(self.horizontalLayout_36)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_3 = QLabel(self.groupBox_15)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_24.addWidget(self.label_3)

        self.customAttrEnumNames_lineEdit = QLineEdit(self.groupBox_15)
        self.customAttrEnumNames_lineEdit.setObjectName(u"customAttrEnumNames_lineEdit")
        self.customAttrEnumNames_lineEdit.setEnabled(False)

        self.verticalLayout_24.addWidget(self.customAttrEnumNames_lineEdit)


        self.verticalLayout_25.addLayout(self.verticalLayout_24)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.customAttrApply_Btn = QPushButton(self.groupBox_15)
        self.customAttrApply_Btn.setObjectName(u"customAttrApply_Btn")
        sizePolicy2.setHeightForWidth(self.customAttrApply_Btn.sizePolicy().hasHeightForWidth())
        self.customAttrApply_Btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_42.addWidget(self.customAttrApply_Btn)

        self.customAttrKeepVal_chkBox = QCheckBox(self.groupBox_15)
        self.customAttrKeepVal_chkBox.setObjectName(u"customAttrKeepVal_chkBox")
        self.customAttrKeepVal_chkBox.setChecked(True)

        self.horizontalLayout_42.addWidget(self.customAttrKeepVal_chkBox)


        self.verticalLayout_26.addLayout(self.horizontalLayout_42)

        self.customAttrResetVal_Btn = QPushButton(self.groupBox_15)
        self.customAttrResetVal_Btn.setObjectName(u"customAttrResetVal_Btn")

        self.verticalLayout_26.addWidget(self.customAttrResetVal_Btn)


        self.verticalLayout_27.addWidget(self.groupBox_15)

        self.verticalSpacer_5 = QSpacerItem(20, 609, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_5)

        self.tabWidget.addTab(self.tab_attr, "")
        self.tab_jnt = QWidget()
        self.tab_jnt.setObjectName(u"tab_jnt")
        self.verticalLayout_22 = QVBoxLayout(self.tab_jnt)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.crJnt_Btn = QPushButton(self.tab_jnt)
        self.crJnt_Btn.setObjectName(u"crJnt_Btn")

        self.verticalLayout_22.addWidget(self.crJnt_Btn)

        self.groupBox_9 = QGroupBox(self.tab_jnt)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.parConstraint_chkBox = QCheckBox(self.groupBox_9)
        self.parConstraint_chkBox.setObjectName(u"parConstraint_chkBox")
        self.parConstraint_chkBox.setChecked(True)

        self.gridLayout_3.addWidget(self.parConstraint_chkBox, 0, 1, 1, 1)

        self.scaleCons_chkBox = QCheckBox(self.groupBox_9)
        self.scaleCons_chkBox.setObjectName(u"scaleCons_chkBox")
        self.scaleCons_chkBox.setChecked(True)

        self.gridLayout_3.addWidget(self.scaleCons_chkBox, 1, 1, 1, 1)

        self.orientCons_chkBox = QCheckBox(self.groupBox_9)
        self.orientCons_chkBox.setObjectName(u"orientCons_chkBox")

        self.gridLayout_3.addWidget(self.orientCons_chkBox, 1, 0, 1, 1)

        self.pointCons_chkBox = QCheckBox(self.groupBox_9)
        self.pointCons_chkBox.setObjectName(u"pointCons_chkBox")

        self.gridLayout_3.addWidget(self.pointCons_chkBox, 0, 0, 1, 1)

        self.chainJnt_chkBox = QCheckBox(self.groupBox_9)
        self.chainJnt_chkBox.setObjectName(u"chainJnt_chkBox")
        self.chainJnt_chkBox.setChecked(True)

        self.gridLayout_3.addWidget(self.chainJnt_chkBox, 2, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.suffix_chkBox = QCheckBox(self.groupBox_9)
        self.suffix_chkBox.setObjectName(u"suffix_chkBox")
        self.suffix_chkBox.setChecked(True)

        self.horizontalLayout_19.addWidget(self.suffix_chkBox)

        self.jntSuffixName_lineEdit = QLineEdit(self.groupBox_9)
        self.jntSuffixName_lineEdit.setObjectName(u"jntSuffixName_lineEdit")

        self.horizontalLayout_19.addWidget(self.jntSuffixName_lineEdit)


        self.gridLayout_3.addLayout(self.horizontalLayout_19, 2, 1, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_3)

        self.createSelJnt_Btn = QPushButton(self.groupBox_9)
        self.createSelJnt_Btn.setObjectName(u"createSelJnt_Btn")

        self.verticalLayout_15.addWidget(self.createSelJnt_Btn)


        self.horizontalLayout_20.addLayout(self.verticalLayout_15)


        self.verticalLayout_22.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.tab_jnt)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_7 = QLabel(self.groupBox_10)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_16.addWidget(self.label_7)

        self.label_8 = QLabel(self.groupBox_10)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_16.addWidget(self.label_8)

        self.label_9 = QLabel(self.groupBox_10)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_16.addWidget(self.label_9)


        self.horizontalLayout_25.addLayout(self.verticalLayout_16)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.orientPAxisX_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.orientPAxisX_rBtn)
        self.orientPAxisX_rBtn.setObjectName(u"orientPAxisX_rBtn")
        self.orientPAxisX_rBtn.setChecked(True)

        self.horizontalLayout_21.addWidget(self.orientPAxisX_rBtn)

        self.orientPAxisY_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup.addButton(self.orientPAxisY_rBtn)
        self.orientPAxisY_rBtn.setObjectName(u"orientPAxisY_rBtn")
        self.orientPAxisY_rBtn.setAutoExclusive(False)

        self.horizontalLayout_21.addWidget(self.orientPAxisY_rBtn)

        self.orientPAxisZ_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup.addButton(self.orientPAxisZ_rBtn)
        self.orientPAxisZ_rBtn.setObjectName(u"orientPAxisZ_rBtn")

        self.horizontalLayout_21.addWidget(self.orientPAxisZ_rBtn)


        self.verticalLayout_19.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.orientSecAxisX_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.orientSecAxisX_rBtn)
        self.orientSecAxisX_rBtn.setObjectName(u"orientSecAxisX_rBtn")
        self.orientSecAxisX_rBtn.setChecked(False)

        self.horizontalLayout_22.addWidget(self.orientSecAxisX_rBtn)

        self.orientSecAxisY_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup_2.addButton(self.orientSecAxisY_rBtn)
        self.orientSecAxisY_rBtn.setObjectName(u"orientSecAxisY_rBtn")
        self.orientSecAxisY_rBtn.setChecked(False)

        self.horizontalLayout_22.addWidget(self.orientSecAxisY_rBtn)

        self.orientSecAxisZ_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup_2.addButton(self.orientSecAxisZ_rBtn)
        self.orientSecAxisZ_rBtn.setObjectName(u"orientSecAxisZ_rBtn")
        self.orientSecAxisZ_rBtn.setChecked(True)

        self.horizontalLayout_22.addWidget(self.orientSecAxisZ_rBtn)


        self.verticalLayout_19.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.orientWorldAxisX_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.orientWorldAxisX_rBtn)
        self.orientWorldAxisX_rBtn.setObjectName(u"orientWorldAxisX_rBtn")
        self.orientWorldAxisX_rBtn.setChecked(False)

        self.horizontalLayout_24.addWidget(self.orientWorldAxisX_rBtn)

        self.orientWorldAxisY_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup_3.addButton(self.orientWorldAxisY_rBtn)
        self.orientWorldAxisY_rBtn.setObjectName(u"orientWorldAxisY_rBtn")

        self.horizontalLayout_24.addWidget(self.orientWorldAxisY_rBtn)

        self.orientWorldAxisZ_rBtn = QRadioButton(self.groupBox_10)
        self.buttonGroup_3.addButton(self.orientWorldAxisZ_rBtn)
        self.orientWorldAxisZ_rBtn.setObjectName(u"orientWorldAxisZ_rBtn")
        self.orientWorldAxisZ_rBtn.setChecked(True)

        self.horizontalLayout_24.addWidget(self.orientWorldAxisZ_rBtn)


        self.verticalLayout_19.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_25.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.orientPrimeNeg_chkBox = QCheckBox(self.groupBox_10)
        self.orientPrimeNeg_chkBox.setObjectName(u"orientPrimeNeg_chkBox")

        self.verticalLayout_20.addWidget(self.orientPrimeNeg_chkBox)

        self.orientSecNeg_chkBox = QCheckBox(self.groupBox_10)
        self.orientSecNeg_chkBox.setObjectName(u"orientSecNeg_chkBox")

        self.verticalLayout_20.addWidget(self.orientSecNeg_chkBox)

        self.orientWorldNeg_chkBox = QCheckBox(self.groupBox_10)
        self.orientWorldNeg_chkBox.setObjectName(u"orientWorldNeg_chkBox")

        self.verticalLayout_20.addWidget(self.orientWorldNeg_chkBox)


        self.horizontalLayout_25.addLayout(self.verticalLayout_20)


        self.verticalLayout_21.addLayout(self.horizontalLayout_25)

        self.orientChd_chkBox = QCheckBox(self.groupBox_10)
        self.orientChd_chkBox.setObjectName(u"orientChd_chkBox")
        self.orientChd_chkBox.setChecked(True)

        self.verticalLayout_21.addWidget(self.orientChd_chkBox)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.orientJntHelper_Btn = QPushButton(self.groupBox_10)
        self.orientJntHelper_Btn.setObjectName(u"orientJntHelper_Btn")

        self.horizontalLayout_23.addWidget(self.orientJntHelper_Btn)

        self.orientJnt_Btn = QPushButton(self.groupBox_10)
        self.orientJnt_Btn.setObjectName(u"orientJnt_Btn")

        self.horizontalLayout_23.addWidget(self.orientJnt_Btn)


        self.verticalLayout_21.addLayout(self.horizontalLayout_23)


        self.verticalLayout_22.addWidget(self.groupBox_10)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.displayJntAxis_Btn = QPushButton(self.tab_jnt)
        self.displayJntAxis_Btn.setObjectName(u"displayJntAxis_Btn")

        self.horizontalLayout_26.addWidget(self.displayJntAxis_Btn)

        self.axisChd_chkBox = QCheckBox(self.tab_jnt)
        self.axisChd_chkBox.setObjectName(u"axisChd_chkBox")
        self.axisChd_chkBox.setChecked(True)

        self.horizontalLayout_26.addWidget(self.axisChd_chkBox)


        self.verticalLayout_22.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.splitJnt_spBox = QSpinBox(self.tab_jnt)
        self.splitJnt_spBox.setObjectName(u"splitJnt_spBox")
        self.splitJnt_spBox.setMinimum(2)
        self.splitJnt_spBox.setValue(2)

        self.horizontalLayout_18.addWidget(self.splitJnt_spBox)

        self.splitJnt_Btn = QPushButton(self.tab_jnt)
        self.splitJnt_Btn.setObjectName(u"splitJnt_Btn")

        self.horizontalLayout_18.addWidget(self.splitJnt_Btn)


        self.verticalLayout_22.addLayout(self.horizontalLayout_18)

        self.mirrorJnt_Btn = QPushButton(self.tab_jnt)
        self.mirrorJnt_Btn.setObjectName(u"mirrorJnt_Btn")
        self.mirrorJnt_Btn.setEnabled(False)

        self.verticalLayout_22.addWidget(self.mirrorJnt_Btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_jnt, "")
        self.tab_transforms = QWidget()
        self.tab_transforms.setObjectName(u"tab_transforms")
        self.verticalLayout_14 = QVBoxLayout(self.tab_transforms)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_6 = QGroupBox(self.tab_transforms)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.prefix_rBtn = QRadioButton(self.groupBox_6)
        self.prefix_rBtn.setObjectName(u"prefix_rBtn")
        self.prefix_rBtn.setChecked(False)

        self.horizontalLayout_17.addWidget(self.prefix_rBtn)

        self.suffix_rBtn = QRadioButton(self.groupBox_6)
        self.suffix_rBtn.setObjectName(u"suffix_rBtn")
        self.suffix_rBtn.setChecked(True)

        self.horizontalLayout_17.addWidget(self.suffix_rBtn)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_17)

        self.label_suffix = QLabel(self.groupBox_6)
        self.label_suffix.setObjectName(u"label_suffix")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_suffix.sizePolicy().hasHeightForWidth())
        self.label_suffix.setSizePolicy(sizePolicy9)
        self.label_suffix.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_12.addWidget(self.label_suffix)

        self.suffix_edit = QLineEdit(self.groupBox_6)
        self.suffix_edit.setObjectName(u"suffix_edit")

        self.horizontalLayout_12.addWidget(self.suffix_edit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.keepSuffix_chkBox = QCheckBox(self.groupBox_6)
        self.keepSuffix_chkBox.setObjectName(u"keepSuffix_chkBox")
        self.keepSuffix_chkBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.keepSuffix_chkBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.zero_btn = QPushButton(self.groupBox_6)
        self.zero_btn.setObjectName(u"zero_btn")

        self.verticalLayout_4.addWidget(self.zero_btn)


        self.verticalLayout_14.addWidget(self.groupBox_6)

        self.mirrorTransforms_grpBox = QGroupBox(self.tab_transforms)
        self.mirrorTransforms_grpBox.setObjectName(u"mirrorTransforms_grpBox")
        self.mirrorTransforms_grpBox.setEnabled(True)
        self.verticalLayout_13 = QVBoxLayout(self.mirrorTransforms_grpBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_8 = QGroupBox(self.mirrorTransforms_grpBox)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.mirObj_chkBox = QRadioButton(self.groupBox_8)
        self.mirObj_chkBox.setObjectName(u"mirObj_chkBox")
        self.mirObj_chkBox.setChecked(True)

        self.horizontalLayout_16.addWidget(self.mirObj_chkBox)

        self.mirWorld_chkBox = QRadioButton(self.groupBox_8)
        self.mirWorld_chkBox.setObjectName(u"mirWorld_chkBox")
        self.mirWorld_chkBox.setChecked(False)

        self.horizontalLayout_16.addWidget(self.mirWorld_chkBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_16)


        self.verticalLayout_13.addWidget(self.groupBox_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.mirrorLRLabel = QLabel(self.mirrorTransforms_grpBox)
        self.mirrorLRLabel.setObjectName(u"mirrorLRLabel")

        self.horizontalLayout_15.addWidget(self.mirrorLRLabel)

        self.mirrorLR_edit = QLineEdit(self.mirrorTransforms_grpBox)
        self.mirrorLR_edit.setObjectName(u"mirrorLR_edit")

        self.horizontalLayout_15.addWidget(self.mirrorLR_edit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnMirrorX = QPushButton(self.mirrorTransforms_grpBox)
        self.btnMirrorX.setObjectName(u"btnMirrorX")
        sizePolicy8.setHeightForWidth(self.btnMirrorX.sizePolicy().hasHeightForWidth())
        self.btnMirrorX.setSizePolicy(sizePolicy8)
        self.btnMirrorX.setMinimumSize(QSize(0, 24))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.btnMirrorX.setFont(font3)
        self.btnMirrorX.setStyleSheet(u"background-color: rgb(255, 70, 70);\n"
"color: white;\n"
"border: 0px;")

        self.horizontalLayout_6.addWidget(self.btnMirrorX)

        self.btn_mirrorY = QPushButton(self.mirrorTransforms_grpBox)
        self.btn_mirrorY.setObjectName(u"btn_mirrorY")
        sizePolicy8.setHeightForWidth(self.btn_mirrorY.sizePolicy().hasHeightForWidth())
        self.btn_mirrorY.setSizePolicy(sizePolicy8)
        self.btn_mirrorY.setMinimumSize(QSize(0, 24))
        self.btn_mirrorY.setFont(font3)
        self.btn_mirrorY.setStyleSheet(u"background-color: rgb(72, 216, 0);\n"
"color: white;\n"
"border: 0px;")

        self.horizontalLayout_6.addWidget(self.btn_mirrorY)

        self.btn_mirrorZ = QPushButton(self.mirrorTransforms_grpBox)
        self.btn_mirrorZ.setObjectName(u"btn_mirrorZ")
        sizePolicy8.setHeightForWidth(self.btn_mirrorZ.sizePolicy().hasHeightForWidth())
        self.btn_mirrorZ.setSizePolicy(sizePolicy8)
        self.btn_mirrorZ.setMinimumSize(QSize(0, 24))
        self.btn_mirrorZ.setFont(font3)
        self.btn_mirrorZ.setStyleSheet(u"background-color: blue;\n"
"color: white;\n"
"border: 0px;")

        self.horizontalLayout_6.addWidget(self.btn_mirrorZ)


        self.verticalLayout_13.addLayout(self.horizontalLayout_6)


        self.verticalLayout_14.addWidget(self.mirrorTransforms_grpBox)

        self.parentAsChain_Btn = QPushButton(self.tab_transforms)
        self.parentAsChain_Btn.setObjectName(u"parentAsChain_Btn")

        self.verticalLayout_14.addWidget(self.parentAsChain_Btn)

        self.verticalSpacer = QSpacerItem(20, 516, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_transforms, "")
        self.tab_utils = QWidget()
        self.tab_utils.setObjectName(u"tab_utils")
        self.verticalLayout_28 = QVBoxLayout(self.tab_utils)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.spawnAvgLoc_grpBox = QGroupBox(self.tab_utils)
        self.spawnAvgLoc_grpBox.setObjectName(u"spawnAvgLoc_grpBox")
        self.horizontalLayout_43 = QHBoxLayout(self.spawnAvgLoc_grpBox)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_13 = QLabel(self.spawnAvgLoc_grpBox)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_43.addWidget(self.label_13)

        self.avgLocName_lineEdit = QLineEdit(self.spawnAvgLoc_grpBox)
        self.avgLocName_lineEdit.setObjectName(u"avgLocName_lineEdit")

        self.horizontalLayout_43.addWidget(self.avgLocName_lineEdit)

        self.avgLocSpawn_Btn = QPushButton(self.spawnAvgLoc_grpBox)
        self.avgLocSpawn_Btn.setObjectName(u"avgLocSpawn_Btn")

        self.horizontalLayout_43.addWidget(self.avgLocSpawn_Btn)


        self.verticalLayout_28.addWidget(self.spawnAvgLoc_grpBox)

        self.oneLiner_grpBox = QGroupBox(self.tab_utils)
        self.oneLiner_grpBox.setObjectName(u"oneLiner_grpBox")
        self.oneLiner_grpBox.setMinimumSize(QSize(0, 61))
        self.verticalLayout_29 = QVBoxLayout(self.oneLiner_grpBox)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.oneLiner_lineEdit = QLineEdit(self.oneLiner_grpBox)
        self.oneLiner_lineEdit.setObjectName(u"oneLiner_lineEdit")

        self.verticalLayout_29.addWidget(self.oneLiner_lineEdit)


        self.verticalLayout_28.addWidget(self.oneLiner_grpBox)

        self.verticalSpacer_6 = QSpacerItem(20, 804, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_6)

        self.tabWidget.addTab(self.tab_utils, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.label_5 = QLabel(MainWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5)

        self.label_4 = QLabel(MainWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_12.addLayout(self.verticalLayout_8)

        QWidget.setTabOrder(self.spawnMult_spBox, self.asCrv)
        QWidget.setTabOrder(self.asCrv, self.asJnt)
        QWidget.setTabOrder(self.asJnt, self.asReplace)
        QWidget.setTabOrder(self.asReplace, self.spawnAtPivot_rBtn)
        QWidget.setTabOrder(self.spawnAtPivot_rBtn, self.spawnAtCenter_rBtn)
        QWidget.setTabOrder(self.spawnAtCenter_rBtn, self.attrVisibility_chkBox)
        QWidget.setTabOrder(self.attrVisibility_chkBox, self.createCtlSfx_lineEdit)
        QWidget.setTabOrder(self.createCtlSfx_lineEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.btn_createCtl)
        QWidget.setTabOrder(self.btn_createCtl, self.col_22)
        QWidget.setTabOrder(self.col_22, self.col_25)
        QWidget.setTabOrder(self.col_25, self.col_26)
        QWidget.setTabOrder(self.col_26, self.col_28)
        QWidget.setTabOrder(self.col_28, self.col_29)
        QWidget.setTabOrder(self.col_29, self.attrScale_chkBox)
        QWidget.setTabOrder(self.attrScale_chkBox, self.transY_chkBox)
        QWidget.setTabOrder(self.transY_chkBox, self.spTransform)
        QWidget.setTabOrder(self.spTransform, self.transX_chkBox)
        QWidget.setTabOrder(self.transX_chkBox, self.transZ_chkBox)
        QWidget.setTabOrder(self.transZ_chkBox, self.attrRotate_chkBox)
        QWidget.setTabOrder(self.attrRotate_chkBox, self.attrTranslate_chkBox)
        QWidget.setTabOrder(self.attrTranslate_chkBox, self.angle_box)
        QWidget.setTabOrder(self.angle_box, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.btn_rotateX)
        QWidget.setTabOrder(self.btn_rotateX, self.btn_rotateY)
        QWidget.setTabOrder(self.btn_rotateY, self.btn_rotateZ)
        QWidget.setTabOrder(self.btn_rotateZ, self.sizeX)
        QWidget.setTabOrder(self.sizeX, self.sizeY)
        QWidget.setTabOrder(self.sizeY, self.sizeZ)
        QWidget.setTabOrder(self.sizeZ, self.sizeStepSpinBox)
        QWidget.setTabOrder(self.sizeStepSpinBox, self.resizeSlider)
        QWidget.setTabOrder(self.resizeSlider, self.copyShp_Btn)
        QWidget.setTabOrder(self.copyShp_Btn, self.saveShp_btn)
        QWidget.setTabOrder(self.saveShp_btn, self.attrTransX_chkBox)
        QWidget.setTabOrder(self.attrTransX_chkBox, self.attrTransY_chkBox)
        QWidget.setTabOrder(self.attrTransY_chkBox, self.attrTransZ_chkBox)
        QWidget.setTabOrder(self.attrTransZ_chkBox, self.attrRotateX_chkBox)
        QWidget.setTabOrder(self.attrRotateX_chkBox, self.attrRotateY_chkBox)
        QWidget.setTabOrder(self.attrRotateY_chkBox, self.attrRotateZ_chkBox)
        QWidget.setTabOrder(self.attrRotateZ_chkBox, self.attrScaleX_chkBox)
        QWidget.setTabOrder(self.attrScaleX_chkBox, self.attrScaleY_chkBox)
        QWidget.setTabOrder(self.attrScaleY_chkBox, self.attrScaleZ_chkBox)
        QWidget.setTabOrder(self.attrScaleZ_chkBox, self.attrAuto_chkBox)
        QWidget.setTabOrder(self.attrAuto_chkBox, self.attrSet_Btn)
        QWidget.setTabOrder(self.attrSet_Btn, self.customAttrCreate_rBtn)
        QWidget.setTabOrder(self.customAttrCreate_rBtn, self.customAttrEdit_rBtn)
        QWidget.setTabOrder(self.customAttrEdit_rBtn, self.customAttrList_cBox)
        QWidget.setTabOrder(self.customAttrList_cBox, self.customAttrLoad_Btn)
        QWidget.setTabOrder(self.customAttrLoad_Btn, self.customAttrName_lineEdit)
        QWidget.setTabOrder(self.customAttrName_lineEdit, self.customAttrNiceName_lineEdit)
        QWidget.setTabOrder(self.customAttrNiceName_lineEdit, self.customAttrKeyable_rBtn)
        QWidget.setTabOrder(self.customAttrKeyable_rBtn, self.customAttrNonKeyable_rBtn)
        QWidget.setTabOrder(self.customAttrNonKeyable_rBtn, self.customAttrHidden_rBtn)
        QWidget.setTabOrder(self.customAttrHidden_rBtn, self.customAttrFloat_rBtn)
        QWidget.setTabOrder(self.customAttrFloat_rBtn, self.customAttrInt_rBtn)
        QWidget.setTabOrder(self.customAttrInt_rBtn, self.customAttrBool_rBtn)
        QWidget.setTabOrder(self.customAttrBool_rBtn, self.customAttrEnum_rBtn)
        QWidget.setTabOrder(self.customAttrEnum_rBtn, self.customAttrVector_rBtn)
        QWidget.setTabOrder(self.customAttrVector_rBtn, self.customAttrValue_lineEdit)
        QWidget.setTabOrder(self.customAttrValue_lineEdit, self.customAttrMin_chkBox)
        QWidget.setTabOrder(self.customAttrMin_chkBox, self.customAttrMinVal_spinBox)
        QWidget.setTabOrder(self.customAttrMinVal_spinBox, self.customAttrMax_chkBox)
        QWidget.setTabOrder(self.customAttrMax_chkBox, self.customAttrMaxVal_spinBox)
        QWidget.setTabOrder(self.customAttrMaxVal_spinBox, self.customAttrEnumNames_lineEdit)
        QWidget.setTabOrder(self.customAttrEnumNames_lineEdit, self.customAttrApply_Btn)
        QWidget.setTabOrder(self.customAttrApply_Btn, self.customAttrKeepVal_chkBox)
        QWidget.setTabOrder(self.customAttrKeepVal_chkBox, self.customAttrResetVal_Btn)
        QWidget.setTabOrder(self.customAttrResetVal_Btn, self.crJnt_Btn)
        QWidget.setTabOrder(self.crJnt_Btn, self.parConstraint_chkBox)
        QWidget.setTabOrder(self.parConstraint_chkBox, self.scaleCons_chkBox)
        QWidget.setTabOrder(self.scaleCons_chkBox, self.orientCons_chkBox)
        QWidget.setTabOrder(self.orientCons_chkBox, self.pointCons_chkBox)
        QWidget.setTabOrder(self.pointCons_chkBox, self.chainJnt_chkBox)
        QWidget.setTabOrder(self.chainJnt_chkBox, self.suffix_chkBox)
        QWidget.setTabOrder(self.suffix_chkBox, self.jntSuffixName_lineEdit)
        QWidget.setTabOrder(self.jntSuffixName_lineEdit, self.createSelJnt_Btn)
        QWidget.setTabOrder(self.createSelJnt_Btn, self.orientPAxisX_rBtn)
        QWidget.setTabOrder(self.orientPAxisX_rBtn, self.orientPAxisY_rBtn)
        QWidget.setTabOrder(self.orientPAxisY_rBtn, self.orientPAxisZ_rBtn)
        QWidget.setTabOrder(self.orientPAxisZ_rBtn, self.orientSecAxisX_rBtn)
        QWidget.setTabOrder(self.orientSecAxisX_rBtn, self.orientSecAxisY_rBtn)
        QWidget.setTabOrder(self.orientSecAxisY_rBtn, self.orientSecAxisZ_rBtn)
        QWidget.setTabOrder(self.orientSecAxisZ_rBtn, self.orientWorldAxisX_rBtn)
        QWidget.setTabOrder(self.orientWorldAxisX_rBtn, self.orientWorldAxisY_rBtn)
        QWidget.setTabOrder(self.orientWorldAxisY_rBtn, self.orientWorldAxisZ_rBtn)
        QWidget.setTabOrder(self.orientWorldAxisZ_rBtn, self.orientPrimeNeg_chkBox)
        QWidget.setTabOrder(self.orientPrimeNeg_chkBox, self.orientSecNeg_chkBox)
        QWidget.setTabOrder(self.orientSecNeg_chkBox, self.orientWorldNeg_chkBox)
        QWidget.setTabOrder(self.orientWorldNeg_chkBox, self.orientChd_chkBox)
        QWidget.setTabOrder(self.orientChd_chkBox, self.orientJntHelper_Btn)
        QWidget.setTabOrder(self.orientJntHelper_Btn, self.orientJnt_Btn)
        QWidget.setTabOrder(self.orientJnt_Btn, self.displayJntAxis_Btn)
        QWidget.setTabOrder(self.displayJntAxis_Btn, self.axisChd_chkBox)
        QWidget.setTabOrder(self.axisChd_chkBox, self.splitJnt_spBox)
        QWidget.setTabOrder(self.splitJnt_spBox, self.splitJnt_Btn)
        QWidget.setTabOrder(self.splitJnt_Btn, self.mirrorJnt_Btn)
        QWidget.setTabOrder(self.mirrorJnt_Btn, self.prefix_rBtn)
        QWidget.setTabOrder(self.prefix_rBtn, self.suffix_rBtn)
        QWidget.setTabOrder(self.suffix_rBtn, self.suffix_edit)
        QWidget.setTabOrder(self.suffix_edit, self.keepSuffix_chkBox)
        QWidget.setTabOrder(self.keepSuffix_chkBox, self.zero_btn)
        QWidget.setTabOrder(self.zero_btn, self.mirObj_chkBox)
        QWidget.setTabOrder(self.mirObj_chkBox, self.mirWorld_chkBox)
        QWidget.setTabOrder(self.mirWorld_chkBox, self.mirrorLR_edit)
        QWidget.setTabOrder(self.mirrorLR_edit, self.btnMirrorX)
        QWidget.setTabOrder(self.btnMirrorX, self.btn_mirrorY)
        QWidget.setTabOrder(self.btn_mirrorY, self.btn_mirrorZ)
        QWidget.setTabOrder(self.btn_mirrorZ, self.parentAsChain_Btn)
        QWidget.setTabOrder(self.parentAsChain_Btn, self.avgLocName_lineEdit)
        QWidget.setTabOrder(self.avgLocName_lineEdit, self.avgLocSpawn_Btn)
        QWidget.setTabOrder(self.avgLocSpawn_Btn, self.oneLiner_lineEdit)
        QWidget.setTabOrder(self.oneLiner_lineEdit, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.spObject)
        QWidget.setTabOrder(self.spObject, self.colorRandom_btn)
        QWidget.setTabOrder(self.colorRandom_btn, self.sizeStepSpinBox_2)

        self.retranslateUi(MainWindow)
        self.customAttrEdit_rBtn.toggled.connect(self.customAttrList_cBox.setEnabled)
        self.customAttrMin_chkBox.toggled.connect(self.customAttrMinVal_spinBox.setEnabled)
        self.customAttrMax_chkBox.toggled.connect(self.customAttrMaxVal_spinBox.setEnabled)
        self.customAttrEnum_rBtn.toggled.connect(self.customAttrEnumNames_lineEdit.setEnabled)
        self.customAttrEnum_rBtn.toggled.connect(self.customAttrValue_lineEdit.setDisabled)
        self.attrTranslate_chkBox.toggled.connect(self.attrTransY_chkBox.setEnabled)
        self.attrTranslate_chkBox.toggled.connect(self.attrTransX_chkBox.setEnabled)
        self.attrTranslate_chkBox.toggled.connect(self.attrTransZ_chkBox.setEnabled)
        self.attrRotate_chkBox.toggled.connect(self.attrRotateX_chkBox.setEnabled)
        self.attrRotate_chkBox.toggled.connect(self.attrRotateY_chkBox.setEnabled)
        self.attrRotate_chkBox.toggled.connect(self.attrRotateZ_chkBox.setEnabled)
        self.attrScale_chkBox.toggled.connect(self.attrScaleX_chkBox.setEnabled)
        self.attrScale_chkBox.toggled.connect(self.attrScaleY_chkBox.setEnabled)
        self.attrScale_chkBox.toggled.connect(self.attrScaleZ_chkBox.setEnabled)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        self.col_18.setDefault(False)
        self.col_16.setDefault(False)
        self.col_20.setDefault(False)
        self.col_14.setDefault(False)
        self.col_12.setDefault(False)
        self.col_10.setDefault(False)
        self.col_17.setDefault(False)
        self.col_11.setDefault(False)
        self.col_15.setDefault(False)
        self.col_19.setDefault(False)
        self.col_21.setDefault(False)
        self.col_13.setDefault(False)
        self.col_1.setDefault(False)
        self.col_2.setDefault(False)
        self.col_3.setDefault(False)
        self.col_4.setDefault(False)
        self.col_5.setDefault(False)
        self.col_6.setDefault(False)
        self.col_7.setDefault(False)
        self.col_8.setDefault(False)
        self.col_9.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"R.U.S.A.K v0.6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Control Creator", None))
        self.asCrv.setText(QCoreApplication.translate("MainWindow", u"as Curve", None))
        self.asJnt.setText(QCoreApplication.translate("MainWindow", u"as Joint", None))
        self.asReplace.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"At:", None))
        self.spawnAtPivot_rBtn.setText(QCoreApplication.translate("MainWindow", u"Pivot", None))
        self.spawnAtCenter_rBtn.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Spawn Mult:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Suffix: ", None))
        self.createCtlSfx_lineEdit.setText(QCoreApplication.translate("MainWindow", u"Ctrl", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"QuickCreate", None))
        self.shp_CrossArrow.setText("")
        self.shp_Arrow.setText("")
        self.shp_Needle.setText("")
        self.shp_ArrowBent.setText("")
        self.shp_CrossArrowBent.setText("")
        self.shp_Circle.setText("")
        self.shp_Square.setText("")
        self.shp_Cross.setText("")
        self.shp_Sphere.setText("")
        self.shp_Box.setText("")
        self.btn_createCtl.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.col_22.setText("")
        self.col_18.setText("")
        self.col_16.setText("")
        self.col_20.setText("")
        self.col_14.setText("")
        self.col_12.setText("")
        self.col_10.setText("")
        self.col_17.setText("")
        self.col_23.setText("")
        self.col_11.setText("")
        self.col_15.setText("")
        self.col_19.setText("")
        self.col_21.setText("")
        self.col_13.setText("")
        self.col_1.setText("")
        self.col_2.setText("")
        self.col_3.setText("")
        self.col_4.setText("")
        self.col_5.setText("")
        self.col_6.setText("")
        self.col_7.setText("")
        self.col_8.setText("")
        self.col_9.setText("")
        self.col_24.setText("")
        self.col_25.setText("")
        self.col_26.setText("")
        self.col_27.setText("")
        self.col_28.setText("")
        self.col_29.setText("")
        self.col_30.setText("")
        self.col_31.setText("")
#if QT_CONFIG(tooltip)
        self.colorRandom_btn.setToolTip(QCoreApplication.translate("MainWindow", u"randomize ctrl color", None))
#endif // QT_CONFIG(tooltip)
        self.colorRandom_btn.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Color Picker", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Space", None))
#if QT_CONFIG(tooltip)
        self.spObject.setToolTip(QCoreApplication.translate("MainWindow", u"Use object transform space", None))
#endif // QT_CONFIG(tooltip)
        self.spObject.setText(QCoreApplication.translate("MainWindow", u"Object", None))
#if QT_CONFIG(tooltip)
        self.spTransform.setToolTip(QCoreApplication.translate("MainWindow", u"Use shape transform space", None))
#endif // QT_CONFIG(tooltip)
        self.spTransform.setText(QCoreApplication.translate("MainWindow", u"Transform", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.transX_chkBox.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.transY_chkBox.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.transZ_chkBox.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_resizeStep_2.setText(QCoreApplication.translate("MainWindow", u"Step: ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.label_angle.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.btn_rotateX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_rotateY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.btn_rotateZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.sizeX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.sizeY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.sizeZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_resizeStep.setText(QCoreApplication.translate("MainWindow", u"Step: ", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Shape Transforms", None))
#if QT_CONFIG(tooltip)
        self.copyShp_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"copy selected ctrls to last selected ctrl shape", None))
#endif // QT_CONFIG(tooltip)
        self.copyShp_Btn.setText(QCoreApplication.translate("MainWindow", u"Copy Shape", None))
        self.saveShp_btn.setText(QCoreApplication.translate("MainWindow", u"Save Selected Shape", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ctrl), QCoreApplication.translate("MainWindow", u"Controllers", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Lock n Hide Transform Attrs", None))
        self.attrTranslate_chkBox.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.attrTransY_chkBox.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.attrTransX_chkBox.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.attrTransZ_chkBox.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.attrRotate_chkBox.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.attrRotateX_chkBox.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.attrRotateY_chkBox.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.attrRotateZ_chkBox.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.attrScale_chkBox.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.attrScaleX_chkBox.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.attrScaleY_chkBox.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.attrScaleZ_chkBox.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.attrVisibility_chkBox.setText(QCoreApplication.translate("MainWindow", u"Visibility", None))
#if QT_CONFIG(tooltip)
        self.attrAuto_chkBox.setToolTip(QCoreApplication.translate("MainWindow", u"automatically apply to selection when the values changed", None))
#endif // QT_CONFIG(tooltip)
        self.attrAuto_chkBox.setText(QCoreApplication.translate("MainWindow", u"Auto Apply", None))
#if QT_CONFIG(tooltip)
        self.attrSet_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"set current values to selection", None))
#endif // QT_CONFIG(tooltip)
        self.attrSet_Btn.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Custom Attributes", None))
        self.customAttrCreate_rBtn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.customAttrEdit_rBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.customAttrList_cBox.setItemText(0, QCoreApplication.translate("MainWindow", u"item1", None))
        self.customAttrList_cBox.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.customAttrList_cBox.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.customAttrList_cBox.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.customAttrList_cBox.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.customAttrList_cBox.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.customAttrList_cBox.setItemText(6, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.customAttrList_cBox.setItemText(7, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.customAttrLoad_Btn.setText(QCoreApplication.translate("MainWindow", u"Load Custom Attrs", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.customAttrName_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"myAttribute", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nice Name:", None))
        self.customAttrNiceName_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"My Attribute", None))
        self.keyable_grpBox.setTitle(QCoreApplication.translate("MainWindow", u"Keyable", None))
        self.customAttrKeyable_rBtn.setText(QCoreApplication.translate("MainWindow", u"Keyable", None))
        self.customAttrNonKeyable_rBtn.setText(QCoreApplication.translate("MainWindow", u"Non-Keyable", None))
        self.customAttrHidden_rBtn.setText(QCoreApplication.translate("MainWindow", u"Hidden", None))
        self.customAttrType_grpBox.setTitle(QCoreApplication.translate("MainWindow", u"Type", None))
        self.customAttrFloat_rBtn.setText(QCoreApplication.translate("MainWindow", u"Float", None))
        self.customAttrInt_rBtn.setText(QCoreApplication.translate("MainWindow", u"Int", None))
        self.customAttrBool_rBtn.setText(QCoreApplication.translate("MainWindow", u"Boolean", None))
        self.customAttrEnum_rBtn.setText(QCoreApplication.translate("MainWindow", u"Enum", None))
        self.customAttrVector_rBtn.setText(QCoreApplication.translate("MainWindow", u"Vector", None))
        self.customAttrString_rBtn.setText(QCoreApplication.translate("MainWindow", u"String", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Value:", None))
        self.customAttrValue_lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.customAttrMin_chkBox.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.customAttrMax_chkBox.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enum Names", None))
        self.customAttrEnumNames_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"separate with comma (,)", None))
#if QT_CONFIG(tooltip)
        self.customAttrApply_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"create/apply edits on selected", None))
#endif // QT_CONFIG(tooltip)
        self.customAttrApply_Btn.setText(QCoreApplication.translate("MainWindow", u"Create Attribute", None))
        self.customAttrKeepVal_chkBox.setText(QCoreApplication.translate("MainWindow", u"Keep Values", None))
        self.customAttrResetVal_Btn.setText(QCoreApplication.translate("MainWindow", u"Reset Values", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_attr), QCoreApplication.translate("MainWindow", u"Attributes", None))
        self.crJnt_Btn.setText(QCoreApplication.translate("MainWindow", u"Create Joints", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Create Joint on Selected", None))
        self.parConstraint_chkBox.setText(QCoreApplication.translate("MainWindow", u"ParentConstraint", None))
        self.scaleCons_chkBox.setText(QCoreApplication.translate("MainWindow", u"Scale Constraint", None))
        self.orientCons_chkBox.setText(QCoreApplication.translate("MainWindow", u"OrientConstraint", None))
        self.pointCons_chkBox.setText(QCoreApplication.translate("MainWindow", u"PointConstraint", None))
        self.chainJnt_chkBox.setText(QCoreApplication.translate("MainWindow", u"Chain", None))
        self.suffix_chkBox.setText(QCoreApplication.translate("MainWindow", u"Suffix:", None))
        self.jntSuffixName_lineEdit.setText(QCoreApplication.translate("MainWindow", u"bJnt", None))
        self.createSelJnt_Btn.setText(QCoreApplication.translate("MainWindow", u"Create Joint(s)", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Orient Joint", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Primary Axis:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Secondary Axis:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Secondary Axis World Orientation:", None))
        self.orientPAxisX_rBtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.orientPAxisY_rBtn.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.orientPAxisZ_rBtn.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.orientSecAxisX_rBtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.orientSecAxisY_rBtn.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.orientSecAxisZ_rBtn.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.orientWorldAxisX_rBtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.orientWorldAxisY_rBtn.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.orientWorldAxisZ_rBtn.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.orientPrimeNeg_chkBox.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.orientSecNeg_chkBox.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.orientWorldNeg_chkBox.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.orientChd_chkBox.setText(QCoreApplication.translate("MainWindow", u"Children", None))
        self.orientJntHelper_Btn.setText(QCoreApplication.translate("MainWindow", u"Create/Update Helper(s)", None))
        self.orientJnt_Btn.setText(QCoreApplication.translate("MainWindow", u"Orient Joint(s)", None))
        self.displayJntAxis_Btn.setText(QCoreApplication.translate("MainWindow", u"Toggle Display Axis", None))
        self.axisChd_chkBox.setText(QCoreApplication.translate("MainWindow", u"Children", None))
#if QT_CONFIG(tooltip)
        self.splitJnt_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"select start joint and end joint to split", None))
#endif // QT_CONFIG(tooltip)
        self.splitJnt_Btn.setText(QCoreApplication.translate("MainWindow", u"Split Joints", None))
        self.mirrorJnt_Btn.setText(QCoreApplication.translate("MainWindow", u"Mirror Joints", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_jnt), QCoreApplication.translate("MainWindow", u"Joints", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Zero Transform", None))
        self.prefix_rBtn.setText(QCoreApplication.translate("MainWindow", u"Prefix", None))
        self.suffix_rBtn.setText(QCoreApplication.translate("MainWindow", u"Suffix", None))
        self.label_suffix.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.suffix_edit.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.keepSuffix_chkBox.setText(QCoreApplication.translate("MainWindow", u"Keep Previous Suffix", None))
        self.zero_btn.setText(QCoreApplication.translate("MainWindow", u"Zero Transform", None))
        self.mirrorTransforms_grpBox.setTitle(QCoreApplication.translate("MainWindow", u"Mirror Transform", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Space", None))
#if QT_CONFIG(tooltip)
        self.mirObj_chkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Use object transform space", None))
#endif // QT_CONFIG(tooltip)
        self.mirObj_chkBox.setText(QCoreApplication.translate("MainWindow", u"Object", None))
#if QT_CONFIG(tooltip)
        self.mirWorld_chkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Use shape transform space", None))
#endif // QT_CONFIG(tooltip)
        self.mirWorld_chkBox.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.mirrorLRLabel.setText(QCoreApplication.translate("MainWindow", u"LeftName, RightName:", None))
        self.mirrorLR_edit.setText(QCoreApplication.translate("MainWindow", u"_L_,_R_", None))
        self.btnMirrorX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_mirrorY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.btn_mirrorZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.parentAsChain_Btn.setText(QCoreApplication.translate("MainWindow", u"Parent as Chain", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_transforms), QCoreApplication.translate("MainWindow", u"Transforms", None))
        self.spawnAvgLoc_grpBox.setTitle(QCoreApplication.translate("MainWindow", u"Spawn Average Locator", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.avgLocName_lineEdit.setText(QCoreApplication.translate("MainWindow", u"average_Loc", None))
        self.avgLocSpawn_Btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.oneLiner_grpBox.setTitle(QCoreApplication.translate("MainWindow", u"OneLiner", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_utils), QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"By Fauzan Syabana", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"zansyabana@gmail.com", None))
    # retranslateUi

