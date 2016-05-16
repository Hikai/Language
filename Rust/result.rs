fn bo(x: i32) -> Result<i32, i32> {
    if x == 1 {
        Ok(1 + 1)
    }
    else {
        Err(1)
    }
}

fn main() {
    let a = bo(1);
}