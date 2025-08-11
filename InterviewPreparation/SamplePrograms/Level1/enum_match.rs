
enum MessageType {
    FATAL,
    MAJOR,
    MINOR,
    COSMO
}

fn handle_message(typeM:MessageType) {
    match typeM {
        MessageType::FATAL => {println!("Handle FATAL!!!")},
        MessageType::MAJOR => {println!("Handle MAJOR!!!")},
        _ => println!("Default!!!")
    }

}

fn main() {
    handle_message(MessageType::MINOR);
}


