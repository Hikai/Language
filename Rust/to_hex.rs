fn to_hex (chr: u32) -> Vec<u32> {
    let mut hex_operand = chr;
    let mut vec = Vec::new();

    loop {
        
        if chr <= 15 {
            break;
        }
        
        vec.push(hex_operand % 16);
        
        hex_operand /= 16;
        if hex_operand > 15 {
            continue;
        }
        else {
            vec.push(hex_operand);
            break;
        }

    }

    vec.reverse();
    
    vec
}

fn main() {
    let a = 256;
    let vec = to_hex(a);
    print!("{} hex -> ", a);
    for v in vec {
        print!("{}", v);
    }
}
