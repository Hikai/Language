fn main() {
    // let table_base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    let plain = "abc";
    // let bytes = plain.len() * 8 / 6;
    let padding = plain.len() * 8 % 6;
    if padding != 0 {
        // padding process.
    }
    let mut result = 0;
    let mut index = plain.len() - 1;
    let mut count = 0;
    while index >= 0 {
        result += (256u32.pow(count) * plain.as_bytes()[index] as u32);
        // println!("{}", plain.as_bytes()[index]);
        if index == 0 {
            break;
        }
        index -= 1;
        count += 1;
    }
    println!("{}", result);
}
