use std::cmp::Ordering;
use std::io;

fn main() {
    let mut a = String::new();
    let mut b = String::new();
    println!("Input 1 : ");
    io::stdin().read_line(&mut a).expect("failed to read line");
    println!("Input 2 : ");
    io::stdin().read_line(&mut b).expect("failed to read line");
    match a.cmp(&b) {
        Ordering::Less => println!("a small"),
        Ordering::Greater => println!("a big"),
        Ordering::Equal => println!("equal"),
    }
}
