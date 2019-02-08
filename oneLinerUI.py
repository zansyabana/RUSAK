import pymel.core as pm
from fsfunclib import oneLiner

class oneLinerWindow(object):

    windowName = "OneLiner"

    def show(self):

        if pm.window(self.windowName, q=True, exists=True):
            pm.deleteUI(self.windowName)
            pm.windowPref(self.windowName, remove=True)
        pm.window(self.windowName, s=True, w=300, h=100, rtf=False)

        self.buildUI()

        pm.showWindow()

    def buildUI(self):
        toolTip = 'Character replacement symbols:' \
                  '\n! = old name' \
                  '\n# = numbering based on selection, add more # for more digits' \
                  '\n\nFind and replace method:' \
                  '\n"oldName">"newName" (without quotes)' \
                  '\n\nRemove first or last character(s):' \
                  '\n-(amount of characters to remove) = removes specific amounts of characters from last character'\
                  '\n+(amount of characters to remove) = removes specific amounts of characters from first character' \
                  '\n\nAdd these symbols at the end to change the selection method:' \
                  '\n/s = selected only (this is default, you dont have to type this)' \
                  '\n/h = add items from all hierarchy descendants of selected items' \
                  '\n/a = all objects in scene'

        column = pm.columnLayout(cal='center', adj=True)
        pm.separator(h=15, style='none')
        self.rnmInput = pm.textField(ec=self.runFunc, aie=True, w=200, ann=toolTip)
        pm.separator(h=10, style='none')
        pm.text(label='Hover mouse to text field for tool tips')
        pm.text(label='by Fauzan Syabana')
        pm.separator(h=10, style='none')

    def runFunc(self,*args):
        self.rnmQ = pm.textField(self.rnmInput, text=True,q=True)
        oneLiner(self.rnmQ)