use actix_web::{web, HttpServer, App, Responder};

#[actix_web::get("/greet/{id}")]
async fn greet(user_id: web::Path<u32>) -> impl Responder {
    format!("Hello {user_id}.. Congratulations for reaching me :)")
}

#[actix_web::main]
async fn main() ->std::io::Result<()> {
    HttpServer::new( || App::new().service(greet))
        .bind(("127.0.0.01", 8181))?
        .workers(2)
        .run()
        .await
}
