
pub mod webserver {
    use std::net::{TcpListener, TcpStream};
    pub struct TcpServer{
        addr:String,        
        conns:i32,
        server:i32,
    }

    impl TcpServer {
        pub fn new(address:String) -> Self {
            let a = String::from("..");
            let myself = TcpServer{addr:address, 
            conns:0,
            server:-1};
            myself.server = TcpListener::bind(address).expect("FAILED to BIND!!!");
            myself
        }
    }
}
