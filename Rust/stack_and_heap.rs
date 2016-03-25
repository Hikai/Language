fn main() {
	let a = 10; // Stack allocate.
	let b = Box::new(20); // Heap allocate.
}
