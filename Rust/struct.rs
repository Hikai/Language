struct Test {
    a: i32,
    b: i32,
}

fn main() {
    let a = Test {a: 1, b: 0};
    let mut b = Test{a: 0, b: 1};
    let mut c = Test{a: 3, b: 0};
    b.b += 1;
    c = Test{b: 2, .. c};
    println!("{}, {}", a.a, a.b);
    println!("{}, {}", b.a, b.b);
    println!("{}, {}", c.a, c.b);
}
