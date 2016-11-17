use std::time::Duration;

fn main() {
    let sec = Duration::new(10, 5);
    println!("{}", sec.as_secs());
    println!("{}", sec.subsec_nanos());
}
