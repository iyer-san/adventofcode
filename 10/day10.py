
filename = "adventofcode/10/input.txt"

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

adapters = read_integers(filename)

built_in_adapter = max(adapters) + 3
adapters.append(built_in_adapter)
adapters.sort()
current_jolt = 0

one_jolt_diff = 0
two_jolt_diff = 0
three_jolt_diff = 0

for jolt in adapters:
    if (jolt-current_jolt == 1):
        one_jolt_diff += 1
    elif (jolt-current_jolt == 2):
        two_jolt_diff += 1
    elif (jolt-current_jolt == 3):
        three_jolt_diff += 1
    current_jolt = jolt

print('part 1 {}'.format(one_jolt_diff*three_jolt_diff))
