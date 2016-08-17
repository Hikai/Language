use std::env;
use std::ffi::OsStr;
use std::fs::File;
use std::io::Read;
use std::path::Path;

fn file_read(ref_path: &OsStr) -> [u8; 1024] {
    let mut byte_store = [0u8; 1024];

    let path = Path::new(ref_path);
    let mut file = File::open(&path).unwrap();
    file.read(&mut byte_store).unwrap();

    return byte_store;
}

fn ref_str_to_ref_osstr(arg_filename: &str) -> &OsStr {
    let ref_osstr: &OsStr = OsStr::new(arg_filename);

    return ref_osstr;
}

fn main() {
    let args: Vec<_> = env::args().collect();

    if args.len() != 2 {
        println!("Usage: binary_open.exe [filename]");
        std::process::exit(1);
    }

    let ref_osstr: &OsStr = ref_str_to_ref_osstr(&args[1]);

    let store = file_read(ref_osstr);

    let mut count = 0;
    for byte in store.iter() {
        print!("{:3} ", byte);
        if count >= 7 {
            println!("");

            count = 0;
        }
        else {
            count += 1;
        }
    }
}
