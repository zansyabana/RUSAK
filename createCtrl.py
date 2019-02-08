import pymel.core as pm
import json

curveLibPath = __file__.replace('createCtrl.py', 'FScurveLibrary.json')
curveLib_file = open(curveLibPath, 'r')
curveLib = json.load(curveLib_file)
curveLib_file.close()


class createControls():
    def __init__(self):
        pass

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
            crv = eval(curveLib[crvShp])

        else:
            crv = eval(curveLib[crvShp])
            jnt = pm.joint()
            pm.parent(jnt,w=True)
            shp = crv.listRelatives(c=True, type='nurbsCurve')[0]
            pm.parent(shp, jnt, s=True, r=True)
            shp.rename(jnt + 'Shape')
            jnt.drawStyle.set(2)
            pm.delete(crv)
            crv = jnt

        try:
            self.align(crv, slt[0])
        except:
            pass

    def saveCtl(self,name):

        obj = pm.selected()[0]
        cvPoints = []
        max = obj.spans.get()
        deg = obj.d.get()
        for i in range(0, max + 1):
            pointXYZ = obj.controlPoints[i].get()
            pointX = pointXYZ[0]
            pointY = pointXYZ[1]
            pointZ = pointXYZ[2]
            points = (pointX, pointY, pointZ)
            cvPoints.append(points)

        oldDataFile = open(curveLibPath, 'r')
        crvShapeInfo = json.load(oldDataFile)
        oldDataFile.close()
        crvShapeInfo[name] = 'pm.curve(p={}, d={})'.format(cvPoints, deg)
        print crvShapeInfo
        with open(curveLibPath, mode='w') as insertData:
            json.dump(crvShapeInfo,insertData,indent=4)
            insertData.close()
