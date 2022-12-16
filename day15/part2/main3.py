import re

def distance(a: tuple, b: tuple) -> int:
    sum = 0
    for i in range(2):
        sum += abs(a[i]-b[i])
    return sum

def is_within_boundaries(x,y,m):
    return x >= 0  and x <= m and y >= 0 and y <= m

def is_within_search_space(row,m):
    sensor,_,d = row
    sensor_x, sensor_y = sensor
    for i in range(d+1):
        _a = sensor_x+i
        _b = sensor_x-i
        _c = sensor_y+(d-i)
        _d = sensor_y-(d-i)
        if is_within_boundaries(_a,_c,m) and is_within_boundaries(_a,_d,m)  and is_within_boundaries(_b,_c,m) and is_within_boundaries(_b,_d,m):
            return True
    return False

def is_within_range_of_sensors(point, data):
    return any([ distance(point,sensor) <= d for sensor,_,d in data ])


def part2(filename, m):
    data=[]
    with open(filename) as f:
        for line in f:
            result = re.search(r"^Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)$", line.strip())
            sensor = (int(result.group(1)),int(result.group(2)))
            beacon = (int(result.group(3)),int(result.group(4)))
            _d = distance(sensor, beacon)
            data.append([sensor,beacon,distance(sensor,beacon)])

    # filter out sensors that don't have beacons in the search space
    _data = [x for x in data if is_within_search_space(x,m)]
    # print(_data)

    # trace the outline of beacon radius and if it is within search space
    # add the point to a set
    points = set()

    for row in _data:
        sensor,beacon,d = row
        sensor_x, sensor_y = sensor
        d += 1
        for i in range(d+1):
            _a = sensor_x+i
            _b = sensor_x-i
            _c = sensor_y+(d-i)
            _d = sensor_y-(d-i)
            if is_within_boundaries(_a,_c,m):
                points.add((_a,_c))
            if is_within_boundaries(_a,_d,m):
                points.add((_a,_d))
            if is_within_boundaries(_b,_c,m):
                points.add((_b,_c))
            if is_within_boundaries(_b,_d,m):
                points.add((_b,_d))

    # now points contain the search set of points
    print(len(points))

    # iterate through the points and see if it is not within range of any sensors
    points = [*points]
    # result = [point for point in points if not is_within_range_of_sensors(point,data)]

    count = 0
    for point in points:
        if not is_within_range_of_sensors(point, data):
            _x, _y = point
            print(_x * 4000000 + _y)
            return
        count+=1
        if(count % 100000 == 0):
            print(count)


    # print((14,11) in result)
    # print(result)
    # print(is_within_range_of_sensors((14,11),_data))
    # for point in points:
        # for sensor,beacon,d in _data:

    # # remove all points that are within manhattan distance from a sensor
    # for sensor,beacon,d in data:
    #     sensor_x, sensor_y = sensor
    #     for i in range(j+2):
    #         # if i == 0 and sensor in points:
    #         #     # remove the sensor itself
    #         #     points.remove(sensor)
    #         # else:
    #         _a = (sensor_x+i,sensor_y+(j-i))
    #         _b = (sensor_x+i,sensor_y-(j-i))
    #         _c = (sensor_x-i,sensor_y+(j-i))
    #         _d = (sensor_x-i,sensor_y-(j-i))
    #         if _a in points:
    #             points.remove(_a)
    #         if _b in points:
    #             points.remove(_b)
    #         if _c in points:
    #             points.remove(_c)
    #         if _d in points:
    #             points.remove(_d)

    # print(len(points))
    # x,y = points.pop()
    # print(x * 4000000 + y)


part2('./day15/data.txt', 4000000)
# part2('./day15/testdata.txt', 20)