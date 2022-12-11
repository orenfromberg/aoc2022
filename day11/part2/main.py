#test
# monkeys = [
# {
#     "items": [79, 98],
#     "op": ["mul",19],
#     "test": 23,
#     "if_true": 2,
#     "if_false": 3
# },
# {
#     "items": [54, 65, 75, 74],
#     "op": ["add",6],
#     "test": 19,
#     "if_true": 2,
#     "if_false": 0
# },
# {
#     "items": [79, 60, 97],
#     "op": ["pow",2],
#     "test": 13,
#     "if_true": 1,
#     "if_false": 3
# },
# {
#     "items": [74],
#     "op": ["add",3],
#     "test": 17,
#     "if_true": 0,
#     "if_false": 1
# },
# ]

# actual data
monkeys = [
{
    "items": [59, 74, 65, 86],
    "op": ["mul",19],
    "test": 7,
    "if_true": 6,
    "if_false": 2
},
{
    "items": [62, 84, 72, 91, 68, 78, 51],
    "op": ["add",1],
    "test": 2,
    "if_true": 2,
    "if_false": 0
},
{
    "items": [78, 84, 96],
    "op": ["add",8],
    "test": 19,
    "if_true": 6,
    "if_false": 5
},
{
    "items": [97, 86],
    "op": ["pow",2],
    "test": 3,
    "if_true": 1,
    "if_false": 0
},
{
    "items": [50],
    "op": ["add",6],
    "test": 13,
    "if_true": 3,
    "if_false": 1
},
{
    "items": [73, 65, 69, 65, 51],
    "op": ["mul",17],
    "test": 11,
    "if_true": 4,
    "if_false": 7
},
{
    "items": [69, 82, 97, 93, 82, 84, 58, 63],
    "op": ["add",5],
    "test": 5,
    "if_true": 5,
    "if_false": 7
},
{
    "items": [81, 78, 82, 76, 79, 80],
    "op": ["add",3],
    "test": 17,
    "if_true": 3,
    "if_false": 4
},
]

counts = [0 for x in range(len(monkeys))]
rounds = 0

tests = [monkey["test"] for monkey in monkeys]
factor = 1
for t in tests:
    factor *= t

# for monkey in monkeys:
while(rounds != 10000):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        # inspect items
        while(len(monkey["items"])):
            item = monkey["items"].pop(0)
            if(monkey["op"][0] == 'add'):
                item += monkey["op"][1]
            elif(monkey["op"][0] == 'mul'):
                item *= monkey["op"][1]
            elif(monkey["op"][0] == 'pow'):
                item *= item
            # item //= 3
            item = item % factor
            if (item % monkey["test"] == 0):
                monkeys[monkey["if_true"]]["items"].append(item)
            else:
                monkeys[monkey["if_false"]]["items"].append(item)
            counts[i] += 1
    rounds += 1
counts.sort()
print(counts.pop() * counts.pop())