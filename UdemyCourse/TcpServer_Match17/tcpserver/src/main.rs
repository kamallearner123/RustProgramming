use env_logger;
pub mod webserver;

use log::{debug, error, info};
fn main() {
    env_logger::init();
    let address = String::from("127.0.0.18989");
    if address.contains(":") {
        debug!("Address = {}", address);
    } else {
        error!("Invalid address!!!");
    }
    let TCP_SERVER = webserver::TcpServer::new(address);

    println!("Hello, world!");
}
