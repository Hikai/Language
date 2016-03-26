fn heap_allocate(value: i32) -> Box<i32> {
	let alloc = Box::new(value);
	alloc // same (return alloc;)
}

fn main() {
	let a = heap_allocate(10);
	println!("a : {}", a);
}
