extern crate regex;
use regex::Regex;

pub fn check_phonenum(n&:str)->bool {
    
    let re = Regex::new(r"\d{10}").unwrap();
    return re.is_match(n);

}
