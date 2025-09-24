#![no_std]
#![no_main]

use cortex_m_rt::entry;
use panic_halt as _;
use stm32l4xx_hal as hal;
use hal::{pac, prelude::*};

#[entry]
fn main() -> ! {
    let dp = pac::Peripherals::take().unwrap();
    let mut flash = dp.FLASH.constrain();
    let mut rcc = dp.RCC.constrain();
    let mut pwr = dp.PWR.constrain(&mut rcc.apb1r1);
    
    // Use default clocking for simplicity
    let _clocks = rcc.cfgr.freeze(&mut flash.acr, &mut pwr);

    let mut gpioa = dp.GPIOA.split(&mut rcc.ahb2);
    // PA5 is the green LED on STM32L476RG Nucleo board  
    let mut led = gpioa.pa5.into_push_pull_output(&mut gpioa.moder, &mut gpioa.otyper);

    loop {
        led.toggle();
        cortex_m::asm::delay(8_000_000);
    }
}

