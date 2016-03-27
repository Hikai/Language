struct Test {
    a: i32,
    b: i32,
}

fn main() {
    let a = Test {a: 1, b: 0};
    let mut b = Test{a:0, b: 1};
    b.b += 1;
    println!("{}, {}", a.a, a.b);
    println!("{}, {}", b.a, b.b);
}
