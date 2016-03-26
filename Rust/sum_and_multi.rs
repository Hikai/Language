fn sum_and_multi(x: i32, y: i32) -> (i32, i32) {
    (x + y, x * y)
}

fn main() {
    let (a, b) = sum_and_multi(10, 20);
    println!("+ : {}, * : {}", a, b);
}
