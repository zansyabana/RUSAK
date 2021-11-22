#---------written by:----------------------
#-------Fauzan Syabana---------------------
#------zansyabana@gmail.com----------------
#Licensed under MIT License

import pymel.core as pm
import maya.cmds as mc
import json
import os

from pymel.core.system import undo
from pymel.core.windows import falloffCurve


class createControls():
    def __init__(self):
        self.fileName = os.path.realpath(__file__)
        self.curveLibPath = self.fileName.replace(os.path.basename(__file__), 'FScurveLibrary.json')
        self.curveLib_file = open(self.curveLibPath)
        self.curveLib = json.load(self.curveLib_file)
        self.curveLib_file.close()

    def align(self,tgt, src):
        trans = pm.xform(str(src) + ".scalePivot", q=True, ws=True, t=True)
        rot = pm.xform(src, q=True, ws=True, ro=True)
        transX = trans[0]
        transY = trans[1]
        transZ = trans[2]
        pm.xform(tgt, ws=True, t=trans)
        pm.xform(tgt, ws=True, ro=rot)

    def crCtl(self, obj, crvShp='circle', asJnt=False, asReplace=False):
        pm.undoInfo(openChunk=True)
            # Defines to convert the controller as shaped joint
        if asJnt == True:
            crv = eval(self.curveLib[crvShp])
            jnt = pm.joint()
            pm.parent(jnt,w=True)
            shp = crv.getShape()
            pm.parent(shp, jnt, s=True, r=True)
            shp.rename(jnt + 'Shape')
            jnt.drawStyle.set(2)
            pm.delete(crv)
            crv = jnt
            


        elif asReplace == True:
            crv = eval(self.curveLib[crvShp])
            curShp = obj.getShape()
            pm.delete(curShp)
            pm.parent(obj,r=True)
            shp = crv.getShape()
            pm.parent(shp, obj, s=True, r=True)
            shp.rename(obj+"Shape")   
            pm.delete(crv)
            crv = obj
            
        else:
            crv = eval(self.curveLib[crvShp])
            
            
        try:
            self.align(crv, obj)
        except:
            pass

        pm.undoInfo(closeChunk=True)
        return crv

    def saveCtl(self,name):

        obj = pm.selected()[0]
        cvPoints = []
        knots = obj.getKnots()
        max = obj.spans.get()
        deg = obj.d.get()
        cvs = pm.getAttr(obj.cp,s=1)
        form = obj.f.get()
        if form == 2:
            per = True
        else:
            per = False
        for i in range(0, cvs):
            pointXYZ = obj.controlPoints[i].get()
            pointX = pointXYZ[0]
            pointY = pointXYZ[1]
            pointZ = pointXYZ[2]
            points = (pointX, pointY, pointZ)
            cvPoints.append(points)
            # knot = obj.getKnot(i)
            # knots.append(knot)

        oldDataFile = open(self.curveLibPath, 'r')
        crvShapeInfo = json.load(oldDataFile)
        oldDataFile.close()
        crvShapeInfo[name] = 'pm.curve(p={}, d={}, k={},per={})'.format(cvPoints, deg, knots,per)
        # print crvShapeInfo
        with open(self.curveLibPath, mode='w') as insertData:
            json.dump(crvShapeInfo,insertData,indent=4)
            insertData.close()

    def setColor(self,obj, CCode):
        pm.undoInfo(openChunk=True)
        obj.getShape().overrideEnabled.set(1)
        obj.getShape().overrideColor.set(CCode)
        pm.undoInfo(closeChunk=True)

def zeroTrans(sfx, keep=True,*args):
    pm.undoInfo(openChunk=True)
    selected = mc.ls(sl=True)

    for i in selected:
        if keep:
            mc.select(i)
            mc.group(name=i + sfx)
            select02 = mc.ls(i, i + sfx)
            mc.copyAttr(select02[0], select02[1], v=True)
            mc.move(0, 0, 0, i, ls=True)
            mc.rotate(0, 0, 0, i, a=True)
            mc.scale(1, 1, 1, i)
        else:
            oldSfx = "_"+i.split('_')[-1]
            mc.select(i)
            grp = mc.group(name=i.replace(oldSfx,sfx))
            select02 = mc.ls(i, grp)
            mc.copyAttr(select02[0], select02[1], v=True)
            mc.move(0, 0, 0, i, ls=True)
            mc.rotate(0, 0, 0, i, a=True)
            mc.scale(1, 1, 1, i)
    pm.undoInfo(closeChunk=True)

