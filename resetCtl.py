import pymel.core as pm

slt = pm.selected()

for i in slt:
    trList = [i.translateX,i.translateY,i.translateZ,i.rotateX,i.rotateY,i.rotateZ]
    for attr in trList:
        try:
            attr.set(0)
        except:
            pass
    scList = [i.scaleX,i.scaleY,i.scaleZ]
    for scale in scList:
        try:
            scale.set(1)
        except:
            pass