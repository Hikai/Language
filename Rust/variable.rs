fn main() {
	let (a, b) = (1, 2);
	let c: i32 = 3;
	let d = 4; // d: i32
	let e = 5; // e is not change.
	let mut f = 6; // f able change.
	println!("{}, {}, {}, {}, {}, {}", a, b, c, d, e, f);
	f = 7;
	let g = &mut f;
	println!("{}", g);
	let tuples = ((1, 2, 3), (4, 5, 6));
	println!("{:?}", tuples);
}
