use std::io::prelude::*;
use std::net::TcpStream;

fn main() {
    let mut stream = TcpStream::connect("127.0.0.1:80").unwrap();
    let _ = stream.write_all(b"abcdef").unwrap();
    let mut buf = [0u8; 128];
    let _ = stream.read(&mut buf);

    for i in buf.iter() {
        print!("{}", *i as char);
    }

    drop(stream);
}
