/// A simple struct representing a rectangle.
struct Rectangle {
    /// The width of the rectangle.
    width: u32,
    
    /// The height of the rectangle.
    height: u32,
}

impl Rectangle {
    /// Calculates the area of the rectangle.
    ///
    /// # Returns
    ///
    /// The area of the rectangle.
    fn area(&self) -> u32 {
        self.width * self.height
    }
}


/// Adds two numbers together.
///
/// # Arguments
/// * `a` - The first integer.
/// * `b` - The second integer.
///
/// # Returns
/// The sum of `a` and `b`.
fn add(a: i32, b: i32) -> i32 {
    a + b
}

/// Main Function
///
/// # Arguments
///
///
/// # Returns
/// 
/// Nothing
fn main() {
    println!("Hello, world!");
}
