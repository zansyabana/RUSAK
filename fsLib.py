#---------written by:----------------------
#-------Fauzan Syabana---------------------
#------zansyabana@gmail.com----------------
#Licensed under MIT License

import pymel.core as pm
import maya.cmds as mc
import json
import os
from pathlib import Path


class createControls():
    def __init__(self):
        self.fileName = os.path.realpath(__file__)
        self.curveLibPath = self.fileName.replace(os.path.basename(__file__), 'FScurveLibrary.json')
        self.curveLib_file = open(self.curveLibPath)
        self.curveLib = json.load(self.curveLib_file)
        self.curveLib_file.close()

        userPath = Path(os.getenv("USERPROFILE")) / "Documents" / "maya"/"scripts"/"rusakUserCurveLib.json"
        if userPath.exists():
            self.userCurveLib_file = open(userPath)
            self.userCurveLib = json.load(self.userCurveLib_file)
            self.curveLib.update(self.userCurveLib)

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

    def saveCtl(self,name,obj=None,customPath=''):
        if not obj:
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
        if customPath:
            savePath = customPath
            
        else:
            savePath = self.curveLibPath
        oldDataFile = open(savePath, 'r')
        crvShapeInfo = json.load(oldDataFile)
        oldDataFile.close()
        crvShapeInfo[name] = 'pm.curve(p={}, d={}, k={},per={})'.format(cvPoints, deg, knots,per)
        # print crvShapeInfo
        with open(savePath, mode='w') as insertData:
            json.dump(crvShapeInfo,insertData,indent=4)
            insertData.close()

    def setColor(self,obj, CCode):
        pm.undoInfo(openChunk=True)
        obj.getShape().overrideEnabled.set(1)
        obj.getShape().overrideColor.set(CCode)
        pm.undoInfo(closeChunk=True)

def zeroTrans(sfx, keep=True,prefix=False,*args):
    pm.undoInfo(openChunk=True)
    selected = mc.ls(sl=True)

    for i in selected:
        if keep:
            if prefix:
                grpName = sfx +"_"+ i
            else:
                grpName = i +"_"+ sfx
            mc.select(i)
            mc.group(name=grpName)
            select02 = mc.ls(i, grpName)
            mc.copyAttr(select02[0], select02[1], v=True)
            mc.move(0, 0, 0, i, ls=True)
            mc.rotate(0, 0, 0, i, a=True)
            mc.scale(1, 1, 1, i)
        else:
            if prefix:
                oldSfx = "_"+i.split('_')[0]
            else:
                oldSfx = "_"+i.split('_')[-1]
            mc.select(i)
            grp = mc.group(name=i.replace(oldSfx,sfx))
            select02 = mc.ls(i, grp)
            mc.copyAttr(select02[0], select02[1], v=True)
            mc.move(0, 0, 0, i, ls=True)
            mc.rotate(0, 0, 0, i, a=True)
            mc.scale(1, 1, 1, i)
    pm.select(selected)
    pm.undoInfo(closeChunk=True)

