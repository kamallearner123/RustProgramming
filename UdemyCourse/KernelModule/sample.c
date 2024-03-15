#include <linux/l=kernel.h>
#include <linux/module.h>

int init_module() {
    printk(KERN_IFNO " Starting module sample: KAmal:\n");
    return 0;
}

void cleanup_module() {
    printk(KERN_INFO " END: sample module Kamal\n");
}
