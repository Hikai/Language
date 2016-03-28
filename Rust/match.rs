fn sum(x: i32) -> i32 {
    x + 1
}

fn main() {
    match sum(1) {
        1 => println!("1"),
        2 => println!("2"),
        3 => println!("3"),
        _ => println!("Default"),
    }
}
