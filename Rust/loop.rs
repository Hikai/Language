fn main() {
    let mut i = 0;
    loop { // infinite loop
        println!("A");
        i += 1;
        if i == 10 {
            break;
        }
    }
    let mut sum = 0;
    i = 1;
    while i <= 100 {
        sum += i;
        i += 1;
    }
    println!("Sum : {}", sum);
}
