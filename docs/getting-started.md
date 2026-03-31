# Getting Started with Local Video Generation

This guide will help you get started with local video generation using stable-diffusion.cpp.

## What This System Does

This system provides:
- **Text-to-Video**: Generate videos from text prompts
- **Image-to-Video**: Convert images to animated videos
- **Hardware Detection**: Automatically detects your system capabilities
- **Model Recommendations**: Recommends appropriate models based on your RAM/VRAM

## Requirements

- **Minimum**: 8 GB RAM, 50 GB free storage
- **Recommended**: 16 GB+ RAM, 100 GB+ free storage
- **Optimal**: 32 GB+ RAM, 200 GB+ free storage

## Installation Steps

### Step 1: Clone the Repository

```bash
cd ~
git clone https://github.com/naesen5/local-video.git
cd local-video
```

### Step 2: Install Dependencies

```bash
bash scripts/install_local_video.sh
```

This will install:
- Python dependencies (gradio, opencv-python, numpy)
- stable-diffusion.cpp (C/C++ backend)
- All required system packages

### Step 3: Run Hardware Detection

```bash
python3 scripts/detect_hardware.py
```

This will show your system capabilities and recommend appropriate models.

### Step 4: Choose Your Interface

#### Option A: Jupyter Notebook

Open `notebooks/text-to-video.ipynb` or `notebooks/image-to-video.ipynb` in Jupyter:

```bash
jupyter notebook notebooks/text-to-video.ipynb
```

#### Option B: Web Interface

Launch the Gradio web interface:

```bash
python3 webui/app.py
```

Then open your browser to `http://localhost:7860`

## First Video Generation

### Text-to-Video

1. Open `notebooks/text-to-video.ipynb` in Jupyter
2. Find the cell with `prompt = "..."`
3. Change the text to your prompt (e.g., `"A beautiful sunset in coastal city"`)
4. Run the cell (Shift+Enter)
5. Wait for video generation (5-15 minutes depending on hardware)

### Image-to-Video

1. Open `notebooks/image-to-video.ipynb` in Jupyter
2. Find the cell with the image input
3. Upload your image
4. Change the text prompt to describe the motion
5. Run the cell
6. Wait for video generation

## Understanding What's What

### Why This Works

Video generation works by:
1. **Text Encoder**: Converts your text prompt into numbers (embeddings)
2. **Noise Scheduler**: Starts with random noise
3. **U-Net Model**: Repeatedly cleans the noise, guided by your text
4. **Frame Generation**: Creates each video frame step-by-step
5. **Video Assembly**: Combines frames into a video file

### Why RAM/VRAM Matters

Video generation uses:
- **Model weights**: 1-10 GB depending on model size
- **Input/output data**: 1-4 GB
- **Intermediate computations**: 2-10 GB

More RAM/VRAM = larger models = better quality videos.

### Why Hardware Detection Helps

The detection script:
- Checks your RAM size
- Checks your GPU/VRAM
- Recommends appropriate models
- Prevents "out of memory" errors

## Troubleshooting

### Out Memory Error

If you see "Out Memory" or "CUDA out memory":
- Reduce video length (fewer frames)
- Reduce resolution (smaller width/height)
- Use a smaller model

### Slow Generation

If generation is too slow:
- Use fewer frames (8 instead 16)
- Use lower resolution (128x128)
- Enable GPU if available

### Model Not Found

If you see "Model Not Found":
- Check internet connection
- First download may take 5-15 minutes
- Models are cached for reuse

## Next Steps

1. **Watch your video**: Open the saved file in your video player
2. **Try different prompts**: Change the text and generate again
3. **Adjust quality**: Change frames/resolution for different results
4. **Try image-to-video**: Use the image-to-video notebook

## Getting Help

If you see errors:
1. Check internet connection
2. Check RAM/VRAM usage
3. Try a smaller model
4. Check the documentation in `docs/` folder
