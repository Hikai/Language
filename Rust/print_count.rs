use std::time::Duration;
use std::thread;

fn incre_print_count(start: u32, end: u32, increment: u32) {
    for i in start..end {
        print!("\r{}", i);
        i += increment;
    }
}

fn decre_print_count(start: u32, end: u32, decrement: u32) {
    for i in (start..end).rev() {
        print!("\r{}", i);
        i -= decrement;
    }
}

fn main() {
    incre_print_count(0, 1000000, 2);
    println!("");
    decre_print_count(0, 1000000, 2);
}
