"""Tests for webui/app.py imports."""

import os
import sys

# Add scripts to path for local imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))


class TestWebUIImports:
    """Tests that webui/app.py imports succeed."""

    def test_gradio_import(self):
        """Verify gradio can be imported."""
        import gradio

        assert gradio is not None

    def test_torch_import(self):
        """Verify torch can be imported."""
        import torch

        assert torch is not None

    def test_numpy_import(self):
        """Verify numpy can be imported."""
        import numpy

        assert numpy is not None

    def test_pil_import(self):
        """Verify PIL can be imported."""
        from PIL import Image

        assert Image is not None

    def test_detect_hardware_import(self):
        """Verify detect_hardware module can be imported."""
        from detect_hardware import get_system_info

        assert callable(get_system_info)

    def test_recommend_models_import(self):
        """Verify recommend_models module can be imported."""
        from recommend_models import recommend_models

        assert callable(recommend_models)
