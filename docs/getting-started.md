# Getting Started with Local Video Generation

This guide covers both supported backends: **diffusers/transformers** (recommended) and **stable-diffusion.cpp**.

## Prerequisites

Before we begin, ensure you have:
- Python 3.9 or newer
- pip (Python package manager)
- FFmpeg installed (`brew install ffmpeg` / `apt-get install ffmpeg`)
- At least 16 GB RAM (more recommended for video generation)
- Optional: GPU with at least 8 GB VRAM for faster generation

## Option A: diffusers/transformers Backend (Recommended)

### Installation

```bash
git clone https://github.com/naesen5/local-video.git
cd local-video

# Run the unified installer
chmod +x scripts/install_local_video.sh
./scripts/install_local_video.sh

# Activate virtual environment
source venv/bin/activate
```

The installer will:
- Create a Python virtual environment
- Install torch, diffusers, transformers, gradio, and all dependencies
- Install FFmpeg if not present

### Quick Start

```bash
# Check your hardware
python3 scripts/detect_hardware.py

# Get model recommendations
python3 scripts/recommend_models.py

# Launch the web interface
python webui/app.py
```

Then open `http://localhost:7860` in your browser.

### Using Jupyter Notebooks

```bash
jupyter notebook notebooks/text-to-video.ipynb
jupyter notebook notebooks/image-to-video.ipynb
jupyter notebook notebooks/advanced-usage.ipynb
```

## Option B: stable-diffusion.cpp Backend

Best for CPU-only systems or when you need lower memory overhead.

### Requirements
- cmake
- git
- C/C++ compiler (Xcode CLT on macOS, `build-essential` on Linux)
- Minimum: 16 GB RAM, 50 GB free storage
- Recommended: 24 GB+ RAM, 100 GB+ free storage

### Installation

```bash
git clone https://github.com/naesen5/local-video.git
cd local-video
bash scripts/install_local_video.sh
```

This installs:
- stable-diffusion.cpp (C/C++ backend)
- Python dependencies (gradio, opencv-python, numpy)
- All required system packages

### Quick Start

```bash
# Detect hardware
python3 scripts/detect_hardware.py

# Launch notebook
jupyter notebook notebooks/text-to-video.ipynb

# Or web interface
python3 webui/app.py
```

## Choosing a Backend

| Factor | diffusers | stable-diffusion.cpp |
|--------|-----------|----------------------|
| Model selection | Very broad (HuggingFace) | Limited to GGUF-compatible |
| CPU performance | Slower | Faster |
| GPU performance | Excellent | Good |
| Memory usage | Higher | Lower |
| Setup complexity | Low (pip) | Higher (build from source) |

If you have a GPU with 8GB+ VRAM, use diffusers. If you're CPU-only or have limited RAM, try stable-diffusion.cpp.

## Troubleshooting

### Out of Memory
- Reduce video length (fewer frames)
- Reduce resolution (smaller width/height)
- Use a smaller model (see `docs/model-selection.md`)

### Slow Generation
- Use fewer frames (8 instead of 16)
- Use lower resolution (128×128)
- Enable GPU if available (`torch.cuda.is_available()`)

### Installation Fails
- Ensure Python 3.9+ is installed
- On macOS: `xcode-select --install` for C/C++ compiler
- On Linux: `sudo apt-get install build-essential cmake`