def transformShapes(t=0, r=0, s=0, rx=0, ry=0, rz=0, scaleVal=0, objSpace=True, tx=0, ty=0, tz=0, *args):
    """
    Optimized transformShapes:
    - suspend viewport refresh for the whole operation
    - avoid selecting components; operate on component lists via cmds
    - compute pivot as numeric tuple and minimize Python/Maya round-trips

    Inputs match the original API.
    """
    # preserve original selection so we can restore it later
    orig_sel = mc.ls(sl=True)
    # normalize selection to transform nodes (users might select components)
    sel = pm.ls(orig_sel, transforms=True)
    if not sel:
        # nothing to operate on (no transform nodes found)
        return

    # Note: undo handling is left to the caller (e.g. UI) so callers
    # can group multiple incremental changes (slider dragging) into
    # a single undo chunk. We still suspend refresh here for safety
    # if the caller hasn't already.
    try:
        mc.refresh(suspend=True)
        for i in sel:
            # determine CV end index (mirror original logic)
            max_spans = i.spans.get()
            deg = i.d.get()
            if i.f.get() == 2:
                end_range = max_spans - 1
            else:
                end_range = (max_spans + deg) - 1

            if end_range <= 0:
                # nothing to do for this curve
                continue

            # build list of component names for cmds (strings are faster than PyNodes here)
            comp_list = [str(cv) for cv in i.cv[0:end_range]]

            # compute average (world) position of CVs
            pts = [pm.pointPosition(str(i.cv[idx]), w=True) for idx in range(0, end_range)]
            if not pts:
                continue
            avg_x = sum(p[0] for p in pts) / len(pts)
            avg_y = sum(p[1] for p in pts) / len(pts)
            avg_z = sum(p[2] for p in pts) / len(pts)
            pivot = (avg_x, avg_y, avg_z)

            # translate
            if t == 1:
                # apply relative translation to components
                move_x = tx
                move_y = ty
                move_z = tz

                # If objSpace == False we want transform-space (local to object)
                # Try to move using cmds with object-space flag first. If that
                # fails (different Maya builds), fall back to computing the
                # world-space offset by transforming the local vector by the
                # object's world matrix and move in world space.
                try:
                    if objSpace:
                        mc.move(move_x, move_y, move_z, comp_list, r=True)
                    else:
                        # object-space move (local axes)
                        mc.move(move_x, move_y, move_z, comp_list, r=True, os=True)
                except Exception:
                    try:
                        # compute world-space delta using object's world matrix
                        mat = i.getMatrix(worldSpace=True)
                        local_vec = pm.datatypes.Vector(move_x, move_y, move_z)
                        world_vec = local_vec * mat
                        pm.select(comp_list, r=True)
                        pm.move(world_vec.x, world_vec.y, world_vec.z, r=True, ws=True)
                    except Exception:
                        # last-resort fallback: selection-based world move
                        pm.select(comp_list, r=True)
                        pm.move(move_x, move_y, move_z, r=True, ws=True)

            # scale
            if s == 1:
                scale_x = scaleVal if rx != 0 else 1
                scale_y = scaleVal if ry != 0 else 1
                scale_z = scaleVal if rz != 0 else 1

                # Try cmds first (faster, no selection). Some Maya versions don't accept
                # a pivot flag for component operations; fall back to PyMel + selection
                try:
                    if objSpace:
                        mc.scale(scale_x, scale_y, scale_z, comp_list, r=True)
                    else:
                        mc.scale(scale_x, scale_y, scale_z, comp_list, r=True, pivot=pivot)
                except Exception:
                    # fallback: select components and use PyMel which accepts pivot arg
                    pm.select(comp_list, r=True)
                    if objSpace:
                        pm.scale(scale_x, scale_y, scale_z, r=True)
                    else:
                        pm.scale(scale_x, scale_y, scale_z, r=True, p=pivot)

            # rotate
            if r == 1:
                try:
                    if objSpace:
                        mc.rotate(rx, ry, rz, comp_list, r=True)
                    else:
                        mc.rotate(rx, ry, rz, comp_list, r=True, pivot=pivot)
                except Exception:
                    pm.select(comp_list, r=True)
                    if objSpace:
                        pm.rotate(rx, ry, rz, r=True)
                    else:
                        pm.rotate(rx, ry, rz, r=True, p=pivot)

        # restore original selection (may contain components)
        try:
            if orig_sel:
                mc.select(orig_sel, r=True)
            else:
                mc.select(clear=True)
        except Exception:
            # best-effort restore using PyMel
            try:
                pm.select(orig_sel)
            except Exception:
                pass

    finally:
        mc.refresh(suspend=False)


def splitJoint(splitNum,*args):
    """Insert intermediate joints between two selected joints.

    splitNum is treated as the number of segments to divide the span into.
    For example, splitNum=2 will insert one joint at the midpoint.
    """
    sel = pm.selected(type='joint')
    if len(sel) != 2:
        pm.warning("Select 2 joints only")
        return

    startJnt = sel[0]
    endJnt = sel[1]

    # validate splitNum
    try:
        n = int(splitNum)
    except Exception:
        pm.warning("splitNum must be an integer")
        return
    if n <= 0:
        pm.warning("splitNum must be >= 1")
        return

    # get world positions
    startJntPos = pm.xform(startJnt, q=True, ws=True, t=True)
    endJntPos = pm.xform(endJnt, q=True, ws=True, t=True)

    # compute vector and segment increment
    distVector = pm.datatypes.Vector(endJntPos) - pm.datatypes.Vector(startJntPos)
    totalLength = distVector.length()
    # number of segments = n, new joints to insert = n - 1
    if n == 1:
        # nothing to insert
        return

    # create intermediate joints at fractional positions along the vector
    pm.undoInfo(openChunk=True)
    try:
        # detach end joint so we can reparent it under the last created joint
        orig_parent = endJnt.getParent()
        try:
            pm.parent(endJnt, world=True)
        except Exception:
            pass

        new_joints = []
        # select start joint so pm.joint creates children under it
        pm.select(startJnt, r=True)
        for i in range(1, n):
            t = float(i) / float(n)
            pos_vec = pm.datatypes.Vector(startJntPos) + (distVector * t)
            # create joint at world position; pm.joint will parent to the current selection
            j = pm.joint(p=(pos_vec.x, pos_vec.y, pos_vec.z))
            new_joints.append(j)

        # reparent the original end joint under the last new joint (or start if no new)
        if new_joints:
            try:
                pm.parent(endJnt, new_joints[-1])
            except Exception:
                pass

        # orient the joint chain to produce reasonable joint orientation
        try:
            pm.joint(startJnt, e=True, zso=True, oj='xyz', sao='yup', ch=True, spa=True)
        except Exception:
            pass

    finally:
        # restore original parent if it existed (only if it wasn't world)
        try:
            if orig_parent:
                # if endJnt was reparented to a new joint we don't want to undo that;
                # only attempt to restore if we failed to reparent above
                pass
        except Exception:
            pass
        pm.undoInfo(closeChunk=True)

