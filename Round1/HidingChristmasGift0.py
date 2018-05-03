'''
Hiding Christmas Gifts (100 Marks)
There are N houses in a city connected by exactly N - 1 roads. There is exactly 1 shortest
path from any house to any other house. The houses are numbered from 1 to N.

Since Christmas is about to come so Santa has decided to hide gifts in these houses.
Santa will come to the city for M consecutive days. Each day he will come to a house
a first and will go till house b hiding a gift in each house that comes in the path.
                              (Image for sample input 1)
Can you tell the maximum number of gifts any house has after M days.

Input Format
First line of input contains 2 integers N - the number of houses in the city and
M - the number of days for which Santa comes to the city.

Next N - 1 lines contains two integers u and v meaning there is a road
between house u and house v, u != v.

Next M lines contains two integers ai and bi representing the starting and
ending house on ith visit of Santa.

Constraints
1 <= N <= 100, 000
1 <= M <= 100, 000
1 <= u, v <= N
1 <= a, b <= N

Output Format
A single integer representing the maximum number of gifts in any house.

Sample TestCase 1
Input
4 2
1 2
2 3
2 4
1 4
3 4
Output
2
Explanation
See the image above. The purple diamonds represent the gifts hidden during Santa’s first visit
and the red diamonds represent the gifts hidden during Santa’s second visit. We can see that
houses 2 and 4 has maximum number of gifts hidden. Both are having 2 gifts hidden, hence
the answer is 2.

Sample TestCase 2
Input
5 10
3 4
1 5
4 2
5 4
5 4
5 4
3 5
4 3
4 3
1 3
3 5
5 4
1 5
3 4
Output
9
Explanation
See the following image. The house number 4 has maximum number of hidden gifts i.e. 9.
(Ignore color of diamonds in this case)


19 4
1 7
7 8
8 12
11 7
1 6
1 14
10 6
2 6
3 6
13 6
14 15
5 14
4 14
10 9
17 2
18 3
5 16
13 19
19 17
16 9
10 19
12 1
#######3
'''

#f = open('in.txt','r')
#print(f.read())

'''
with open('in.txt') as f:
    line = f.readline().split(' ')
    line = [int(i) for i in line]
    nHouse, nDays = line
print(nHouse)
print(nDays)
'''

leafNode = []
linkNode = []
parentNode = []
##making path maps
def makePath(h1,h2,path):
    # combos : h1=h2=parent OR h1=parent,h2=leaf OR h1=parent,h2=link OR h1=link,h2=leaf OR h1=link,h2=link
    if h1 in parentNode and h2 in parentNode:  # h1=h2=parent
        #print('h1=h2=parent', h1, h2)
        if h1<h2:
            path[h1].append([h2])
        else:
            path[h2].append([h1])
    elif h1 in parentNode:
        if h2 in leafNode:  # h1=parent,h2=leaf
            #print('h1=parent,h2=leaf',h1,h2)
            path[h1].append([h2])
        elif h2 in linkNode:    #h1=parent,h2=link
            #print('h1=parent,h2=link',h1,h2)
            path[h1].append([h2])
    elif h2 in parentNode:
        if h1 in leafNode:  # h1=leaf,h2=parent
            # print('h1=leaf,h2=parent',h1,h2)
            path[h2].append([h1])
        elif h1 in linkNode:    #h1=link,h2=parent
            #print('h1=link,h2=parent',h1,h2)
            path[h2].append([h1])
    elif h1 in linkNode:
        if h2 in leafNode:  # h1=link,h2=leaf
            #print('h1=link,h2=leaf',h1,h2)
            p,ln = findParent([h1])
            path[p].append([h1,h2])
        elif h2 in linkNode:
            p,ln = findParent([h1,h2])
            path[p].append(p)
    elif h2 in linkNode:
        if h1 in leafNode:  # h1=leaf,h2=link
            #print('h1=leaf,h2=link',h1,h2)
            p,ln = findParent([h2])
            path[p].append([h2,h1])
        elif h1 in linkNode:
            p = findParent([h2,h1])
            path[p].append(p)

def findParent(linkN):
    for i in range(1, nHouse):
        # print(line[i])
        houseInfo = line[i].split(' ')
        houseInfo = [int(i) for i in houseInfo]
        h1, h2 = houseInfo
        if h1 == linkN[0] or h2 == linkN[0]:
            if h1 in parentNode:
                return (h1,linkN)
            elif h1 in linkNode:
                findParent([h1]+linkN)
            elif h2 in parentNode:
                return (h2,linkN)
            elif h2 in linkNode:
                findParent([h2]+linkN)
##end makePath

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
#print(houseOccurance)
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
for i in range(1, nHouse):
    # print(line[i])
    houseInfo = line[i].split(' ')
    houseInfo = [int(i) for i in houseInfo]
    h1, h2 = houseInfo
    #print(h1,h2)
    #makePath(h1,h2,path)
print(path)
'''
#checking for broken links - NO NEED as link-parent combination above somehow took care of it
for v in path.values():
    for i,lv in enumerate(v):
        print(lv)
'''
##

##Counting presents:for every key check if
houseCount = [0]*(nHouse+1)
for i in range(nHouse,nHouse+nDays):
    #print(line[i])
    houseInfo = line[i].split(' ')
    houseInfo = [int(i) for i in houseInfo]
    startHouse, endHouse = houseInfo
    # combos : leaf-leaf, leaf-link, leaf-parent, link-link, link-parent, parent-parent
    for k,v in path.items():
        flag = k1 = 0
        for i,lv in enumerate(v):
            print(k, lv)
            #if k == startHouse or k == endHouse:  # parent
            #    houseCount[k] += 1
            if startHouse in lv or endHouse in lv:
                if len(lv)>1 and lv[0] != startHouse and lv[0] != startHouse:   #leaf-link(pair)
                    if k1 != k:
                        flag = 0
                    if flag == 0:
                        houseCount[k] += 1
                        flag = 1
                        k1 = k
                    for ele in lv:
                        houseCount[ele] += 1
                        if ele == startHouse or ele == startHouse:
                            break
                elif len(lv) == 1:  #leaf(single)
                    if k1 != k:
                        flag = 0
                    if flag == 0:
                        houseCount[k] += 1
                        flag = 1
                        k1 = k
                    for ele in lv:
                        houseCount[ele] += 1

print(houseCount)
print(max(houseCount))
##
'''
2 ISSUES:
1. if both start and end are parents
2. if 2 parents have a link inbetween(current input:last line)
'''