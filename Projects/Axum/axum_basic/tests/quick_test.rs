use anyhow::Result;

#[tokio::test]
async fn quick_test_01() -> Result<()> {
    let hc = httpc_test::new_client("http://localhost:8080")?;

    let res = hc.do_get("/hello").await?; // httpc_test::Response

    println!("Status: {}.", res.status());
    println!("Body: {:?}.", res.text_body()); // Access as a field, not a method

    // Test verdict
    assert_eq!(res.status(), 200, "Expected HTTP 200 OK");
    assert!(
        res.text_body().unwrap().contains("Hello.... Welcome to first program of Axum!!! :"),
        "Expected 'Hello.... Welcome to first program of Axum!!! :' but got: {:?}",
        res.text_body()
    );

    Ok(())
}

#[tokio::test]
async fn quick_test_02() -> Result<()> {
    let hc = httpc_test::new_client("http://localhost:8080")?;

    let res = hc.do_get("/hi").await?; // httpc_test::Response

    println!("Status: {}.", res.status());
    println!("Body: {:?}.", res.text_body()); // Access as a field, not a method

    // Test verdict
    assert_eq!(res.status(), 200, "Expected HTTP 200 OK");
    assert!(
        res.text_body().unwrap().contains("Hi..... Welcome to first program of Axum!!! :"),
        "Expected 'Hi..... Welcome to first program of Axum!!! :' but got: {:?}",
        res.text_body()
    );

    Ok(())
}

