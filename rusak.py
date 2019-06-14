from __future__ import (division, # unicode_literals,
                        absolute_import)

import os
import sys
import RUSAK.fsLib as fs
from functools import partial

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide.QtCore import Qt, Slot, QMetaObject, QAbstractTableModel, QObject, SIGNAL
from PySide.QtUiTools import QUiLoader
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QIcon, QSizePolicy, QColor
from PySide.QtWebKit import QWebView, QWebPage


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

import RUSAK.rusakUI as py_ui
reload(py_ui)

import shiboken
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
        return shiboken.wrapInstance(long(ptr), QWidget)




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
        self.shp_Circle.clicked.connect(partial(self.createControl,'circle')))
        self.shp_Square.clicked.connect(partial(self.createControl,'square')))

    def createControl(self, shp):
        fs.createControls().crCtl(crvShp=shp,asJnt=False)


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
