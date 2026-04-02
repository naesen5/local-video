#!/bin/bash
#
# Unified Installation Script for Local Video Generation
# This script installs all dependencies for the local video generation system
#

set -e

echo "========================================="
echo "Local Video Generation Installation"
echo "========================================="

# Detect operating system
OS=$(uname -s)
echo "Detected OS: $OS"

# Detect Python version
PYTHON_CMD="python3"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
    echo "Python version: $PYTHON_VERSION"
else
    echo "Error: Python3 not found"
    exit 1
fi

# Detect package manager
if command -v brew &> /dev/null; then
    PKG_MGR="brew"
elif command -v apt &> /dev/null; then
    PKG_MGR="apt"
elif command -v yum &> /dev/null; then
    PKG_MGR="yum"
else
    PKG_MGR="unknown"
fi
echo "Package manager: $PKG_MGR"

# Install system dependencies
echo ""
echo "=== Installing System Dependencies ==="

if [ "$PKG_MGR" = "brew" ]; then
    echo "Installing with Homebrew..."
    brew install ffmpeg
elif [ "$PKG_MGR" = "apt" ]; then
    echo "Installing with APT..."
    sudo apt-get update
    sudo apt-get install -y ffmpeg
elif [ "$PKG_MGR" = "yum" ]; then
    echo "Installing with YUM..."
    sudo yum install -y ffmpeg
else
    echo "Warning: Unknown package manager. Please install ffmpeg manually"
fi

# Install Python dependencies
echo ""
echo "=== Installing Python Dependencies ==="

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
echo "Installing Python packages..."
pip install torch diffusers transformers gradio pillow opencv-python numpy

# Verify installation
echo ""
echo "=== Verification ==="

# Check Python packages
echo "Checking Python packages..."
python3 -c "import torch; print(f'PyTorch: {torch.__version__}')"
python3 -c "import diffusers; print(f'Diffusers: {diffusers.__version__}')"
python3 -c "import transformers; print(f'Transformers: {transformers.__version__}')"
python3 -c "import gradio; print(f'Gradio: {gradio.__version__}')"
python3 -c "import cv2; print(f'OpenCV: {cv2.__version__}')"

# Check ffmpeg
echo ""
echo "Checking ffmpeg..."
ffmpeg -version | head -n 1

echo ""
echo "========================================="
echo "Installation Complete!"
echo "========================================="
echo ""
echo "To use the system:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the web interface: python webui/app.py"
echo "3. Or use the notebooks in the notebooks/ folder"
echo ""
echo "For more documentation, check the docs/ folder"
