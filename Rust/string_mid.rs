fn mid(str: &str, std: usize, num: usize) -> Vec<char> {
    if std > num {
        panic!("Error standart > number");
    }
    let mut buf_char: Vec<char> = Vec::new();
    let mut i = std;
    loop {
        if i == num + 1 {
            break;
        }
        buf_char.push(str.as_bytes()[i] as char);
        i += 1;
    }
    
    buf_char
}

fn main() {
    let a = "abcdefgh";
    println!("{:?}", mid(a, 1, 2));
}
