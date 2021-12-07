def get_bits(data, i):
    return [x[i] for x in data]


def decide(bits, target):
    return bits.count(target) > len(bits) / 2 and "1" or "0"

def findMatching(data: list, index: int, more: bool) -> list:
    count1 = get_bits(data, index).count("1")
    count0 = get_bits(data, index).count("0")
    target = count1 > count0 and "1" or "0"
    if count1 == count0:
        target = more and "1" or "0"
    if more:
        return [bits for bits in data if bits[index] == target]
    else:
        return [bits for bits in data if bits[index] != target]

def part1(data):
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        bits = get_bits(data, i)
        gamma += decide(bits, "1")
        epsilon += decide(bits, "0")
    print(f"{'-' * 20}\nGamma:   {gamma}\nEpsilon: {epsilon}\nAnswer:  {int(gamma, 2) * int(epsilon, 2)}\n{'-' * 20}")

def solve(data, more):
    index = 0
    matching = findMatching(data, index, more)
    while len(matching) > 1 and not more:
        matching = findMatching(data, index, more)
        index += index % len(matching)
    print(matching[0])

def part2(data):
    oxygen = solve(data, True)
    co2 = solve(data, False)

if __name__ == "__main__":
    with open("test", "r") as file:
        data = file.read().strip().split("\n")
    part1(data)
    # part2(data)