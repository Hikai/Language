fn main() {
    let mut a = 1;
    {
        let z = 20; // if exit block, delete variable.
        a *= z;
    }
    println!("{}", a);
}
