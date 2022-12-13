# -1 = not in the right order
# 0 = equal
# 1 = in the right order
def compare(left, right) -> int:
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

# true if in the right order, false if not
def test_pair(left: str, right: str) -> bool:
    result = compare(eval(left),eval(right))
    return result != -1

lines = []
with open('./day13/data.txt') as f:
    for _line in f:
        line = _line.strip()
        if line != '':
            lines.append(line.strip())

lines.append('[[2]]')
lines.append('[[6]]')

done = False
while not done:
    modified=False
    for i in range(len(lines)-1):
        left = lines[i]
        right = lines[i+1]
        if not test_pair(lines[i], lines[i+1]):
            buf = lines[i]
            lines[i] = lines[i+1]
            lines[i+1] = buf
            modified=True
    if not modified:
        done = True

for i in range(len(lines)):
    if lines[i] == '[[2]]':
        left = i+1
    if lines[i] == '[[6]]':
        right = i+1

print(left * right)