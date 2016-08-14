fn to_hex (chr: u32) -> String {
    let mut hex_operand = chr;
    let mut vec_hex = Vec::new();
    let mut str_result = String::new();

    if chr >= 16 {
        loop {
            
            if chr <= 15 {
                break;
            }
            
            vec_hex.push(alphabet_match_lower(hex_operand % 16));
            
            hex_operand /= 16;
            if hex_operand > 15 {
                continue;
            }
            else {
                vec_hex.push(alphabet_match_lower(hex_operand));
                break;
            }

        }
    }
    else {
        vec_hex.push(alphabet_match_lower(hex_operand));
    }

    vec_hex.reverse();
    
    for item in vec_hex {
        str_result.push_str(item.as_ref());
    }
    
    str_result
}

fn alphabet_match_lower (hex: u32) -> String {
    let alphabet = match hex {
        10 => "a".to_string(),
        11 => "b".to_string(),
        12 => "c".to_string(),
        13 => "d".to_string(),
        14 => "e".to_string(),
        15 => "f".to_string(),
        _ => hex.to_string(),
    };

    alphabet
}

fn main() {
    let a = "abcde";
    let mut vec_hex = Vec::new();
    for c in a.chars() {
        print!("{} ", to_hex(c as u32));
        vec_hex.push(c as u32);
    }
}
