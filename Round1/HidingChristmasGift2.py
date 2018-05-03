leafNode = []
linkNode = []
parentNode = []
def findBranches(path):
    for i in range(1, nHouse):
        houseInfo = line[i].split(' ')
        houseInfo = [int(i) for i in houseInfo]
        h1, h2 = houseInfo
        if h1 in parentNode and h2 in parentNode:
            path[h1].append([h2])
            path[h2].append([h1])

        elif h1 in parentNode:
            if h2 in linkNode:
                br = findChild([h1, h2])
                if br == None:
                    path[h1].append([h2])
                else:
                    path[h1].append(br)
            elif h2 in leafNode:
                path[h1].append([h2])

        elif h2 in parentNode:
            if h1 in linkNode:
                br = findChild([h2, h1])
                if br == None:
                    path[h2].append([h1])
                else:
                    path[h2].append(br)
            elif h1 in leafNode:
                path[h2].append([h1])

def findChild(br):
    branch = []
    for i in range(1, nHouse):
        houseInfo = line[i].split(' ')
        houseInfo = [int(i) for i in houseInfo]
        h1, h2 = houseInfo

        if br[-1] == h1:
            if h2 in linkNode and h2 not in br:
                branch = findChild(br + [h2])
                return (branch)
            elif h2 in leafNode:
                return (br[1:] + [h2])
        elif br[-1] == h2:
            if h1 in linkNode and h1 not in br:
                branch = findChild(br + [h1])
                return (branch)
            elif h1 in leafNode:
                return (br[1:] + [h1])

    if len(br) != 0 and br[-1] in leafNode:
        print('leafnode found in link-link combo', br)
        return (br[1:])
    elif len(br) != 0 and br[-1] in linkNode:
        print('linkNode found in link-link combo', br)
        return (br[1:])

'''
        if br[-1] == h1:
            if h2 in linkNode:
                if len(br) <= 2:
                    branch = findChild(br + [h2])
                elif h1 in br and h2 in br:
                    return(br[1:])
            elif h2 in leafNode:
                return (br[1:] + [h2])
        elif br[-1] == h2:
            if h1 in linkNode:
                if len(br) <= 2:
                    branch = findChild(br + [h1])
                if h1 in br and h2 in br:
                    return(br[1:])
            elif h1 in leafNode:
                return (br[1:] + [h1])
        
    if len(branch) != 0 and branch[-1] in leafNode:
        print('leafnode found in link-link combo',branch)
        return (branch)
   if len(branch) != 0 and branch[-1] in linkNode:
        print('linkNode found in link-link combo',branch)
        return (branch)               
'''

#########################################
with open('in6.txt') as f:
    line = f.readlines()

cityInfo = line[0].split(' ')
cityInfo = [int(i) for i in cityInfo]
nHouse, nDays = cityInfo

#print(line[18])
houseOccurance = [0]*(nHouse+1)
#print(len(houseOccurance))

##counting no of occurances to find leafNode, linkNode, parentNode
for i in range(1,nHouse):
    #print(line[i])
    houseInfo = line[i].split(' ')
    houseInfo = [int(i) for i in houseInfo]
    h1, h2 = houseInfo
    #print(h1, h2)
    houseOccurance[h1] += 1
    houseOccurance[h2] += 1
print(houseOccurance)
for i in range(len(houseOccurance)):
    if houseOccurance[i] == 1:
        leafNode.append(i)
    if houseOccurance[i] == 2:
        linkNode.append(i)
    if houseOccurance[i] > 2:
        parentNode.append(i)
print('leafNodes    ', leafNode)
print('linkNodes    ', linkNode)
print('parentNodes  ', parentNode)
##leafNode, linkNode, parentNode

path = dict((node, []) for node in parentNode)

##Populating dictionary/creating map
findBranches(path)
print(path)
##

##Santa's path
def leafPath(hOne, hTwo):
    hOneKey = hTwoKey = None

    hTwoInfoDict = {}
    for key, value in path.items():
        for i, listValue in enumerate(value):

            if hOne in listValue:
                hOneKey = key
                hOneLV = listValue
                if hTwoKey == hOneKey:
                    break
            if hTwo in listValue:
                hTwoKey = key
                hTwoInfoDict.update({key: listValue})
                if hTwoKey == hOneKey:
                    break
    #print(hTwoInfoDict)
    if hOneKey in hTwoInfoDict.keys():
        houseCount[hOneKey] += 1
        if hOneLV == hTwoInfoDict.get(hOneKey):
            houseCount[hOneKey] -= 1
        if sorted(hOneLV) == sorted(hTwoInfoDict.get(hOneKey)):
            for ele in hOneLV:
                houseCount[ele] += 1
            return
        else:
            for ele in hOneLV:
                houseCount[ele] += 1
            for ele in hTwoInfoDict.get(hOneKey):
                houseCount[ele] += 1
                if ele == hTwo:
                    break
            return

    elif hTwoKey == None:
        houseCount[hTwo] += 1
        houseCount[hOne] += 1
        return

    else:
        for ele in hOneLV:
            houseCount[ele] += 1
        for ele in hTwoInfoDict.get(hTwoKey):
            houseCount[ele] += 1
            if ele == hTwo:
                break
        parentPath(hOneKey, hTwoKey)
        return

