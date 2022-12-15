import re

def distance(a: tuple, b: tuple) -> int:
    sum = 0
    for i in range(2):
        sum += abs(a[i]-b[i])
    return sum

data=[]

with open('./day15/data.txt') as f:
    for line in f:
        result = re.search(r"^Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)$", line.strip())
        a = (int(result.group(1)),int(result.group(2)))
        b = (int(result.group(3)),int(result.group(4)))
        data.append([a,b,distance(a,b)])

min_x = min([row[0][0] for row in data])
max_x = max([row[0][0] for row in data])
max_d = max([row[2] for row in data])

# tests if (x,y) is not a beacon within range of this sensor
def cant_be_beacon(x,y,data) -> bool:
    sensor = data[0]
    beacon = data[1]
    d = data[2]
    _d = distance((x,y),sensor)
    if (x,y) != sensor and (x,y) != beacon and _d <= d:
        return True
    else:
        return False

y = 2000000
# y=10
count = 0
_from = min_x-max_d #-1605551
_to = max_x+max_d+1 #5599294
for x in range(min_x-max_d, max_x+max_d+1,1):
    result = False
    for i in [cant_be_beacon(x,y,row) for row in data]:
        result = result or i
    if result:
        count+=1
        continue

print(count)