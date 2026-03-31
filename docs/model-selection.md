# Model Selection Guide

Choosing the right model for your hardware and use case.

## Model Categories

### Text-to-Video Models

These models generate videos from text prompts. Higher requirements, but more exciting results.

**Models:**
- `odyssey-systems/Wan2.1-T2V-1.3B-bf16` - Lightweight, good for learning (1.3B params)
- `Wan-AI/Wan2.1-T2V-1.3B` - Standard quality, most popular (1.3B params)
- `stabilityai/stable-video-diffusion-img2vid` - Image-to-video base
- `stabilityai/stable-video-diffusion-img2vid-xt` - Image-to-video XT (best quality)

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

| Use Case | Recommended Model | RAM | VRAM | Notes |
|----------|-----------------|-----|------|-------|
| Learning/Testing | odyssey-systems/Wan2.1-T2V-1.3B-bf16 | 16 GB | 8 GB | Lightweight, good for low-end hardware |
| Daily Use | Wan-AI/Wan2.1-T2V-1.3B | 20 GB | 10 GB | Balanced quality and cost |
| High Quality | stabilityai/stable-video-diffusion-img2vid-xt | 24 GB | 10 GB | Best quality open model |
| Image-to-Video | stabilityai/stable-video-diffusion-img2vid | 16 GB | 8 GB | Base quality |

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
