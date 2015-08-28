use std::env;

fn main()
{
	let args: Vec<_> = env::args().collect(); // Get command line argument.
	if args.len() != 2 {
		println!("Usage : file argv[1]");
	}
	println!("{}", args[1]);
	if (16303 - 8725).to_string() == args[1] { // Compare between args[1] and "7578".
		println!("K3Y");
		println!(": .`v5-)4-@"); // Key. XD
	} else {
		println!(":P"); // :P
	}
}