fn main() {
    let server = Server::new("127.0.0.1:8080".to_string());

    let _get = Method::GET;
    let _put = Method::PUT;
    let _delete = Method::DELETE;

    let _new_req: Request;

    server.run();
}

struct Server {
    addr:String,
}
impl Server {
    fn new(addr: String) -> Self {
        Self{ addr }
    }
    fn run(self) {
        println!("Listening on {}", self.addr);
    }
}


enum Method {
    GET, PUT, DELETE,
}

struct Request {
    path: String,
    query_string: String,
    method: Method,
}