def createJntOnSel(objs=[],pac=False,sc=False,oc=False,poc=False,sfx='bJnt',chain=False):
    pm.undoInfo(openChunk=True)
    jnts=[]
    for obj in objs:
        #get obj world position
        pos=pm.xform(obj,q=True,ws=True,t=True)
        #get obj world rotation
        rot=pm.xform(obj,q=True,ws=True,ro=True)    
        pm.select(clear=True)
        jnt=pm.joint(p=pos,name=str(obj)+'_'+sfx)
        pm.xform(jnt,ws=True,ro=rot)
        jnts.append(jnt)
        if jnts.index(jnt)!=0 and chain:
            pm.parent(jnt,jnts[jnts.index(jnt)-1])
            orientJoints([jnt])
        else:
            orientJoints([jnt])
        if pac:
            pm.parentConstraint(obj,jnt,mo=True)
        if sc:
            pm.scaleConstraint(obj,jnt,mo=True)
        if oc:
            pm.orientConstraint(obj,jnt,mo=True)
        if poc:
            pm.pointConstraint(obj,jnt,mo=True)
    #orient the joints after all created, check the translate of the next joint to determine the aim vector
    pm.select(objs)
    pm.undoInfo(closeChunk=True)
    return jnts

def toggleJointAxis(children=False,*args):
    sel = pm.selected(type='joint')
    if children:
        jntList = []
        for i in sel:
            jntList.append(i)
            children = i.listRelatives(ad=True, type='joint')
            #reverse the list to make sure the parent joint is first
            children.reverse()
            for child in children:
                jntList.append(child)
        sel = jntList
    if any([i.displayLocalAxis.get() == 0 for i in sel]):
        for i in sel:
            i.displayLocalAxis.set(1)
    else:
        for i in sel:
            i.displayLocalAxis.set(0)

