mod pixel_mod;
use pixel_mod::pixel_mod::*;


fn main() {
    let rows = 10;
    let cols = 20;
    

    let myPic: GrayscaleMap = GrayscaleMap{
        pixels_data: vec![0; rows*cols],
        size: (rows, cols)
    };

    println!("My pic data = {:?}", myPic);


    let ptr = Box::new(GrayscaleMap::new(20, 30));

    std::thread::sleep(std::time::Duration::from_secs(1));

    // Copying partial data from existing instance myPic
    let mut myPic3 = GrayscaleMap{
        pixels_data: vec![1,2,3],
        .. myPic
    };
    println!("My pic data myPic2= {:?}", myPic3);


    let mut myPic2 = myPic.clone();
    myPic2.pixels_data[0] = 1;
    println!("My pic data myPic2= {:?}", myPic2);

    let myPic4 = myPic;
    println!("My pic data myPic4= {:?}", myPic4);

    //println!("My pic {:?}", myPic); //^^^^^ value borrowed here after move

}

