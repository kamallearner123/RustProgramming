use serd::{Serialize, Deserialize};
use sync::Arc;
use tokio::sync:RwLaock;


pub struct backend {
    pub address:String, #https://127.0.0.1:8080
    pub health:bool
}

pub struct backend_pool {
    backends: Arx<RwLoack<Vec<backend>>>,
    index: Arc<RwLoack<usize>>


}


