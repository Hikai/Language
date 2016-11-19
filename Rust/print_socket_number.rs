use std::net::TcpListener;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:80").unwrap();
    for stream in listener.incoming() {
        match stream {
            Err(log) => println!("{:?}", log),
            Ok(stream) => println!("{:?}", stream)
        };
    }

    drop(listener);
}
