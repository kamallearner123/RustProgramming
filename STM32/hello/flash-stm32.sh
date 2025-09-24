#!/bin/bash

echo "=== STM32L476RG Flash Script ==="
echo ""

# Check if board is connected
echo "Checking for connected STM32 board..."
if sudo ~/.cargo/bin/probe-rs list | grep -q "ST-LINK"; then
    echo "✅ STM32L476RG board detected!"
else
    echo "❌ No STM32 board found. Please:"
    echo "   1. Connect your STM32L476RG Nucleo board via USB"
    echo "   2. Make sure the ST-LINK jumpers are properly set"
    echo "   3. Try a different USB cable"
    exit 1
fi

echo ""
echo "Building project for STM32L476RG..."

# Set correct environment
export PATH="$HOME/.cargo/bin:$HOME/.rustup/toolchains/stable-aarch64-apple-darwin/bin:$PATH"

# Build the project
if cargo build --release; then
    echo "✅ Build successful!"
else
    echo "❌ Build failed!"
    exit 1
fi

echo ""
echo "Flashing binary to STM32L476RG..."

# Try multiple approaches to flash
BINARY_PATH="target/thumbv7em-none-eabihf/release/hello"

echo "Trying method 1: cargo embed..."
if sudo -E PATH="$PATH" RUSTUP_HOME="$HOME/.rustup" CARGO_HOME="$HOME/.cargo" ~/.cargo/bin/cargo embed --release; then
    echo "✅ Flashing successful with cargo embed!"
    echo ""
    echo "🎉 Your STM32L476RG should now be running the LED blink program!"
    echo "   Look for the green LED (PA5) blinking on your Nucleo board."
    exit 0
fi

echo "Method 1 failed, trying method 2: probe-rs download..."
if sudo ~/.cargo/bin/probe-rs download --chip STM32L476RG "$BINARY_PATH"; then
    echo "✅ Flashing successful with probe-rs!"
    echo ""
    echo "🎉 Your STM32L476RG should now be running the LED blink program!"
    echo "   Look for the green LED (PA5) blinking on your Nucleo board."
    exit 0
fi

echo ""
echo "❌ All flashing methods failed. This is likely a USB permissions issue on macOS."
echo ""
echo "To fix this permanently:"
echo "1. Install libusb: brew install libusb"
echo "2. Add your user to the _usbmuxd group: sudo dseditgroup -o edit -a \$USER -t user _usbmuxd"
echo "3. Restart your computer"
echo ""
echo "Alternative: Use STM32CubeIDE or STM32CubeProgrammer to flash the binary:"
echo "   Binary location: $(pwd)/$BINARY_PATH"