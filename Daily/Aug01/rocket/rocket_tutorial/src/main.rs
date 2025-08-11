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

/*
Study Rust no_std and embedded-hal for ECU development.
Prototype CAN sensor on NXP S32K or STM32.
Integrate with IdsM/IdsR and AUTOSAR stack.
Build SOC dashboard with Actix Web + Yew.
Explore Ferrocene for ISO/SAE 21434 certification.
 */