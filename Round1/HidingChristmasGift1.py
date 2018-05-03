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
                br = findChild([h2])
                if br == None:
                    path[h1].append([h2])
                else:
                    path[h1].append(br)
            elif h2 in leafNode:
                path[h1].append([h2])

        elif h2 in parentNode:
            if h1 in linkNode:
                br = findChild([h1])
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
            if h2 in linkNode:
                branch = findChild(br + [h2])
            elif h2 in leafNode:
                return (br+[h2])
        elif br[-1] == h2:
            if h1 in linkNode:
                branch = findChild(br+[h1])
            elif h1 in leafNode:
                return (br+[h1])
    print(branch)
    if len(branch) != 0 and branch[-1] in leafNode:
        print('leafnode found in link-link combo')
        return (branch)

#########################################
with open('in.txt') as f:
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

path = dict((node,[]) for node in parentNode)

##Populating dictionary/creating map
findBranches(path)
print(path)
##

##Counting presents:for every key check if
pC = None
def leafPath(hOne, hTwo):
    for key, value in path.items():
        for i, listValue in enumerate(value):
            global pC
            if hOne in listValue:
                if key != pC:
                    houseCount[key] += 1
                    pC = key
                for ele in listValue:
                    houseCount[ele] += 1
            elif hTwo in listValue and hTwo in leafNode:
                if key != pC:
                    houseCount[key] += 1
                    pC = key
                for ele in listValue:
                    houseCount[ele] += 1
            elif hTwo in listValue and hTwo in linkNode:
                if key != pC:
                    houseCount[hTwo] += 1
                    pC = key
                for ele in listValue:
                    houseCount[ele] += 1
                    if ele == hTwo:
                        break
        if hTwo in parentNode:
            if hTwo != pC:
                houseCount[hTwo] += 1

houseCount = [0]*(nHouse+1)
for i in range(nHouse,nHouse+nDays):
    #print(line[i])
    houseInfo = line[i].split(' ')
    houseInfo = [int(i) for i in houseInfo]
    startHouse, endHouse = houseInfo
    # combos : leaf-leaf, leaf-link, leaf-parent, link-link, link-parent, parent-parent
    if startHouse in leafNode:
        leafPath(startHouse,endHouse)

    #elif

for i in range(len(houseCount)):
    print(i, houseCount[i])
#print(max(houseCount))