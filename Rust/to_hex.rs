fn to_hex (chr: u32) -> Vec<String> {
    let mut hex_operand = chr;
    let mut vec = Vec::new();

    if chr >= 16 {
        loop {
            
            if chr <= 15 {
                break;
            }
            
            vec.push(alphabet_match(hex_operand % 16));
            
            hex_operand /= 16;
            if hex_operand > 15 {
                continue;
            }
            else {
                vec.push(alphabet_match(hex_operand));
                break;
            }

        }
    }
    else {
        vec.push(alphabet_match(hex_operand));
    }

    vec.reverse();
    
    vec
}

fn alphabet_match (hex: u32) -> String {
    let alphabet;
    
    match hex {
        10 => alphabet = "a".to_string(),
        11 => alphabet = "b".to_string(),
        12 => alphabet = "c".to_string(),
        13 => alphabet = "d".to_string(),
        14 => alphabet = "e".to_string(),
        15 => alphabet = "f".to_string(),
        _ => alphabet = hex.to_string(),
    };

    alphabet
}

fn main() {
    // let a = "abcde";
    // let mut vec = Vec::new();
    let a = 63;
    let vec = to_hex(a as u32);
    // for c in a.chars() {
    //     print!("{} ", to_hex(c as u32));
    //     vec.push(c as u32);
    // }
    print!("{} hex -> ", a);
    for v in vec {
        print!("{}", v);
    }
}
