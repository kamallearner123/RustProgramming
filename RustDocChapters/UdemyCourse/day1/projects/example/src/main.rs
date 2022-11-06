fn add_tail(str1: & mut String) {
    str1.push_str(" kumar");
}

fn main() {
    println!("Hello, world!");
    let mut cmd = "kamal".to_string();
    add_tail(& mut cmd);
    println!("name = {}", cmd);
}
