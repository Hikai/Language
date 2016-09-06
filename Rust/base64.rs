fn matching_table(base64_code: usize) -> char {
    let table_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    table_base64.as_bytes()[base64_code] as char
}

fn three_bytes_encode(str_plain: &str) -> String {
    let rev_plain = str_plain.chars().rev().collect::<String>();
    let result_256 = to_256(&rev_plain);
    let result_64 = to_64(&rev_plain, result_256);
    let mut vec_chr = Vec::new();

    for chr in result_64 {
        vec_chr.push(matching_table(chr as usize));
    }

    let s = vec_chr.into_iter().collect();
    s
}

fn to_256(str_plain: &str) -> u32 {
    let mut count = 0;
    let mut index = 0;
    let mut result = 0;

    while index <= str_plain.len() - 1 {
        result += 256u32.pow(count as u32) * str_plain.as_bytes()[index] as u32;
        count += 1;
        index += 1;
    }

    result
}

fn to_64(str_plain: &str, value_256: u32) -> Vec<u32> {
    let byte_chrs = str_plain.len() * 8 / 6;
    let mut count = 0;
    let mut vec_result = Vec::new();

    while count != byte_chrs {
        vec_result.push(value_256 / 64u32.pow(count as u32) % 64);
        count += 1;
    }

    vec_result.reverse();
    vec_result
}

fn main() {
    let plain = "abc";
    println!("{} -> {}", plain, three_bytes_encode(&plain));
}
