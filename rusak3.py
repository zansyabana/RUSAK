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
import maya.mel as mel
import json
from PySide2.QtWidgets import QLineEdit, QSpinBox, QDoubleSpinBox, QRadioButton, QCheckBox, QComboBox



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
        # restore saved widget defaults (best-effort)
        try:
            self._load_user_defaults()
        except Exception:
            pass
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
        self.crJnt_Btn.clicked.connect(lambda:mel.eval('JointTool'))
        self.createSelJnt_Btn.clicked.connect(self.createJntOnSelect)
        self.pointCons_chkBox.stateChanged.connect(self.uncheckParentConstraint)
        self.orientCons_chkBox.stateChanged.connect(self.uncheckParentConstraint)
        self.parConstraint_chkBox.stateChanged.connect(self.uncheckPointOrientConstraint)
        self.displayJntAxis_Btn.clicked.connect(fs.toggleJointAxis)
        self.orientJnt_Btn.clicked.connect(fs.orientJoints)
        self.saveShp_btn.clicked.connect(self.saveSelectedShape)

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

    def _defaults_path(self):
        up = os.environ.get('USERPROFILE') or os.path.expanduser('~')
        folder = os.path.join(up, 'maya', 'scripts')
        try:
            os.makedirs(folder, exist_ok=True)
        except Exception:
            pass
        return os.path.join(folder, 'rusakUserDefaults.json')

    def _save_user_defaults(self):
        """Save QLineEdit, QSpinBox/QDoubleSpinBox, QRadioButton, QCheckBox and QComboBox values to JSON."""
        data = {}
        try:
            for w in self.findChildren(QLineEdit):
                name = w.objectName()
                if name:
                    data[name] = w.text()
            for w in self.findChildren(QSpinBox):
                name = w.objectName()
                if name:
                    data[name] = w.value()
            for w in self.findChildren(QDoubleSpinBox):
                name = w.objectName()
                if name:
                    data[name] = w.value()
            for w in self.findChildren(QRadioButton):
                name = w.objectName()
                if name:
                    data[name] = w.isChecked()
            for w in self.findChildren(QCheckBox):
                name = w.objectName()
                if name:
                    data[name] = w.isChecked()
            for w in self.findChildren(QComboBox):
                name = w.objectName()
                if name:
                    data[name] = w.currentIndex()

            path = self._defaults_path()
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        except Exception:
            pass

    def _load_user_defaults(self):
        """Load defaults from JSON and apply to widgets if present."""
        path = self._defaults_path()
        if not os.path.exists(path):
            return
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            return

        try:
            for name, val in data.items():
                widget = getattr(self, name, None)
                if widget is None:
                    # try findChild by object name (any QWidget)
                    try:
                        widget = self.findChild(QWidget, name)
                    except Exception:
                        widget = None
                if widget is None:
                    continue
                # apply value based on widget type
                try:
                    if isinstance(widget, QLineEdit):
                        widget.setText(str(val))
                    elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                        widget.setValue(val)
                    elif isinstance(widget, (QRadioButton, QCheckBox)):
                        widget.setChecked(bool(val))
                    elif isinstance(widget, QComboBox):
                        idx = int(val)
                        if 0 <= idx < widget.count():
                            widget.setCurrentIndex(idx)
                except Exception:
                    pass
        except Exception:
            pass

    def closeEvent(self, event):
        try:
            self._save_user_defaults()
        except Exception:
            pass
        try:
            super(MainWindow, self).closeEvent(event)
        except Exception:
            QWidget.closeEvent(self, event)

    def randomizeColor(self):
        sel = pm.selected()
        for i in sel:
            randCol = random.randint(1,31)
            fs.createControls().setColor(i,randCol)

    def createJntOnSelect(self):
        sel = pm.selected()
        sfx = self.jntSuffixName_lineEdit.text()
        pac = self.parConstraint_chkBox.isChecked()
        sc = self.scaleCons_chkBox.isChecked()
        oc = self.orientCons_chkBox.isChecked()
        poc = self.pointCons_chkBox.isChecked()
        chain = self.chainJnt_chkBox.isChecked()
        fs.createJntOnSel(sel,pac,sc,oc,poc,sfx,chain)
    def uncheckParentConstraint(self):
        if self.pointCons_chkBox.isChecked() or self.orientCons_chkBox.isChecked():
            self.parConstraint_chkBox.setChecked(False)
    def uncheckPointOrientConstraint(self):
        if self.parConstraint_chkBox.isChecked():
            self.pointCons_chkBox.setChecked(False)
            self.orientCons_chkBox.setChecked(False)

    def saveSelectedShape(self):
        slt = pm.selected(type='transform')
        slt = [i for i in slt if i.getShape() and isinstance(i.getShape(), pm.nodetypes.NurbsCurve)]
        if slt == []:
            pm.warning("Please select a curve shape to save")
            return
        else:
            shp = slt[-1]
            #open a dialog to get the name
            # name, ok = fs.simpleInputDialog.getText(self, "Save Curve Shape", "Enter name for the curve shape:")
            resulf = pm.promptDialog(
                title='Save Curve Shape',
                message='Enter name for the curve shape:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
            )
            if resulf == 'OK':
                name = pm.promptDialog(query=True, text=True)
                ok = True
            if ok and name:
                savePath = Path(os.getenv('USERPROFILE') or os.path.expanduser('~'))/'Documents'/'maya'/'scripts'/'rusakUserCurveLib.json'
                if not savePath.exists():
                    savePath.parent.mkdir(parents=True, exist_ok=True)
                    #create empty json file
                    with open(savePath.as_posix(), 'w') as f:
                        json.dump({}, f)
                fs.createControls().saveCtl(name,obj=shp,customPath=savePath.as_posix())
                pm.informBox("Save Curve Shape", "Curve shape '{}' saved successfully.".format(name))
            self.comboBox.clear()
            self.comboBox.addItems([i for i in fs.createControls().curveLib])
        
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
