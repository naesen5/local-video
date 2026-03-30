# Model Selection Guide

Choosing the right model for your hardware and use case.

## Model Categories

### Text-to-Image Models

These models generate images from text prompts. Useful for:
- Creating reference images for video generation
- Understanding how models work before video
- Faster generation for testing

**Models:**
- `stabilityai/stable-diffusion-xl-base` - Base quality, works on most systems
- `stabilityai/sdxl-sublime` - Enhanced quality, needs more RAM

### Text-to-Video Models

These models generate videos from text prompts. Higher requirements, but more exciting results.

**Models:**
- `genius-ai-video/sora-lite` - Lightweight, good for learning
- `genius-ai-video/video-diffusion-1` - Standard quality, most popular
- `genius-ai-video/video-diffusion-2` - Advanced, best quality
- `stabilityai/stable-video-diffusion` - Stability AI's implementation

## How to Choose

### Step 1: Check Your Hardware

```bash
python3 scripts/detect_hardware.py
```

### Step 2: Get Recommendations

```bash
python3 scripts/recommend_models.py
```

### Step 3: Select Based on Use Case

| Use Case | Recommended Model | RAM | VRAM |
|----------|-----------------|-----|------|
| Learning/Testing | sora-lite | 16 GB | 8 GB |
| Daily Use | video-diffusion-1 | 24 GB | 12 GB |
| High Quality | video-diffusion-2 | 32 GB | 16 GB |
| Professional | stable-video-diffusion | 48 GB | 24 GB |

## Model Parameters

### Key Parameters

- **Resolution**: 256x256 (fast) vs 512x512 (quality)
- **Frame count**: 16 frames (short) vs 64 frames (longer)
- **Inference steps**: 50 (fast) vs 100 (quality)

### Trade-offs

| Setting | Speed | Quality | RAM |
|---------|-------|---------|-----|
| Low (256x256, 16 frames, 50 steps) | Fast | Lower | Low |
| Medium (512x512, 32 frames, 75 steps) | Medium | Good | Medium |
| High (512x512, 64 frames, 100 steps) | Slow | Best | High |

## Getting Started with Your Model

Once you've selected a model, you'll need to:

1. **Install the model**: Run `bash scripts/install_local_video.sh` with your model name
2. **Configure the notebook**: Set the model name in the notebook
3. **Run the generation**: Follow the notebook instructions

## Advanced Model Options

### Custom Models

You can use any Hugging Face model by specifying the full path:

```python
model_name = "your-user/your-model"
```

### Model Combining

Advanced users can combine models:
- Use text-to-image model for frame generation
- Use video interpolation model to smooth transitions
- Use upscaling model for higher resolution

## Troubleshooting Model Issues

### Model Not Found

```bash
# Check internet connection
# Check Hugging Face access token if needed
```

### Out of Memory

- Reduce resolution
- Reduce frame count
- Use a smaller model
- Close other applications

### Slow Generation

- Use GPU if available
- Reduce inference steps
- Use smaller resolution
- Use a more efficient model
