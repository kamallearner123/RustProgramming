use actix_web::{web, HttpServer, App, Responder};
use serde::{Serialize, Deserialize};
use std::sync::{Arc, Mutex};
use std::collections::HashMap;

#[derive(Serialize, Deserialize)]
struct Message {
    id: u8,
    content: String,
}


// Type: to keep the data : MQTT broker
type UserDB = Arc<Mutex<HashMap<u8, String>>>;

#[actix_web::get("/greet/{id}")]
async fn greet(user_id: web::Path<u32>) -> impl Responder {
    format!("Hello {user_id}.. Congratulations for reaching me :)")
}


#[actix_web::get("/fetch/{id}")]
async fn fetch(user_id: web::Path<u8>, db: web::Data<UserDB>) -> impl Responder {
    let db = db.lock().unwrap();
    let id = user_id.into_inner();
    println!("Fetching message for user ID: {id}");
    if let Some(message) = db.get(&id) {
        format!("Fetched message for user {id}: {message}")
    } else {
        format!("No message found for user {id}")
    }
}

#[actix_web::post("/feed")]
async fn feed(userData:web::Json<Message>,
            db: web::Data<UserDB>) -> impl Responder{
    
    let mut db = db.lock().unwrap();
    let user_data = userData.content.clone();
    let new_id = userData.id;
    
    let response = format!("ID: {new_id}, Message: {user_data} Insertion was succseeful!!!");

    println!("Response = {response}");
    db.insert(new_id, user_data);
    return response;
}

#[actix_web::main]
async fn main() ->std::io::Result<()> {

    let msgDB:UserDB = Arc::new(
                        Mutex::new(
                            HashMap::new()
                        )
                    );

    HttpServer::new( move|| {
            let app_data = web::Data::new(msgDB.clone());
            App::new().app_data(app_data).service(feed).service(greet).service(fetch)}
        )
        .bind(("127.0.0.01", 8181))?
        .workers(2)
        .run()
        .await
}
