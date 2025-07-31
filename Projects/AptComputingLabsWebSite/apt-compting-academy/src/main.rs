// src/main.rs

use actix_web::{web, App, HttpServer, middleware::Logger};
use crate::routes;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Initialize the logger
    std::env::set_var("RUST_LOG", "actix_web=info");

    // Start the HTTP server
    HttpServer::new(|| {
        App::new()
            .wrap(Logger::default()) // Middleware for logging
            .configure(routes::init_routes) // Configure routes
    })
    .bind("127.0.0.1:8080")? // Bind to the specified address and port
    .run()
    .await
}