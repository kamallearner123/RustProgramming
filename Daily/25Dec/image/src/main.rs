use std::fs::File;
use image::ColorType;
use image::png::PNGEncoder;

fn write_image(filename :&str, pixels : &[u8], bounds:(usize, usize)) -> Result<(), std::io::Error> 
{
    let output = File::create(filename);
    let encoder = PNGEncoder::new(output);
    Ok(())
}

fn main() {
    println!("Hello, world!");
}
