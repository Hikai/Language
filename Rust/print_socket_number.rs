use std::net::{TcpListener, TcpStream};

fn print_info(stream: &TcpStream) {
    let dest_addr = stream.local_addr();
    let src_addr = stream.peer_addr();
    println!("{:?}, {:?}", dest_addr, src_addr)
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:80").unwrap();
    for stream in listener.incoming() {
        match stream {
            Err(log) => println!("{:?}", log),
            Ok(stream) => print_info(&stream)
        };
    }

    drop(listener);
}
