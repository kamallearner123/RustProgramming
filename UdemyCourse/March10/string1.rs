use std::io;

fn main() {
    let string = String::from("This is string!!!\u{2764} \u{1F355}");
    let string_slice = &string[..4]; //borrow
    let string_borrow = &string;

    dbg!(&string);
    dbg!(string_borrow);
    dbg!(string_slice);
}
