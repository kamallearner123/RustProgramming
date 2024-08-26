#include <iostream>
#include <future>
#include <thread>

void asyncComputation(std::promise<int> p) {
    try {
        // Simulate some computation
        std::this_thread::sleep_for(std::chrono::seconds(20));
        int result = 42; // Computed result
        p.set_value(result); // Set the result
    } catch (...) {
        p.set_exception(std::current_exception()); // Set any exception thrown
    }
}

int main() {
    std::promise<int> p;
    std::future<int> result = p.get_future();

    // Start the asynchronous computation in a separate thread
    std::thread t(asyncComputation, std::move(p));

    // Do some other work in the main thread
    std::cout << "Main thread is free to do other work...\n";

    // Wait for the result
    try {
        int value = result.get(); // This call blocks until the result is available
        std::cout << "The result of the computation is: " << value << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }

    t.join(); // Wait for the thread to finish

    return 0;
}
