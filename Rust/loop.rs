fn main() {
    loop { // infinite loop
        println!("A");
    }
    let mut sum = 0;
    let mut i = 1;
    while i <= 100 {
        sum += i;
        i += 1;
    }
    println!("Sum : {}", sum);
}
