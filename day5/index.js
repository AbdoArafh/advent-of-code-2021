import colors from "colors";
import { readFileSync } from "fs";

const test = `0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2`;

class Point {
  constructor(x, y, token) {
    this.x = +x;
    this.y = +y;
    this.key = x.toString() + "," + y.toString();
  }
}

class Line {
  constructor(a, b) {
    this.a = a;
    this.b = b;
  }

  get isHorizontalOrVertical() {
    return this.a.x === this.b.x || this.a.y === this.b.y;
  }

  get points() {
    let { x: fx, y: fy } = this.a;
    let { x: sx, y: sy } = this.b;

    if (fx === sx && fy === sy) return [];
    if (fx === sx) {
      const arr = [];
      if (sy > fy) {
        for (let i = fy; i <= sy; i++) {
          arr.push(i);
        }
      } else {
        for (let i = sy; i <= fy; i++) {
          arr.push(i);
        }
      }

      return arr.map((y) => new Point(fx, y));
    }
    if (fy == sy) {
      const arr = [];
      if (sx > fx) {
        for (let i = fx; i <= sx; i++) {
          arr.push(i);
        }
      } else {
        for (let i = sx; i <= fx; i++) {
          arr.push(i);
        }
      }

      return arr.map((x) => new Point(x, fy));
    }
    if (fx > sx && fy > sy) {
      let temp = this.a;
      this.a = this.b;
      this.b = temp;
    }

    const slope = (this.b.y - this.a.y) / (this.b.x - this.a.x);

    console.log("reached here!");
    return [];
    // return [(x, int(x*slope)) for x in range(p1[0], p2[0]) if int(x*slope) == x*slope and (x, int(x*slope)) != p1]
  }
}

function strToLine(token) {
  const [_a, _b] = token.split(" -> ");
  const a = new Point(..._a.split(","), token);
  const b = new Point(..._b.split(","), token);
  return new Line(a, b);
}

class Board {
  constructor() {
    this._board = new Map();
    this._greatestX = 0;
    this._greatestY = 0;
    this._results = 0;
  }

  add(line) {
    line.points.forEach((p) => {
      if (this._board.has(p.key)) {
        this._board.set(p.key, this._board.get(p.key) + 1);
        if (this._board.get(p.key) === 2) {
          this._results++;
        }
      } else {
        this._board.set(p.key, 1);
        this._greatestX = p.x > this._greatestX ? p.x : this._greatestX;
        this._greatestY = p.y > this._greatestY ? p.y : this._greatestY;
      }
    });
  }

  render() {
    if (this._greatestX < 70) {
      const points = Array.from(Array(this._greatestX + 1)).map(() =>
        Array.from(Array(this._greatestY + 1)).map(() => 0)
      );
      for (const [key, value] of this._board.entries()) {
        const [x, y] = key.split(",").map((n) => +n);
        points[x][y] = value;
      }
      points.forEach((line) => console.log(line.reduce((a, b) => a + " " + b)));
    }

    console.log(
      "----------------------\nAnswer => " +
        this._results.toString().green +
        "\n"
    );
  }
}

function main() {
  const input = readFileSync("input").toString().trim();
  const _lines = input.split("\n");
  const lines = _lines.map((line) => strToLine(line));
  const straightLines = lines.filter((line) => line.isHorizontalOrVertical);

  const board = new Board();
  straightLines.forEach((line) => board.add(line));
  board.render();
}

main();
