fn test (tuples: (i32, f32)) -> (f32, i32) {
    let (integer, float) = tuples;
    (float, integer)
}

fn main() {
    let tuples = (123, 321.123);
    println!("{:?}", test(tuples));
}
