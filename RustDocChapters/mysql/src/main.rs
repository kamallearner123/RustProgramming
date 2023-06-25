fn main() {
    println!("Hello, world!");
    print!("Weight = {}", calculate_weight_on_mars(10.1));
}


fn calculate_weight_on_mars(weight: f32) -> f32 {
    weight*0.6
}