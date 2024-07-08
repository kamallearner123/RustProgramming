
fn main() {
    let mut strings: Vec<String> = vec!["Kamal".to_string(), "Kumar".to_string()];

    let found = 'name_search: loop {
        if let Some(p) = &strings.pop() {
            println!("Checking");
            println!("string = {}", p);
            for c in p.chars() {
                if c == 'a' {
                    break 'name_search true;
                }
            }
        } else {
            break 'name_search false;
        }
    };

    println!("Valie of found = {}", found);
}