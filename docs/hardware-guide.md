# Hardware Guide for Local Video Generation

Understanding your hardware requirements for local video generation.

## Minimum Requirements

| Component | Minimum | Recommended | Optimal |
|-----------|---------|-------------|---------|
| RAM | 16 GB | 32 GB | 64 GB+ |
| VRAM | 8 GB | 16 GB | 32 GB+ |
| Storage | 50 GB free | 100 GB free | 200 GB+ |
| CPU | 4 cores | 8 cores | 16+ cores |

## Hardware Detection

Run the detection script to see your system info:

```bash
python3 scripts/detect_hardware.py --json
```

This will output detailed information about:
- System information
- CPU details
- RAM capacity and usage
- GPU information
- Storage availability

## GPU Recommendations

### Apple Silicon (M1, M2, M3)

- **Metal backend**: Use Apple's Metal acceleration
- **Recommended models**: sora-lite, sdxl-sublime
- **Memory sharing**: CPU and GPU share RAM, so system RAM counts as total memory

### NVIDIA GPUs

- **CUDA support**: Full acceleration
- **Recommended models**: All models up to video-diffusion-2
- **VRAM requirement**: Check minimum VRAM in model documentation

### AMD GPUs

- **Limited support**: Some models may not work
- **CPU fallback**: System will use CPU if GPU not supported
- **Recommended**: Use CPU-only mode for reliability

## RAM Management

### What's RAM Usage?

Video generation uses RAM for:
- Model weights (1-10 GB depending on model)
- Input/output data (1-4 GB)
- Intermediate computations (2-10 GB)

### Tips for Low-RAM Systems

1. **Close other applications** before generating
2. **Use smaller models** (sora-lite instead video-diffusion-2)
3. **Generate shorter videos** (fewer frames)
4. **Use lower resolution** (256x256 instead 512x512)

## Storage Requirements

### Model Storage

| Model | Size | Notes |
|-------|------|-------|
| sora-lite | 2-4 GB | Lightweight, good for testing |
| video-diffusion-1 | 5-8 GB | Standard quality |
| video-diffusion-2 | 10-15 GB | High quality |
| stable-video-diffusion | 15-20 GB | Best quality |

### Cache Storage

Transformers/diffusers cache models in `~/.cache/huggingface/`:
- First model download: 5-10 GB
- Additional models: 2-5 GB each
- Total cache: 20-50 GB recommended

## Benchmarking Your Hardware

Run the hardware detection and model recommendation:

```bash
python3 scripts/detect_hardware.py --json > hw-report.json
python3 scripts/recommend_models.py --hardware hw-report.json
```

This will tell you which models are recommended for your hardware.
