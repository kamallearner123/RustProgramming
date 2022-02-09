extern crate regex;
use regex::Regex;

mod myregex;

fn main() {
    let mystr = "kamal 9711223344";
    
    let flag = myregex::check_phonenum(mystr);

    println!("Is match ? {} ", flag);
    println!("Hello, world!");
}
