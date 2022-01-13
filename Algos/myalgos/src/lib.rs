
pub fn bubblesort<T:PartialOrd> (v: &mut[T]) {

    for j in 0..v.len()-1 {
        for i in 0..v.len()-j-1 {
            if v[i] > v[i+1] {
                v.swap(i,i+1)
            }
        }
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    use super::*;
    #[test]
    fn test_bubble_sort() {
        let mut v = vec![4,6,2,9,0];
        bubblesort(&mut v);
        //assert_eq!(v[0], 0);
        for i in 0..v.len()-1 {
            println!("va l = {}", v[i])
        }
    }

}
/*
fn main() {
        let mut v = vec![4,6,2,9,0];
        bubblesort(&mut v);
        //assert_eq!(v[0], 0);
        for i in 0..v.len()-1 {
            println!("va l = {}", v[i])
        }
}

*/
