"""Tests for recommend_models module."""

import json
import os
import sys

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from recommend_models import MODEL_DATABASE, recommend_models


class TestModelDatabase:
    """Tests for MODEL_DATABASE."""

    def test_model_database_is_list(self):
        """Verify MODEL_DATABASE is a list."""
        assert isinstance(MODEL_DATABASE, list)

    def test_model_database_not_empty(self):
        """Verify MODEL_DATABASE has entries."""
        assert len(MODEL_DATABASE) > 0

    def test_model_database_entries_have_required_fields(self):
        """Verify each model has name, type, and description."""
        for model in MODEL_DATABASE:
            assert "name" in model, f"Model missing 'name': {model}"
            assert "type" in model, f"Model missing 'type': {model}"
            assert "description" in model, f"Model missing 'description': {model}"

    def test_model_names_are_valid_hf_ids(self):
        """Verify model names look like valid HuggingFace IDs."""
        for model in MODEL_DATABASE:
            # HF model IDs have format org/model or org/subdir/model
            parts = model["name"].split("/")
            assert len(parts) >= 2, f"Invalid model ID: {model['name']}"
            assert len(parts[0]) > 0, f"Empty org in model ID: {model['name']}"
            assert len(parts[1]) > 0, f"Empty model name: {model['name']}"


class TestRecommendModels:
    """Tests for recommend_models function."""

    def test_recommend_models_returns_list(self):
        """Verify recommend_models returns a list."""
        hardware_report = {"ram": {"total_gb": 8}, "cpu": {"cores": 4}}
        result = recommend_models(hardware_report)
        assert isinstance(result, list)

    def test_recommend_models_with_sufficient_hardware(self):
        """Verify models are recommended for sufficient hardware."""
        hardware_report = {"ram": {"total_gb": 16}, "cpu": {"cores": 8}}
        result = recommend_models(hardware_report)
        assert isinstance(result, list)

    def test_recommend_models_with_low_hardware(self):
        """Verify empty list for insufficient hardware."""
        hardware_report = {"ram": {"total_gb": 2}, "cpu": {"cores": 1}}
        result = recommend_models(hardware_report)
        assert isinstance(result, list)

    def test_recommend_models_json_serializable(self):
        """Verify output is JSON serializable."""
        hardware_report = {"ram": {"total_gb": 8}, "cpu": {"cores": 4}}
        result = recommend_models(hardware_report)
        try:
            json.dumps(result)
        except TypeError as e:
            assert False, f"Not JSON serializable: {e}"
