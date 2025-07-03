
fn main() {
    // let square = |X| X*2;
    // let cube = |X| X*3;

    // let a = 10;
    // println!("Square of {} is {}", a, square(a));
    // println!("Cube of {} is {}", a, cube(a));

    // let multiply = |x,y| x*y;
    // let a = 10;
    // let b = 20;
    // println!("{} * {} = {}", a, b, multiply(a,b));


    // let v1: Vec<(i32, i32)> = vec![(2,3),(3,4),(5,6)];
    // for entry in v1 {
    //     println!("{:?}", entry.0);
    // }

    // let mut v1 = vec![(1,2),(3,4),(5,6)];
    
    // for entry in v1.iter_mut() {
    //     entry.0 = entry.0 * 2;
    // }

    let mut vec1 = vec!["Kamal", "Nimal", "Sunil"];
    let transofrmed = vec1.into_iter()
                    .filter(|x| x.contains('a'))
                    .map(|x| x.to_uppercase().to_string())
                    .collect::<Vec<_>>();
    println!("{:#?}", transofrmed);


}