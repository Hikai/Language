struct A {
    x: i32,
}

impl Drop for A {
    fn drop(&mut self) {
        println!("Drop");
    }
}

fn main() {
    let a = A {x: 0};
    println!("{}", a.x);
}
