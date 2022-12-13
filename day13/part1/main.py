# -1 = not in the right order
# 0 = equal
# 1 = in the right order

def compare(left, right) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        elif left < right:
            return 1
        else:
            return -1
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) > 0:
            return 1
        elif len(left) > 0 and len(right) == 0:
            return -1
        elif len(left) == 0 and len(right) == 0:
            return 0
        result = compare(left[0], right[0])
        if result == 0:
            return compare(left[1:], right[1:])
        else:
            return result
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left],right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left,[right])    

sum = 0
count = 1
with open('./day13/data.txt') as f:
    while(True):
        left = eval(f.readline())
        right = eval(f.readline())
        result = compare(left, right)
        if result != -1:
            sum += count
        count += 1
        line = f.readline()
        if not line:
            break

print(sum)