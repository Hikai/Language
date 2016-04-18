struct A {
    x: i32,
    y: i32,
}

trait Test { // function prototype declaration
    fn multi(&self) -> i32;
}

impl Test for A { // function definition
    fn multi(&self) -> i32 {
        self.x * self.y
    }
}

fn main() {
    let a = A {
        x: 123,
        y: 321,
    };
    println!("Result : {}", a.multi());
}
