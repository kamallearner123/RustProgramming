use std::str::FromStr;

/*
enum Option<T> {
    Some(T),
    None,
}*/

fn parse_pair<T: FromStr>(s: &str, seperator: char) -> Option<(T, T)> {
    match s.find(seperator) {
        None => None,
        Some(index) => match (T::from_str(&s[..index]), T::from_str(&s[index + 1..])) {
            (Ok(r), Ok(l)) => Some((r, l)),
            _ => None,
        },
    }
}
fn main() {
    println!("Start of the program!!!");
    println!("{:?}", parse_pair::<i32>("1,2", ','));
    println!("{:?}", parse_pair::<i32>("1:2", ':'));
    println!("{:?}", parse_pair::<f32>("1.1,2", ','));
    println!("{:?}", parse_pair::<i32>("1,2", ','));
}
