from __future__ import (division, # unicode_literals,
                        absolute_import)

import os
import sys

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
