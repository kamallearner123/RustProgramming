fn main() {
    let mut data: Vec<i32> = vec![3,6,9,2,1,4];
    let r1: &mut[i32] = &mut data[1..];
    for i in 0..3 {
        r1[i]=10;
    }

    modify(r1);
    println!("{:?}", data);

}

fn modify(data:&mut [i32]) {
    for i in 0..3 {
        data[i] = 20;
    }
}

