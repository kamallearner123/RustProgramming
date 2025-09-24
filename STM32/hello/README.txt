================================================================================
STM32L476RG RUST EMBEDDED PROJECT - COMPLETE SETUP GUIDE
================================================================================

OVERVIEW
--------
This is a complete Rust embedded project for the STM32L476RG microcontroller
that blinks the green LED (PA5) on a Nucleo-L476RG development board.

HARDWARE REQUIRED
-----------------
- STM32L476RG Nucleo development board
- USB cable (USB-A to USB-B Mini)
- Computer with macOS/Linux/Windows

PROJECT STRUCTURE
------------------
├── Cargo.toml              # Rust project configuration with STM32L4 dependencies
├── src/main.rs              # Main application code (LED blink)
├── memory.x                 # Memory layout for STM32L476RG (96KB RAM, 1024KB Flash)
├── Embed.toml              # Probe-rs configuration for flashing/debugging
├── .cargo/config.toml      # Cargo configuration for embedded target
├── cargo-embedded.sh       # Build script with correct Rust toolchain
├── flash-stm32.sh          # Automated flashing script
└── README.md               # Detailed project documentation

INITIAL PROBLEM SOLVED
----------------------
The original issue was a conflict between Homebrew's Rust installation and 
rustup. Homebrew's Rust doesn't support embedded targets like thumbv7em-none-eabihf.

SOLUTION: Use rustup's Rust toolchain with proper PATH configuration.

COMPLETE SETUP STEPS
--------------------

1. INSTALL RUST EMBEDDED TARGET
   rustup target add thumbv7em-none-eabihf

2. INSTALL PROBE-RS (for flashing and debugging)
   curl --proto '=https' --tlsv1.2 -LsSf https://github.com/probe-rs/probe-rs/releases/latest/download/probe-rs-tools-installer.sh | sh

3. INSTALL ST-LINK TOOLS (for macOS compatibility)
   brew install stlink

4. FIX MACOS USB PERMISSIONS (if needed)
   brew install libusb
   sudo dseditgroup -o edit -a $USER -t user _usbmuxd
   # Then restart your computer

KEY CONFIGURATION FILES
-----------------------

Cargo.toml:
- Uses stm32l4xx-hal crate with "stm32l476" and "rt" features
- Cortex-M runtime and panic handler dependencies

memory.x:
- Defines STM32L476RG memory layout
- Flash: 0x08000000, 1024KB
- RAM: 0x20000000, 96KB

.cargo/config.toml:
- Sets default target to thumbv7em-none-eabihf
- Configures linker flags for embedded target

Embed.toml:
- Configures probe-rs for STM32L476RG chip
- Enables flashing and reset functionality

BUILDING THE PROJECT
--------------------

Using the provided script (recommended):
   ./cargo-embedded.sh build --release

Manual approach:
   PATH="$HOME/.cargo/bin:$HOME/.rustup/toolchains/stable-aarch64-apple-darwin/bin:$PATH" cargo build --release

FLASHING TO BOARD
-----------------

1. CONNECT HARDWARE
   - Connect STM32L476RG Nucleo board to computer via USB
   - Ensure ST-LINK jumpers are properly configured on the board

2. VERIFY CONNECTION
   probe-rs list
   # Should show: STLink V2-1 -- [device ID] (ST-LINK)

3. FLASH THE BINARY

   Option A - Automated script (easiest):
   ./flash-stm32.sh

   Option B - Manual cargo embed:
   sudo -E PATH="$HOME/.cargo/bin:$HOME/.rustup/toolchains/stable-aarch64-apple-darwin/bin:$PATH" RUSTUP_HOME="$HOME/.rustup" CARGO_HOME="$HOME/.cargo" ~/.cargo/bin/cargo embed --release

   Option C - Direct binary flash:
   sudo ~/.cargo/bin/probe-rs download --chip STM32L476RG target/thumbv7em-none-eabihf/release/hello

EXPECTED BEHAVIOR
-----------------
After successful flashing:
- The green LED (PA5) on the Nucleo-L476RG board will blink continuously
- Blink rate: approximately 10Hz (due to 8_00_000 delay cycles)
- The program runs in an infinite loop

CODE EXPLANATION
----------------
The main.rs code performs these steps:
1. Initialize STM32L476RG peripherals (RCC, Flash, Power)
2. Configure system clocks using default settings
3. Configure GPIO Port A with AHB2 clock enable
4. Set PA5 as push-pull output (connected to green LED)
5. Toggle LED state in infinite loop with delay

TROUBLESHOOTING
--------------

PROBLEM: "can't find crate for core" error
SOLUTION: Ensure rustup's Rust is used instead of Homebrew's
         Use the provided cargo-embedded.sh script

PROBLEM: "Probe not found" or USB access errors
SOLUTION: 1. Install libusb: brew install libusb
         2. Add user to USB group: sudo dseditgroup -o edit -a $USER -t user _usbmuxd
         3. Restart computer
         4. Use sudo with flash commands

PROBLEM: LED not blinking after flash
SOLUTION: 1. Check that PA5 LED exists on your board
         2. Verify successful flash with probe-rs list
         3. Press reset button on the board
         4. Check power supply (USB connection)

PROBLEM: Wrong chip detected
SOLUTION: Try different chip variants in Embed.toml:
         - STM32L476RG
         - STM32L476RGTx
         Check available chips: probe-rs chip list | grep L476

ALTERNATIVE FLASHING METHODS
---------------------------
If probe-rs fails, you can use:
1. STM32CubeIDE with the generated binary file
2. STM32CubeProgrammer 
3. OpenOCD with appropriate configuration
4. ST-LINK Utility (Windows only)

Binary location: target/thumbv7em-none-eabihf/release/hello

DEVELOPMENT WORKFLOW
-------------------
1. Edit src/main.rs
2. Build: ./cargo-embedded.sh build --release
3. Flash: ./flash-stm32.sh
4. Observe LED behavior
5. Debug if needed: cargo embed (starts GDB session)

USEFUL COMMANDS
--------------
Check build:           ./cargo-embedded.sh check
Build debug:           ./cargo-embedded.sh build
Build release:         ./cargo-embedded.sh build --release
Flash and debug:       ./cargo-embedded.sh embed
List probes:           probe-rs list
List supported chips:  probe-rs chip list | grep L476
Clean build cache:     ./cargo-embedded.sh clean

SUCCESS INDICATORS
-----------------
✅ Project builds without errors
✅ probe-rs detects ST-LINK debugger
✅ Flash operation completes successfully
✅ Green LED (PA5) blinks on Nucleo board
✅ No error messages in terminal

This completes the full setup for STM32L476RG Rust embedded development!

================================================================================
Created: September 24, 2025
Target: STM32L476RG Nucleo Board
Language: Rust (embedded, no_std)
Tools: rustup, probe-rs, cargo-embed
================================================================================