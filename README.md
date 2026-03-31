# Local Video Generation with stable-diffusion.cpp

This repository provides a complete pathway for local video generation using stable-diffusion.cpp.

## What This System Does

- **Text-to-Video**: Generate videos from text prompts
- **Image-to-Video**: Convert images to animated videos
- **Hardware Detection**: Automatically detects your system capabilities
- **Model Recommendations**: Recommends appropriate models based on your RAM/VRAM

## Requirements

- **Minimum**: 16 GB RAM, 50 GB free storage
- **Recommended**: 24 GB+ RAM, 100 GB+ free storage
- **Optimal**: 32 GB+ RAM, 200 GB+ free storage

## Installation

```bash
cd ~
git clone https://github.com/naesen5/local-video.git
cd local-video
bash scripts/install_local_video.sh
```

This will install:
- Python dependencies (gradio, opencv-python, numpy)
- stable-diffusion.cpp (C/C++ backend)
- All required system packages

## Quick Start

### Hardware Detection

```bash
python3 scripts/detect_hardware.py
```

### Text-to-Video (Jupyter Notebook)

```bash
jupyter notebook notebooks/text-to-video.ipynb
```

### Image-to-Video (Jupyter Notebook)

```bash
jupyter notebook notebooks/image-to-video.ipynb
```

### Web Interface

```bash
python3 webui/app.py
```

Then open your browser to `http://localhost:7860`

## Supported Models

### Text-to-Video
- `odyssey-systems/Wan2.1-T2V-1.3B-bf16` (lightweight, 1.3B params)
- `Wan-AI/Wan2.1-T2V-1.3B` (standard, 1.3B params)

### Image-to-Video
- `stabilityai/stable-video-diffusion-img2vid` (base quality)
- `stabilityai/stable-video-diffusion-img2vid-xt` (best quality)

## Documentation

- `docs/getting-started.md` - Getting started guide
- `docs/hardware-guide.md` - Hardware requirements
- `docs/model-selection.md` - Model selection guide

## Troubleshooting

### Out Memory Error

- Reduce video length (fewer frames)
- Reduce resolution (smaller width/height)
- Use a smaller model

### Slow Generation

- Use fewer frames (8 instead 16)
- Use lower resolution (128x128)
- Enable GPU if available

## License

This project is provided under the terms of the local-video repository.
