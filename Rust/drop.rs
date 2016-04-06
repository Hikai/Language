struct A {
    x: i32,
}

impl A {
    fn increase(&self, x: i32) -> i32 {
        x + 1
    }
}

impl Drop for A {
    fn drop(&mut self) {
        println!("A drop");
    }
}

fn main() {
    let a = A {x: 2};
    let b = a.increase(a.x);
    println!("{}", b);
}
