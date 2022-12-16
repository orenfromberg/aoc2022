import re

def distance(a: tuple, b: tuple) -> int:
    sum = 0
    for i in range(2):
        sum += abs(a[i]-b[i])
    return sum

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

def contains_line(y, row):
    sensor = row[0]
    radius = row[2]
    max_y = sensor[1] + radius
    min_y = sensor[1] - radius
    return y > min_y and y < max_y

def check_line(y, data):
    # filter data
    _data = [row for row in data if contains_line(y, row)]
    count = 0
    min_x = min([row[0][0] for row in _data])
    max_x = max([row[0][0] for row in _data])
    max_d = max([row[2] for row in _data])


    _from = min_x-max_d
    _to = max_x+max_d+1
    for x in range(min_x-max_d, max_x+max_d+1,1):
        result = False
        for i in [cant_be_beacon(x,y,row) for row in _data]:
            result = result or i
        if result:
            count+=1
            continue
    return count

def check_beacon(max, row):
    # check if sensor can possibly have a beacon in our search space
    sensor = row[0]
    radius = row[2]
    max_x = sensor[0] + radius
    min_x = sensor[0] - radius
    max_y = sensor[1] + radius
    min_y = sensor[1] - radius
    a= (min_x > 0 and min_x < max) or (max_x > 0 and max_x < max)
    b= (min_y > 0 and min_y < max) or (max_y > 0 and max_y < max)
    return a and b

def is_within_range_of_sensors(x,y,data):
    # iterate over sensors and check that this point is within range
    # or a beacon 
    foo = [row for row in data if distance(row[0],(x,y)) <= row[2]]
    if len(foo) == 0:
        return False
    else:
        return True

def is_beacon(x,y,data):
    foo = [row for row in data if (x,y) == data[1]]

def check_grid(max, data):
    # get sensors that have beacons in the search space
    _data = [row for row in data if check_beacon(max, row)]

    _beacons = [row[1] for row in _data]
    # iterate through search space
    for x in range(0,max+1,1):
        for y in range(0, max+1,1):
            # test if this coordinate is within range of any of the sensors
            if not is_within_range_of_sensors(x,y,_data) and (x,y) not in _beacons:
                print(f'{x} and {y}')
                return x * 4000000 + y

filename = './day15/data.txt'; arg = 2000000
# filename = './day15/testdata.txt'; arg = 20
data=[]
with open(filename) as f:
    for line in f:
        result = re.search(r"^Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)$", line.strip())
        a = (int(result.group(1)),int(result.group(2)))
        b = (int(result.group(3)),int(result.group(4)))
        data.append([a,b,distance(a,b)])
    
print(check_grid(arg,data))
