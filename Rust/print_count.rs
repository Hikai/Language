use std::time::Duration;
use std::thread;

fn print_count(start: u32, end: u32, increament: u32) {
    for i in start..end {
        print!("\r{}", i);
        i += increament;
    }
}

fn main() {
    print_count(0, 1000000);
}
