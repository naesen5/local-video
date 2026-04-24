#!/usr/bin/env python3
"""
Hardware detection script for local video generation.
Detects CPU, RAM, VRAM and provides system information.
"""

import json
import platform
import subprocess


def get_system_info():
    """Get basic system information."""
    return {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }


def get_ram_info():
    """Get RAM information."""
    system = platform.system()

    if system == "Darwin":  # macOS
        try:
            import psutil

            mem = psutil.virtual_memory()
            return {
                "total_gb": round(mem.total / (1024**3), 2),
                "available_gb": round(mem.available / (1024**3), 2),
                "used_gb": round(mem.used / (1024**3), 2),
                "percent": mem.percent,
            }
        except ImportError:
            return {"error": "Install psutil: pip install psutil"}

    elif system == "Linux":
        try:
            import psutil

            mem = psutil.virtual_memory()
            return {
                "total_gb": round(mem.total / (1024**3), 2),
                "available_gb": round(mem.available / (1024**3), 2),
                "used_gb": round(mem.used / (1024**3), 2),
                "percent": mem.percent,
            }
        except ImportError:
            return {"error": "Install psutil: pip install psutil"}

    elif system == "Windows":
        try:
            import psutil

            mem = psutil.virtual_memory()
            return {
                "total_gb": round(mem.total / (1024**3), 2),
                "available_gb": round(mem.available / (1024**3), 2),
                "used_gb": round(mem.used / (1024**3), 2),
                "percent": mem.percent,
            }
        except ImportError:
            return {"error": "Install psutil: pip install psutil"}

    return {"error": "Unknown system or psutil not available"}


def get_vram_info():
    """Get VRAM (GPU) information."""
    system = platform.system()

    # Try to get NVIDIA GPU info
    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query=gpu,name,memory.total,memory.free,temperature.gpu",
                "--format=csv,noheader,nounits",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode == 0:
            lines = result.stdout.strip().split("\n")
            gpus = []
            for line in lines:
                parts = line.split(",")
                if len(parts) >= 3:
                    gpus.append(
                        {
                            "name": parts[0].strip() if len(parts) > 0 else "Unknown",
                            "total_memory_mb": (
                                int(parts[1].strip()) if len(parts) > 1 else 0
                            ),
                            "free_memory_mb": (
                                int(parts[2].strip()) if len(parts) > 2 else 0
                            ),
                        }
                    )
            return {"gpus": gpus}
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Try macOS Metal info
    if system == "Darwin":
        try:
            result = subprocess.run(
                ["system_profiler", "SPDisplaysDataType"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            # Parse Metal GPU info
            if "Metal" in result.stdout:
                return {"gpus": [{"name": "Apple Metal", "supported": True}]}
        except Exception:
            pass

    return {"gpus": [], "message": "No GPU detected or GPU tools not installed"}


def get_cpu_info():
    """Get CPU information."""
    system = platform.system()

    if system == "Darwin":
        try:
            result = subprocess.run(
                ["sysctl", "-n", "hw.cpufreq"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return {
                "max_frequency_hz": (
                    result.stdout.strip() if result.stdout else "Unknown"
                )
            }
        except Exception:
            return {"message": "Could not determine CPU frequency"}

    elif system == "Linux":
        try:
            with open("/proc/cpuinfo", "r") as f:
                lines = f.readlines()
                cpu_info = {}
                for line in lines:
                    if "cpu MHz" in line:
                        cpu_info["max_frequency_hz"] = (
                            int(line.split(":")[1].strip()) * 1000000
                        )
                return cpu_info
        except Exception:
            return {"message": "Could not determine CPU info"}

    elif system == "Windows":
        try:
            result = subprocess.run(
                ["wmic", "cpu", "get", "MaxClockSpeed"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return {
                "max_frequency_hz": (
                    result.stdout.strip() if result.stdout else "Unknown"
                )
            }
        except Exception:
            return {"message": "Could not determine CPU info"}

    return {"message": "Unknown system"}


def get_storage_info():
    """Get storage information."""
    try:
        import psutil

        disk = psutil.disk_usage("/")
        return {
            "total_gb": round(disk.total / (1024**3), 2),
            "free_gb": round(disk.free / (1024**3), 2),
            "used_gb": round(disk.used / (1024**3), 2),
            "percent": disk.percent,
        }
    except ImportError:
        return {"error": "Install psutil: pip install psutil"}


def get_full_hardware_report():
    """Get complete hardware report."""
    report = {
        "timestamp": __import__("datetime").datetime.now().isoformat(),
        "system": get_system_info(),
        "cpu": get_cpu_info(),
        "ram": get_ram_info(),
        "vram": get_vram_info(),
        "storage": get_storage_info(),
    }
    return report


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Hardware detection for local video generation"
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--short", action="store_true", help="Short output")

    args = parser.parse_args()

    report = get_full_hardware_report()

    if args.json:
        print(json.dumps(report, indent=2))
    elif args.short:
        ram = report["ram"]
        vram = report["vram"]
        print(f"RAM: {ram.get('total_gb', 'N/A')} GB total")
        print(f"VRAM: {len(vram.get('gpus', []))} GPU(s) detected")
    else:
        print("=" * 50)
        print("HARDWARE DETECTION REPORT")
        print("=" * 50)
        print(
            f"Platform: {report['system']['platform']} {report['system']['platform_release']}"
        )
        print(f"Python: {report['system']['python_version']}")
        print()
        print(f"RAM: {report['ram'].get('total_gb', 'N/A')} GB total")
        print(f"VRAM: {len(report['vram'].get('gpus', []))} GPU(s) detected")
        for gpu in report["vram"].get("gpus", []):
            print(f"  - {gpu.get('name', 'Unknown')}")
        print()
        print(f"Storage: {report['storage'].get('free_gb', 'N/A')} GB free")
        print("=" * 50)
