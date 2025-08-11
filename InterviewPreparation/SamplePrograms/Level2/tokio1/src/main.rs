use tokio::time::{Duration, sleep};


#[tokio::main]
async fn main() {
    let t1 = tokio::spawn(async {
        let local_task = sleep(Duration::from_millis(4000));
        local_task.await;
        println!("Done... waiting... 4 secs");
    });
    let t2 = tokio::spawn(async {
        let local_task = sleep(Duration::from_millis(2000));
        local_task.await;
        println!("Done... waiting...");
    });

    sleep(Duration::from_millis(1000));
    tokio::try_join!(t1, t2).unwrap();
    //tokio::join(t1);
    println!("Exit program...");
}
