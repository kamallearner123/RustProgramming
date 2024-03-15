pub mod http {
    use std::io::Read;
    use std::net::TcpListener;
    use std::net::TcpStream; //Import Read trait
    #[derive(Debug)]
    pub enum REQUEST_TYPE {
        GET,
        PUT,
        DELETE,
    }
    #[derive(Debug)]
    pub struct request {
        data: String,
        reqId: REQUEST_TYPE,
    }
    impl request {
        pub fn new(data: String) -> Self {
            let reqId = REQUEST_TYPE::GET;
            Self { data, reqId }
        }

        fn print(self) {
            println!("Data = {:?}", self);
        }

        pub fn print_details(self) {
            self.print();
        }
    }

    #[derive(Debug)]
    pub struct Server {
        addr: String,
        conn: u32,
    }

    impl Server {
        pub fn new(addr: String) -> Self {
            let conn = 1000;
            Self { addr, conn }
        }
        pub fn run(self) {
            let listener = TcpListener::bind(&self.addr).unwrap();
            //println!("listener = {:?}", listener);
            //match listener {
            //    Ok(value) => println!("Value = {:?}", value),
            //    Err(err) => println!("Error \u{1F641} = {:?}", err),
            //}

            loop {
                match listener.accept() {
                    Ok((mut stream, _)) => {
                        let mut buffer = [0; 10240]; // number, number of times
                        match stream.read(&mut buffer) {
                            //fn read(&mut self, buf : &mut[u8])
                            Ok(_) => {
                                println!("Received bytes = {}", String::from_utf8_lossy(&buffer));
                            }
                            Err(e) => println!("Error while reading {:?}", e),
                        }
                    }
                    Err(e) => println!("Failed.. e = {:?}", e),
                }
            }
        }
    }
}
