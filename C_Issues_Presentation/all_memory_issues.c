#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void func1() {
    int *ptr = (int *)malloc(sizeof(int));
    *ptr = 42;
    free(ptr);
    printf("Pointer value: %d\n", *ptr);
}

void func2() {
    char buffer[5];
    strncpy(buffer, "This is too long", 10); 
    printf("Buffer content: %s\n", buffer); 
}

void func3() {
    int *ptr = (int *)malloc(sizeof(int) * 5);
    free(ptr);
    ptr[0] = 10;
    printf("value: %d\n", ptr[0]);
}

void func4() {
    int *ptr = NULL;
    *ptr = 10;
}

void func5() {
    int *ptr = (int *)malloc(sizeof(int));
    printf("Uninitialized memory value: %d\n", *ptr);
    free(ptr);
}

void double_free() {
    int *ptr = (int *)malloc(sizeof(int));
    free(ptr);
    // Double free: freeing memory that has already been freed.
    free(ptr); // Undefined behavior
}

int main() {
    dangling_pointer();
    buffer_overflow();
    use_after_free();
    null_pointer_dereference();
    uninitialized_memory();
    double_free();
    return 0;
}
//
