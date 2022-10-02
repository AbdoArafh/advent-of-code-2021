#[derive(Debug)]
enum Direction {
    Forward(isize),
    Down(isize),
    Up(isize),
}

#[derive(Debug)]
struct Point(isize, isize);

impl Point {
    fn new() -> Self {
        Self(0, 0)
    }

    fn apply_dir(&mut self, dir: &Direction) {
        match dir {
            Direction::Forward(n) => self.0 += *n,
            Direction::Up(n) => self.1 -= *n,
            Direction::Down(n) => self.1 += *n,
        }
    }

    fn get_result(&self) -> isize {
        self.0 * self.1
    }
}
pub struct App {
    directions: Vec<Direction>,
    coords: Point,
}

impl App {
    pub fn from(input: &str) -> Self {
        let directions: Vec<Direction> = input
            .lines()
            .map(|line| {
                let result: Vec<&str> = line.split(" ").collect();
                let n = result[1].parse().expect("Not an integer");
                let dir = match result[0] {
                    "forward" => Direction::Forward(n),
                    "down" => Direction::Down(n),
                    "up" => Direction::Up(n),
                    _ => panic!("An unknown command"),
                };

                dir
            })
            .collect();

        Self {
            directions,
            coords: Point::new(),
        }
    }

    pub fn run(&mut self) {
        for direction in &self.directions {
            self.coords.apply_dir(direction);
        }
    }

    pub fn result(&self) -> isize {
        self.coords.get_result()
    }

    pub fn print_result(&self) {
        let dir_len = self.directions.len();
        if dir_len < 10 {
            println!("directions: {:?}", self.directions);
        }
        println!("number of directions: {}", dir_len);
        println!("final coords: {:?}", self.coords);
        println!("final result: {}", self.coords.get_result());
    }
}
