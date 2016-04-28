fn main() {
    let a = 10;
    match a {
        ref b => println!("a : {}", b),
    }
}
