#!/usr/bin/env python3
"""
Model recommendation script for local video generation.
Recommends appropriate transformers/diffusers models based on hardware.
"""

import json
import sys
from pathlib import Path


# Model database with memory requirements (in GB)
MODEL_DATABASE = [
    {
        "name": "stabilityai/stable-diffusion-xl-base",
        "type": "text-to-image",
        "min_ram_gb": 8,
        "min_vram_gb": 4,
        "description": "Base Stable Diffusion XL model for high-quality image generation",
        "recommended": True
    },
    {
        "name": "stabilityai/sdxl-sublime",
        "type": "text-to-image",
        "min_ram_gb": 12,
        "min_vram_gb": 6,
        "description": "SDXL Sublime for enhanced quality and speed",
        "recommended": True
    },
    {
        "name": "genius-ai-video/sora-lite",
        "type": "text-to-video",
        "min_ram_gb": 16,
        "min_vram_gb": 8,
        "description": "Lightweight video generation model",
        "recommended": True
    },
    {
        "name": "genius-ai-video/video-diffusion-1",
        "type": "text-to-video",
        "min_ram_gb": 24,
        "min_vram_gb": 12,
        "description": "Standard video diffusion model",
        "recommended": True
    },
    {
        "name": "genius-ai-video/video-diffusion-2",
        "type": "text-to-video",
        "min_ram_gb": 32,
        "min_vram_gb": 16,
        "description": "Advanced video diffusion model",
        "recommended": False
    },
    {
        "name": "stabilityai/stable-video-diffusion",
        "type": "text-to-video",
        "min_ram_gb": 32,
        "min_vram_gb": 16,
        "description": "Stability AI's stable video diffusion",
        "recommended": False
    },
    {
        "name": "stabilityai/pixel-diffusion-2",
        "type": "text-to-video",
        "min_ram_gb": 48,
        "min_vram_gb": 24,
        "description": "Pixel-level video diffusion",
        "recommended": False
    },
]


def recommend_models(hardware_report):
    """
    Recommend models based on hardware report.
    
    Args:
        hardware_report: Dictionary with hardware information
        
    Returns:
        List of recommended models sorted by recommendation priority
    """
    ram_gb = hardware_report.get("ram", {}).get("total_gb", 0)
    gpus = hardware_report.get("vram", {}).get("gpus", [])
    
    # Calculate available VRAM (use minimum of all GPUs for safety)
    if gpus:
        available_vram_gb = min(gpu.get("free_memory_mb", 0) / 1024 for gpu in gpus)
    else:
        available_vram_gb = 0
    
    # Find models that fit in available memory
    compatible_models = []
    for model in MODEL_DATABASE:
        if ram_gb >= model["min_ram_gb"] and available_vram_gb >= model["min_vram_gb"]:
            compatible_models.append(model)
    
    # Sort by recommendation priority
    compatible_models.sort(key=lambda x: (not x.get("recommended", False), x["min_ram_gb"]))
    
    return compatible_models


def get_model_summary(models, hardware_report):
    """Generate a human-readable summary of model recommendations."""
    ram_gb = hardware_report.get("ram", {}).get("total_gb", 0)
    gpus = hardware_report.get("vram", {}).get("gpus", [])
    
    summary = []
    summary.append("=" * 60)
    summary.append("MODEL RECOMMENDATIONS")
    summary.append("=" * 60)
    summary.append(f"Hardware: {ram_gb} GB RAM, {len(gpus)} GPU(s)")
    summary.append("")
    
    if not models:
        summary.append("⚠️  No models found that fit your hardware.")
        summary.append("Consider upgrading your system or using cloud-based generation.")
        return "\n".join(summary)
    
    summary.append(f"Found {len(models)} compatible model(s):")
    summary.append("")
    
    for i, model in enumerate(models, 1):
        summary.append(f"{i}. {model['name']}")
        summary.append(f"   Type: {model['type']}")
        summary.append(f"   Description: {model['description']}")
        summary.append(f"   Minimum RAM: {model['min_ram_gb']} GB")
        summary.append(f"   Minimum VRAM: {model['min_vram_gb']} GB")
        summary.append("")
    
    summary.append("=" * 60)
    
    return "\n".join(summary)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Model recommendation for local video generation")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--hardware", type=str, help="Path to hardware report JSON")
    
    args = parser.parse_args()
    
    # Load hardware report
    if args.hardware:
        with open(args.hardware, "r") as f:
            hardware_report = json.load(f)
    else:
        # Try to load from default location
        hw_file = Path.home() / ".openclaw" / "homework" / "state" / "hardware-report.json"
        if hw_file.exists():
            with open(hw_file, "r") as f:
                hardware_report = json.load(f)
        else:
            # Use defaults for demo
            hardware_report = {
                "ram": {"total_gb": 16},
                "vram": {"gpus": []}
            }
    
    # Get recommendations
    models = recommend_models(hardware_report)
    
    if args.json:
        print(json.dumps(models, indent=2))
    else:
        print(get_model_summary(models, hardware_report))
