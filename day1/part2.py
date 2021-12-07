with open("input", "r") as file:
    data = file.read().strip().split("\n")

data = [int(x) for x in data]

booleans = []

def sum_of_three(data, index):
    return sum(data[index:index+3])

def compare(a, b):
    booleans.append(b > a)

def answer():
    print("The answer is: " + str(booleans.count(True)))

def solve():
    real_data = []
    for i in range(len(data) - 2):
        real_data.append(sum_of_three(data, i))
    for i in range(len(real_data) - 1):
        compare(real_data[i], real_data[i+1])

if __name__ == "__main__":
    solve()
    answer()