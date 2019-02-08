import pymel.core as pm


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