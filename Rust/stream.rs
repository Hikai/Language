use std::net::TcpStream;

fn main() {
    let stream = TcpStream::connect("127.0.0.1:80").unwrap();
    println!("{:?}", stream);
}
