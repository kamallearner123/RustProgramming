use std::fs::File;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let output = match File::create("sample.txt") {
        Ok(fp) => fp,
        Err(error) => return Err(Box::new(error)),
    };

    println!("{:?}", output);

    Ok(())
}
