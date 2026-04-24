#!/usr/bin/env python3
"""
Gradio Web Interface for Local Video Generation

This provides a user-friendly web interface for:
- Text-to-Video generation
- Image-to-Video generation
- Model selection based on hardware
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import gradio as gr
import numpy as np
import torch
from PIL import Image

from scripts.detect_hardware import detect_hardware
from scripts.recommend_models import recommend_models

# Import local modules


class VideoGenerationUI:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.current_model = None
        self.pipe = None

        print(f"Initializing UI on {self.device}")

    def load_model(self, model_name):
        """Load a video generation model"""
        try:
            # DiffusionPipeline not used — pipeline() handles loading
            from transformers import pipeline

            print(f"Loading model: {model_name}")

            self.pipe = pipeline(
                "text-to-video",
                model=model_name,
                device=0 if self.device == "cuda" else -1,
            )

            return f"✅ Model loaded: {model_name}\nDevice: {self.device}"
        except Exception as e:
            return f"❌ Error loading model: {e}\n\nTry a smaller model or CPU"

    def generate_text_to_video(self, prompt, model_name, num_frames, height, width):
        """Generate video from text prompt"""
        try:
            # Load model if not already loaded
            if self.pipe is None or self.current_model != model_name:
                status = self.load_model(model_name)
                if "Error" in status or "❌" in status:
                    return None, status

            # Generate video
            frames = self.pipe(
                prompt,
                num_frames=int(num_frames),
                height=int(height),
                width=int(width),
                num_inference_steps=50,
            )

            # Save video
            output_dir = "output"
            os.makedirs(output_dir, exist_ok=True)

            safe_prompt = "".join(
                c if c.isalnum() or c in " -_" else "_" for c in prompt[:30]
            )
            output_path = os.path.join(output_dir, f"video_{safe_prompt}.mp4")

            # Save frames as video
            import cv2

            if frames:
                first_frame = frames[0]
                if hasattr(first_frame, "size"):
                    h, w = first_frame.size[1], first_frame.size[0]
                else:
                    h, w = first_frame.shape[:2]

                fourcc = cv2.VideoWriter_fourcc("mp4v")
                video = cv2.VideoWriter(output_path, fourcc, 4.0, (w, h))

                for frame in frames:
                    if hasattr(frame, "convert"):
                        frame = frame.convert("RGB")
                    if hasattr(frame, "numpy"):
                        frame_np = frame.numpy()
                    else:
                        frame_np = np.array(frame)
                    frame_bgr = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)
                    video.write(frame_bgr)

                video.release()

                status = f"✅ Video generated: {output_path}\nFrames: {len(frames)}\nSize: {w}x{h}"
                return output_path, status
            else:
                return None, "❌ No frames generated"

        except Exception as e:
            return None, f"❌ Error: {e}"

    def generate_image_to_video(self, image, prompt, model_name, num_frames):
        """Generate video from image and text prompt"""
        try:
            if self.pipe is None or self.current_model != model_name:
                status = self.load_model(model_name)
                if "Error" in status or "❌" in status:
                    return None, status

            # Convert Gradio image to PIL
            if image is None:
                return None, "❌ No image provided"

            if isinstance(image, np.ndarray):
                pil_image = Image.fromarray(image)
            else:
                pil_image = Image.fromarray(np.array(image))

            # Generate video frames
            frames = []
            for i in range(int(num_frames)):
                frame_prompt = f"{prompt}, frame {i+1}/{int(num_frames)}"
                frame = self.pipe(
                    frame_prompt,
                    image=pil_image,
                    num_inference_steps=30,
                )
                frames.append(frame)

            # Save video
            output_dir = "output"
            os.makedirs(output_dir, exist_ok=True)

            safe_prompt = "".join(
                c if c.isalnum() or c in " -_" else "_" for c in prompt[:30]
            )
            output_path = os.path.join(
                output_dir, f"video_from_image_{safe_prompt}.mp4"
            )

            import cv2

            if frames:
                first_frame = frames[0]
                if hasattr(first_frame, "size"):
                    h, w = first_frame.size[1], first_frame.size[0]
                else:
                    h, w = first_frame.shape[:2]

                fourcc = cv2.VideoWriter_fourcc("mp4v")
                video = cv2.VideoWriter(output_path, fourcc, 4.0, (w, h))

                for frame in frames:
                    if hasattr(frame, "convert"):
                        frame = frame.convert("RGB")
                    if hasattr(frame, "numpy"):
                        frame_np = frame.numpy()
                    else:
                        frame_np = np.array(frame)
                    frame_bgr = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)
                    video.write(frame_bgr)

                video.release()

                status = f"✅ Video generated from image: {output_path}"
                return output_path, status
            else:
                return None, "❌ No frames generated"

        except Exception as e:
            return None, f"❌ Error: {e}"

    def get_hardware_info(self):
        """Get current hardware information"""
        try:
            hw = detect_hardware()
            recommendations = recommend_models(hw)

            info = f"""
