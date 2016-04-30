fn main() {
    let a = 10;
    let mut b = 1;
    match a {
        ref c => println!("a : {}", c),
    }
    match b {
    	ref mut d => {
    		*d += 1;
    		println!("b : {}", d);
    	},
    }
}
