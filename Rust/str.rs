fn main() {
    let str = "abcdef";
    let mut a = &str[1..3];
    let mut b = "abc";
    println!("{}", a);
    a = &str[0..4];
    println!("{}", a);
    b.push_str("def");
    println!("{}", b);
}
