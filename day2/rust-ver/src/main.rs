use rust_ver::App;
use std::env;
use std::fs;

fn main() {
    let mut args = env::args();
    args.next();

    if let Some(filename) = args.next() {
        let input = String::from(
            fs::read_to_string(filename)
                .expect("Couldn't read file")
                .trim_end(),
        );
        let mut app = App::from(&input);
        app.run();
        app.print_result();
    } else {
        eprintln!("No file name was provided");
        std::process::exit(1);
    }
}
