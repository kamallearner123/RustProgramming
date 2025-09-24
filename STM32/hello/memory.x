/* Memory layout for STM32L476RG */
MEMORY
{
  /* Flash memory - 1024K */
  FLASH : ORIGIN = 0x08000000, LENGTH = 1024K
  
  /* SRAM1 - 96K */
  RAM : ORIGIN = 0x20000000, LENGTH = 96K
}

/* Stack starts at the end of RAM */
_stack_start = ORIGIN(RAM) + LENGTH(RAM);