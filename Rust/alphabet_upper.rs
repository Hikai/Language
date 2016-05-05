fn alphabet_upper(str: String) {
    for ascii in str.as_bytes() {
        let a = ascii - 32;
        print!("{} ", a as char);
    }
}

fn main() {
    let a = "abcd".to_string();
    alphabet_upper(a);
}
