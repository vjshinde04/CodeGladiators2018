with open('in5.txt') as f:
    line = f.readlines()

cityInfo = line[0].split(' ')
cityInfo = [int(i) for i in cityInfo]
nHouse, nDays = cityInfo

for i in range(1,nHouse):
    #print(line[i])
    houseInfo = line[i].split(' ')
    houseInfo = [int(i) for i in houseInfo]
    h1, h2 = houseInfo

    h1 += 19
    h2 += 19
    print(h1,h2)