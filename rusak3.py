#---------written by:----------------------
#-------Fauzan Syabana---------------------
#------zansyabana@gmail.com----------------
#Licensed under MIT License

from __future__ import (division, # unicode_literals,
                        absolute_import)
import os
import sys
import importlib
if 'S:/prodEnv/Maya/omens/omens_td/Rigging' not in sys.path:
    sys.path.append('S:/prodEnv/Maya/omens/omens_td/Rigging')
from RUSAK import fsLib as fs
from oneLiner3 import selector, oneLiner
importlib.reload(fs)
from functools import partial

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
#from Qt.QtCore import Qt, Slot, QMetaObject, QAbstractTableModel, QObject, SIGNAL
#from Qt.QtUiTools import QUiLoader
#from Qt import QtGui, QtWidgets
from PySide2.QtGui import QIcon, QColor
from Qt.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QSizePolicy
#from Qt.QtWebKit import QWebView, QWebPage
#from PySide2 import QtCore, QtGui



SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

from RUSAK import rusakUI as py_ui
importlib.reload(py_ui)
try:
    import shiboken as sb
except:
    import  shiboken2 as sb
import maya.OpenMayaUI as apiUI
import pymel.core as pm
import maya.cmds as cmds

icon_circle = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/circle.png').replace('\\','/'))
icon_square = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/square.png').replace('\\','/'))
icon_sphere = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/sphere.png').replace('\\','/'))
icon_box = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/box.png').replace('\\','/'))
icon_cross = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/cross.png').replace('\\','/'))
icon_crossArrow = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/crossArrow.png').replace('\\','/'))
icon_arrowDouble = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/arrowDouble.png').replace('\\','/'))
icon_arrowBent = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/arrowBent.png').replace('\\','/'))
icon_crossArrowBent = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/crossArrowBent.png').replace('\\','/'))
icon_needle = QIcon(os.path.join(SCRIPT_DIRECTORY,'icons/needle.png').replace('\\','/'))



