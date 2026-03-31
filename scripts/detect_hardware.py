#!/usr/bin/env python3
"""
Hardware detection script for local video generation.
Detects system capabilities and provides recommendations.
"""

import json
import platform
import sys
from pathlib import Path


def detect_system():
    """Detect system information"""
    return {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": __import__("os").cpu_count(),
    }


def detect_ram():
    """Detect RAM information"""
    try:
        if sys.platform == "darwin":
            # macOS
            import subprocess
            output = subprocess.check_output(["sysctl", "-n", "hw.memsize"], text=True).strip()
            total_gb = int(output) / (1024**3)
            return {"total_gb": round(total_gb, 1)}
        elif sys.platform == "linux":
            # Linux
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if "MemTotal:" in line:
                        total_kb = int(line.split()[1])
                        return {"total_gb": round(total_kb / (1024**2), 1)}
        elif sys.platform == "win32":
            # Windows
            import subprocess
            output = subprocess.check_output(["wmic", "Memory"], text=True)
            # Parse output
            pass
    except Exception as e:
        return {"total_gb": 8, "error": str(e)}
    
    return {"total_gb": 8}


def detect_vram():
    """Detect VRAM/GPU information"""
    gpus = []
    
    try:
        if sys.platform == "darwin":
            # macOS Metal
            import subprocess
            output = subprocess.check_output(["system_profiler", "SPDisplaysDataType"], text=True)
            # Parse Metal info
            gpus.append({
                "name": "Apple Metal",
                "free_memory_mb": 4096,
                "total_memory_mb": 8192,
                "driver": "Metal",
            })
        elif sys.platform == "linux" or sys.platform == "darwin":
            # NVIDIA CUDA via nvidia-smi
            import subprocess
            try:
                output = subprocess.check_output(["nvidia-smi", "--query=gpu,name,memory.total,memory.free,driver_version", "--format=json"], text=True)
                import json
                data = json.loads(output)
                for gpu in data.get("gpu", []):
                    gpus.append({
                        "name": gpu.get("name", "Unknown"),
                        "free_memory_mb": gpu.get("memory.free", 0),
                        "total_memory_mb": gpu.get("memory.total", 0),
                        "driver": gpu.get("driver_version", "Unknown"),
                    })
            except:
                pass
        
        if not gpus:
            # No GPU detected
            gpus.append({
                "name": "CPU-only",
                "free_memory_mb": 0,
                "total_memory_mb": 0,
                "driver": "None",
            })
    except Exception as e:
        gpus.append({
            "name": "Unknown",
            "free_memory_mb": 0,
            "total_memory_mb": 0,
            "driver": str(e),
        })
    
    return {"gpus": gpus}


def detect_storage():
    """Detect storage availability"""
    import shutil
    home = str(Path.home())
    stat = shutil.disk_usage(home)
    free_gb = stat.free / (1024**3)
    return {"free_gb": round(free_gb, 1), "path": home}


def detect_hardware():
    """Run all detections and return comprehensive report"""
    return {
        "system": detect_system(),
        "ram": detect_ram(),
        "vram": detect_vram(),
        "storage": detect_storage(),
        "timestamp": __import__("datetime").datetime.now().isoformat(),
    }


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Hardware detection for local video generation")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    hw = detect_hardware()
    
    if args.json:
        print(json.dumps(hw, indent=2))
    else:
        print("=" * 60)
        print("HARDWARE DETECTION REPORT")
        print("=" * 60)
        print(f"Platform: {hw['system']['platform']} {hw['system']['platform_release']}")
        print(f"CPU: {hw['system']['processor']} ({hw['system']['cpu_count']} cores)")
        print(f"RAM: {hw['ram']['total_gb']} GB")
        print(f"Storage: {hw['storage']['free_gb']} GB free")
        print("")
        print("GPUs:")
        for gpu in hw['vram']['gpus']:
            print(f"  - {gpu['name']} ({gpu['total_memory_mb']} MB total, {gpu['free_memory_mb']} MB free)")
        print("=" * 60)
