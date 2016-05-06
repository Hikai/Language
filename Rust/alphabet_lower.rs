fn alphabet_lower(str: String) {
    for ascii in str.as_bytes() {
        let a = ascii + 32;
        print!("{} ", a as char);
    }
}

fn main() {
    let a = "ABCD".to_string();
    alphabet_lower(a);
}
