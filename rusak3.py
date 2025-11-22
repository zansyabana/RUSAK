#---------written by:----------------------
#-------Fauzan Syabana---------------------
#------zansyabana@gmail.com----------------
#Licensed under MIT License

from __future__ import (division, # unicode_literals,
                        absolute_import)
import os
import sys
import random
from pathlib import Path
filePaths = Path(__file__).parent
icons = filePaths/'icons'
for pth in [filePaths, icons]:
    if pth.as_posix() not in sys.path:
        sys.path.append(pth.as_posix())
import importlib
import fsLib as fs
# from oneLiner3 import selector, oneLiner
importlib.reload(fs)
from functools import partial

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
#from Qt.QtCore import Qt, Slot, QMetaObject, QAbstractTableModel, QObject, SIGNAL
#from Qt.QtUiTools import QUiLoader
#from Qt import QtGui, QtWidgets
from PySide2.QtGui import QIcon, QColor
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QSizePolicy
#from Qt.QtWebKit import QWebView, QWebPage
#from PySide2 import QtCore, QtGui



SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


import rusakUI as py_ui
importlib.reload(py_ui)
try:
    import shiboken as sb
except:
    import  shiboken2 as sb
import maya.OpenMayaUI as apiUI
import pymel.core as pm
import maya.cmds as cmds



