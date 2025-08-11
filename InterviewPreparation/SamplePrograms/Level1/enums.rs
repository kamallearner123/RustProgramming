#[derive(Debug)]
enum issueType {
    FATAL,
    MAJOR,
    MINOR,
    COSMO
}


fn main() {
    let msg_type:issueType = issueType::MINOR;
    println!("type = {:?}", msg_type);
}

