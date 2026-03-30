#!/bin/bash
set -euo pipefail

# Install script for local video generation
# This script installs all dependencies and stable-diffusion.cpp

echo "========================================"
echo "Local Video Generation Installer"
echo "========================================"
echo ""

# Check OS
echo "Detected OS: $(uname -s)"
echo ""

# Install system dependencies
echo "=== Installing system dependencies ==="

if [[ "$(uname -s)" == "Darwin" ]]; then
    # macOS
    echo "macOS detected - checking Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found. Please install Homebrew: https://homebrew.sh/"
        exit 1
    fi
    brew update
    brew install cmake git ffmpeg
elif [[ "$(uname -s)" == "Linux" ]]; then
    # Linux
    echo "Linux detected - installing system packages..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y cmake git ffmpeg
    elif command -v yum &> /dev/null; then
        sudo yum install -y cmake git ffmpeg
    elif command -v pacman &> /dev/null; then
        sudo pacman -Sy cmake git ffmpeg
    else
        echo "Unknown package manager. Please install cmake, git, and ffmpeg manually."
    fi
else
    echo "Unknown OS. Please install cmake, git, and ffmpeg manually."
fi

echo ""

# Install Python dependencies
echo "=== Installing Python dependencies ==="
python3 -m pip install --upgrade pip
python3 -m pip install gradio opencv-python numpy Pillow

echo ""

# Clone and build stable-diffusion.cpp
echo "=== Installing stable-diffusion.cpp ==="

SDCPP_DIR="$HOME/.local/stable-diffusion.cpp"

if [[ -d "$SDCPP_DIR" ]]; then
    echo "stable-diffusion.cpp already installed. Updating..."
    cd "$SDCPP_DIR"
    git pull origin main
else
    echo "Cloning stable-diffusion.cpp..."
    git clone https://github.com/leejet/stable-diffusion.cpp.git "$SDCPP_DIR"
    cd "$SDCPP_DIR"
fi

# Build stable-diffusion.cpp
echo "Building stable-diffusion.cpp (this may take a few minutes)..."
mkdir -p build
cd build
cmake ..
make -j$(nproc)

echo ""

# Install Python bindings
echo "Installing Python bindings..."
cd "$SDCPP_DIR"
python3 -m pip install -e .

echo ""

# Create cache directory
echo "=== Creating cache directory ==="
mkdir -p "$HOME/.cache/huggingface"
echo "Cache directory: $HOME/.cache/huggingface"

echo ""
echo "========================================"
echo "Installation complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Run hardware detection: python3 scripts/detect_hardware.py"
echo "2. Try text-to-video: jupyter notebook notebooks/text-to-video.ipynb"
echo "3. Or launch web UI: python3 webui/app.py"
echo ""
