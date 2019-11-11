from __future__ import (division, # unicode_literals,
                        absolute_import)

import os
import sys
import RUSAK.fsLib as fs
reload(fs)
from functools import partial

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
# from Qt.QtCore import Qt, Slot, QMetaObject, QAbstractTableModel, QObject, SIGNAL
# from Qt.QtUiTools import QUiLoader
from Qt import QtGui, QtWidgets
from Qt.QtGui import QIcon, QColor
from Qt.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QSizePolicy
# from Qt.QtWebKit import QWebView, QWebPage


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

import RUSAK.rusakUI as py_ui
reload(py_ui)
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
        return sb.wrapInstance(long(ptr), QWidget)




class MainWindow(MayaQWidgetDockableMixin, QMainWindow, py_ui.Ui_MainWindow):

    def __init__(self, parent=getMayaWindow()):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
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
        # self.shp_Arrow.clicked.connect(partial(self.createControl,'square'))
        self.shp_CrossArrow.clicked.connect(partial(self.createControl,'crossArrow'))
        # self.shp_ArrowBent.clicked.connect(partial(self.createControl,'square'))
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

    def createControl(self, shp):
        if self.asJnt.isChecked():
            fs.createControls().crCtl(crvShp=shp,asJnt=True)
        else:
            fs.createControls().crCtl(crvShp=shp,asJnt=False)
    def createControl2(self):
        shp = self.comboBox.currentText()
        if self.asJnt.isChecked():
            fs.createControls().crCtl(crvShp=shp,asJnt=True)
        else:
            fs.createControls().crCtl(crvShp=shp,asJnt=False)

    def changeColor(self, color):
        slt = pm.selected()
        for i in slt:
            fs.createControls().setColor(i,color)

    def applyZero(self):
        fs.zeroTrans(self.suffix_edit.text(),self.suffix_keep.isChecked())


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
