use std::env;
use std::fs;

mod day11;

fn main() {
    let mut args = env::args().skip(1);
    let mut day: u32 = 11;
    let mut is_demo: bool = false;

    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--day" => {
                if let Some(input_day) = args.next() {
                    day = input_day.parse().expect("day must be a number");
                }
            }
            "--demo" => {
                is_demo = true;
            }
            _ => {}
        }
    }

    let input = load_input(day, is_demo);
    
    println!("=== Day {} {} ===", day, if is_demo { "(demo)" } else { "" });
    
    run_day(day, &input);
}

fn load_input(day: u32, is_demo: bool) -> String {
    let filename = if is_demo { "demo-input.txt" } else { "input.txt" };
    let path = format!("day{:02}/{}", day, filename);
    
    fs::read_to_string(&path)
        .unwrap_or_else(|_| panic!("Could not read file: {}", path))
}

fn run_day(day: u32, input: &str) {
    match day {
        11 => day11::solve(input),
        // Add more days here:
        // 12 => days::day12::solve(input),
        _ => eprintln!("Day {} not implemented yet!", day),
    }
}