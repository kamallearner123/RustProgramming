#!/bin/bash

# Set the correct PATH to use rustup instead of Homebrew Rust
export PATH="$HOME/.cargo/bin:$HOME/.rustup/toolchains/stable-aarch64-apple-darwin/bin:$PATH"

# Function to show usage
show_usage() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  check           - Check the project for errors"
    echo "  build           - Build the project"
    echo "  build --release - Build optimized release version"
    echo "  flash           - Build and flash to STM32 target"
    echo "  flash --release - Build release version and flash to STM32"
    echo "  embed           - Build, flash and start debugging session"
    echo "  run             - Same as embed"
    echo ""
    echo "Hardware setup:"
    echo "  - Connect your STM32F407 board via ST-Link debugger"
    echo "  - Ensure ST-Link drivers are installed"
}

# Handle special commands
case "$1" in
    "flash")
        if [ "$2" = "--release" ]; then
            echo "Building and flashing release version..."
            cargo build --release && cargo flash --release
        else
            echo "Building and flashing debug version..."
            cargo build && cargo flash
        fi
        ;;
    "embed")
        echo "Building, flashing and starting debug session..."
        cargo embed
        ;;
    "run")
        echo "Building, flashing and starting debug session..."
        cargo embed
        ;;
    "help"|"-h"|"--help")
        show_usage
        ;;
    "")
        show_usage
        ;;
    *)
        # Run the cargo command with the correct Rust toolchain
        cargo "$@"
        ;;
esac