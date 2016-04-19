fn main() {
    let a = 5;
    let b = 2;
    match (a, b) {
        (5, 2) => println!("a, b correct"),
        (5, _) => println!("a correct"),
        (_, 2) => println!("b correct"),
        (_, _) => println!("fail"),
    }
}