def getMayaWindow():
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """
    ptr = apiUI.MQtUtil.mainWindow()
    if ptr is not None:
        return sb.wrapInstance(int(ptr), QWidget)




class MainWindow(MayaQWidgetDockableMixin, QWidget, py_ui.Ui_MainWindow):

    def __init__(self, parent=getMayaWindow()):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.resizeSliderVal = 0
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
        # color button wiring: map UI `col_<name>` buttons to their color index
        for idx in range(1,32):
            btn = getattr(self, 'col_{}'.format(idx), None)
            if btn is not None:
                btn.clicked.connect(lambda checked=False, i=idx: self.changeColor(i))
        self.zero_btn.clicked.connect(self.applyZero)
        self.resizeSlider.sliderPressed.connect(self.beginScale)
        self.resizeSlider.sliderMoved.connect(self.setScale)
        self.resizeSlider.sliderReleased.connect(self.resetSlider)
        # translation controls
        # slider + step/spinbox: resizeSlider_2 and sizeStepSpinBox_2 in UI
        self.translateSliderVal = 0
        try:
            self.resizeSlider_2.sliderPressed.connect(self.beginTranslate)
            self.resizeSlider_2.sliderMoved.connect(self.setTranslate)
            self.resizeSlider_2.sliderReleased.connect(self.resetTranslate)
        except Exception:
            # UI may not have the widgets in some layouts; fail silently
            pass
        self.btn_rotateX.clicked.connect(self.setRotateX)
        self.btn_rotateY.clicked.connect(self.setRotateY)
        self.btn_rotateZ.clicked.connect(self.setRotateZ)
        self.copyShp_Btn.clicked.connect(self.replaceShape)
        self.parentAsChain_Btn.clicked.connect(self.chainParent)
        # self.lineOneLiner.editingFinished.connect(self.runOneLiner)
        self.splitJnt_Btn.clicked.connect(self.splitJoints)
        self.colorRandom_btn.clicked.connect(self.randomizeColor)
        

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
        # read spawn multiplier from UI (safe fallback to 1.0)
        try:
            spawn_mult = float(self.spawnMult_spBox.value())
        except Exception:
            spawn_mult = 1.0


        print(spawn_mult)
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
            if spawn_mult != 1.0:
                print("scaling by:", spawn_mult)
                fs.transformShapes(s=1, rx=1,ry=1,rz=1,scaleVal=spawn_mult, objSpace=True)
        except:
            pass
            
        pm.undoInfo(closeChunk=True)

    def createControl2(self):
        shp1 = self.comboBox.currentText()
        self.createControl(shp1)

    def changeColor(self, color):
        print("set color to:", color)
        slt = pm.selected()
        for i in slt:
            fs.createControls().setColor(i,color)

    def applyZero(self):
        prefix = self.prefix_rBtn.isChecked()
        fs.zeroTrans(self.suffix_edit.text(),self.keepSuffix_chkBox.isChecked(),prefix)

    def setScale(self):
        # read axis flags as ints (faster/clearer)
        sx = 1 if self.sizeX.isChecked() else 0
        sy = 1 if self.sizeY.isChecked() else 0
        sz = 1 if self.sizeZ.isChecked() else 0

        sliderValue = self.resizeSlider.sliderPosition()
        stepValue = float(self.sizeStepSpinBox.value())

        # compute how many "steps" changed since last call
        delta = sliderValue - self.resizeSliderVal
        if delta == 0:
            return

        # compute a single scale factor for the whole delta
        if delta > 0:
            scaleFactor = stepValue ** delta
        else:
            scaleFactor = (1.0 / stepValue) ** (-delta)

        # force transform-space (pivoted) behavior regardless of UI mode
        objSpace = False

        # caller (beginScale/resetSlider) handles undo and refresh so we only
        # perform the transform here.
        fs.transformShapes(s=1, rx=sx, ry=sy, rz=sz, scaleVal=scaleFactor, objSpace=objSpace)

        # store current slider for next delta
        self.resizeSliderVal = sliderValue

    def resetSlider(self):
        # close the undo chunk started in beginScale and restore refresh
        try:
            cmds.refresh(suspend=False)
        except Exception:
            pass
        try:
            pm.undoInfo(closeChunk=True)
        except Exception:
            pass

        self.resizeSlider.setValue(0)
        self.resizeSliderVal = 0

    def beginScale(self):
        # start a single undo chunk for the slider drag and suspend refresh
        self.resizeSliderVal = self.resizeSlider.sliderPosition()
        try:
            pm.undoInfo(openChunk=True)
        except Exception:
            pass
        try:
            cmds.refresh(suspend=True)
        except Exception:
            pass

    def setTranslate(self):
        """Called while translation slider is moved. Applies a relative translation
        to selected shapes' CVs using the step value and axis checkboxes.
        """
        # axis flags
        tx_flag = 1 if getattr(self, 'transX_chkBox', None) and self.transX_chkBox.isChecked() else 0
        ty_flag = 1 if getattr(self, 'transY_chkBox', None) and self.transY_chkBox.isChecked() else 0
        tz_flag = 1 if getattr(self, 'transZ_chkBox', None) and self.transZ_chkBox.isChecked() else 0

        sliderValue = self.resizeSlider_2.sliderPosition() if hasattr(self, 'resizeSlider_2') else 0
        stepValue = float(self.sizeStepSpinBox_2.value()) if hasattr(self, 'sizeStepSpinBox_2') else 1.0

        # delta from last call
        delta = sliderValue - self.translateSliderVal
        if delta == 0:
            return

        # compute relative translation amount (delta * step)
        move_amount = delta * stepValue

        tx = move_amount if tx_flag else 0
        ty = move_amount if ty_flag else 0
        tz = move_amount if tz_flag else 0

        # force transform-space (pivoted) behavior regardless of UI mode
        objSpace = False

        # caller (beginTranslate/resetTranslate) handles undo and refresh
        fs.transformShapes(t=1, tx=tx, ty=ty, tz=tz, objSpace=objSpace)

        self.translateSliderVal = sliderValue

    def resetTranslate(self):
        # close undo chunk and restore refresh started in beginTranslate
        try:
            cmds.refresh(suspend=False)
        except Exception:
            pass
        try:
            pm.undoInfo(closeChunk=True)
        except Exception:
            pass

        if hasattr(self, 'resizeSlider_2'):
            self.resizeSlider_2.setValue(0)
        self.translateSliderVal = 0

    def beginTranslate(self):
        # start a single undo chunk for the translate slider drag and suspend refresh
        self.translateSliderVal = self.resizeSlider_2.sliderPosition() if hasattr(self, 'resizeSlider_2') else 0
        try:
            pm.undoInfo(openChunk=True)
        except Exception:
            pass
        try:
            cmds.refresh(suspend=True)
        except Exception:
            pass

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

    def chainParent(self):
        sel = pm.selected()
        for i in sel:
            if i != sel[-1]:
                pm.parent(i, sel[sel.index(i)+1])

    def splitJoints(self):
        jntNum = self.splitJnt_spBox.value()
        fs.splitJoint(jntNum)

    def randomizeColor(self):
        sel = pm.selected()
        for i in sel:
            randCol = random.randint(1,31)
            fs.createControls().setColor(i,randCol)
def main():
    global ui
    try:
        ui.close()
    except:
        pass
    ui = MainWindow()
    # Show as dockable, but floating by default so it's not docked on first open.
    # User can dock it later via the Maya workspace control UI.
    try:
        ui.show(dockable=True, floating=True)
    except Exception:
        # Fallback to plain show() if the Maya mixin doesn't accept these args
        ui.show()
    ui.raise_()

if __name__ == '__main__':
    main()
