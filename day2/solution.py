class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def add(self, other):
        self.x += other.x
        self.y += other.y
    def mult(self, factor):
        self.x *= factor
        self.y *= factor
    def copy(self):
        return Vector2D(self.x, self.y)


def print_answer(part: str, pos: Vector2D):
    print(f"{'-' * 20}\nPART {part}:\nDepth: {pos.x}\nHorizontal: {pos.y}\nAnswer: {pos.x * pos.y}\n{'-' * 20}")

def part1(data):
    vectors = {
        "forward": Vector2D(1, 0),
        "down": Vector2D(0, 1),
        "up": Vector2D(0, -1)
    }
    pos = Vector2D()
    for line in data:
        name, factor = line.split(" ")
        vector = vectors[name].copy()
        vector.mult(int(factor))
        pos.add(vector)
    print_answer("ONE", pos)

def part2(data):
    aim = 0
    pos = Vector2D()
    commands = {
        "down": lambda x: aim + x,
        "up": lambda x: aim - x,
    }
    for line in data:
        command, factor = line.split(" ")
        factor = int(factor)
        if command in commands:
            aim = commands[command](factor)
        elif command == "forward":
            pos.add(Vector2D(factor * aim, factor))
    print_answer("TWO", pos)


if __name__ == "__main__":
    with open("input", "r") as file:
        data = file.read().strip().split("\n")
    part1(data)
    part2(data)
    
