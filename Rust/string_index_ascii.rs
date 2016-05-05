fn print(str: String) {
    for ascii in str.as_bytes() {
        print!("{} ", *ascii as char);
    }
}

fn main() {
    let a = "abcd".to_string();
    print(a);
}
