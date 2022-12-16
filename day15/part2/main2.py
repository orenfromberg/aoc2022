import re

def distance(a: tuple, b: tuple) -> int:
    sum = 0
    for i in range(2):
        sum += abs(a[i]-b[i])
    return sum

filename = './day15/data.txt'; arg = 4000000
# filename = './day15/testdata.txt'; arg = 20
data=[]
with open(filename) as f:
    for line in f:
        result = re.search(r"^Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)$", line.strip())
        sensor = (int(result.group(1)),int(result.group(2)))
        beacon = (int(result.group(3)),int(result.group(4)))
        _d = distance(sensor, beacon)
        # data.append({
        #     "sensor": sensor,
        #     "beacon": beacon,
        #     "distance": d
        # })
        data.append([sensor,beacon,distance(sensor,beacon)])

# print(data)
points = {(y,x) for y in range(arg+1) for x in range(arg+1)}

# print(len(points))

# remove all points that are within manhattan distance from a sensor
for sensor,beacon,d in data:
    # print(f'{sensor} {beacon} {d}')
    sensor_x, sensor_y = sensor
    for j in range(d+1):
        for i in range(j+1):
            # if i == 0 and sensor in points:
            #     # remove the sensor itself
            #     points.remove(sensor)
            # else:
            _a = (sensor_x+i,sensor_y+(j-i))
            _b = (sensor_x+i,sensor_y-(j-i))
            _c = (sensor_x-i,sensor_y+(j-i))
            _d = (sensor_x-i,sensor_y-(j-i))
            if _a in points:
                points.remove(_a)
            if _b in points:
                points.remove(_b)
            if _c in points:
                points.remove(_c)
            if _d in points:
                points.remove(_d)

print(len(points))
x,y = points.pop()
print(x * 4000000 + y)