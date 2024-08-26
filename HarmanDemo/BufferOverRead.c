#include <stdio.h>

void buffer_overread() {
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i <= 5; i++) {
        printf("%d\n", arr[i]);
    }
}

int main() {
    buffer_overread();
    return 0;
}

