fn main() {
	for i in 2..10 {
		for j in 1..10 {
			println!("{} * {} = {}", i, j, i * j);
		}
		println!("-------------");
	}
}