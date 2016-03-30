fn main() {
    let str = "abcdef";
    let mut a = &str[1..3];
    println!("{}", a);
    a = &str[0..4];
    println!("{}", a); 
}
