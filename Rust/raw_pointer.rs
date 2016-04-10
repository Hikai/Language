fn main() {
    let a = 1;
    let mut b = 2;
    let raw_a = &a as *const i32;
    let raw_a2 = &a;
    let raw_mut_b = &mut b as *mut i32;
    let raw_mut_b2 = &mut b;
    let mut refer = unsafe { *raw_a };
    println!("{}", refer);
    refer = *raw_a2;
    println!("{}", refer);
    refer = unsafe { *raw_mut_b };
    println!("{}", refer);
    refer = *raw_mut_b2;
    println!("{}", refer);
}
