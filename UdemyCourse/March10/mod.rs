fn main() {
    let s1 = Server::Server::new("127.0.0.1:8080".to_string());
    println!("{:?}", s1);
    s1.run();
}

mod Server {
    #[derive(Debug)]
    enum Method {
        DELETE,
        GET,
    }
    #[derive(Debug)]
    pub struct Server {
        addr: String,
        path: String,
        query: Option<String>,
        method: Method,
    }

    impl Server {
        pub fn new(addr: String) -> Self {
            let path = String::new();
            let query = Some(String::new());
            let method = Method::DELETE;
            Self {
                addr,
                path,
                query,
                method,
            }
        }

        pub fn run(self) {
            println!("running server!!");
        }
    }
}
