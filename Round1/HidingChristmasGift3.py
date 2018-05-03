import time
start = time.time()

with open('in8.txt') as f:
    line = f.readlines()

cityInfo = line[0].split(' ')
cityInfo = [int(i) for i in cityInfo]
nHouse, nDays = cityInfo
########################################################
houseInfo = []
for i in range(1,nHouse):
    #print(line[i])
    pairInfo = line[i].split(' ')
    pairInfo = [int(value) for value in pairInfo]
    #h1, h2 = pairInfo
    houseInfo.append(pairInfo)

dayInfo = []
for i in range(nHouse,nHouse+nDays):
    #print(line[i])
    pairInfo = line[i].split(' ')
    pairInfo = [int(value) for value in pairInfo]
    #startHouse, endHouse = pairInfo
    dayInfo.append(pairInfo)
########################################################
graph = {}
#print(graph)


for pairInfo in houseInfo:
    h1, h2 = pairInfo
    if h1 in graph.keys():
        if h2 not in graph[h1]:
            graph[h1].append(h2)
    else:
        graph[h1] = [h2]

    if h2 in graph.keys():
        if h1 not in graph[h2]:
            graph[h2].append(h1)
    else:
        graph[h2] = [h1]
print(graph)


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    '''
    if not graph.has_key(start):
        return None
    '''
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

houseCount = [0]*(nHouse+1)

for pairInfo in dayInfo:
    #print(line[i])
    startHouse, endHouse = pairInfo
    if startHouse in graph.keys() and endHouse in graph.keys():
        path = find_path(graph, startHouse, endHouse)
        for ele in path:
            houseCount[ele] += 1

houseCountDict = dict((node, None) for node in graph.keys())
for i in range(len(houseCount)):
    houseCountDict[i] = houseCount[i]
print(houseCountDict)

print(max(houseCount))

end = time.time()
print(end-start)
