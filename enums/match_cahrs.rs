fn categorize_letter(c: char) {
    match c {
        'a'..='f' => println!("The letter is between 'a' and 'f'."),
        'g'..='l' => println!("The letter is between 'g' and 'l'."),
        'm'..='r' => println!("The letter is between 'm' and 'r'."),
        's'..='z' => println!("The letter is between 's' and 'z'."),
        _ => println!("The letter is out of the expected range."),
    }
}

fn main() {
    let letter = 'h';
    categorize_letter(letter);
}

