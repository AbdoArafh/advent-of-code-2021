from re import split

def format(cell):
    return cell["value"].rjust(2, " ")

def log(winner):
    print()
    winner.render()
    unmarked = winner.unmarked()
    print(f"\nLast Move                 => {winner.last_play}")
    print(f"The sum of unmarked cells => {sum(unmarked)}")
    print(f"\nThe solution is           => {sum(unmarked) * winner.last_play}")

class Board:
    def __init__(self, input):
        self.grid = []
        self.last_play = -1
        self.won = False
        for line in input.strip().split("\n"):
            self.grid.append([])
            for cell in split(r" +", line.strip()):
                self.grid[-1].append({"value": cell, "checked": False})

    def unmarked(self):
        arr = []
        for i in self.grid:
            for j in i:
                if not j["checked"]:
                    arr.append(int(j["value"]))
        return arr

    def render(self):
        for i in self.grid:
            for j in i:
                if j["checked"]:
                    print('\x1b[6;0;42m' + format(j) + '\x1b[0m', end=" ")
                else:
                    print(format(j), end=" ")
            print()

    def play(self, target):
        i, j = self.find(target)
        if i == -1: return
        self.grid[i][j]["checked"] = True
        self.last_play = int(target)

    def find(self, target):
        for (i, row) in enumerate(self.grid):
            for (j, cell) in enumerate(row):
                if cell["value"] == target:
                    return (i, j)
        return (-1, -1)

    def play_multiple(self, targets):
        for target in targets:
            self.play(target)

    def check_win(self):
        for row in self.grid:
            if [x["checked"] for x in row].count(True) == len(row):
                self.won = True
                return (True, [int(x["value"]) for x in row])
        for i in range(len(self.grid)):
            arr = [self.grid[j][i]["checked"] for j in range(len(self.grid[0]))]
            if arr.count(True) == len(self.grid):
                self.won = True
                return (True, [int(self.grid[j][i]["value"]) for j in range(len(self.grid[0]))])
        return False


class Game_master:
    def __init__(self, raw_data, part=1):
        self.part = part
        arr = raw_data.strip().split("\n\n")
        self.turns = arr[0].strip().split(",")
        raw_boards = arr[1:]
        self.boards = [Board(x) for x in raw_boards]
    def start(self):
        if self.part == 1:
            for turn in self.turns:
                for board in self.boards:
                    board.play(turn)
                    isWinner = board.check_win()
                    if isWinner:
                        log(board)
                        return
        elif self.part == 2:
            winner = False
            for turn in self.turns:
                for board in self.boards:
                    if board.won: continue
                    board.play(turn)
                    isWinner = board.check_win()
                    if isWinner:
                        winner = board
            print("-" * 20 + " Part Two " + "-" * 20)
            log(winner)



game_master = Game_master(open("input", 'r').read(), 1)
game_master.start()
game_master = Game_master(open("input", 'r').read(), 2)
game_master.start()