**Hardware Information**
- RAM: {hw.get('ram_gb', 'Unknown')} GB
- VRAM: {hw.get('vram_gb', 'N/A')} GB
- Device: {self.device}
- CUDA: {torch.cuda.is_available()}

**Recommended Models**
"""
            for model in recommendations[:3]:
                info += f"- {model['name']}: {model['description']}\n"

            return info
        except Exception as e:
            return f"❌ Error getting hardware info: {e}"

    def create_interface(self):
        """Create the Gradio interface"""

        with gr.Blocks(title="Local Video Generation", theme=gr.themes.Soft()) as demo:
            gr.Markdown("# 🎥 Local Video Generation")
            gr.Markdown(
                "Generate videos from text or images using diffusers/transformers"
            )

            with gr.Tab("Hardware Info"):
                hardware_btn = gr.Button("Get Hardware Info")
                hardware_output = gr.Markdown()
                hardware_btn.click(self.get_hardware_info, outputs=hardware_output)

            with gr.Tab("Text-to-Video"):
                gr.Markdown("### Generate Video from Text")

                with gr.Row():
                    with gr.Column():
                        prompt_txt = gr.Textbox(
                            label="Prompt",
                            placeholder="Enter your text prompt here...",
                            value="A beautiful sunset in coastal city",
                        )
                        model_dd = gr.Dropdown(
                            label="Model",
                            choices=[
                                "ali-vilab/text-to-video-ms-1.7b",
                                "zai-org/CogVideoX-2b",
                                "Wan-AI/Wan2.1-T2V-1.3B",
                            ],
                            value="ali-vilab/text-to-video-ms-1.7b",
                        )
                        num_frames_sl = gr.Slider(
                            label="Number of Frames",
                            minimum=4,
                            maximum=32,
                            value=16,
                            step=4,
                        )
                        height_sl = gr.Slider(
                            label="Height", minimum=128, maximum=512, value=256, step=64
                        )
                        width_sl = gr.Slider(
                            label="Width", minimum=128, maximum=512, value=256, step=64
                        )
                        generate_txt_btn = gr.Button(
                            "Generate Video", variant="primary"
                        )

                    with gr.Column():
                        output_video = gr.Video(label="Generated Video")
                        status_txt = gr.Textbox(label="Status", lines=5)

                generate_txt_btn.click(
                    self.generate_text_to_video,
                    inputs=[prompt_txt, model_dd, num_frames_sl, height_sl, width_sl],
                    outputs=[output_video, status_txt],
                )

            with gr.Tab("Image-to-Video"):
                gr.Markdown("### Generate Video from Image")

                with gr.Row():
                    with gr.Column():
                        input_image = gr.Image(label="Input Image")
                        prompt_img_txt = gr.Textbox(
                            label="Prompt",
                            placeholder="Describe the motion...",
                            value="Peaceful animated scene",
                        )
                        model_img_dd = gr.Dropdown(
                            label="Model",
                            choices=[
                                "stabilityai/stable-video-diffusion-img2vid",
                                "stabilityai/stable-video-diffusion-img2vid-xt",
                            ],
                            value="stabilityai/stable-video-diffusion-img2vid",
                        )
                        num_frames_img_sl = gr.Slider(
                            label="Number of Frames",
                            minimum=4,
                            maximum=16,
                            value=8,
                            step=2,
                        )
                        generate_img_btn = gr.Button(
                            "Generate Video", variant="primary"
                        )

                    with gr.Column():
                        output_video_img = gr.Video(label="Generated Video")
                        status_img = gr.Textbox(label="Status", lines=5)

                generate_img_btn.click(
                    self.generate_image_to_video,
                    inputs=[
                        input_image,
                        prompt_img_txt,
                        model_img_dd,
                        num_frames_img_sl,
                    ],
                    outputs=[output_video_img, status_img],
                )

            with gr.Tab("Documentation"):
                gr.Markdown("""
                ## 📖 Documentation

                ### Getting Started
                1. Choose your hardware mode
                2. Select a model based on your RAM/VRAM
                3. Enter your text prompt or upload image
                4. Adjust parameters (frames, resolution)
                5. Click generate

                ### Hardware Requirements
                - **Minimum**: 4GB RAM (smaller models only)
                - **Recommended**: 8GB+ RAM or 4GB+ VRAM
                - **Optimal**: 16GB+ RAM or 8GB+ VRAM

                ### Tips
                - Start with fewer frames for testing
                - Use smaller resolution for faster generation
                - Enable GPU if available
                - Monitor RAM/VRAM usage

                ### Troubleshooting
                - Out Memory: Reduce frames/resolution
                - Slow: Use GPU or smaller model
                - Errors: Check internet connection for model download
                """)

        return demo


def main():
    """Main entry point"""
    print("Starting Local Video Generation UI...")
    print(f"Device: {'GPU' if torch.cuda.is_available() else 'CPU'}")

    ui = VideoGenerationUI()
    demo = ui.create_interface()

    # Launch the interface
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)


if __name__ == "__main__":
    main()
