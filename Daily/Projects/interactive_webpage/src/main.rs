use actix_files::NamedFile;
use actix_web::{web, App, HttpServer, Responder, HttpResponse, middleware::Logger};
use serde::Deserialize;
use std::env;
use std::path::PathBuf;

#[derive(Deserialize)]
struct UserChoice {
    choice: String,
    extra_choice: Option<String>,
}

async fn index() -> impl Responder {
    HttpResponse::Ok().body(include_str!("../static/index.html"))
}

async fn get_options() -> actix_web::Result<NamedFile> {
    let path: PathBuf = "./static/options.json".parse().unwrap();
    Ok(NamedFile::open(path)?)
}
async fn handle_choice(choice: web::Form<UserChoice>) -> impl Responder {
    //println!("Received choice: {:?}", choice);

    match choice.choice.as_str() {
        "option1" => HttpResponse::Ok().body("You selected option 1"),
        "option2" => {
            if let Some(extra_choice) = &choice.extra_choice {
                match extra_choice.as_str() {
                    "extra1" => HttpResponse::Ok().body("You selected option 2 and extra option 1"),
                    "extra2" => HttpResponse::Ok().body("You selected option 2 and extra option 2"),
                    _ => HttpResponse::Ok().body("Invalid extra choice"),
                }
            } else {
                HttpResponse::Ok().body("You selected option 2")
            }
        },
        _ => HttpResponse::Ok().body("Invalid choice"),
    }
}


#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Initialize logging
    env::set_var("RUST_LOG", "actix_web=info");
    env_logger::init();

    // Log server startup
    println!("Starting server at http://127.0.0.1:8080");

    // Start the HTTP server
    HttpServer::new(|| {
        App::new()
            .wrap(Logger::default())
            .route("/", web::get().to(index))
            .route("/options", web::get().to(get_options))
            .route("/submit", web::post().to(handle_choice))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
