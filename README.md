# 🎥 Local Video Generation

This repository provides a complete pathway for local video generation using diffusers/transformers. It includes full documentation, Jupyter notebooks, and a web interface for text-to-video and image-to-video operations.

## 📋 Overview

- **Full markdown documentation** explaining how to get local video generation working
- **Jupyter notebooks** demonstrating video generation
- **Instructions effective for non-technical users**
- **Hardware auto-detection** that recommends appropriate transformers/diffusers versions
- **Web interface** powered by Gradio for text-to-video and image-to-video operations
- **Automatic model selection** based on user's RAM/VRAM constraints

## 🚀 Quick Start

### Option 1: Unified Installation Script (Recommended)

```bash
# Clone the repository
git clone https://github.com/YOUR-REPO/local-video.git
cd local-video

# Run the installation script
chmod +x scripts/install_local_video.sh
./scripts/install_local_video.sh

# Activate the virtual environment
source venv/bin/activate

# Run the web interface
python webui/app.py
```

### Option 2: Manual Installation

```bash
# Install system dependencies
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html

# Install Python dependencies
pip install torch diffusers transformers gradio pillow opencv-python numpy

# Run the web interface
python webui/app.py
```

## 📖 Documentation

- **Getting Started**: `docs/getting-started.md`
- **Hardware Guide**: `docs/hardware-guide.md`
- **Model Selection**: `docs/model-selection.md`

## 📓 Jupyter Notebooks

- **Text-to-Video**: `notebooks/text-to-video.ipynb`
- **Image-to-Video**: `notebooks/image-to-video.ipynb`
- **Advanced Usage**: `notebooks/advanced-usage.ipynb`

## 🌐 Web Interface

Run the web interface:

```bash
python webui/app.py
```

Then open your browser to `http://localhost:7860`

### Features:
- **Hardware Info**: Check your system specifications
- **Text-to-Video**: Generate videos from text prompts
- **Image-to-Video**: Generate videos from images
- **Model Selection**: Choose appropriate models based on your hardware

## 🔧 Hardware Requirements

| RAM/VRAM | Model | Quality | Speed |
|----------|-------|---------|-------|
| 4GB+ | text-to-video-1 | Low | Fast |
| 8GB+ | text-to-video-2 | Medium | Medium |
| 16GB+ | text-to-video-3 | High | Slow |

### Minimum Requirements:
- **RAM**: 4GB (smaller models only, low quality)
- **VRAM**: 4GB+ (if using GPU)

### Recommended:
- **RAM**: 8GB+ or **VRAM**: 4GB+
- **RAM**: 16GB+ or **VRAM**: 8GB+ (optimal)

## 🛠️ Scripts

- `scripts/detect_hardware.py`: Detect your system's hardware capabilities
- `scripts/recommend_models.py`: Recommend appropriate models based on hardware
- `scripts/install_local_video.sh`: Unified installation script

## 🌐 Web Interface Files

- `webui/app.py`: Main Gradio application
- `webui/templates/index.html`: Web interface HTML
- `webui/static/style.css`: Web interface CSS

## 📦 Requirements

### System Dependencies:
- Python 3.8+
- FFmpeg

### Python Dependencies:
- torch
- diffusers
- transformers
- gradio
- pillow
- opencv-python
- numpy

## 🤖 About

This repository was created to provide a complete, user-friendly pathway for local video generation after the sunsetting of Sora. It focuses on:
- Non-technical user accessibility
- Hardware-aware model recommendations
- Comprehensive documentation
- Multiple interfaces (notebooks, web)

## 📄 License

See LICENSE file.

## 🙋 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a branch for your changes
3. Submit a pull request

---

**Need help?** Check the documentation in the `docs/` folder or open an issue.
