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
try:
    from PySide2.QtGui import QIcon, QColor
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QSizePolicy
except:
    from PySide6.QtGui import QIcon, QColor
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QSizePolicy
#from Qt.QtWebKit import QWebView, QWebPage
#from PySide2 import QtCore, QtGui



SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

sys.path.append(SCRIPT_DIRECTORY)


try:
    import shiboken2 as sb
except:
    import  shiboken6 as sb
import maya.OpenMayaUI as apiUI
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import json
try:
    from PySide2.QtWidgets import QLineEdit, QSpinBox, QDoubleSpinBox, QRadioButton, QCheckBox, QComboBox
    import rusakUI2 as rusakUI

except:
    from PySide6.QtWidgets import QLineEdit, QSpinBox, QDoubleSpinBox, QRadioButton, QCheckBox, QComboBox
    import rusakUI6 as rusakUI
importlib.reload(rusakUI)


def getMayaWindow():
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """
    ptr = apiUI.MQtUtil.mainWindow()
    if ptr is not None:
        return sb.wrapInstance(int(ptr), QWidget)




class MainWindow(MayaQWidgetDockableMixin, QWidget):

    def __init__(self, parent=getMayaWindow()):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = rusakUI.Ui_MainWindow()
        self.ui.setupUi(self)
        # restore saved widget defaults (best-effort)
        try:
            self._load_user_defaults()
        except Exception:
            pass
        self.resizeSliderVal = 0

        self.ui.shp_Circle.clicked.connect(partial(self.createControl,'circle'))
        self.ui.shp_Sphere.clicked.connect(partial(self.createControl,'sphere'))
        self.ui.shp_Square.clicked.connect(partial(self.createControl,'square'))
        self.ui.shp_Box.clicked.connect(partial(self.createControl,'box'))
        self.ui.shp_Cross.clicked.connect(partial(self.createControl,'cross'))
        self.ui.shp_Arrow.clicked.connect(partial(self.createControl,'arrowDouble'))
        self.ui.shp_CrossArrow.clicked.connect(partial(self.createControl,'crossArrow'))
        self.ui.shp_ArrowBent.clicked.connect(partial(self.createControl,'arrowDoubleCurve'))
        self.ui.shp_CrossArrowBent.clicked.connect(partial(self.createControl,'crossArrowBent'))
        self.ui.shp_Needle.clicked.connect(partial(self.createControl,'needleCircle'))
        self.ui.comboBox.addItems([i for i in fs.createControls().curveLib])
        self.ui.btn_createCtl.clicked.connect(self.createControl2)
        # color button wiring: map UI `col_<name>` buttons to their color index
        for idx in range(1,32):
            btn = getattr(self.ui, 'col_{}'.format(idx), None)
            if btn is not None:
                btn.clicked.connect(lambda checked=False, i=idx: self.changeColor(i))
        self.ui.zero_btn.clicked.connect(self.applyZero)
        self.ui.resizeSlider.sliderPressed.connect(self.beginScale)
        self.ui.resizeSlider.sliderMoved.connect(self.setScale)
        self.ui.resizeSlider.sliderReleased.connect(self.resetSlider)
        # translation controls
        # slider + step/spinbox: resizeSlider_2 and sizeStepSpinBox_2 in UI
        self.translateSliderVal = 0
        try:
            self.ui.resizeSlider_2.sliderPressed.connect(self.beginTranslate)
            self.ui.resizeSlider_2.sliderMoved.connect(self.setTranslate)
            self.ui.resizeSlider_2.sliderReleased.connect(self.resetTranslate)
        except Exception:
            # UI may not have the widgets in some layouts; fail silently
            pass
        self.ui.btn_rotateX.clicked.connect(self.setRotateX)
        self.ui.btn_rotateY.clicked.connect(self.setRotateY)
        self.ui.btn_rotateZ.clicked.connect(self.setRotateZ)
        self.ui.copyShp_Btn.clicked.connect(self.replaceShape)
        self.ui.parentAsChain_Btn.clicked.connect(self.chainParent)
        # self.ui.lineOneLiner.editingFinished.connect(self.runOneLiner)
        self.ui.splitJnt_Btn.clicked.connect(self.splitJoints)
        self.ui.colorRandom_btn.clicked.connect(self.randomizeColor)
        self.ui.crJnt_Btn.clicked.connect(lambda:mel.eval('JointTool'))
        self.ui.createSelJnt_Btn.clicked.connect(self.createJntOnSelect)
        self.ui.pointCons_chkBox.stateChanged.connect(self.uncheckParentConstraint)
        self.ui.orientCons_chkBox.stateChanged.connect(self.uncheckParentConstraint)
        self.ui.parConstraint_chkBox.stateChanged.connect(self.uncheckPointOrientConstraint)
        self.ui.displayJntAxis_Btn.clicked.connect(self.toggleJointAxis)
        self.ui.orientJnt_Btn.clicked.connect(lambda: self.orientJoints(helper=False))
        self.ui.orientJntHelper_Btn.clicked.connect(lambda: self.orientJoints(helper=True))
        self.ui.saveShp_btn.clicked.connect(self.saveSelectedShape)

        self.ui.asReplace.toggled.connect(self.ctrlSfxEnableDisable)
        self.ui.attrSet_Btn.clicked.connect(self.setChannelBoxTransforms)

        self.ui.attrTranslate_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrRotate_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrScale_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrTransX_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrTransY_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrTransZ_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrRotateX_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrRotateY_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrRotateZ_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrScaleX_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrScaleY_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrScaleZ_chkBox.toggled.connect(self.toggleChannelBoxTransforms)
        self.ui.attrVisibility_chkBox.toggled.connect(self.toggleChannelBoxTransforms)

        # custom attribute creation
        self.ui.customAttrList_cBox.clear()
        self.toggleEditAttrRadioButtons()
        self.ui.customAttrApply_Btn.clicked.connect(self.runCustomAttributeFunction)
        self.ui.customAttrResetVal_Btn.clicked.connect(self.resetCustomAttributeFields)
        self.ui.customAttrLoad_Btn.clicked.connect(self.loadCustomAttrOnSelection)
        self.ui.customAttrEdit_rBtn.toggled.connect(self.toggleEditAttrRadioButtons)
        self.ui.customAttrList_cBox.currentTextChanged.connect(self.loadSelectedCustomAttr)

        #temp disable grpBoxes
        self.ui.oneLiner_grpBox.setEnabled(False)
        self.ui.mirrorTransforms_grpBox.setEnabled(False)
        self.ui.spawnAvgLoc_grpBox.setEnabled(False)

    def ctrlSfxEnableDisable(self):
        if self.ui.asReplace.isChecked():
            self.ui.createCtlSfx_lineEdit.setEnabled(False)
        else:
            self.ui.createCtlSfx_lineEdit.setEnabled(True)
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
            spawn_mult = float(self.ui.spawnMult_spBox.value())
        except Exception:
            spawn_mult = 1.0

        suffix = self.ui.createCtlSfx_lineEdit.text()
        # print(spawn_mult)
        if slt == []:
            dummyGrp = pm.group(em=True,w=True)
            if self.ui.asJnt.isChecked():
                crv = fs.createControls().crCtl(dummyGrp,crvShp=shp,asJnt=True)
                crvs.append(crv)
                crv.rename(suffix)
            elif self.ui.asReplace.isChecked():
                crv = fs.createControls().crCtl(dummyGrp, crvShp=shp,asReplace=True)
                crvs.append(crv)

            else:
                crv = fs.createControls().crCtl(dummyGrp,crvShp=shp,asJnt=False)
                crvs.append(crv)
                crv.rename(suffix)
           
            pm.delete(dummyGrp)
        else:
            if self.ui.spawnAtCenter_rBtn.isChecked():
                atCenter=True
            else:
                atCenter=False

            for i in slt:
                if self.ui.asJnt.isChecked():
                    crv = fs.createControls().crCtl(i,crvShp=shp,asJnt=True,atCenter=atCenter)
                    crvs.append(crv)
                    crv.rename(i+"_"+suffix)
                elif self.ui.asReplace.isChecked():
                    crv = fs.createControls().crCtl(i, crvShp=shp,asReplace=True,atCenter=atCenter)
                    crvs.append(crv)

                else:
                    crv = fs.createControls().crCtl(i,crvShp=shp,asJnt=False,atCenter=atCenter)
                    crvs.append(crv)
                    crv.rename(i+"_"+suffix)

        try:
            pm.select(crvs)
            if spawn_mult != 1.0:
                print("scaling by:", spawn_mult)
                fs.transformShapes(s=1, rx=1,ry=1,rz=1,scaleVal=spawn_mult, objSpace=True)
        except:
            pass
            
        pm.undoInfo(closeChunk=True)

    def createControl2(self):
        shp1 = self.ui.comboBox.currentText()
        self.createControl(shp1)

    def changeColor(self, color):
        print("set color to:", color)
        slt = pm.selected()
        for i in slt:
            fs.createControls().setColor(i,color)

    def applyZero(self):
        prefix = self.ui.prefix_rBtn.isChecked()
        fs.zeroTrans(self.ui.suffix_edit.text(),self.ui.keepSuffix_chkBox.isChecked(),prefix)

    def setScale(self):
        # read axis flags as ints (faster/clearer)
        sx = 1 if self.ui.sizeX.isChecked() else 0
        sy = 1 if self.ui.sizeY.isChecked() else 0
        sz = 1 if self.ui.sizeZ.isChecked() else 0

        sliderValue = self.ui.resizeSlider.sliderPosition()
        stepValue = float(self.ui.sizeStepSpinBox.value())

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
        objSpace = self.ui.spTransform.isChecked()

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

        self.ui.resizeSlider.setValue(0)
        self.resizeSliderVal = 0

    def beginScale(self):
        # start a single undo chunk for the slider drag and suspend refresh
        self.resizeSliderVal = self.ui.resizeSlider.sliderPosition()
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
        tx_flag = 1 if getattr(self.ui, 'transX_chkBox', None) and self.ui.transX_chkBox.isChecked() else 0
        ty_flag = 1 if getattr(self.ui, 'transY_chkBox', None) and self.ui.transY_chkBox.isChecked() else 0
        tz_flag = 1 if getattr(self.ui, 'transZ_chkBox', None) and self.ui.transZ_chkBox.isChecked() else 0

        sliderValue = self.ui.resizeSlider_2.sliderPosition() if hasattr(self.ui, 'resizeSlider_2') else 0
        stepValue = float(self.ui.sizeStepSpinBox_2.value()) if hasattr(self.ui, 'sizeStepSpinBox_2') else 1.0

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

        if hasattr(self.ui, 'resizeSlider_2'):
            self.ui.resizeSlider_2.setValue(0)
        self.translateSliderVal = 0

    def beginTranslate(self):
        # start a single undo chunk for the translate slider drag and suspend refresh
        self.translateSliderVal = self.ui.resizeSlider_2.sliderPosition() if hasattr(self.ui, 'resizeSlider_2') else 0
        try:
            pm.undoInfo(openChunk=True)
        except Exception:
            pass
        try:
            cmds.refresh(suspend=True)
        except Exception:
            pass

    def setRotateX(self):
        angle = self.ui.angle_box.value()
        if self.ui.spTransform.isChecked():
            fs.transformShapes(r=1,rx=angle,objSpace=True)
        else:
            fs.transformShapes(r=1,rx=angle,objSpace=False)

    def setRotateY(self):
        angle = self.ui.angle_box.value()
        if self.ui.spTransform.isChecked():
            fs.transformShapes(r=1,ry=angle,objSpace=True)
        else:
            fs.transformShapes(r=1,ry=angle,objSpace=False)

    def setRotateZ(self):
        angle = self.ui.angle_box.value()
        if self.ui.spTransform.isChecked():
            fs.transformShapes(r=1,rz=angle,objSpace=True)
        else:
            fs.transformShapes(r=1,rz=angle,objSpace=False)

    def printText(self):
        print(self.lineOneLiner.text())

    def chainParent(self):
        sel = pm.selected()
        for i in sel:
            if i != sel[-1]:
                pm.parent(i, sel[sel.index(i)+1])

    def splitJoints(self):
        jntNum = self.ui.splitJnt_spBox.value()
        fs.splitJoint(jntNum)

    def _defaults_path(self):
        # Use %USERPROFILE%/Documents/maya/scripts as the defaults folder
        up = os.environ.get('USERPROFILE') or os.path.expanduser('~')
        folder = os.path.join(up, 'Documents', 'maya', 'scripts')
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
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                print("[rusak] saved user defaults to:", path, "(", len(data), "items)")
            except Exception as e:
                print("[rusak] failed to save user defaults:", e)
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
        except Exception as e:
            print("[rusak] failed to read defaults file:", e)
            return

        try:
            print("[rusak] loading user defaults from:", path, "(", len(data), "items)")
            for name, val in data.items():
                widget = getattr(self.ui, name, None)
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
        except Exception as e:
            print("[rusak] error applying defaults:", e)
            pass

    def closeEvent(self, event):
        # print("[rusak] closeEvent triggered")
        try:
            self._save_user_defaults()
        except Exception as e:
            print("[rusak] _save_user_defaults error:", e)
            pass
        try:
            super(MainWindow, self).closeEvent(event)
        except Exception:
            QWidget.closeEvent(self, event)

    def hideEvent(self, event):
        """Fallback save when the widget is hidden (common for dockable windows)."""
        # print("[rusak] hideEvent triggered")
        try:
            self._save_user_defaults()
        except Exception as e:
            print("[rusak] _save_user_defaults error (hideEvent):", e)
            pass
        try:
            super(MainWindow, self).hideEvent(event)
        except Exception:
            QWidget.hideEvent(self, event)

    def randomizeColor(self):
        sel = pm.selected()
        for i in sel:
            randCol = random.randint(1,31)
            fs.createControls().setColor(i,randCol)

    def createJntOnSelect(self):
        sel = pm.selected()
        sfx = self.ui.jntSuffixName_lineEdit.text()
        pac = self.ui.parConstraint_chkBox.isChecked()
        sc = self.ui.scaleCons_chkBox.isChecked()
        oc = self.ui.orientCons_chkBox.isChecked()
        poc = self.ui.pointCons_chkBox.isChecked()
        chain = self.ui.chainJnt_chkBox.isChecked()
        fs.createJntOnSel(sel,pac,sc,oc,poc,sfx,chain)
    def uncheckParentConstraint(self):
        if self.ui.pointCons_chkBox.isChecked() or self.ui.orientCons_chkBox.isChecked():
            self.ui.parConstraint_chkBox.setChecked(False)
    def uncheckPointOrientConstraint(self):
        if self.ui.parConstraint_chkBox.isChecked():
            self.ui.pointCons_chkBox.setChecked(False)
            self.ui.orientCons_chkBox.setChecked(False)

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
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems([i for i in fs.createControls().curveLib])
    def orientJoints(self,helper=False):
        if self.ui.orientPAxisX_rBtn.isChecked():
            primeAxis = 'X'
        elif self.ui.orientPAxisY_rBtn.isChecked():
            primeAxis = 'Y'
        else:
            primeAxis = 'Z'

        if self.ui.orientSecAxisX_rBtn.isChecked():
            secondaryAxis = 'X'
        elif self.ui.orientSecAxisY_rBtn.isChecked():
            secondaryAxis = 'Y'
        else:
            secondaryAxis = 'Z'
        if self.ui.orientWorldAxisX_rBtn.isChecked():
            worldAxis = 'X'
        elif self.ui.orientWorldAxisY_rBtn.isChecked():
            worldAxis = 'Y'
        else:
            worldAxis = 'Z'
        primeNegative = self.ui.orientPrimeNeg_chkBox.isChecked()
        secondaryNegative = self.ui.orientSecNeg_chkBox.isChecked()
        worldNegative = self.ui.orientWorldNeg_chkBox.isChecked()
        children = self.ui.orientChd_chkBox.isChecked()
        fs.orientJoints(primeAxis=primeAxis,
                        secondaryAxis=secondaryAxis,
                        worldAxis=worldAxis,
                        primeNegative=primeNegative,
                        secondaryNegative=secondaryNegative,
                        worldNegative=worldNegative,
                        children=children,helper=helper)
    def toggleJointAxis(self):
        childs = self.ui.axisChd_chkBox.isChecked()
        fs.toggleJointAxis(childs)
        
    def setChannelBoxTransforms(self):
        translates = self.ui.attrTranslate_chkBox.isChecked()
        rotates = self.ui.attrRotate_chkBox.isChecked()
        scales = self.ui.attrScale_chkBox.isChecked()

        if translates:
            translateX = self.ui.attrTransX_chkBox.isChecked()
            translateY = self.ui.attrTransY_chkBox.isChecked()
            translateZ = self.ui.attrTransZ_chkBox.isChecked()
        else:
            translateX = False
            translateY = False
            translateZ = False
        if rotates:
            rotateX = self.ui.attrRotateX_chkBox.isChecked()
            rotateY = self.ui.attrRotateY_chkBox.isChecked()
            rotateZ = self.ui.attrRotateZ_chkBox.isChecked()
        else:
            rotateX = False
            rotateY = False
            rotateZ = False
        if scales:
            scaleX = self.ui.attrScaleX_chkBox.isChecked()
            scaleY = self.ui.attrScaleY_chkBox.isChecked()
            scaleZ = self.ui.attrScaleZ_chkBox.isChecked()
        else:
            scaleX = False
            scaleY = False
            scaleZ = False

        slt = pm.selected()
        for i in slt:
            attrsDict = {
                'translateX': translateX,
                'translateY': translateY,
                'translateZ': translateZ,
                'rotateX': rotateX,
                'rotateY': rotateY,
                'rotateZ': rotateZ,
                'scaleX': scaleX,
                'scaleY': scaleY,
                'scaleZ': scaleZ,
                'visibility': self.ui.attrVisibility_chkBox.isChecked(),
                }

            for atr,value in attrsDict.items():
                # print(atr,value)
                try:
                    atrNode = pm.PyNode(f'{i}.{atr}')
                    # atrNode.set(lock=(not value))
                    # atrNode.set(cb=value)
                    pm.setAttr(atrNode, e=True, keyable=value, channelBox=value,lock=not value)
                    atrNode.set(keyable=value)
                except:
                    pass
    def toggleChannelBoxTransforms(self):
        if self.ui.attrAuto_chkBox.isChecked():
            self.setChannelBoxTransforms()

    def runCustomAttributeFunction(self):
        if self.ui.customAttrEdit_rBtn.isChecked():
            self.editCustomAttribute()
        else:
            self.createCustomAttribute()
    def editCustomAttribute(self):
        attrName = self.ui.customAttrList_cBox.currentText()
        if not attrName:
            pm.warning("Please select an attribute to edit")
            return
        slt = pm.selected()
        for i in slt:
            try:
                attrFull = f'{i}.{attrName}'
                atrType = pm.getAttr(attrFull, type=True)
                # print("attrFull:", attrFull)
                # print("atrType:", atrType)
                if not pm.attributeQuery(attrName, node=i, exists=True):
                    pm.warning(f"Attribute '{attrName}' does not exist on '{i}'")
                    continue
                # get new name
                newAttrName = self.ui.customAttrName_lineEdit.text()
                if newAttrName and newAttrName != attrName:
                    pm.renameAttr(attrFull, newAttrName)
                    attrFull = f'{i}.{newAttrName}'
                    attrName = newAttrName  # update for subsequent uses
                # get new nice name
                attrNiceName = self.ui.customAttrNiceName_lineEdit.text()
                if attrNiceName and attrNiceName != pm.attributeQuery(attrName, node=i, niceName=True):
                    pm.addAttr(attrFull, e=True, niceName=attrNiceName)
                pm.refreshEditorTemplates()
                if atrType in ['long','double']:
                    # get min/max
                    if self.ui.customAttrMin_chkBox.isChecked():
                        minVal = self.ui.customAttrMinVal_spinBox.value()
                        pm.addAttr(attrFull, e=True, hasMinValue=True)
                        pm.addAttr(attrFull, e=True, minValue=minVal)
                    else:
                        pm.addAttr(attrFull, e=True, hasMinValue=False)
                    if self.ui.customAttrMax_chkBox.isChecked():
                        maxVal = self.ui.customAttrMaxVal_spinBox.value()
                        pm.addAttr(attrFull, e=True, hasMaxValue=True)
                        pm.addAttr(attrFull, e=True, maxValue=maxVal)
                    else:
                        pm.addAttr(attrFull, e=True, hasMaxValue=False)
                    # get new default value
                    newDefaultValue = self.ui.customAttrValue_lineEdit.text()
                    if newDefaultValue:
                        try:
                            if atrType == 'long':
                                intVal = int(newDefaultValue)
                                pm.setAttr(attrFull, intVal)
                            elif atrType == 'double':
                                floatVal = float(newDefaultValue)
                                pm.setAttr(attrFull, floatVal)
                        except:
                            pass
                elif atrType == 'enum':
                    # get enum names from line edit, split by comma
                    enumNames = self.ui.customAttrEnumNames_lineEdit.text()
                    # print("enumNames:", enumNames)
                    enumNamesList = [name.strip() for name in enumNames.split(',') if name.strip()]
                    # print("enumNamesList:", enumNamesList)
                    if enumNamesList:
                        pm.addAttr(attrFull, e=True,en=':'.join(enumNamesList))
            except Exception as e:
                print(f"Error editing attribute: {e}")                

        if not self.ui.customAttrKeepVal_chkBox.isChecked():
            self.resetCustomAttributeFields()
    def createCustomAttribute(self):
        attrName = self.ui.customAttrName_lineEdit.text()
        attrNiceName = self.ui.customAttrNiceName_lineEdit.text()
        hasMin = self.ui.customAttrMin_chkBox.isChecked()
        hasMax = self.ui.customAttrMax_chkBox.isChecked()
        minVal = self.ui.customAttrMinVal_spinBox.value()
        maxVal = self.ui.customAttrMaxVal_spinBox.value()
        attrValue = self.ui.customAttrValue_lineEdit.text()

        #get attribute type
        if self.ui.customAttrInt_rBtn.isChecked():
            attrType = 'long'
        elif self.ui.customAttrFloat_rBtn.isChecked():
            attrType = 'double'
        elif self.ui.customAttrBool_rBtn.isChecked():
            attrType = 'bool'
        elif self.ui.customAttrEnum_rBtn.isChecked():
            attrType = 'enum'
        elif self.ui.customAttrString_rBtn.isChecked():
            attrType = 'string'
        elif self.ui.customAttrVector_rBtn.isChecked():
            attrType = 'double3'

        # get attribute keyable, non-keyable, channel box
        if self.ui.customAttrKeyable_rBtn.isChecked():
            isKeyable = True
        else:
            isKeyable = False
        if self.ui.customAttrHidden_rBtn.isChecked():
            hidden = True
        else:
            hidden = False

        slt = pm.selected()
        for i in slt:
            try:
                keysDict = {
                    'longName': attrName,
                    'attributeType': attrType,
                    'keyable': isKeyable,
                }
                if attrNiceName:
                    keysDict['niceName'] = attrNiceName
                if attrType == 'enum':
                    # get enum names from line edit, split by comma
                    enumNames = self.ui.customAttrEnumNames_lineEdit.text()
                    enumNamesList = [name.strip() for name in enumNames.split(',') if name.strip()]
                    keysDict['enumName'] = ':'.join(enumNamesList)
                if attrType == 'long':
                    if attrValue:
                        try:
                            intVal = int(attrValue)
                            keysDict['defaultValue'] = intVal
                        except:
                            pass
                elif attrType == 'double':
                    if attrValue:
                        try:
                            floatVal = float(attrValue)
                            keysDict['defaultValue'] = floatVal
                        except:
                            pass
                elif attrType == 'bool':
                    if attrValue != 'False' and attrValue != 'false' and attrValue != '0' and attrValue != '':
                        boolVal = True
                    else:
                        boolVal = False
                    keysDict['defaultValue'] = boolVal
                if attrType in ['long','double']:
                    if hasMin:
                        keysDict['hasMinValue'] = True
                        keysDict['minValue'] = minVal
                    if hasMax:
                        keysDict['hasMaxValue'] = True
                        keysDict['maxValue'] = maxVal
                pm.addAttr(i, **keysDict)
                newAttr = f'{i}.{attrName}'
                print("newAttr:", newAttr)
                print("Hidden:", hidden)
                print("isKeyable:", isKeyable)
                if hidden:
                    pm.setAttr(newAttr, lock=True, keyable=False, channelBox=False)
                if not isKeyable and not hidden:
                    pm.setAttr(newAttr, channelBox=True)

            except Exception as e:
                print(f"Error adding attribute: {e}")

        if not self.ui.customAttrKeepVal_chkBox.isChecked():
            self.resetCustomAttributeFields()
    def resetCustomAttributeFields(self):
        self.ui.customAttrName_lineEdit.setText("")
        self.ui.customAttrNiceName_lineEdit.setText("")
        self.ui.customAttrMin_chkBox.setChecked(False)
        self.ui.customAttrMax_chkBox.setChecked(False)
        self.ui.customAttrMinVal_spinBox.setValue(0)
        self.ui.customAttrMaxVal_spinBox.setValue(1)
        self.ui.customAttrFloat_rBtn.setChecked(True)
        self.ui.customAttrKeyable_rBtn.setChecked(True)
        self.ui.customAttrEnumNames_lineEdit.setText("")

    def loadCustomAttrOnSelection(self):
        #get custom attributes available from all selected object
        slt = pm.selected()
        customAttrsLs = []
        for i in slt:
            allAttrs = pm.listAttr(i, userDefined=True)
            customAttrsLs.append(allAttrs)
        #get the intersection of all custom attributes
        customAttrs = set(customAttrsLs[0]) if customAttrsLs else set()
        for attrs in customAttrsLs[1:]:
            customAttrs &= set(attrs)
        customAttrs = list(customAttrs)

        self.ui.customAttrList_cBox.clear()
        self.ui.customAttrList_cBox.addItems(customAttrs)
        return customAttrs
    
    def toggleEditAttrRadioButtons(self):
        if self.ui.customAttrEdit_rBtn.isChecked():
            self.ui.customAttrApply_Btn.setText("Edit Attribute")
            self.ui.customAttrType_grpBox.setEnabled(False)
        else:
            self.ui.customAttrApply_Btn.setText("Create Attribute")
            self.ui.customAttrType_grpBox.setEnabled(True)

    def loadSelectedCustomAttr(self):
        attrName = self.ui.customAttrList_cBox.currentText()
        if attrName:
            slt = pm.selected()
            if not slt:
                return
            firstObj = slt[0]
            if not pm.attributeQuery(attrName, node=firstObj, exists=True):
                pm.warning(f"Attribute '{attrName}' does not exist on the first selected object.")
                return
            attrType = pm.getAttr(f'{firstObj}.{attrName}', type=True)
            self.ui.customAttrName_lineEdit.setText(attrName)
            self.ui.customAttrNiceName_lineEdit.setText(pm.attributeQuery(attrName, node=firstObj, niceName=True))
            if attrType == 'long':
                self.ui.customAttrInt_rBtn.setChecked(True)
            elif attrType == 'double':
                self.ui.customAttrFloat_rBtn.setChecked(True)
            elif attrType == 'bool':
                self.ui.customAttrBool_rBtn.setChecked(True)
            elif attrType == 'enum':
                self.ui.customAttrEnum_rBtn.setChecked(True)
                enumNames = pm.attributeQuery(attrName, node=firstObj, le=True)[0]
                self.ui.customAttrEnumNames_lineEdit.setText(enumNames.replace(':', ', '))
            elif attrType == 'string':
                self.ui.customAttrString_rBtn.setChecked(True)
            elif attrType == 'double3':
                self.ui.customAttrVector_rBtn.setChecked(True)
            # get default value
            try:
                defaultValue = pm.getAttr(f'{firstObj}.{attrName}')
                self.ui.customAttrValue_lineEdit.setText(str(defaultValue))
            except Exception:
                self.ui.customAttrValue_lineEdit.setText("")
            if attrType in ['long','double']:
                hasMin = pm.attributeQuery(attrName, node=firstObj, mne=True)
                hasMax = pm.attributeQuery(attrName, node=firstObj, mxe=True)
                self.ui.customAttrMin_chkBox.setChecked(hasMin)
                self.ui.customAttrMax_chkBox.setChecked(hasMax)
                if hasMin:
                    minVal = pm.attributeQuery(attrName, node=firstObj, min=True)
                    if minVal:
                        minVal = float(minVal[0])
                    self.ui.customAttrMinVal_spinBox.setValue(minVal)
                if hasMax:
                    maxVal = pm.attributeQuery(attrName, node=firstObj, max=True)
                    if maxVal:
                        maxVal = float(maxVal[0])
                    self.ui.customAttrMaxVal_spinBox.setValue(maxVal)

        
def main():
    global ui
    try:
        ui.close()
    except:
        pass
    ui = MainWindow()
    # Show as dockable, but floating by default so it's not docked on first open.
    # User can dock it later via the Maya workspace control UI.
    # try:
    #     ui.show(dockable=True, floating=True)
    # except Exception:
    #     # Fallback to plain show() if the Maya mixin doesn't accept these args
    #     ui.show()
    ui.show(dockable=True, floating=True)
    ui.raise_()

if __name__ == '__main__':
    main()
