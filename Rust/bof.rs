extern {
    pub fn strcpy(dest: *mut u8, src: *const u8) -> *mut u8;
    pub fn puts(s: *const u8) -> i32;
}

fn main() {
    let args: Vec<_> = std::env::args().collect();
    if args.len() != 2 {
        panic!("Usage: file argument")
    }
    let mut buf = [0u8; 200];
    unsafe {
      strcpy(buf.as_mut_ptr(), args[1].as_ptr());
      puts(buf.as_ptr());
    }
}
