fn main() {
    let a = (10, 5);
    match a {
        (x, y) if x >= 10 && y < 10 => println!("{}, {}", x, y),
        (x, _) if x >= 10 => println!("{}", x),
        (_, y) if y < 10 => println!("{}", y),
        _ => println!("not"),
    }
}
