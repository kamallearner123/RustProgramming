#![feature(proc_macro_hygiene, decl_macro)]

use rocket::{get, routes};

#[get("/")]
fn index() -> &'static str {
    "Hello, Rocket!"
}

#[rocket::main]
async fn main() -> Result<(), rocket::Error> {
    rocket::build()
        .mount("/", routes![index])
        .launch()
        .await
}