def getMayaWindow():
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """
    ptr = apiUI.MQtUtil.mainWindow()
    if ptr is not None:
        return sb.wrapInstance(int(ptr), QWidget)




class MainWindow(MayaQWidgetDockableMixin, QMainWindow, py_ui.Ui_MainWindow):

    def __init__(self, parent=getMayaWindow()):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.resizeSliderVal = 0
        self.shp_Circle.setIcon(icon_circle)
        self.shp_Square.setIcon(icon_square)
        self.shp_Sphere.setIcon(icon_sphere)
        self.shp_Box.setIcon(icon_box)
        self.shp_Cross.setIcon(icon_cross)
        self.shp_Arrow.setIcon(icon_arrowDouble)
        self.shp_CrossArrow.setIcon(icon_crossArrow)
        self.shp_ArrowBent.setIcon(icon_arrowBent)
        self.shp_CrossArrowBent.setIcon(icon_crossArrowBent)
        self.shp_Needle.setIcon(icon_needle)
        self.shp_Circle.clicked.connect(partial(self.createControl,'circle'))
        self.shp_Sphere.clicked.connect(partial(self.createControl,'sphere'))
        self.shp_Square.clicked.connect(partial(self.createControl,'square'))
        self.shp_Box.clicked.connect(partial(self.createControl,'box'))
        self.shp_Cross.clicked.connect(partial(self.createControl,'cross'))
        self.shp_Arrow.clicked.connect(partial(self.createControl,'arrowDouble'))
        self.shp_CrossArrow.clicked.connect(partial(self.createControl,'crossArrow'))
        self.shp_ArrowBent.clicked.connect(partial(self.createControl,'arrowDoubleCurve'))
        self.shp_CrossArrowBent.clicked.connect(partial(self.createControl,'crossArrowBent'))
        self.shp_Needle.clicked.connect(partial(self.createControl,'needleCircle'))
        self.comboBox.addItems([i for i in fs.createControls().curveLib])
        self.btn_createCtl.clicked.connect(self.createControl2)
        self.col_red.clicked.connect(partial(self.changeColor,13))
        self.col_blue.clicked.connect(partial(self.changeColor,29))
        self.col_green.clicked.connect(partial(self.changeColor,14))
        self.col_cyan.clicked.connect(partial(self.changeColor,18))
        self.col_purple.clicked.connect(partial(self.changeColor,9))
        self.col_yellow.clicked.connect(partial(self.changeColor,17))
        self.col_black.clicked.connect(partial(self.changeColor,1))
        self.col_white.clicked.connect(partial(self.changeColor,16))
        self.col_blue2.clicked.connect(partial(self.changeColor,5))
        self.col_green2.clicked.connect(partial(self.changeColor,7))
        self.col_pink.clicked.connect(partial(self.changeColor,20))
        self.col_brown.clicked.connect(partial(self.changeColor,10))
        self.zero_btn.clicked.connect(self.applyZero)
        self.resizeSlider.sliderMoved.connect(self.setScale)
        self.resizeSlider.sliderReleased.connect(self.resetSlider)
        self.btn_rotateX.clicked.connect(self.setRotateX)
        self.btn_rotateY.clicked.connect(self.setRotateY)
        self.btn_rotateZ.clicked.connect(self.setRotateZ)
        self.btn_copyShape.clicked.connect(self.replaceShape)
        self.lineOneLiner.editingFinished.connect(self.runOneLiner)
        

    def replaceShape(self):
        pm.undoInfo(openChunk=True)
        slt = pm.selected()
        shp = slt[-1]
        crvs = []
        for i in slt:
            if i != slt[-1]:
                curShp = i.getShape()
                pm.delete(curShp)
                crv = pm.duplicate(slt[-1])[0]
                crvShp = crv.getShape()
                pm.parent(crvShp,i,s=True,r=True)
                crvShp.rename(i+"Shape")
                pm.delete(crv)
        pm.select(slt)
        pm.undoInfo(closeChunk=True)

    def createControl(self, shp):
        pm.undoInfo(openChunk=True)
        slt = pm.selected()
        crvs = []

        if slt == []:
            dummyGrp = pm.group(em=True,w=True)
            if self.asJnt.isChecked():
                crv = fs.createControls().crCtl(dummyGrp,crvShp=shp,asJnt=True)
                crvs.append(crv)
            elif self.asReplace.isChecked():
                crv = fs.createControls().crCtl(dummyGrp, crvShp=shp,asReplace=True)
                crvs.append(crv)

            else:
                crv = fs.createControls().crCtl(dummyGrp,crvShp=shp,asJnt=False)
                crvs.append(crv)
            pm.delete(dummyGrp)
        else:
            for i in slt:
                if self.asJnt.isChecked():
                    crv = fs.createControls().crCtl(i,crvShp=shp,asJnt=True)
                    crvs.append(crv)
                elif self.asReplace.isChecked():
                    crv = fs.createControls().crCtl(i, crvShp=shp,asReplace=True)
                    crvs.append(crv)

                else:
                    crv = fs.createControls().crCtl(i,crvShp=shp,asJnt=False)
                    crvs.append(crv)
        try:
            pm.select(crvs)
        except:
            pass
            
        pm.undoInfo(closeChunk=True)

    def createControl2(self):
        shp1 = self.comboBox.currentText()
        self.createControl(shp1)

    def changeColor(self, color):
        slt = pm.selected()
        for i in slt:
            fs.createControls().setColor(i,color)

    def applyZero(self):
        fs.zeroTrans(self.suffix_edit.text(),self.suffix_keep.isChecked())

    def setScale(self):
        if self.sizeX.isChecked():
            sx = 1
        else:
            sx = 0
        if self.sizeY.isChecked():
            sy = 1
        else:
            sy = 0
        if self.sizeZ.isChecked():
            sz = 1
        else:
            sz = 0

        sliderValue = self.resizeSlider.sliderPosition()
        stepValue = self.sizeStepSpinBox.value()
        if sliderValue < self.resizeSliderVal:
            scaleValue = 1/stepValue
        else:
            scaleValue = stepValue

        if self.spTransform.isChecked():
            fs.transformShapes(s=1,rx=sx,ry=sy,rz=sz, scaleVal=scaleValue,objSpace=False)
        else:
            fs.transformShapes(s=1,rx=sx,ry=sy,rz=sz, scaleVal=scaleValue,objSpace=True)


        self.resizeSliderVal = sliderValue

    def resetSlider(self):
        self.resizeSlider.setValue(0)
        self.resizeSliderVal = 0

    def setRotateX(self):
        angle = self.angle_box.value()
        if self.spTransform.isChecked():
            fs.transformShapes(r=1,rx=angle,objSpace=False)
        else:
            fs.transformShapes(r=1,rx=angle,objSpace=True)

    def setRotateY(self):
        angle = self.angle_box.value()
        if self.spTransform.isChecked():
            fs.transformShapes(r=1,ry=angle,objSpace=False)
        else:
            fs.transformShapes(r=1,ry=angle,objSpace=True)

    def setRotateZ(self):
        angle = self.angle_box.value()
        if self.spTransform.isChecked():
            fs.transformShapes(r=1,rz=angle,objSpace=False)
        else:
            fs.transformShapes(r=1,rz=angle,objSpace=True)

    def printText(self):
        print(self.lineOneLiner.text())
    def runOneLiner(self):
        rnmQ = self.lineOneLiner.text()
        oneLiner(rnmQ)


def main():
    global ui
    try:
        ui.close()
    except:
        pass
    ui = MainWindow()
    # ui.show(dockable=True, area='right', floating=False) #example to dock the window to the right side of Maya Main Window
    ui.show()
    ui.raise_()

if __name__ == '__main__':
    main()
