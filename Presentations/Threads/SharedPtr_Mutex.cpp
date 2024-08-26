#include <iostream>
#include <memory>
#include <thread>
#include <vector>
#include <mutex>

void increment_shared_value(std::shared_ptr<int> ptr, std::mutex& mtx) {
    for (int i = 0; i < 100; ++i) {
        // Lock the mutex before accessing the shared resource
        std::lock_guard<std::mutex> lock(mtx);
        (*ptr)++;
    }
}

int main() {
    // Create a shared resource
    auto shared_value = std::make_shared<int>(0);
    std::mutex mtx;  // Mutex to protect access to the shared resource
    std::vector<std::thread> threads;

    // Create multiple threads that will increment the shared value
    for (int i = 0; i < 10; ++i) {
        threads.emplace_back(increment_shared_value, shared_value, std::ref(mtx));
    }

    // Wait for all threads to finish
    for (auto& t : threads) {
        t.join();
    }

    // Print the final value of the shared resource
    std::cout << "Final value: " << *shared_value << std::endl;

    return 0;
}
