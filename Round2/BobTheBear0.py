"""
Bob is a grizzly bear and just like all grizzlies he loves hunting salmon fish.
Bob has a strategy for catching salmons. He stands at the edge of the river and
waits for the fishes to cross him. Whenever a fish comes in the same line as
that of Bob, he catches it.

For the sake of the problem assume the river is flowing from left to right and
Bob is currently sitting at x-coordinate = 0 (origin). All the fishes are swimming
with the river's flow at a uniform speed of 1 from left to right.
The x-coordinates increases as we move rightwards in the river and
decreases as we move leftwards. Initially all the fishes has non-positive x-coordinates.

You are given the information about N salmons in two arrays len and time,
where len[i] = length of the ith salmon and time[i] = time at which
the head of the ith salmon reaches the x-coordinate = 0 (origin).
So, at any time T, the ith salmon  has its head at
x-coordinate = T - time[i] and tail at x-coordinate = T - time[i] - len[i].

At any point of time Bob can catch all the salmons whose any part of body
(between head and tail, both inclusive) is at origin.

Bob wants to catch salmons no more than twice. What is the maximum number of
Salmons Bob can catch?



Input Format
First line of input contains an integer N representing the number of salmons.

Second line of input contains N space separated integers representing the
contents of array len.

Third line of input contains N space separated integers representing the
contents of array time.

The last line of input is kept blank.



Constraints
1 <= N <= 1000

1 <= len[i] <= 1000, 000, 000

0 <= time[i] <= 1000, 000, 000



Output Format
An integer representing the maximum number of salmons Bob can catch.

Sample TestCase 1
Input
5
2 4 4 2 4
1 4 1 6 4
Output
5
Explanation
The situation at time = 0 is shown in the following figure.

The red line denotes x = 0 (origin) ,Bob is sitting. The blue line shows 1st salmon,
the orange one shows 2nd salmon, the green one shows 3rd salmon and so on.

Bob will catch salmon 1 and 3 at time = 2 and will catch salmon 2, 4 and 5 at time = 7.

Sample TestCase 2
Input
1
1
2
Output
1
"""

with open('bb3.txt') as f:
    line = f.readlines()
#print(line)

nSalmons = int(line[0])
print(nSalmons)
lenSalmons = line[1].split(' ')
lenSalmons = [int(i) for i in lenSalmons]
print(lenSalmons)
timeSalmons = line[2].split(' ')
timeSalmons = [int(i) for i in timeSalmons]
print(timeSalmons)

def getSalmonTimeRange(lenSalmons, timeSalmons):
    salmonTimeRange = {}
    for k,s in enumerate(lenSalmons):
        ts = list(range(timeSalmons[k], timeSalmons[k]+s+1))
        salmonTimeRange[k+1] = ts
    return(salmonTimeRange)
'''
lastInstance = []
for key,value in salmonTimeRange.items():
    lastInstance.append(max(value))
catchInstance = dict((key, []) for key in range(1,max(lastInstance)+1))
print(lastInstance)
print(catchInstance)
'''
def getCatchCount(salmons):
    catchInstance = {}
    instanceCount = {}
    for key,value in salmons.items():
        for x in value:
            if x not in catchInstance.keys():
                catchInstance[x] = [key]
            else:
                catchInstance[x].append(key)
            if x not in instanceCount.keys():
                instanceCount[x] = 1
            else:
                instanceCount[x] += 1
    return(catchInstance,instanceCount)
'''
def getCatchCount(salmons, catch):
    instanceCount = [0]*(max(catch.keys())+1)
    for key,value in salmons.items():
        for x in value:
            instanceCount[x] += 1
    return(instanceCount)
'''
salmonTimeRange0 = getSalmonTimeRange(lenSalmons, timeSalmons)
print('salmonTimeRange0', salmonTimeRange0)
(catchInstance0,catchCount0) = getCatchCount(salmonTimeRange0)
print('catchInstance0',catchInstance0)
print('catchCount0',catchCount0)

maxCount = []
flag = None
for index,count in enumerate(catchCount0):
    if index != 0:
        leftoutLenSalmons = lenSalmons.copy()
        leftoutTimeSalmons = timeSalmons.copy()
        salmonGroup = catchInstance0[index]
        #print(salmonGroup)
        if flag != salmonGroup:
            flag = salmonGroup.copy()
            salmonGroup.sort(reverse=True)
            for s in salmonGroup:
                leftoutLenSalmons.pop(s-1)
                leftoutTimeSalmons.pop(s-1)
            #print(leftoutLenSalmons)
            #print(leftoutTimeSalmons)
            leftoutSalmonTimeRange = getSalmonTimeRange(leftoutLenSalmons, leftoutTimeSalmons)
            zzz,leftoutCatchCount = getCatchCount(leftoutSalmonTimeRange)
            maxCount.append(len(salmonGroup) + max(leftoutCatchCount.values()))

print(max(maxCount))
