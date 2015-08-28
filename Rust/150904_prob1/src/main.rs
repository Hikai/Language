// 150904 Reversing Prob1
use std::io;
use std::char;
use std::process;
fn main()
{
	let ans: [u32; 8] = [124, 63, 76, 124, 36, 34, 124, 34];
	let mut key: [u32; 8] = [0, 0, 0, 0, 0, 0, 0, 0];
	for i in 0..8 {
		let mut input = String::new();
		io::stdin().read_line(&mut input).ok().expect("Failed to read line");
		let input: u32 = input.trim().parse().ok().expect("Plz type a number");
		// ASCII range : 0 ~ 127
		if input > 127 {
			process::exit(1);
		}
		if input == ans[i] {
			key[i] = 1;
		}
	}
	println!("");
	if key[0] == 1 && key[1] == 1 && key[2] == 1 && key[3] == 1 && key[4] == 1 && key[5] == 1 && key[6] == 1 && key[7] == 1{
		// Print to key.
		for a in 0..8 {
			let chg = char::from_u32(ans[a]).unwrap();
			print!("{}", chg);
		}
	}
}