'''
            if hOne in listValue:
                hOneKey = key
                for ele in listValue:
                    houseCount[ele] += 1
            elif hTwo in listValue and hTwo in leafNode:
                hTwoKey = key
                for ele in listValue:
                    houseCount[ele] += 1
            elif hTwo in listValue and hTwo in linkNode:
                hTwoKey = key
                for ele in listValue:
                    houseCount[ele] += 1
                    if ele == hTwo:
                        break
        pC = None
        if hTwo in parentNode:
            hTwoKey = hTwo
        if hOneKey != hTwoKey and hOneKey is not None and hTwoKey is not None:
            houseCount[hOneKey] -= 1
            parentPath(hOneKey,hTwoKey)
            return
'''
def linkPath(hOne, hTwo):
    ki = hOneKey = hTwoKey = None
    for k, v in path.items():
        for i, lv in enumerate(v):

            if hOne in lv:
                if str(k) + str(i) != ki:
                    ki = str(k) + str(i)
                    hOneKey = k
                    for ele in lv:
                        houseCount[ele] += 1
                        if ele == hOne:
                            break
                elif str(k)+str(i) == ki:
                    if lv.index(hOne) > lv.index(hTwo):
                        for ele in lv:
                            houseCount[ele] += 1
                            if ele == hOne:
                                break

            if hTwo in lv and hTwo in linkNode:
                if str(k)+str(i) != ki:
                    ki = str(k) + str(i)
                    hTwoKey = k
                    for ele in lv:
                        houseCount[ele] += 1
                        if ele == hTwo:
                            break
                elif str(k)+str(i) == ki:
                    if lv.index(hTwo) > lv.index(hOne):
                        for ele in lv:
                            houseCount[ele] += 1
                        if ele == hTwo:
                            break

        ki = None
        if hTwoKey == hOneKey:
            houseCount[hTwoKey] += 1
        if hOneKey != hTwoKey and hOneKey is not None and hTwoKey is not None:
            parentPath(hOneKey,hTwoKey)
            return
        if hTwoKey == None:
            houseCount[hTwo] += 1
            return

nonJointParents = []
def parentPath(hOne, hTwo):
    nonJointParents.append(hTwo)
    flag = noJoinFlag = 0
    for key, value in path.items():
        if hOne == key:
            houseCount[hOne] += 1
            if [hTwo] in value:
                houseCount[hTwo] += 1
                return
            else:
                hOneValues = value
                noJoinFlag += 1
        elif hTwo == key:
            houseCount[hTwo] += 1
            if [hOne] in value:
                houseCount[hOne] += 1
                return
            else:
                hTwoValues = value
                noJoinFlag += 1
########2 extreme parents having a link and a parent : (3,8)
    if noJoinFlag == 2:
        for i, listValue1 in enumerate(hOneValues):
            for j, listValue2 in enumerate(hTwoValues):
                if sorted(listValue1) == sorted(listValue2):
                    for ele in listValue2:
                        houseCount[ele] += 1
                    return
                if len(listValue2) == 1 and listValue2[0] in parentNode and listValue2[0] not in nonJointParents:
                    houseCount[hOne] -= 1
                    parentPath(hOne, listValue2[0])
                    return
            if len(listValue1) == 1 and listValue1[0] in parentNode:
                houseCount[hTwo] -= 1
                parentPath(listValue1[0], hTwo)
                return
##Santa's path

##Counting presents:for every key check if
houseCount = [0]*(nHouse+1)
for i in range(nHouse,nHouse+nDays):
    #print(line[i])
    houseInfo = line[i].split(' ')
    houseInfo = [int(i) for i in houseInfo]
    startHouse, endHouse = houseInfo
    if startHouse == endHouse:
        if startHouse in parentNode or startHouse in linkNode or startHouse in leafNode:
            houseCount[startHouse] += 1
            continue
    if startHouse not in parentNode and startHouse not in linkNode and startHouse not in leafNode:
        continue
    if endHouse not in parentNode and endHouse not in linkNode and endHouse not in leafNode:
        continue
    if len(parentNode) == 0 and startHouse in leafNode and endHouse in leafNode:
        houseCount = [x+1 for x in houseCount]
        continue
    # combos : leaf-leaf, leaf-link, leaf-parent, link-link, link-parent, parent-parent
    if startHouse in leafNode and endHouse not in leafNode:
        leafPath(startHouse,endHouse)
        continue
    elif endHouse in leafNode and startHouse not in leafNode:
        leafPath(endHouse,startHouse)
        continue
    elif startHouse in leafNode and endHouse in leafNode:
        leafPath(startHouse,endHouse)
        continue

    elif startHouse in linkNode and endHouse not in linkNode:
        linkPath(startHouse,endHouse)
        continue
    elif endHouse in linkNode and startHouse not in linkNode:
        linkPath(endHouse,startHouse)
        continue

    elif startHouse in parentNode and endHouse in parentNode:
        parentPath(startHouse,endHouse)
        continue

#for i in range(len(houseCount)):
#    print(i, houseCount[i])
print(houseCount[1:])
print(max(houseCount[1:]))