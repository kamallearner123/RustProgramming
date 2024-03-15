use http::http::{request, Server, REQUEST_TYPE};
mod http;

fn main() {
    let reqType: REQUEST_TYPE = REQUEST_TYPE::DELETE;
    let r1 = request::new("data".to_string());
    r1.print_details();

    let s1 = Server::new("127.0.0.1:8080".to_string());
    println!("Server details : {:?}", s1);
    s1.run();
}
