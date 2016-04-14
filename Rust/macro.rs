macro_rules! match_exam {
    ($x:expr) => (match $x {
        1 => 123,
        _ => 321,
    });
}

fn main() {
    println!("{}", match_exam!(3));
}
