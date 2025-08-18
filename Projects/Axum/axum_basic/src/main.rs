#![allow(unused)]

use axum::Router;
use axum::routing::get;
use axum::response::Html;
use std::net::SocketAddr;

async fn hello_route() ->Html<&'static str> {
    Html("Hello.... Welcome to first program of Axum!!! :")
}
async fn hi_route() ->Html<&'static str> {
    Html("Hi..... Welcome to first program of Axum!!! :")
}

#[tokio::main]
async fn main() ->Result<(),()> {

    println!("Going to start server!!!...");
    
    // Create a routing service.
    let RoutingSv:Router = Router::new()
        .route("/hello", get(hello_route))
        .route("/hi", get(hi_route));


    // Create a TCP server.
    let addr:SocketAddr = SocketAddr::from(([127,0,0,1],8080));
    let stream = tokio::net::TcpListener::bind(&addr)
        .await
        .map_err(|e| println!("Addr {}, failed to bind with error {}", addr, e))?;   

    axum::serve(stream, RoutingSv)
        .await
        .map_err(|err| println!("error = {}", err))?;
    Ok(())
}
