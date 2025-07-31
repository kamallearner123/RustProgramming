mod.rs

use actix_web::{web, HttpResponse, Responder};

pub fn configure_routes(cfg: &mut web::ServiceConfig) {
    cfg.service(index)
        .service(about);
}

async fn index() -> impl Responder {
    HttpResponse::Ok().body("Welcome to Apt Computing Academy!")
}

async fn about() -> impl Responder {
    HttpResponse::Ok().body("About Apt Computing Academy")
}