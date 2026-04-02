# 🎥 Local Video Generation

This repository provides a complete pathway for local video generation. It includes full documentation, Jupyter notebooks, and a web interface for text-to-video and image-to-video operations.

Two backends are supported:
- **diffusers/transformers** (recommended): Python-native, broad model support, Gradio web UI
- **stable-diffusion.cpp**: C/C++ backend, lower memory overhead, faster on CPU-only systems

## 📋 Overview

- **Full markdown documentation** explaining how to get local video generation working
- **Jupyter notebooks** demonstrating video generation
- **Instructions effective for non-technical users**
- **Hardware auto-detection** that recommends appropriate models based on your RAM/VRAM
- **Web interface** powered by Gradio for text-to-video and image-to-video operations
- **Automatic model selection** based on user's RAM/VRAM constraints

## 🚀 Quick Start

### Option 1: Unified Installation Script (Recommended)

```bash
# Clone the repository
git clone https://github.com/naesen5/local-video.git
cd local-video

# Run the installation script
chmod +x scripts/install_local_video.sh
./scripts/install_local_video.sh

# Activate the virtual environment
source venv/bin/activate

# Run the web interface
python webui/app.py
```

### Option 2: Manual Installation (diffusers backend)

```bash
# Install system dependencies
# macOS
brew install ffmpeg
# Ubuntu/Debian
sudo apt-get install ffmpeg
# Windows: download from https://ffmpeg.org/download.html

# Install Python dependencies
pip install torch diffusers transformers gradio pillow opencv-python numpy

# Run the web interface
python webui/app.py
```

### Option 3: stable-diffusion.cpp backend

```bash
git clone https://github.com/naesen5/local-video.git
cd local-video
bash scripts/install_local_video.sh

# Detect your hardware capabilities
python3 scripts/detect_hardware.py

# Launch notebook or web UI
jupyter notebook notebooks/text-to-video.ipynb
# or
python3 webui/app.py
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

| RAM/VRAM | Recommended Model | Quality | Speed |
|----------|-------------------|---------|-------|
| 4GB+ | ali-vilab/text-to-video-ms-1.7b | Low | Fast |
| 8GB+ | Wan-AI/Wan2.1-T2V-1.3B | Medium | Medium |
| 16GB+ | zai-org/CogVideoX-2b | High | Slow |
| 32GB+ | zai-org/CogVideoX-5b | Best | Slow |

### Minimum Requirements:
- **RAM**: 4GB (smaller models only, low quality)
- **VRAM**: 4GB+ (if using GPU)

### Recommended:
- **RAM**: 16GB+ or **VRAM**: 8GB+

## 🛠️ Scripts

- `scripts/detect_hardware.py`: Detect your system's hardware capabilities
- `scripts/recommend_models.py`: Recommend appropriate models based on hardware
- `scripts/install_local_video.sh`: Unified installation script

## 📦 Requirements

### System Dependencies:
- Python 3.9+
- FFmpeg

### Python Dependencies (diffusers backend):
- torch, diffusers, transformers, gradio, pillow, opencv-python, numpy

### stable-diffusion.cpp backend:
- cmake, git, C/C++ compiler (Xcode CLT on macOS, build-essential on Linux)

## 🤖 About

This repository provides a complete, user-friendly pathway for local video generation. It focuses on non-technical user accessibility, hardware-aware model recommendations, comprehensive documentation, and dual-backend support (diffusers + stable-diffusion.cpp).

## 📄 License

See LICENSE file.

## 🙋 Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request.

---

**Need help?** Check the documentation in the `docs/` folder or open an issue.
