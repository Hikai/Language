use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("a.txt");
    let display = path.display();

    let mut file = match File::open(&path) {
        Err(log) => panic!("failed to open: {}\n -> {}", display, log.description()),
        Ok(file) => file,
    };

    let mut content = String::new();
    match file.read_to_string(&mut content) {
        Err(log) => panic!("failed to read: {}\n -> {}", display, log.description()),
        Ok(_) => print!("{}\n\n{}", display, content),
    };
}