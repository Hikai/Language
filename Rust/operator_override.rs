use std::ops::Mul;
trait Calc<T> {
    fn size(&self) -> T;
}

struct Square<T> {
    x: T,
    y: T,
}

impl<T> Calc<T> for Square<T> where T: Mul<Output=T> + Copy {
    fn size(&self) -> T {
        self.x * self.y
    }
}

fn main() {
    let a = Square {
        x: 10,
        y: 20,
    };
    println!("Size : {}", a.size());
}
