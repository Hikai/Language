fn main() {
	enum Char {
		life {
			hp: i32,
			mp: i32,
		},
		stet {
			attack: i32,
		},
	}
	let a: Char = Char::life(hp: 100, mp: 50);
}
