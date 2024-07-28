
fn main() {
    let mut nums: Vec<i32> = [1,2,3,4,5].to_vec();
    let num: i32 = 'outer: loop {
        let n = match nums.pop(){
            Some(num2) => num2,
            None => break 0,
        };

        // if n == 0 {
        //     break 0;
        // }

        for i in 1.. {
            if i*i == n {
                println!("Breaking outer!!!");
                break 'outer n;
            }
            if i*i > n {
                println!("Break!!!");
                break;
            }
        }
    };
    println!("{}", num);
}
