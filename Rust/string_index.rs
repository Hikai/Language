fn print(str: String) {
    for ascii in str.as_bytes() {
        print!("{} ", ascii);
    }
}

fn main() {
    let a = "abcd".to_string();
    print(a);
}