def transformShapes(t=0,r=0,s=0, rx=0,ry=0,rz=0, scaleVal=0, objSpace=True, *args):
    pm.undoInfo(openChunk=True)
    obj = pm.selected()
    for i in obj:
        max = i.spans.get()
        deg = i.d.get()
        cvss = max+deg
        cvPosX = []
        cvPosY = []
        cvPosZ = []

        if i.f.get() == 2:
            endRange = max-1
        else:
            endRange =  cvss-1
        for cvs in range(0,endRange):
            cv = i.cv[cvs]
            pos = pm.pointPosition(cv,w=True)
            cvPosX.append(pos[0])
            cvPosY.append(pos[1])
            cvPosZ.append(pos[2])
        avgPosX = sum(cvPosX)/len(cvPosX)
        avgPosY = sum(cvPosY)/len(cvPosY)
        avgPosZ = sum(cvPosZ)/len(cvPosZ)
        avgPosXYZ = ["{}cm".format(avgPosX),"{}cm".format(avgPosY),"{}cm".format(avgPosZ)]
        
        pm.select(i.cv[0:endRange],r=True)
        if s == 1:
            if rx == 0:
                scaleValX = 1
            else:
                scaleValX = scaleVal
            if ry == 0:
                scaleValY = 1
            else:
                scaleValY = scaleVal
            if rz == 0:
                scaleValZ = 1
            else:
                scaleValZ = scaleVal

            if objSpace == True:
                pm.scale(scaleValX,scaleValY,scaleValZ)
            else:
                pm.scale(scaleValX,scaleValY,scaleValZ,p=avgPosXYZ)
                
        if r == 1:
            if objSpace == True:
                pm.rotate(rx,ry,rz,r=True)
            else:
                pm.rotate(rx,ry,rz,r=True,p=avgPosXYZ)

        pm.select(i)
    pm.select(obj)
    pm.undoInfo(closeChunk=True)




def oneLiner(nName, method='s'):

    # get selection method
    if nName.find('/s') != -1:
        method = 's'
        nName = nName.replace('/s', '')
    elif nName.find('/h') != -1:
        method = 'h'
        nName = nName.replace('/h', '')
    elif nName.find('/a') != -1:
        if nName.find('>') != -1:
            method = 'a'
            print method
        nName = nName.replace('/a', '')

    if method == 's':
        slt = pm.selected()
    elif method == 'h':
        sltH = []
        slt = pm.selected()
        for i in slt:
            sltH.append(i)
            for child in reversed(i.listRelatives(ad=True, type='transform')):
                sltH.append(child)
        print sltH
        slt = sltH
    elif method == 'a':
        slt = pm.ls()

    # find numbering replacement
    def numReplace(numName, idx, start=1):
        global padding
        if numName.find('//') != -1:
            start = int(numName[numName.find('//') + 2:len(numName)])
            numName = numName.replace(numName[numName.find('//'):len(numName)], '')
            print start
        number = idx + start
        if numName.find('#') != -1:
            padding = numName.count('#')
            hastag = "{0:#>{1}}".format("#", padding)  # get how many '#' is in the new name
            num = "{0:0>{1}d}".format(number, padding)  # get number
            numName = numName.replace(hastag, num)
        return numName

    for i in slt:  # for every object in selection list
        # check if there is '>' that represents the replacement method
        if nName.find('>') != -1:
            wordSplit = nName.split('>')
            oldWord = wordSplit[0]
            newWord = wordSplit[1]
            try:
                pm.rename(i,i.replace(oldWord,newWord))
            except:
                print "{} is not renamed".format(i)

        # check if the first character is '-' or '+', remove character method
        elif nName[0] == '-':
            charToRemove = int(nName[1:len(nName)])
            try:
                pm.rename(i, i[0:-charToRemove])
            except:
                print "{} is not renamed".format(i)

        elif nName[0] == '+':
            charToRemove = int(nName[1:len(nName)])
            pm.rename(i, i[charToRemove:len(str(i))])

        else:
            newName = numReplace(nName, slt.index(i))
            # get current Name if '!' mentioned
            print i
            if newName.find('!') != -1:
                newName = newName.replace('!', str(i))
                print newName
            try:
                pm.rename(i, newName)
            except:
                print "{} is not renamed".format(i)