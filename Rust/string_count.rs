fn count(str: String) -> i32 {
    let mut count = 0;
    for i in str.as_bytes() {
        count += 1;
    }
    count
}

fn main() {
    let a = "abcd".to_string();
    let b = count(a);
    println!("{}", b);
}
