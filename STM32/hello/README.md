# STM32F407 Rust Project

This is a simple LED blinking project for STM32F407 microcontroller using Rust.

## Hardware Requirements

- STM32F407 development board (like STM32F407VG Discovery)
- ST-Link debugger (usually built into development boards)
- USB cable to connect to your computer

## Software Setup

1. **Rust embedded target**: Already configured
2. **probe-rs**: Already installed for flashing and debugging

## Building and Flashing

### Build only
```bash
./cargo-embedded.sh build          # Debug build
./cargo-embedded.sh build --release # Release build (optimized, smaller)
```

### Flash to STM32
```bash
./cargo-embedded.sh flash           # Build and flash debug version
./cargo-embedded.sh flash --release # Build and flash release version
```

### Debug (flash + debugging session)
```bash
./cargo-embedded.sh embed           # Build, flash and start debugging
./cargo-embedded.sh run             # Same as embed
```

## Hardware Connections

For STM32F407VG Discovery board:
- **LED**: PD12 (orange LED on the board)
- **ST-Link**: Built-in, connect via USB

## Troubleshooting

### If flashing fails:
1. Check that ST-Link drivers are installed
2. Verify the board is connected via USB
3. Try different chip variants in `Embed.toml`:
   - `STM32F407VGTx`
   - `STM32F407VG`
   - `STM32F407`

### Check connected probes:
```bash
probe-rs list
```

### Get chip information:
```bash
probe-rs chip list | grep STM32F407
```

## What the Code Does

The code blinks the orange LED (PD12) on the STM32F407VG Discovery board by:
1. Configuring the GPIO pin as push-pull output
2. Toggling the LED in an infinite loop
3. Adding a delay between toggles

## Files

- `src/main.rs` - Main application code
- `memory.x` - Memory layout for STM32F407
- `Embed.toml` - probe-rs configuration for flashing/debugging
- `.cargo/config.toml` - Cargo configuration for embedded target
- `cargo-embedded.sh` - Convenience script for building and flashing