fn main() {
    let mut a = 5;
    {
        let b = &mut a;
        *b += 1;
    }
    println!("{}", a);
}
