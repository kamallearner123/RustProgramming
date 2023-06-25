use mysql::*;
use std;
use mysql::prelude::*;

#[derive(Debug, PartialEq, Eq)]
struct Payment {
    customer_id: i32,
    amount: i32,
    account_name: Option<String>,
}



fn main() -> std::result::Result<(), Box<dyn std::error::Error>> {
    let url = "127.0.0.1:3306";
    let pool = Pool::new(url)?;

    let mut conn = pool.get_conn();

    conn.query_drop(r"CREATE TEMPORARY TABLE payment (
        customer_id int not null,
        amount int not null,
        account_name text
    )")?;

    let payments = vec![
        Payment { customer_id: 1, amount: 2, account_name: None },
        Payment { customer_id: 3, amount: 4, account_name: Some("foo".into()) },
        Payment { customer_id: 5, amount: 6, account_name: None },
        Payment { customer_id: 7, amount: 8, account_name: None },
        Payment { customer_id: 9, amount: 10, account_name: Some("bar".into()) },
    ];

    conn.exec_batch (
        r"INSERT INTO paument (customer_id, amount, account_name)
        VALUES(:customer_id, :amount, :account_name)",
        payments.iter().map(|p| params! {
            "customer_id" => p.customer_id,
            "amount" => p.amount,
            "account_name" => p.account_name,
        })
    )?;

    println!("Hello, world!");
}
