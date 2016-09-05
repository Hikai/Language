fn main() {
    let plain = "abc";
    let table_base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    let mut index = plain.len() - 1;
    let mut count: usize = 0;
    let mut result = 0;
    let mut vec_result = Vec::new();
    let byte_chrs: usize = plain.len() * 8 / 6;
    let byte_rest = plain.len() * 8 % 6;


    while index != 0 {
        result += 256u32.pow(count as u32) * plain.as_bytes()[index] as u32;
        if index == 1 {
            index -= 1;
            count += 1;
            result += 256u32.pow(count as u32) * plain.as_bytes()[index] as u32;

            break;
        }
        else {
            index -= 1;
            count += 1;
        }
    }
    
    count = 0;
    drop(index);
    
    while count != byte_chrs {
        vec_result.push(result / (64u32.pow(count as u32)) % 64);
        count += 1;
    }
    vec_result.reverse();

    for v in vec_result {
        count = v as usize;
        println!("{}, {}", v, table_base.as_bytes()[count] as char);
    }
}
