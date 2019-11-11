import pymel.core as pm
import maya.cmds as mc
import json
import os



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

    def crCtl(self, crvShp='circle', asJnt=False):
        slt = pm.selected()

        # Defines to convert the controller as shaped joint
        if asJnt == False:
            crv = eval(self.curveLib[crvShp])

        else:
            crv = eval(self.curveLib[crvShp])
            jnt = pm.joint()
            pm.parent(jnt,w=True)
            shp = crv.listRelatives(c=True, type='nurbsCurve')[0]
            pm.parent(shp, jnt, s=True, r=True)
            shp.rename(jnt + 'Shape')
            jnt.drawStyle.set(2)
            pm.delete(crv)
            crv = jnt
            pm.select(jnt)
            print crv

        try:
            self.align(crv, slt[0])
        except:
            pass

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
        obj.overrideEnabled.set(1)
        obj.overrideColor.set(CCode)


def zeroTrans(sfx, keep=True,*args):
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