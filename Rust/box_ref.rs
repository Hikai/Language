fn main() {
    let five = Box::new(5);
    println!("{}", five);
    let a = &five;
    println!("{} {}", a, five);
}
