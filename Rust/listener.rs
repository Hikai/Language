use std::io::{Read, Write, BufReader, BufRead};
use std::net::{TcpListener, TcpStream};
use std::thread;

fn handle_client(stream: TcpStream) {
    let mut reader = BufReader::new(stream);
    for line in reader.by_ref().lines() {
        if line.unwrap() == "" {
            break;
        }
    }

    println!("{:?}", reader);
    reader.into_inner().write_all(b"abcd").unwrap();
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:80").unwrap();
    for stream in listener.incoming() {
        match stream {
            Err(log) => println!("{:?}", log),
            Ok(mut stream) => {
                thread::spawn(move || {
                    handle_client(stream);
                });
            },
        };
    }

    drop(listener);
}