def orientJoints(objs=[],children=False,
                 primeAxis='X',
                 secondaryAxis='Y',
                 worldAxis='Z',
                 primeNegative=False,
                 secondaryNegative=False,
                 worldNegative=False,
                 helper=False,*args):
    pm.undoInfo(openChunk=True)
    if not objs:
        objs = pm.selected(type='joint')
    if children:
        jntList = []
        for i in objs:
            jntList.append(i)
            children = i.listRelatives(ad=True, type='joint')
            #reverse the list to make sure the parent joint is first
            children.reverse()
            for child in children:
                jntList.append(child)
        objs = objs+jntList
    #create a helper locators to help orient the joints
    helperLocs = [i.getParent() for i in pm.ls('*_orientHelper*',type='locator')]
    #sort the helper locs to make sure the parent joint helper is first
    helperLocs.sort(key=lambda x: len(x.getAllParents()))
    helperDict = {}
    for i in helperLocs:
        helperDict[i] = {'new':False}
    for i in objs:
        helperName = str(i)+'_orientHelper'
        if not pm.objExists(helperName):
            loc = pm.spaceLocator(name=str(i)+'_orientHelper')
            pm.parent(loc, i)
            loc.setTranslation([0,0,0], space='object')
            loc.setRotation([0,0,0], space='object')
            loc.displayLocalAxis.set(1)
            helperDict[loc] = {'new':True}

    for loc in helperDict:
        i = loc.getParent()
        i.displayLocalAxis.set(0)
        #get joint children to determine aim vector
        jntChildren = i.getChildren(type='joint')
        if jntChildren:
            #determine aim vector
            primeValue = 1 if primeNegative==False else -1
            if primeAxis == 'X':
                aimVector = pm.datatypes.Vector(primeValue,0,0)
            elif primeAxis == 'Y':
                aimVector = pm.datatypes.Vector(0,primeValue,0)
            elif primeAxis == 'Z':
                aimVector = pm.datatypes.Vector(0,0,primeValue)
            #determine up vector
            secondaryValue = 1 if secondaryNegative==False else -1
            if secondaryAxis == 'X':
                upVector = pm.datatypes.Vector(secondaryValue,0,0)
            elif secondaryAxis == 'Y':
                upVector = pm.datatypes.Vector(0,secondaryValue,0)
            elif secondaryAxis == 'Z':
                upVector = pm.datatypes.Vector(0,0,secondaryValue)
            #determine world up vector
            worldValue = 1 if worldNegative==False else -1
            if worldAxis == 'X':
                worldUpVector = pm.datatypes.Vector(worldValue,0,0)
            elif worldAxis == 'Y':
                worldUpVector = pm.datatypes.Vector(0,worldValue,0)
            elif worldAxis == 'Z':
                worldUpVector = pm.datatypes.Vector(0,0,worldValue)
            #aim constraint the helper locator to the joint child
            if helper or helperDict[loc]['new']:
                aimCon = pm.aimConstraint(jntChildren[0], loc, aim=aimVector, u=upVector, wut='vector', wu=worldUpVector)
                pm.delete(aimCon)
    print(helperDict)
    if not helper:  
        for loc in helperDict:
            jnt = loc.getParent()
            print(jnt)
            #get world orientation
            jntRot = jnt.getRotation(space='object')
            locRot= loc.getRotation(space='object')
            finalRot = [locRot[0]+jntRot[0], locRot[1]+jntRot[1], locRot[2]+jntRot[2]]
            #get the jnt children
            jntChildDict = {}
            jntChildren = jnt.getChildren(type='joint')
            if jntChildren:
                for chd in jntChildren:
                    jntChildDict[chd] = {'location':chd.getTranslation(space='world'),
                                        'rotation':chd.getRotation(space='world')}
                    if pm.objExists(chd+'_orientHelper'):
                       helpLoc = pm.PyNode(chd+'_orientHelper')
                       jntChildDict[chd]['LocLocation'] = helpLoc.getTranslation(space='world')
                       jntChildDict[chd]['LocRotation'] = helpLoc.getRotation(space='world')
            jnt.setRotation(finalRot, space='object')
            loc.setRotation([0,0,0], space='object')

            #convert the rotation to quaternion
            quat=pm.datatypes.EulerRotation(finalRot[0],finalRot[1],finalRot[2]).asQuaternion()
            #get current joint orient
            curOrient = jnt.getOrientation()
            #add quat and current joint orient
            quat = quat * curOrient
            #set the joint orient to quaternion value
            jnt.setOrientation(quat)
            #reset the rotation to 0
            jnt.rotate.set([0,0,0])
            jnt.displayLocalAxis.set(1)
            # #reposition the joint children to avoid translation offset after orienting the joint
            if jntChildDict:
                for chd,value in jntChildDict.items():
                    print(f"Repositioning {chd} to {value}")
                    chd.setTranslation(value['location'], space='world')
                    chd.setRotation(value['rotation'], space='world')
                    if value.get('LocLocation'):
                        helpLoc = pm.PyNode(chd+'_orientHelper')
                        helpLoc.setTranslation(value['LocLocation'], space='world')
                        helpLoc.setRotation(value['LocRotation'], space='world')
        #delete the helper locators
        # for loc in helperDict:
        #     pm.delete(loc)
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
            print(method)
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
        print(sltH)
        slt = sltH
    elif method == 'a':
        slt = pm.ls()

    # find numbering replacement
    def numReplace(numName, idx, start=1):
        global padding
        if numName.find('//') != -1:
            start = int(numName[numName.find('//') + 2:len(numName)])
            numName = numName.replace(numName[numName.find('//'):len(numName)], '')
            # print start
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
                print("{} is not renamed".format(i))

        # check if the first character is '-' or '+', remove character method
        elif nName[0] == '-':
            charToRemove = int(nName[1:len(nName)])
            try:
                pm.rename(i, i[0:-charToRemove])
            except:
                print( "{} is not renamed".format(i))

        elif nName[0] == '+':
            charToRemove = int(nName[1:len(nName)])
            pm.rename(i, i[charToRemove:len(str(i))])

        else:
            newName = numReplace(nName, slt.index(i))
            # get current Name if '!' mentioned
            if newName.find('!') != -1:
                newName = newName.replace('!', str(i))
                # print newName
            try:
                pm.rename(i, newName)
            except:
                print("{} is not renamed".format(i))