# Getting Started with Local Video Generation

This guide will help you get started with local video generation using transformers/diffusers.

## Prerequisites

Before we begin, ensure you have:
- Python 3.9 or newer
- pip (Python package manager)
- At least 16 GB RAM (more recommended for video generation)
- Optional: GPU with at least 8 GB VRAM for faster generation

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/naesen5/local-video.git
cd local-video
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

Run the installation script:

```bash
bash scripts/install_local_video.sh
```

This will:
- Detect your hardware
- Install appropriate versions of transformers/diffusers
- Install all required dependencies

### Step 4: Verify Installation

Run the hardware detection script:

```bash
python3 scripts/detect_hardware.py
```

You should see your hardware information displayed.

## First Video Generation

### Option 1: Using Jupyter Notebook

Launch Jupyter:

```bash
jupyter notebook notebooks/text-to-video.ipynb
```

Follow the step-by-step instructions in the notebook to generate your first video.

### Option 2: Using the Web Interface

Launch the Gradio web interface:

```bash
python3 webui/app.py
```

Then open your browser to `http://localhost:7860` and start generating videos.

## Understanding What's Installing

### Core Libraries

- **transformers**: Hugging Face's transformer library for AI models
- **diffusers**: Hugging Face's library for diffusion models (images and videos)
- **torch/torchvision**: PyTorch for deep learning
- **ffmpeg**: Video processing tools

### Why These Versions?

The installation script detects your hardware and installs:
- **CPU-only**: CPU-optimized PyTorch for systems without GPU
- **GPU-enabled**: CUDA-enabled PyTorch for systems with compatible GPU
- **Model versions**: Compatible with your available RAM/VRAM

## Troubleshooting

### Out of Memory Errors

If you get "Out of Memory" errors:
- Try generating shorter videos
- Use lower resolution (256x256 instead 512x512)
- Close other applications to free RAM
- Consider using a system with more RAM

### Installation Issues

If installation fails:
1. Check Python version: `python3 --version`
2. Ensure you have at least 16 GB free disk space
3. Try installing with verbose output: `pip install -v <package>`

## Next Steps

1. Try the text-to-video notebook
2. Experiment with different prompts
3. Learn about model selection in `docs/model-selection.md`
4. Check hardware requirements in `docs/hardware-guide.md`
