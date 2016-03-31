struct Test {
    a: i32,
    b: i32,
}

struct Test2<T> {
    x: T,
    y: T,
}

fn main() {
    let a = Test {a: 1, b: 0};
    let mut b = Test {a: 0, b: 1};
    let mut c = Test {a: 3, b: 0};
    let d = Test2 {x: 10, y: 20};
    let e = Test2 {x: 10.1, y: 20.2};
    b.b += 1;
    c = Test{b: 2, .. c};
    println!("{}, {}", a.a, a.b);
    println!("{}, {}", b.a, b.b);
    println!("{}, {}", c.a, c.b);
    println!("{}, {}", d.x, d.y);
    println!("{}, {}", e.x, e.y);
}
