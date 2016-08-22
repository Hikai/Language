use std::net::{TcpListener, TcpStream};
use std::thread;

fn handle_client(stream: TcpStream) {
    println!("Peer: {:?}, Local: {:?}", stream.peer_addr(), stream.local_addr());
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:80").unwrap();
    for stream in listener.incoming() {
        match stream {
            Err(log) => println!("{:?}", log),
            Ok(stream) => {
                thread::spawn(move || {
                    handle_client(stream);
                });
            },
        };
    }

    drop(listener);
}
