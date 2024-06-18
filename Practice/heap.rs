
fn main() {
    println!("Try programiz.pro");
    
    let mut v1: Vec<i32> = Vec::new();
    v1.push(10);
    v1.push(20);
    v1.push(30);
    v1.push(30);
    v1.push(30);
    v1.push(-1);
    v1.push(30);
    
    let mut heap: Vec<i32> = Vec::new();
    for i in 0..v1.len() {
        println!("{}", v1[i]);
        heapify(&mut heap, v1[i]);
    }
    
    for i in 0..heap.len() {
        println!("{}", heap[i]);
    }
    

    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
    println!("{:?}", get_num(&mut heap));
}

fn heapify(heap: &mut Vec<i32>, num: i32)
{
    let mut i = heap.len();
    
    heap.push(num);

    while (i!= 0) && (heap[i] > heap[i/2]) {
        (heap[i], heap[i/2]) = (heap[i/2], heap[i]);
        i = i/2;
    }
}

fn get_num(heap: &mut Vec<i32>) -> Option<i32>
{
    let mut i = 0;

    if heap.len() == 0 {
        return None
    }

    let maxlen = heap.len()-1;
    let ret = heap[0];

    (heap[0],heap[maxlen]) = (heap[maxlen], heap[0]);
    
    heap.pop();
    while i< heap.len() {
       let c = if (i*2+1<heap.len()) && (heap[i*2+1]>=heap[i]) {
            i*2+1
        } else {
            i
       };
       let c = if (i*2+2 < heap.len()) && (heap[i*2+2]>=heap[c]) {
            i*2+2
        } else {
            c
       };

        (heap[i], heap[c]) = (heap[c], heap[i]);
        if i==c {
            break;
        }
        i = c;
    }
    Some(ret)
}
