fn add_padding_encode(str_plain: &str) -> Vec<char>{
    let result_256 = to_256(str_plain);
    let result_64 = to_64(str_plain, result_256);
    let mut vec_chr = Vec::new();

    for ascii in result_64 {
        vec_chr.push(matching_table(ascii as usize));
    }

    let mut count = get_padding_count(3 - str_plain.len());
    while count != 0 {
        vec_chr.push('=');
        count -= 1;
    }

    vec_chr
}

fn base64_encode(str_plain: &str) -> String {
    let mut index = 0;
    let mut str_tmp = String::new();
    let mut str_result = String::new();

    while index != str_plain.len() {
        if (index % 3) == 0 && index != 0 {
            str_result.push_str(&(three_bytes_encode(&str_tmp)));
            str_tmp = String::new();
        }
        str_tmp.push(str_plain.as_bytes()[index] as char);
        index += 1;
    }
    if str_tmp.len() != 0 {
        str_result.push_str(&(three_bytes_encode(&str_tmp)));
    }

    str_result
}

fn matching_table(base64_code: usize) -> char {
    let table_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    table_base64.as_bytes()[base64_code] as char
}

fn get_padding_count(byte_rest: usize) -> u32 {
    let count = match byte_rest {
        1 => 1,
        2 => 2,
        _ => 0,
    };

    count
}

fn three_bytes_encode(str_plain: &str) -> String {
    let rev_plain = str_plain.chars().rev().collect::<String>();
    let mut vec_chr = Vec::new();

    if str_plain.len() != 3 {
        vec_chr = add_padding_encode(&rev_plain);
    }
    else {
        let result_256 = to_256(&rev_plain);
        let result_64 = to_64(&rev_plain, result_256);

        for ascii in result_64 {
            vec_chr.push(matching_table(ascii as usize));
        }
    }

    let s = vec_chr.into_iter().collect();
    s
}

fn to_256(str_plain: &str) -> u32 {
    let mut count = 0;

    if str_plain.len() != 3 {
        count = get_padding_count(3 - str_plain.len());
    }

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
    let byte_chrs = 4;
    let mut count = 0;

    if str_plain.len() != 3 {
        count = get_padding_count(3 - str_plain.len());
    }

    let mut vec_result = Vec::new();

    while count != byte_chrs {
        vec_result.push(value_256 / 64u32.pow(count as u32) % 64);
        count += 1;
    }

    vec_result.reverse();
    vec_result
}

fn main() {
    let plain = "abcd";
    println!("{}", base64_encode(&plain));
}
