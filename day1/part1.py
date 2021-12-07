with open("input", "r") as file:
    data = file.read().strip().split("\n")

data = [int(x) for x in data]

booleans = []

def test(a, b):
    return b > a

def solve(data):
    for i in range(len(data) - 1):
        booleans.append(test(data[i], data[i+1]))

if __name__ == "__main__":
    solve(data)
    answer = booleans.count(True)
    print(answer)
