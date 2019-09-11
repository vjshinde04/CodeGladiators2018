def main():
    nSalmons = int(input())

    lenSalmons = input().split(' ')
    lenSalmons = [int(i) for i in lenSalmons]

    timeSalmons = input().split(' ')
    timeSalmons = [int(i) for i in timeSalmons]

    def getSalmonTimeRange(lenSalmons, timeSalmons):
        salmonTimeRange = {}
        for k, s in enumerate(lenSalmons):
            ts = list(range(timeSalmons[k], timeSalmons[k] + s + 1))
            salmonTimeRange[k + 1] = ts
        return (salmonTimeRange)

    def getCatchCount(salmons):
        catchInstance = {}
        instanceCount = {}
        for key, value in salmons.items():
            for x in value:
                if x not in catchInstance.keys():
                    catchInstance[x] = [key]
                else:
                    catchInstance[x].append(key)
                if x not in instanceCount.keys():
                    instanceCount[x] = 1
                else:
                    instanceCount[x] += 1
        # print(catchInstance)
        print(instanceCount.items)
        return (catchInstance, instanceCount)

    salmonTimeRange0 = getSalmonTimeRange(lenSalmons, timeSalmons)
    (catchInstance0, catchCount0) = getCatchCount(salmonTimeRange0)

    maxCount = []
    flag = None
    for index, count in enumerate(catchCount0):
        if index != 0:
            leftoutLenSalmons = lenSalmons.copy()
            leftoutTimeSalmons = timeSalmons.copy()
            salmonGroup = catchInstance0.get(index)
            # print(salmonGroup)
            if index in catchInstance0.keys():
                if flag != salmonGroup:
                    flag = salmonGroup.copy()
                    salmonGroup.sort(reverse=True)
                    for s in salmonGroup:
                        leftoutLenSalmons.pop(s - 1)
                        leftoutTimeSalmons.pop(s - 1)
                    # print(leftoutLenSalmons)
                    # print(leftoutTimeSalmons)
                    leftoutSalmonTimeRange = getSalmonTimeRange(leftoutLenSalmons, leftoutTimeSalmons)
                    zzz, leftoutCatchCount = getCatchCount(leftoutSalmonTimeRange)
                    # maxCount.append(len(salmonGroup) + max(leftoutCatchCount.values()))

    # print(max(maxCount))

"""
    def getCatchInstance(salmons):
        catchInstance = {}
        # instanceCount = []
        for key, value in salmons.items():
            for x in value:
                if x not in catchInstance.keys():
                    catchInstance[x] = [key]
                else:
                    catchInstance[x].append(key)
                # try:
                #    instanceCount[x] += 1
                # except IndexError:
                #    instanceCount.insert(x, 1)
        return (catchInstance)

    def getCatchCount(salmons, catch, last):
        instanceCount = [0] * last
        # print(len(instanceCount), instanceCount)
        for key, value in salmons.items():
            for x in value:
                instanceCount[x] += 1
        return (instanceCount)

    salmonTimeRange0 = getSalmonTimeRange(lenSalmons, timeSalmons)
    catchInstance0 = getCatchInstance(salmonTimeRange0)
    catchCount0 = getCatchCount(salmonTimeRange0, catchInstance0, (max(catchInstance0.keys()) + 1))

    maxCount = []
    flag = None
    for index, count in enumerate(catchCount0):
        if index != 0:
            leftoutLenSalmons = lenSalmons.copy()
            leftoutTimeSalmons = timeSalmons.copy()
            salmonGroup = catchInstance0.get(index)
            if index in catchInstance0.keys():
                if flag != salmonGroup:
                    flag = salmonGroup.copy()
                    salmonGroup.sort(reverse=True)
                    #print(salmonGroup)
                    for s in salmonGroup:
                        leftoutLenSalmons.pop(s - 1)
                        leftoutTimeSalmons.pop(s - 1)
                    leftoutSalmonTimeRange = getSalmonTimeRange(leftoutLenSalmons, leftoutTimeSalmons)
                    leftoutCatchInstance = getCatchInstance(leftoutSalmonTimeRange)
                    # print(leftoutCatchInstance.keys())
                    z = 0
                    for i in leftoutCatchInstance.keys():
                        if i > z:
                            z = i
                    # print(z)
                    leftoutCatchCount = getCatchCount(leftoutSalmonTimeRange, leftoutCatchInstance, z + 1)
                    maxCount.append(len(salmonGroup) + max(leftoutCatchCount))
    print(max(maxCount))
"""


main()