use std::io;

fn main() {
    plet mut input = String::new();
    println!("1 or more input");
    io::stdin().read_line(&mut input).expect("read_line fail");
    if input < 1 {
        panic!("panic");
    }
    println!("{}", input);
}
